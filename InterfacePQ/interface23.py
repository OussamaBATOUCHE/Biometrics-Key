# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface23.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from user import Ui_Frame2


class Ui_Frame(object): 
    def openWindow(self):
        self.window=QtWidgets.QFrame()
        self.ui=Ui_Frame2()
        self.ui.setupUi(self.window)
        self.window.show()

       
        
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(769, 484)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(-10, -20, 801, 501))
        self.label.setStyleSheet("background:#FFFFFF;\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(16, 60, 331, 361))
        self.label_2.setStyleSheet(" \n"
"background-image: url(:/ressource/Bureau/Biometrics-Key/InterfacePQ/image/interface.jpg);\n"
" \n"
" ")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/interface.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setIndent(4)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(350, 60, 401, 421))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(30)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(390, 320, 341, 41))
        self.pushButton.setStyleSheet("background:#1e90ff;\n"
"color:white;\n"
" ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(370, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman,Times,serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: italic;\n"
"font-size:10vw;\n"
"font-family: \"Times New Roman\", Times, serif;\n"
"font-style: italic;\n"
"font-size: 40px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(380, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#a9a9a9;\n"
"font-style: italic;\n"
"font-size:10vw;\n"
" ")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(490, 410, 41, 41))
        self.label_6.setStyleSheet(" \n"
" \n"
"image: url(:/interface/Bureau/image/google-plus.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/google-plus.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setIndent(3)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Frame)
        self.label_7.setGeometry(QtCore.QRect(560, 410, 41, 41))
        self.label_7.setStyleSheet("\n"
"image: url(:/interface/Bureau/image/facebook.png);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/facebook.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setIndent(2)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Frame)
        self.label_8.setGeometry(QtCore.QRect(630, 410, 41, 41))
        self.label_8.setStyleSheet("\n"
"image: url(:/interface/Bureau/image/twitter.png);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/twitter.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setIndent(4)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(390, 180, 341, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 230, 341, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(Frame)
        self.label_9.setGeometry(QtCore.QRect(440, 370, 191, 17))
        self.label_9.setStyleSheet("color:#696969; ")
        self.label_9.setObjectName("label_9")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(600, 280, 177, 41))
        self.commandLinkButton.setStyleSheet("color:#1e90ff;")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Frame)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(600, 360, 177, 41))
        self.commandLinkButton_2.setStyleSheet("color:#1e90ff;")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_10 = QtWidgets.QLabel(Frame)
        self.label_10.setGeometry(QtCore.QRect(390, 150, 121, 17))
        self.label_10.setStyleSheet("color:#696969;\n"
" ")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Frame)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_11.setStyleSheet(" \n"
"image: url(:/interface/Bureau/image/Capture du 2019-11-09 08-47-15.png);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("images/Capture du 2019-11-09 08-47-15.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Frame)
        self.label_12.setGeometry(QtCore.QRect(390, 20, 41, 51))
        self.label_12.setStyleSheet("")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Frame)
        self.label_13.setGeometry(QtCore.QRect(370, 10, 71, 61))
        self.label_13.setStyleSheet("image: url(:/interface/Bureau/image/image4.png);")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("images/image4.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setIndent(3)
        self.label_13.setObjectName("label_13")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 410, 41, 41))
        self.pushButton_2.setStyleSheet("border-radius:10px;\n"
" ")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 410, 41, 41))
        self.pushButton_3.setStyleSheet("border-radius:10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Frame)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 410, 41, 41))
        self.pushButton_4.setStyleSheet("border-radius:10px;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", " LOGIN"))
        self.label_4.setText(_translate("Frame", " Welcome"))
        self.label_5.setText(_translate("Frame", " Sign in to builder"))
        self.lineEdit.setPlaceholderText(_translate("Frame", "Email"))
        self.lineEdit_2.setPlaceholderText(_translate("Frame", "password"))
        self.label_9.setText(_translate("Frame", " Don\'t have an account?"))
        self.commandLinkButton.setText(_translate("Frame", " forget password?"))
        self.commandLinkButton_2.setText(_translate("Frame", " Sign up"))
        self.label_10.setText(_translate("Frame", " Enter Details"))
        self.pushButton_3.setText(_translate("Frame", " "))
        self.pushButton_4.setText(_translate("Frame", " "))
import qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
