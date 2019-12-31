#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 上午10:08
# @Author  : ytq
# @FileName: build_job.py
# @Software: PyCharm
import threading
from time import sleep

from src.jenkins_demo.jenkins_utils import JenkinsUtils
from src.utils.log_utils import LogUtils

log = LogUtils()
class BuildJob:

    def __init__(self):
        pass

    def thread_build(self,th_id, job_name):
        jk = JenkinsUtils(th_id, job_name)
        try:
            jk.jk_build_job()
        except Exception as e:
            print(e)
        sleep(1)

    def do_build(self):
        while True:
            print("*" * 100)
            job_name = input("请输入你要构建的Job名：多个Job请以英文的逗号隔开。\n 单个任务构建可以采取模糊查询匹配，多个任务建议键入任务全名！\n")
            if job_name:
                joblist = job_name.split(",")
                threads = []
                nloops = range(len(joblist))
                for i in nloops:  # 根据输入的box进行多线程的创建
                    t = threading.Thread(target=self.thread_build, args=(i,joblist[i]))
                    threads.append(t)
                for i in nloops:  # start threads 此处并不会执行线程，而是将任务分发到每个线程，同步线程。等同步完成后再开始执行start方法
                    threads[i].start()
                for i in nloops:  # jion()方法等待线程完成
                    threads[i].join()
            else:
                log.warning("用户选择退出！")
                break

if __name__ == '__main__':
    rb = BuildJob()
    rb.do_build()