#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

# 获取连接对象
def get_conn():
    try:
        conn = pymysql.connect(
            host='192.168.3.200',
            port=3306,
            user='root',
            passwd='AyJ34Ve!2Uy',
            db='suricata',
            charset='utf8'
        )
        return conn
    except Exception as e:
        print(e)
        exit(-1)

'''
    获取所有的
'''


def get_topdomain():
    # 获取执行工具
    conn = get_conn()
    cur = conn.cursor()
    list = []
    try:
        # Sql语句
        sql = "select distinct website_url as website_url from website;"
        cur.execute(sql)

        # 获取该表的所有数据
        alldata = cur.fetchall()
        for s in alldata:
            list.append(s[0])

    except Exception as e:
        print(e)
    finally:
        # 对该数据库操作完记得关闭
        cur.close()
        conn.close()

    return list


'''
    获取域名
    @website_url
'''


def get_website(website_url):
    select_count = 0
    # 获取执行工具
    conn = get_conn()
    cur = conn.cursor()
    try:
        # Sql语句
        select_sql = "select * from website where website_url = '%s';" % website_url
        # 查看该表有多少条数据
        select_count = cur.execute(select_sql)

    except Exception as e:
        print(e)
    finally:
        # 对该数据库操作完记得关闭
        cur.close()
        conn.close()
    return select_count



'''
    插入子域名
    @website_name
    @website_url
'''


def insert_subdomain(website_name, website_url):
    # 获取执行工具
    conn = get_conn()
    cur = conn.cursor()

    try:
        # Sql语句
        sql = "INSERT INTO website(website_name, website_url) VALUES (%s,%s);"

        values = (website_name, website_url)

        cur.execute(sql, values)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        # 对该数据库操作完记得关闭
        cur.close()
        conn.close()

if __name__ == '__main__':
    # print(get_topdomain())
    # print(get_website('2231909.0-6.com'))
    insert_subdomain("妈妈说","2231909.0-6.com")
