#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 11:02
# @Author  : Lqq
# @FileName: domain.py
# @Software: PyCharm

import re


def isValidDomainChar(ch):
    return ch.isalpha() or ch.isdigit() or ch == '-'


def isValidDomainSect(sect):
    return len(sect) > 0 and all(isValidDomainChar(ch) for ch in sect)


def areValidDomainSects(sects):
    return all(isValidDomainSect(sect) for sect in sects)


def isValidDomain(domain):
    sects = domain.split('.')
    global TLDS
    return areValidDomainSects(sects[0:-1]) and sects[-1] in TLDS


def main(domain):
    with open('../file/domains.txt', 'r') as f:
        global TLDS
        TLDS = re.split(' |\n', f.read())
        print(TLDS)
    while domain != '':
        if isValidDomain(domain):
            print('Domain valid.')
        else:
            print('Domain invalid.')


if __name__ == '__main__':
    topDomain = "www.baidu.com"
    hosts = topDomain.split(".")

    with open('../file/domains.txt', 'r') as f:
        global TLDS
        TLDS = re.split(' |\n', f.read())
        count = 0
        for host in hosts:
            if host in TLDS:
                count = count+1

