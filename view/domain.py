# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'E:\pycharm_workspase\sprider_baidusubdomains\view\domain.ui'
# #
# # Created by: PyQt5 UI code generator 5.13.0
# #
# # WARNING! All changes made in this file will be lost!
#
#
# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(727, 620)
#
#         # 从数据库获取到的顶级域名
#         self.topDomain = QtWidgets.QComboBox(Form)
#         self.topDomain.setEnabled(True)
#         self.topDomain.setGeometry(QtCore.QRect(470, 50, 221, 31))
#         self.topDomain.setEditable(True)
#         self.topDomain.setObjectName("topDomain")
#
#         # 点击确定
#         self.okButton = QtWidgets.QPushButton(Form)
#         self.okButton.setGeometry(QtCore.QRect(560, 540, 131, 31))
#         self.okButton.setObjectName("okButton")
#
#         # 显示数据记录
#         self.textBrowser = QtWidgets.QTextBrowser(Form)
#         self.textBrowser.setGeometry(QtCore.QRect(40, 40, 331, 531))
#         self.textBrowser.setObjectName("textBrowser")
#
#         # 输入数据库的host
#         self.host = QtWidgets.QLineEdit(Form)
#         self.host.setGeometry(QtCore.QRect(470, 160, 221, 31))
#         self.host.setObjectName("host")
#
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(400, 170, 72, 15))
#         self.label.setObjectName("label")
#
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setGeometry(QtCore.QRect(400, 230, 72, 15))
#         self.label_2.setObjectName("label_2")
#
#         self.label_3 = QtWidgets.QLabel(Form)
#         self.label_3.setGeometry(QtCore.QRect(400, 290, 72, 15))
#         self.label_3.setObjectName("label_3")
#
#         self.label_4 = QtWidgets.QLabel(Form)
#         self.label_4.setGeometry(QtCore.QRect(400, 350, 72, 15))
#         self.label_4.setObjectName("label_4")
#
#         self.label_5 = QtWidgets.QLabel(Form)
#         self.label_5.setGeometry(QtCore.QRect(400, 410, 72, 15))
#         self.label_5.setObjectName("label_5")
#
#         self.label_6 = QtWidgets.QLabel(Form)
#         self.label_6.setGeometry(QtCore.QRect(400, 470, 72, 15))
#         self.label_6.setObjectName("label_6")
#
#         # 输入数据库的端口号
#         self.port = QtWidgets.QLineEdit(Form)
#         self.port.setGeometry(QtCore.QRect(470, 220, 221, 31))
#         self.port.setObjectName("port")
#
#         # 输入数据库的用户名
#         self.user = QtWidgets.QLineEdit(Form)
#         self.user.setGeometry(QtCore.QRect(470, 280, 221, 31))
#         self.user.setObjectName("user")
#
#         # 输入数据库的密码
#         self.passwd = QtWidgets.QLineEdit(Form)
#         self.passwd.setGeometry(QtCore.QRect(470, 340, 221, 31))
#         self.passwd.setObjectName("passwd")
#
#         # 输入数据库
#         self.db = QtWidgets.QLineEdit(Form)
#         self.db.setGeometry(QtCore.QRect(470, 400, 221, 31))
#         self.db.setObjectName("db")
#
#         # 输入数据库的格式
#         self.charset = QtWidgets.QLineEdit(Form)
#         self.charset.setGeometry(QtCore.QRect(470, 460, 221, 31))
#         self.charset.setObjectName("charset")
#
#         # 手动输入域名
#         self.domain = QtWidgets.QLineEdit(Form)
#         self.domain.setGeometry(QtCore.QRect(470, 100, 221, 31))
#         self.domain.setObjectName("domain")
#
#         self.label_7 = QtWidgets.QLabel(Form)
#         self.label_7.setGeometry(QtCore.QRect(400, 60, 72, 15))
#         self.label_7.setObjectName("label_7")
#
#         self.label_8 = QtWidgets.QLabel(Form)
#         self.label_8.setGeometry(QtCore.QRect(400, 110, 72, 15))
#         self.label_8.setObjectName("label_8")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.okButton.setText(_translate("Form", "确定"))
#         self.label.setText(_translate("Form", "host:"))
#         self.label_2.setText(_translate("Form", "port："))
#         self.label_3.setText(_translate("Form", "user："))
#         self.label_4.setText(_translate("Form", "passwd:"))
#         self.label_5.setText(_translate("Form", "db："))
#         self.label_6.setText(_translate("Form", "charset:"))
#         self.label_7.setText(_translate("Form", "database:"))
#         self.label_8.setText(_translate("Form", "input:"))

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

        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(250, 20, 131, 31))
        self.okButton.setObjectName("pushButton")

        self.result = QtWidgets.QTextBrowser(Form)
        self.result.setGeometry(QtCore.QRect(40, 70, 341, 421))
        self.result.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.okButton.setText(_translate("Form", "确定"))
