#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Lqq
# @Software: PyCharm

import sys
import os
import time
import requests
import threading

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5 import QtCore, QtWidgets
from view.domain import Ui_Form
from util.web import get_url, headers
from util.database import get_topdomain, insert_subdomain, get_website
from bs4 import BeautifulSoup as bs


class Combosel(QtWidgets.QWidget):
    def __init__(self):
        super(Combosel, self).__init__()

        self.ui_sel = Ui_Form()
        self.ui_sel.setupUi(self)

        # 获取数据的顶级域名
        self.topdomain = get_topdomain()


        self.ui_sel.topDomain.clear()
        self.ui_sel.topDomain.addItem(u'请选择')
        # 初始化
        for val in self.topdomain:
            self.ui_sel.topDomain.addItem(val)



        self.site = []

        # 连接自己的槽函数
        self.ui_sel.okButton.clicked.connect(self.onActivatedpushButton)

    def get_html(self, keyword, count, list):
        print(keyword)
        loop = True
        try:
            count = count
            url = get_url(keyword, count)
            # get请求，content获取返回包正文
            response = requests.get(url, headers=headers)
            response.encoding = 'utf-8'
            data = response.content
            soup = bs(data, 'html.parser')
            pagelist = soup.find_all("a", attrs={"class": "n"})
            if len(pagelist) == 1:
                if pagelist[0].get_text() == '<上一页':
                    loop = False
            elif len(pagelist) == 0:
                loop = False

            divlist = soup.find_all("div", attrs={"class": "result c-container"})
            for k in divlist:
                text = k.find("a", attrs={'class': 'c-showurl', 'style': 'text-decoration:none;'}).get_text()
                title = k.find("h3", attrs={'class': 't'}).get_text()

                star = 0
                end = 0
                if text.find("//") != -1:
                    star = text.find("//") + 2
                if text.find('/') != -1:
                    end = text.find('/')
                domain = text[star:end]
                dict = {}
                dict[domain] = title
                if dict not in list:
                    print(keyword+": "+domain+", "+title)
                    map = {}
                    map[domain] = title
                    list.append(map)
                    if get_website(domain) == 0:
                        if domain:
                            insert_subdomain(title, domain)
                            self.ui_sel.result.insertPlainText("标题：" + title + "数据添加成功\n")
        except Exception as e:
            print(e)
        return list,loop

    def get_result(self, keyword):
        try:
            # # 显示结果
            self.ui_sel.result.insertPlainText(
                "开始时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "\n")
            self.ui_sel.result.insertPlainText('选择结果：{}'.format(keyword) + "\n")
            self.ui_sel.result.insertPlainText("请稍等正在获取数据....." + "\n")

            count = 0
            list = []
            if keyword == '请选择':
                for topdomain in get_topdomain():
                    loop = True
                    while loop:
                        data, pagelist = self.get_html(topdomain, count, list)
                        if pagelist:
                            count = count + 1
                        else:
                            loop = False
            else:
                loop = True
                while loop:
                    data,pagelist = self.get_html(keyword, count, list)
                    if pagelist:
                        count = count + 1
                    else:
                        loop = False
        except Exception as e:
            print(e)


    # 点击
    def onActivatedpushButton(self):
        try:
            # 清理结果集
            self.ui_sel.result.clear()
            index = self.ui_sel.topDomain.currentIndex()
            val = self.ui_sel.topDomain.itemText(index)
            th = threading.Thread(target=self.get_result, args=(val,))
            th.setDaemon(True)
            th.start()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        Appcombosel = Combosel()
        Appcombosel.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
