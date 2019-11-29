#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import os
from time import sleep

from src.back_money.common.read_yaml import YamlParser
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

    def get_host_from_box(self):
        for key in self.data.keys():
            if "host" in key:
                if self.box in self.data[key][1]["box"]:
                    self.host = self.data[key][0]
            else:
                self.host = None

    def connect_host(self):
        self.get_host_from_box()
        if self.host:
            log.info(str(self.th_id) + "线程：开始连接" + self.env + "环境的BOX: " + self.box + " ,IP为: " + self.host)
            return self.my_ssh_client.ssh_login(self.host, self.user, self.psd)
        else:
            log.error(str(self.th_id) + "线程：输入的BOX："+self.box+"不在本地配置文件中！")

    def check_box_from_host(self):
        if self.connect_host() == 1000:
            log.info(str(self.th_id) + "线程：连接服务器IP：" + self.host + "成功！")
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
        logs = self.my_ssh_client.execute_some_command(command)
        while True:
            sleep(10)
            if "onAllGearsStarted end" in logs:
                log.info(str(self.th_id) + "线程：已经完成对" + self.env + "环境的BOX：" + self.box + "的重启！")
                self.my_ssh_client.ssh_logout()
                break
            elif "ERROR" in logs:
                log.info(logs)
                log.info(str(self.th_id) + "线程：出错了，" + self.env + "环境的BOX：" + self.box + "重启失败！")
                self.my_ssh_client.ssh_logout()
                break
            else:
                log.info(str(self.th_id) + "线程：等待重启完成......")
                log_command = 'cd /qhapp/apps/lo-boxs/%s/;tail -n 100 boxlogs/lifecycle.log'
                logs = self.my_ssh_client.execute_some_command(log_command % self.box)

    def do_reboot(self):
        if self.check_box_from_host():
            self.execute_reboot_command()
        else:
            log.warning(str(self.th_id) + "线程：BOX："+self.box+"不在host中，请参照svn最新的环境信息更新server_host.yaml")