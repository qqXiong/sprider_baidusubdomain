#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Lqq
# @Software: PyCharm

from urllib.parse import urlencode

'''
设置请求头，模拟浏览器访问
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

'''
    获取路径
    https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=e3a83fe3000a02df&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=site%3A0-6.com&oq=site%253A0-6.com&rsv_pq=e3a83fe3000a02df&
    rsv_t=ff987BDF4HNxewRNnG4P0tfDiwuhLD2dnhuHFy3G3tEbTi3TWPrB2eiwOs4&rqlang=cn&rsv_enter=0&rsv_dl=tb&bs=site%3A0-6.com&rsv_sid=1447_21101_29568_29221_26350&_ss=1&
    clist=&hsug=&f4s=1&csor=12&_cr1=27364
    @keyword
    @page
'''


def get_url(keyword, page):
    data = {
        'wd': 'site:'+keyword,  # 修改关键字
        'pn': page * 10,  # 页数
    }
    # 把字典对象转化为url的请求参数
    url = 'https://www.baidu.com/s?' + urlencode(data)
    return url


if __name__ == '__main__':
    # get_list('site:qq.com')
    # print(get_title('2231909.0-6.com'))
    'https://www.csdn.net/'
    # http://tool.chinaz.com/pagestatus/
    # https://store.taobao.com
    # print(get_website('2231909.0-6.com'))
