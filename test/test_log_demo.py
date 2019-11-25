# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 下午9:51
# @Author  : YTQ
# @FileName: test_log_demo.py
# @Software: PyCharm
import datetime
import os
import time


def test_demo():
    time_str = datetime.datetime.now().strftime('%H:%M:%S')
    time_str = "22:02:44"
    log_command = '''
    cd /home/ytq/PycharmProjects/Test_dev_study/src/logs;cat RunLog_20191125.log| grep 退出|awk -F" " '{print $2}'|awk -F"," '{print $1}'
'''
    rst = os.popen(log_command).read().split("\n")
    rst=[x for x in rst if x!='']
    for i in range(len(rst)):
        if time.strptime(rst[i],"%H:%M:%S")>time.strptime(time_str, "%H:%M:%S"):
            print(rst[i]+"完成了对系统的重启")
    