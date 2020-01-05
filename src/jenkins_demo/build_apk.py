#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 下午2:18
# @Author  : ytq
# @FileName: build_apk.py
# @Software: PyCharm
import configparser
import datetime
import os
import re

from jenkinsapi.jenkins import Jenkins

from src.utils.log_utils import LogUtils

log = LogUtils()


def get_jk_config(chose):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'jenkins_server.ini'))
    username = config.get(chose, 'username')
    password = config.get(chose, 'password')
    host = config.get(chose, 'host')
    port = config.get(chose, 'port')
    url = "http://" + host + ":" + port
    return url, username, password


class BuildApk:

    def __init__(self):
        config = get_jk_config("apk_jk")
        self.jk = Jenkins(*config, useCrumb=True)

    def get_jobs(self):
        uat_job_list = []
        for _job in self.jk.keys():
            uat_job_list.append(_job)
        return uat_job_list

    def job_build(self):
        job_list = self.get_jobs()
        print("系统可以打包的apk：" + str(job_list))
        chose = input("选择要打包的apk，默认选择androidAPP-4.0 \n")
        job_name = ""
        if chose =="androidAPP-4.0":
            job_name = "androidAPP-4.0"
            my_job = self.jk.get_job(job_name)
            if not my_job.is_queued_or_running():
                try:
                    last_build = my_job.get_last_buildnumber()
                except Exception as e:
                    last_build = 0
                build_num = last_build + 1
                param = {}
                param["BUILD_CHANNAL"] = "preview"
                param["BUILD_FLAG"] = "ldygo"
                param["BUILD_MESSAGE"] = "jenkins构建-测试环境APP"
                param["BUILD_TYPE"] = "Debug"
                param["tinkerEnabled"] = "false"

                try:
                    self.jk.build_job(job_name,params=param)
                except Exception as e:
                    log.error(str(e))
                while True:
                    if not my_job.is_queued_or_running():
                        # 获取最新一次打包信息
                        count_build = my_job.get_build(build_num)
                        # 获取打包开始时间
                        start_time = count_build.get_timestamp() + datetime.timedelta(hours=8)
                        # 获取打包日志
                        console_out = count_build.get_console()
                        # 获取状态
                        status = count_build.get_status()
                        # 获取变更内容
                        change = count_build.get_changeset_items()
                        log.info(str(start_time) + " 发起的" + job_name + "构建已经完成，构建的状态为： " + status)
                        p2 = re.compile(r".*ERROR.*")
                        err_list = p2.findall(console_out)
                        if status == "SUCCESS":
                            if len(change) > 0:
                                for data in change:
                                    for file_list in data["affectedPaths"]:
                                        log.info(job_name + " 变更的类： " + file_list)
                                    log.info(job_name + " 变更的备注： " + data["msg"])
                                    log.info(job_name + " 变更的提交人： " + data["author"][
                                        "fullName"])
                            else:
                                log.info(job_name + " 本次构建没有变更内容！")
                            if len(err_list) > 0:
                                log.warning(job_name + "构建状态为成功，但包含了以下错误：")
                                for error in err_list:
                                    log.error(error)
                        else:
                            if len(err_list) > 0:
                                log.warning(job_name + "包含了以下错误：")
                                for error in err_list:
                                    log.error(error)
                        break


if __name__ == '__main__':
    ap = BuildApk()
    # print(ap.get_jobs())
    # ap.job_build()
    print("https://fir.im/z3yn")
