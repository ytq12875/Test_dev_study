#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/16 下午5:01
# @Author  : ytq
# @FileName: box_reboot.py
# @Software: PyCharm
import threading
from time import sleep

from src.reboot_box.reboot_box_utils import RebootBox
from src.utils.log_utils import LogUtils

log = LogUtils()

class BoxReboot:

    def __init__(self):
        pass

    def thread_reboot(self,th_id, env_choose, box_name, del_cache):
        rb = RebootBox(th_id, env_choose, box_name, del_cache)
        try:
            rb.do_reboot()
        except Exception as e:
            print(e)
        sleep(1)

    def do_reboot_box(self):
        while True:
            env = input("请输入你要重启的环境序号：\n1.===>融合测试环境\n2.===>预发布环境\n其他输入===>退出\n")
            if str(env) in ("1", "2"):
                if str(env) == "1":
                    env_choose = "uat"
                else:
                    env_choose = "pre"
                box_name = input("请输入你要重启的BOX名：多个BOX请以英文的逗号隔开。\n ").strip()
                boxlist = box_name.split(",")
                del_cache = input("是否清除缓存（y/n）输入非n/N的值则默认清除缓存！：\n")
                threads = []
                nloops = range(len(boxlist))
                for i in nloops:  # 根据输入的box进行多线程的创建
                    t = threading.Thread(target=self.thread_reboot, args=(i, env_choose, boxlist[i], del_cache))
                    threads.append(t)
                for i in nloops:  # start threads 此处并不会执行线程，而是将任务分发到每个线程，同步线程。等同步完成后再开始执行start方法
                    threads[i].start()
                for i in nloops:  # jion()方法等待线程完成
                    threads[i].join()
            else:
                log.warning("用户选择退出！")
                break

if __name__ == '__main__':
    rb = BoxReboot()
    rb.do_reboot_box()