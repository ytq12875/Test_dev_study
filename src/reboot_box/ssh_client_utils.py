#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

import sys
from paramiko import AuthenticationException
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import NoValidConnectionsError

from src.utils.log_utils import LogUtils

log = LogUtils()
class MySshClient():
    def __init__(self):
        self.ssh_client = SSHClient()

    # 此函数用于输入用户名密码登录主机
    def ssh_login(self,host_ip,username,password):
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(host_ip,port=22,username=username,password=password)
        except AuthenticationException:
            log.warning('username or password error')
            return 1001
        except NoValidConnectionsError:
            log.warning('connect time out')
            return 1002
        except:
            log.warning('unknow error')
            log.warning("Unexpected error:"+sys.exc_info()[0])
            return 1003
        return 1000

    # 此函数用于执行command参数中的命令并打印命令执行结果
    def execute_some_command(self,command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return  stdout.read().decode().strip()

    # 此函数用于退出登录
    def ssh_logout(self):
        log.warning('will exit host')
        self.ssh_client.close()

if __name__ == '__main__':
    # 远程主机IP
    host_ip = '10.91.18.102'
    # 远程主机用户名
    username = 'tomcat'
    # 远程主机密码
    password = 'ldygo@9012!@#$%&*#'
    # 要执行的shell命令；换成自己想要执行的命令
    # 自己使用ssh时，命令怎么敲的command参数就怎么写
    command = 'cd /qhapp/apps/lo-boxs/P0611/;tail -n 100 boxlogs/lifecycle.log'
    # 实例化
    my_ssh_client = MySshClient()
    # 登录，如果返回结果为1000，那么执行命令，然后退出
    if my_ssh_client.ssh_login(host_ip, username, password) == 1000:
        log.warning(f"{host_ip}-login success, will execute command：{command}")
        # chan = my_ssh_client.ssh_client.invoke_shell()
        # chan.send(command)
        # print(chan.recv(1000).decode())
        logs = my_ssh_client.execute_some_command(command)
        print(logs)
        my_ssh_client.ssh_logout()