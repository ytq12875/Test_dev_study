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
    def __init__(self, env, box, del_cache="y"):
        ym = YamlParser("server_host", os.getcwd())
        self.env = env
        self.data = ym.get_yaml_data(self.env)
        self.user = self.data["user"]
        self.psd = self.data["psw"]
        self.my_ssh_client = MySshClient()
        self.box = box
        self.del_cache = del_cache

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
            log.info("开始连接"+self.env+"环境的BOX: "+self.box+" ,IP为: "+self.host)
            return self.my_ssh_client.ssh_login(self.host, self.user, self.psd)
        else:
            log.error("输入的BOX不在对应的环境中或者BOX不存在！")

    def check_box_from_host(self):
        if self.connect_host() == 1000:
            log.info("连接服务器IP：" + self.host + "成功！")
            box_list = self.my_ssh_client.execute_some_command('cd /qhapp/apps/lo-boxs/;ls')
            box_list = box_list.split("\n")
            if self.box in box_list:
                log.info("BOX："+self.box+"在"+self.env+"环境的服务器 "+self.host+"中存在！")
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
        log.info("执行命令："+command)
        logs = self.my_ssh_client.execute_some_command(command)
        while True:
            sleep(10)
            if "onAllGearsStarted end" in logs:
                log.info(logs)
                log.info("已经完成对"+self.env+"环境的BOX：" + self.box + "的重启！")
                self.my_ssh_client.ssh_logout()
                break
            else:
                log.info("等待重启完成......")
                log_command = 'cd /qhapp/apps/lo-boxs/%s/;tail -n 30 boxlogs/lifecycle.log'
                logs = self.my_ssh_client.execute_some_command(log_command % self.box)

    def do_reboot(self):
        if self.check_box_from_host():
            self.execute_reboot_command()
        else:
            log.warning("BOX不在host中，请参照svn最新的环境信息更新server_host.yaml")


if __name__ == '__main__':

    def do_reboot_box():
        while True:
            env = input("请输入你要重启的环境序号：\n1.===>融合测试环境\n2.===>预发布环境\n其他输入===>退出\n")
            if str(env) in ("1", "2"):
                if str(env) == "1":
                    env_choose = "uat"
                else:
                    env_choose = "pre"
                box_name = input("请输入你要重启的BOX名：\n ")
                del_cache = input("是否清除缓存（y/n）输入非n/N的值则默认清除缓存！：\n")
                rb = RebootBox(env_choose, box_name, del_cache)
                try:
                    rb.do_reboot()
                except Exception as e:
                    print(e)
                sleep(1)
            else:
                log.warning("用户选择退出！")
                break


    do_reboot_box()