# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 下午9:51
# @Author  : YTQ
# @FileName: test_log_demo.py
# @Software: PyCharm
import datetime
import os
import time

from src.reboot_box.ssh_client_utils import MySshClient

# time_str = datetime.datetime.now().strftime('%H:%M:%S')
time_str = "09:00:22"
def test_demo():
    my_ssh_client = MySshClient()
    my_ssh_client.ssh_login("10.91.18.102", "tomcat", "ldygo@9012!@#$%&*#")
    if is_reboot_success(my_ssh_client,"E0011"):
        print("重启成功")
    if is_reboot_Fail1(my_ssh_client,"E0011"):
        print(is_reboot_Fail1(my_ssh_client,"E0011"))

def is_reboot_success(my_ssh_client,box):
    log_command = " cd /qhapp/apps/lo-boxs/%s/;cat boxlogs/lifecycle.log| grep 'onAllGearsStarted end'|awk -F' ' '{print $2}'|awk -F'.' '{print $1}' "
    logs = my_ssh_client.execute_some_command(log_command % box).split("\n")
    rst = [x for x in logs if x != '']
    print(rst)
    for i in range(len(rst)):
        if time.strptime(rst[i], "%H:%M:%S") >= time.strptime(time_str, "%H:%M:%S"):
            return True

def is_reboot_Fail(my_ssh_client,box):
    log_command = " cd /qhapp/apps/lo-boxs/%s/;cat boxlogs/lifecycle.log| grep 'ERROR'|awk -F' ' '{print $2}'|awk -F'.' '{print $1}' "
    logs = my_ssh_client.execute_some_command(log_command % box).split("\n")
    rst = [x for x in logs if x != '']
    for i in range(len(rst)):
        if time.strptime(rst[i], "%H:%M:%S") >= time.strptime(time_str, "%H:%M:%S"):
            error_log_cmd = "cd /qhapp/apps/lo-boxs/%s/boxlogs; grep -A 48 -i '%s.[0-9][0-9][0-9].ERROR' lifecycle.log"
            error_log = my_ssh_client.execute_some_command(error_log_cmd % (box, rst[i]))
            return error_log

def is_reboot_Fail1(my_ssh_client,box):
    log_command = " cd /qhapp/apps/lo-boxs/%s/boxlogs/2020-03-05/;cat lifecycle.2020-03-05.1.log| grep 'ERROR'|awk -F' ' '{print $2}'|awk -F'.' '{print $1}' "
    logs = my_ssh_client.execute_some_command(log_command % box).split("\n")
    rst = [x for x in logs if x != '']
    for i in range(len(rst)):
        if time.strptime(rst[i], "%H:%M:%S") >= time.strptime(time_str, "%H:%M:%S"):
            error_log_cmd = "cd /qhapp/apps/lo-boxs/%s/boxlogs/2020-03-05/; grep -E'[(%s.[0-9][0-9][0-9].ERROR)|(Caused by:)]' lifecycle.2020-03-05.1.log"
            error_log = my_ssh_client.execute_some_command(error_log_cmd % (box, rst[i]))
            return error_log