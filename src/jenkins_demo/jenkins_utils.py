# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 下午3:10
# @Author  : YTQ
# @FileName: jenkins_utils.py
# @Software: PyCharm
import configparser
import datetime
import os

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
    return url,username,password

class JenkinsUtils:

    def __init__(self,chose):
        config = get_jk_config(chose)
        self.jk = Jenkins(*config)

    def ts(self):
        # print(self.jk[self.jk.keys()[0]].get_config())
        # v_k = {i[0]: list(i[1].keys()) for i in self.jk.views.iteritems()}
        # print(v_k)
        # print(self.jk.keys())
        # for job in self.jk.keys():
        #     if "testdemo" in job:
        #         my_job = self.jk.get_job(job)
        #         print(my_job.get_build(34).get_console())
        pass

    def get_jobs(self):
        return self.jk.keys()

    def get_job_from_keys(self,jobname):
        for my_job_name in self.jk.keys():
            if jobname in my_job_name:
                return my_job_name

    def jk_build_job(self,job_name):
        my_job_name = self.get_job_from_keys(job_name)
        if self.jk.has_job(my_job_name):
            my_job = self.jk.get_job(my_job_name)
            if not my_job.is_queued_or_running():
                try:
                    last_build = my_job.get_last_buildnumber()
                except Exception as e:
                    last_build = 0
                build_num = last_build+1
                # 开始打包
                try:
                    self.jk.build_job(my_job_name)
                except Exception as e:
                    log.error(e)

                # 循环判断Jenkins是否打包完成
                while True:
                    if not my_job.is_queued_or_running():
                        # 获取最新一次打包信息
                        count_build = my_job.get_build(build_num)
                        # 获取打包开始时间
                        start_time = count_build.get_timestamp()+datetime.timedelta(hours=8)
                        # 获取打包日志
                        console_out = count_build.get_console()
                        # 获取状态
                        status = count_build.get_status()
                        #获取变更内容
                        change = count_build.get_changeset_items()
                        log.info(str(start_time) + status)
                        log.info(change)
                        log.info(console_out)
                        break
            else:
                log.warning('Jenkins is running')
        else:
            log.warning('没有该服务')

if __name__ == '__main__':
    jk = JenkinsUtils('uat_jenkins')
    jk.jk_build_job("testdemo")