# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'domain.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(695, 467)
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(540, 410, 131, 31))
        self.okButton.setObjectName("okButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 331, 421))
        self.textBrowser.setObjectName("textBrowser")
        self.host = QtWidgets.QLineEdit(Form)
        self.host.setGeometry(QtCore.QRect(450, 30, 221, 31))
        self.host.setObjectName("host")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 40, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 100, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 160, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 220, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(380, 280, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(380, 340, 72, 15))
        self.label_6.setObjectName("label_6")
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setGeometry(QtCore.QRect(450, 90, 221, 31))
        self.port.setObjectName("port")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(450, 150, 221, 31))
        self.user.setObjectName("user")
        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(450, 210, 221, 31))
        self.passwd.setObjectName("passwd")
        self.db = QtWidgets.QLineEdit(Form)
        self.db.setGeometry(QtCore.QRect(450, 270, 221, 31))
        self.db.setObjectName("db")
        self.charset = QtWidgets.QLineEdit(Form)
        self.charset.setGeometry(QtCore.QRect(450, 330, 221, 31))
        self.charset.setObjectName("charset")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.okButton.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "host:"))
        self.label_2.setText(_translate("Form", "port："))
        self.label_3.setText(_translate("Form", "user："))
        self.label_4.setText(_translate("Form", "passwd:"))
        self.label_5.setText(_translate("Form", "db："))
        self.label_6.setText(_translate("Form", "charset:"))
