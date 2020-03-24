#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import datetime
import os
import re
import time
from time import sleep

from src.web_auto.common.read_yaml import YamlParser
from src.reboot_box.ssh_client_utils import MySshClient
from src.utils.log_utils import LogUtils

log = LogUtils()


class RebootBox:

    def __init__(self, th_id, env, box, del_cache="y"):
        ym = YamlParser("server_host", os.getcwd())
        self.env = env
        self.data = ym.get_yaml_data(self.env)
        self.user = self.data["user"]
        self.psd = self.data["psw"]
        self.my_ssh_client = MySshClient()
        self.box = box
        self.del_cache = del_cache
        self.th_id = th_id
        # self.now_time = datetime.datetime.now().strftime('%H:%M:%S')

    def get_host_from_box(self):
        for key in self.data.keys():
            if "host" in key:
                if self.box in self.data[key]["box"]:
                    self.host = self.data[key]["url"]
            else:
                self.host = None

    def connect_host(self):
        self.get_host_from_box()
        if self.host:
            log.info(str(self.th_id) + "线程：开始连接" + self.env + "环境的BOX: " + self.box + " ,IP为: " + self.host)
            return self.my_ssh_client.ssh_login(self.host, self.user, self.psd)
        else:
            log.error(str(self.th_id) + "线程：输入的BOX：" + self.box + "不在本地配置文件中！")

    def check_box_from_host(self):
        if self.connect_host() == 1000:
            log.info(str(self.th_id) + "线程：连接服务器IP：" + self.host + "成功！")
            server_time = self.my_ssh_client.execute_some_command("date")
            self.now_time = re.findall("[0-2][0-9]:[0-5][0-9]:[0-5][0-9]",server_time)[0]
            box_list = self.my_ssh_client.execute_some_command('cd /qhapp/apps/lo-boxs/;ls')
            box_list = box_list.split("\n")
            if self.box in box_list:
                log.info(str(self.th_id) + "线程：BOX：" + self.box + "在" + self.env + "环境的服务器 " + self.host + "中存在！")
                return True
            else:
                self.my_ssh_client.ssh_logout()
                return False

    def execute_reboot_command(self):
        if self.del_cache == "n" or self.del_cache == "N":
            command_moudle = 'cd /qhapp/apps/lo-boxs/%s/;sh shutdown-box.sh %s; ./launch-box.sh ;'
        else:
            command_moudle = 'cd /qhapp/apps/lo-boxs/%s/; sh shutdown-box.sh %s; rm -rf /qhapp/apps/lo-boxs/repository/com/ldygo/zuche-*; ./launch-box.sh ;'
        command = command_moudle % (self.box, self.box)
        log.info(str(self.th_id) + "线程：执行命令：" + command)
        self.my_ssh_client.execute_some_command(command)
        while True:
            sleep(2)
            if self.is_reboot_success():
                log.info(str(self.th_id) + "线程：已经完成对" + self.env + "环境的BOX：" + self.box + "的重启！")
                self.my_ssh_client.ssh_logout()
                break
            elif self.is_reboot_Fail():
                log.error(
                    str(self.th_id) + "线程：出错了，" + self.env + "环境的BOX: " + self.box + "重启的错误为：" + self.is_reboot_Fail())
                self.my_ssh_client.ssh_logout()
                break
            else:
                # log.info(str(self.th_id) + "线程：等待重启完成......")
                pass

    def is_reboot_success(self):
        log_command = " cd /qhapp/apps/lo-boxs/%s/;cat boxlogs/lifecycle.log| grep 'onAllGearsStarted end'|awk -F' ' '{print $2}'|awk -F'.' '{print $1}' "
        logs = self.my_ssh_client.execute_some_command(log_command % self.box).split("\n")
        rst = [x for x in logs if x != '']
        for i in range(len(rst)):
            if time.strptime(rst[i], "%H:%M:%S") >= time.strptime(self.now_time, "%H:%M:%S"):
                return True

    def is_reboot_Fail(self):
        log_command = " cd /qhapp/apps/lo-boxs/%s/;cat boxlogs/lifecycle.log| grep 'ERROR'|awk -F' ' '{print $2}'|awk -F'.' '{print $1}' "
        logs = self.my_ssh_client.execute_some_command(log_command % self.box).split("\n")
        rst = [x for x in logs if x != '']
        for i in range(len(rst)):
            if time.strptime(rst[i], "%H:%M:%S") >= time.strptime(self.now_time, "%H:%M:%S"):
                error_log_cmd = "cd /qhapp/apps/lo-boxs/%s/boxlogs; grep -A 10 -i '%s.[0-9][0-9][0-9].ERROR' lifecycle.log"
                error_log = self.my_ssh_client.execute_some_command(error_log_cmd % (self.box, rst[i]))
                return error_log

    def do_reboot(self):
        if self.check_box_from_host():
            self.execute_reboot_command()
        else:
            log.warning(str(self.th_id) + "线程：BOX：" + self.box + "不在host中，请参照svn最新的环境信息更新server_host.yaml")
