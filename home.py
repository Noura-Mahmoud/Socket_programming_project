
from PyQt5 import QtCore, QtGui, QtWidgets
from Symptom_client import Ui_MainWindow as app1
from chatbot_client import Ui_Form as app2

import socket
import sys
import errno

user = ''
class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 380)
        Form.setMinimumSize(QtCore.QSize(400, 380))
        Form.setMaximumSize(QtCore.QSize(400, 380))
        font = QtGui.QFont()
        font.setFamily("Juice ITC")
        Form.setFont(font)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        Form.setStyleSheet("QWidget{background-color:white;}\n"
                           "QPushButton{\n"
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
                           "QPushButton:hover{\n"
                           "background-color: rgb(0, 80, 138);\n"
                           "cursor:pointer;}\n"
                           "QLabel#label_8{\n"
                           "color: rgb(0,0,0);\n"
                           "font-size:30px\n"
                           "\n"
                           "}\n"
                           "QLabel{color: rgb(91, 91, 91);}\n"
                           "QLineEdit{\n"
                           "\n"
                           "border-style: solid;\n"
                           "  border-color: rgb(0, 80, 138);\n"
                           "  border-width: 1px;\n"
                           "border-radius:10px;\n"
                           "  box-shadow: 5px 10px;}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 381, 321))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Your Symptom Checker"))
        self.label.setText(_translate("Form", "Please Enter your name"))
        self.pushButton.setText(_translate("Form", "Live Chat"))
        self.pushButton.clicked.connect(lambda:self.Live_Chat())
        self.pushButton_2.setText(_translate("Form", "Automatic Diagnosis"))
        self.pushButton_2.clicked.connect(lambda:self.Automatic_Diagnosis())

    ############### functions starts here ########################

    def Automatic_Diagnosis(self):
        username =self.lineEdit.text()
        if not username :
            self.lineEdit.setStyleSheet("  border-color: rgb(100, 0, 0);\n"
                                        "  border-width: 2px;\n")
            self.label.setStyleSheet("color : rgb(100,0,0)")
        else :
            user = username
            self.window=app1(user)
            self.window.show()
            print(user)

    def Live_Chat(self):
        username =self.lineEdit.text()
        if not username :
            self.lineEdit.setStyleSheet("  border-color: rgb(100, 0, 0);\n"
                                        "  border-width: 2px;\n")
            self.label.setStyleSheet("color : rgb(100,0,0)")
        else :
            user = username
            self.window=app2(user)
            self.window.show()



    # def client(self):
    #     # HEADER_LENGTH = 10
    #     # IP = "127.0.0.1"
    #     # PORT = 5000
    #     # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     # client_socket.connect((IP, PORT))
    #     # client_socket.setblocking(False)
    #     # username = user.encode('utf-8')
    #     # username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    #     # client_socket.send(username_header + username)
    #     # while True:
    #         message = app2.setupUi.self.lineEdit.text()
    #         print(message)
    #         # message = input(f'{user} > ')



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Ui_Form()
    application.show()
    app.exec_()
    

if __name__ == "__main__":
      main()
