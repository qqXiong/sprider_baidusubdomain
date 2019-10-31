# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pycharm_workspase\sprider_baidusubdomains\view\domain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 528)
        self.topDomain = QtWidgets.QComboBox(Form)
        self.topDomain.setEnabled(True)
        self.topDomain.setGeometry(QtCore.QRect(40, 20, 191, 31))
        self.topDomain.setEditable(True)
        self.topDomain.setObjectName("topDomain")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 20, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.result = QtWidgets.QTextBrowser(Form)
        self.result.setGeometry(QtCore.QRect(40, 70, 341, 421))
        self.result.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确定"))
