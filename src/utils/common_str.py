#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 22:11
# @Author  :ytq
# @File    :
import datetime
import random
import time


class CommonStr:
    def get_cn_char(self, num):
        rd_str = ""
        for i in range(num):
            _head = random.randint(0xb0, 0xf7)
            _body1 = random.randint(0xa1, 0xf9)
            val = f'{_head:x}{_body1:x}'
            name = bytes.fromhex(val).decode('GBK')
            rd_str += name
        return rd_str

    def get_time_vale(self):
        now_time = datetime.datetime.now()
        str_time = now_time.strftime("%Y-%m-%d %X")
        return str_time

if __name__ == '__main__':
    com = CommonStr()
    com.get_time_vale()