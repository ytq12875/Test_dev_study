#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/3 12:21
# @Author  :ytq
# @File    :
import os
import random
from src.test_selenium_ex_0803 import TestSeleniumEx
#
# s = [1,2,3,4,5,6]
# print(random.choice(s[4:6]))

#
# demo = TestSeleniumEx()
# print(demo.get_cn_char(3))

import requests


def getIpAddr(ip):
    url = "http://ip.tool.chinaz.com/%s" % ip
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    content = response.text
    str = content[content.find("WhwtdWrap bor-b1s col-gray03"):content.find("clearfix plr10") - 87]  # 大致筛选出归属地所在的字符串
    a = str[::-1]
    b = a[0:a.find(">")]
    return b[::-1].split("<")[0]


def get_commond_result(commond):
    list_a = []
    with os.popen(commond) as f:
        text = f.read()
    for item in text.split(" "):
        if item:
            list_a.append(item)
    return list_a


if __name__ == '__main__':
    list_a = get_commond_result('tasklist|findstr "QQ.exe"')
    list_b = get_commond_result('netstat -ano|findstr "%s" ' % list_a[1])
    for index, value in enumerate(list_b):
        if value == "TCP":
            cus_ip = list_b[index + 2].split(":")[0]
            if cus_ip != "0.0.0.0" and list_b[index+3] == "ESTABLISHED":
                str = getIpAddr(cus_ip)
                print("当前与你QQ活跃连接的IP " + cus_ip + " 来自于 " + str)
            elif cus_ip != "0.0.0.0" and list_b[index+3] == "CLOSE_WAIT":
                str = getIpAddr(cus_ip)
                print("当前与你QQ非活跃连接的IP " + cus_ip + " 来自于 " + str)
