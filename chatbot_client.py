
from PyQt5 import QtCore, QtGui, QtWidgets

import socket
import sys
import errno
import os


class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self,user:str):
        super(Ui_Form,self).__init__()
        self.my_username=user
        self.setupUi(self)
        self.HEADER_LENGTH = 10
        self.IP = "127.0.0.1"
        self.PORT = 5000
        

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.IP, self.PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
        self.client_socket.setblocking(True)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
        username = self.my_username.encode('utf-8')
        username_header = f"{len(username):<{self.HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 627)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("  QWidget {\n"
                           "       \n"
                           "font-size:13px;\n"
                           "            }\n"
                           "QLabel{color: rgb(91, 91, 91);}\n"
                           "QLabel#label_8{\n"
                           "color: rgb(0,0,0);\n"
                           "font-size:30px\n"
                           "\n"
                           "}\n"
                           "QLabel#label_9{background-image: url(:/newPrefix/appointment.png);}\n"
                           "QLabel#label_7{\n"
                           "    color: rgb(91, 91, 91);}\n"
                           "QPushButton#pushButton{\n"
                           "  background-color: #0078d0;\n"
                           "  border: 0;\n"
                           "  border-radius: 20px;\n"
                           "  color: #fff;\n"
                           "  display: inline-block;\n"
                           "  font-family: system-ui,-apple-system,system-ui,\"Segoe UI\",Roboto,Ubuntu,\"Helvetica Neue\",sans-serif;\n"
                           "  font-size: 18px;\n"
                           "  font-weight: 600;\n"
                           "  outline: 0;\n"
                           "  padding: 16px 21px;\n"
                           "  position: relative;\n"
                           "  text-align: center;\n"
                           "  text-decoration: none;\n"
                           "  transition: all .3s;\n"
                           " }\n"
                           "\n"
                           "\n"
                           "QPushButton#pushButton:hover{\n"
                           "background-color: rgb(0, 80, 138);\n"
                           "cursor:pointer;\n"
                           "}\n"
                           "\n"
                           "QPushButton#pushButton_2:hover{\n"
                           "color: rgb(0, 80, 138);\n"
                           "cursor:pointer;}")
        Form.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhTime)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 30, 371, 451))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 500, 361, 82))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setStyleSheet("border:none;\n"
                                        "text-decoration:underline;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Live chat"))
        self.pushButton.setText(_translate("Form", "Send Message"))
        # self.pushButton.clicked.connect(lambda:Client(self.user,self.lineEdit.text()))
        self.pushButton.clicked.connect(lambda:self.chatting())
        self.pushButton_2.setText(_translate("Form", "Switch to automatic diagnosis?"))
        self.pushButton_2.clicked.connect(lambda:self.Automatic_Diagnosis())

    ############### functions starts here ########################
    def Automatic_Diagnosis(self):
        from Symptom_client import Ui_MainWindow as app1
        self.window=app1(self.my_username)
        self.window.show()


    def chatting(self):
        self.msg=self.lineEdit.text()
        message = self.msg.encode('utf-8')
        message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(message_header + message)
        #print("ok")
        self.textEdit.append(f"{self.msg}\n")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form('User')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

