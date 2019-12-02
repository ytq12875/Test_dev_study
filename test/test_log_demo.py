# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 下午9:51
# @Author  : YTQ
# @FileName: test_log_demo.py
# @Software: PyCharm
import datetime
import os
import time

from src.reboot_box.ssh_client_utils import MySshClient


def test_demo():
    # time_str = datetime.datetime.now().strftime('%H:%M:%S')
    time_str = "11:10:22"
    log_command = '''
    cd /qhapp/apps/lo-boxs/gwb01/;cat boxlogs/lifecycle.log | grep 'LifecycleException'|awk -F' ' '{print $2}'|awk -F'.' '{print $1}'
'''
    my_ssh_client = MySshClient()
    my_ssh_client.ssh_login("10.91.138.140", "tomcat", "ldygo@9012!@#$%&*#")
    rst = my_ssh_client.execute_some_command(log_command).split("\n")
    print(rst)
    rst = [x for x in rst if x != '']
    for i in range(len(rst)):
        if time.strptime(rst[i], "%H:%M:%S") >= time.strptime(time_str, "%H:%M:%S"):
            error_log_cmd = "cd /qhapp/apps/lo-boxs/%s/boxlogs; grep -A 10 -i '%s.[0-9][0-9][0-9]|ERROR' lifecycle.log"
            error_log = my_ssh_client.execute_some_command(error_log_cmd %("gwb01",rst[i]))
            print("本次重启时，在"+ rst[i] + "发生了问题！")
            print(error_log)
