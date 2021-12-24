import socket
import sys
import errno
import ssl
import time

HEADER_LENGTH = 10

# IP address and the port number of the server
IP = "127.0.0.1"
PORT = 5000
my_username = input("Username: ")

# Create an SSL context
context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED

# Load CA certificate with which the client will validate the server certificate
context.load_verify_locations("./snakeoil.pem")

# Load client certificate
context.load_cert_chain(certfile="./snakeoil.pem", keyfile="./snakeoil.key")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make the client socket suitable for secure communication
secureClientSocket = context.wrap_socket(client_socket)

# Connect to a given ip and port
secureClientSocket.connect((IP, PORT))

# Obtain the certificate from the server
server_cert = secureClientSocket.getpeercert()

if not server_cert:
    raise Exception("Unable to retrieve server certificate")

notAfterTimestamp = ssl.cert_time_to_seconds(server_cert['notAfter'])
notBeforeTimestamp = ssl.cert_time_to_seconds(server_cert['notBefore'])
currentTimeStamp = time.time()

if currentTimeStamp > notAfterTimestamp:
    raise Exception("Expired server certificate")

if currentTimeStamp < notBeforeTimestamp:
    raise Exception("Server certificate not yet active")


# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
secureClientSocket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
secureClientSocket.send(username)

while True:

    # Wait for user to input a message
    message = input(f'{my_username} > ')

    # If message is not empty - send it
    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')

        # no need for message header with fixed length, the module is capable of receiving arbitary sized messages!
        # message_header = f"{len(0message):<{HEADER_LENGTH}}".encode('utf-8')
        # print(f"sending to serve: {message}")
        secureClientSocket.send(message)
        time.sleep(0.2)

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            # username_header = secureClientSocket.recv(HEADER_LENGTH)

            msg = secureClientSocket.recv()
            print(f"server >> {msg.decode('utf-8')}")

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            # if not len(username_header):
            if not len(msg):
                print('Connection closed by the server')
                sys.exit()

            # print("Secure communication received from server: %s"%msg.decode())
            # print(f'server > {msg}')

            # # Convert header to int value
            # username_length = len(username_header.decode('utf-8').strip())

            # Receive and decode username
            # username = secureClientSocket.recv(username_length).decode('utf-8')

            # # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            # message_header = secureClientSocket.recv(HEADER_LENGTH)
            # message_length = int(message_header.decode('utf-8').strip())
            # message = secureClientSocket.recv(message_length).decode('utf-8')

            # # Print message
            # print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        # if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
        #     print("##############################")
        #     print('Reading error: {}'.format(str(e)))
        #     sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print(f'Reading error: {e}')
        sys.exit()
