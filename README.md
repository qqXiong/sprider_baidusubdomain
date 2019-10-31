<<<<<<< HEAD
# sprider_baidusudomains

目前可用条件：
> * 输入框的顶级域名可以不选择，不选择则选择数据库全部的域名获取域名以及标题
> * （标题是来自百度搜索引擎的显示的）存储到数据库


## 环境
使用环境：
> - win 10 64bits
> - pycharm
> - python3

第三方库：
> * bs4
> * pyqt5
> * requests 
> * os
> * time
> * sys
> * threading


工具：
> * database.py 连接数据库，数据库是写死的
> * conn = pymysql.connect(
                host='192.168.3.200',
                port=3306,
                user='root',
                passwd='AyJ34Ve!2Uy',
                db='suricata',
                charset='utf8'
            )
> * 
> * web.py 获取页面的路径

