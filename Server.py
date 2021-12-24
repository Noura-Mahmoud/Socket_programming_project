import socket
import select
import select
import mysql.connector

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 5000

# Create a socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, so server informs operating system that it's going to use given IP and port.
server_socket.bind((IP, PORT))

# This makes server listen to new connections
server_socket.listen()

# List of sockets for select.select()
sockets_list = [server_socket]

# List of connected clients - socket as a key, user header and name as data
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

# Handles message receiving
def receive_message(client_socket):

    try:

        # Receive our "header" containing message length, it's size is defined and constant
        client_socket.settimeout(20)
            
        message_header = client_socket.recv(HEADER_LENGTH)

        # If we received no data, client gracefully closed a connection.
        if not len(message_header):
            return False

        # Convert header to int value
        message_length = int(message_header.decode('utf-8').strip())

        # Return an object of message header and message data
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except socket.timeout as e:
            print("Time Out")

# CONNECTING TO DB AND CREATING TABLE IF NOT EXIST
def DBConnection():
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql",
                database="Socket")
            print("DB CONNECTED SUCCESSFULLY")    
            mycursor = db.cursor(buffered=True)  
            mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS(IP VARCHAR (255)  NOT NULL PRIMARY KEY,PORT VARCHAR(255) NOT NULL , Dname VARCHAR(255),Mname VARCHAR(255),Lname VARCHAR(255),phone INT(50),mail VARCHAR(255) UNIQUE,Birth_date Date,Doctor_ID INT(150) UNIQUE,syndicate_number INT (100) UNIQUE,salary INT(50),gender VARCHAR(255),address text,job_rank VARCHAR(255),access_level int DEFAULT 2,image LONGBLOB,calendarid VARCHAR (600) UNIQUE )")
            db.commit()
            print("TABLE CREATED SUCCESSFULLY")    
            #QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
        except mysql.connector.Error as e:
            #QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            print("Failed To Connect Database")    
            #sys.exit(1)

def insert_data(ADDRESS,NAME):
    try:
        # CONNECTING TO DB AND CREATING TABLE IF NOT EXIST
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="Socket")
        print("DB CONNECTED SUCCESSFULLY")
        mycursor = db.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS(IPPORT VARCHAR (255)  NOT NULL , NAME VARCHAR(255), MSG VARCHAR(255))")
        #db.commit()
        print("TABLE CREATED SUCCESSFULLY")
        # INSERTING DATA IN THE TABLE
        sql = "INSERT INTO CLIENTS (IPPORT,NAME) VALUES (%s,%s)"
        val = (ADDRESS,NAME)
        mycursor.execute(sql, val)
        # COMMITING CHANGES TO THE DB
        db.commit()
        print("DATA INSERTED SUCCESSFULLY")

    except mysql.connector.Error as e:
        #self.labelResult.setText("Error Inserting Data")
        print(e.errno)

def update_data(ADDRESS,MSG):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="Socket")
        mycursor = db.cursor()
        sql = "UPDATE CLIENTS SET MSG = %s WHERE IPPORT = %s"
        val = (MSG,ADDRESS)
        mycursor.execute(sql, val)
        db.commit()
        print(MSG)
        print("MESSAGE UPDATED SUCCESSFULLY")
    except mysql.connector.Error as e:
      print('An exception occurred... ',e)

while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)


    # Iterate over notified sockets
    for notified_socket in read_sockets:

        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:

            # Accept new connection
        
            client_socket, client_address = server_socket.accept()

            # Client should send his name right away, receive it
            user = receive_message(client_socket)

            # If False - client disconnected before he sent his name
            if user is False:
                continue

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)

            # Also save username and username header
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
            insert_data("{}:{}".format(*client_address),user['data'].decode('utf-8'))

        # Else existing socket is sending a message
        else:

            # Receive message
            message = receive_message(notified_socket)
            

           
            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                del clients[notified_socket]

                continue
            
            update_data("{}:{}".format(*client_address),message['data'].decode('utf-8'))
            
            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
           # response = input('Doctor: ')
           # client_socket.send(response.encode('utf-8'))


            # Iterate over connected clients and broadcast message
            for client_socket in clients:

                # But don't sent it to sender
                if client_socket != notified_socket:

                    # Send user and message (both with their headers)
                
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # It's not really necessary to have this, but will handle some socket exceptions just in case
    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        del clients[notified_socket]



