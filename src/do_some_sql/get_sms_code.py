#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 下午3:13
# @Author  : ytq
# @FileName: get_sms_code.py
# @Software: PyCharm
import datetime
import os
import re

from src.utils.log_utils import LogUtils
from src.utils.mysql_connect_utils import MysqlConnect

path = os.path.dirname(os.getcwd()) + "/web_auto/config"
log = LogUtils()


class GetSmsCode:

    def __init__(self):
        env = input("请输入要查询的环境：\n1.===>融合测试环境\n2.===>预发布环境\n其他===>体验环境\n")
        if str(env) == "1":
            self.db_env = "uat"
        elif str(env) == "2":
            self.db_env = "pre"
        else:
            self.db_env = "ex"
        self.phone = input("请输入要查询的手机号：\n")
        self.month = datetime.datetime.now().strftime('%Y%m')
        self.cus_db = MysqlConnect(self.db_env + "_comm_db", path)

    def get_sms_code(self):
        sql_model = '''select sms_content from crp.notify_sms_send_record_%s where mobile = '%s'and template_id = 'SMS_RENT_20161201002'order by expect_send_time desc;'''
        code_sms = self.cus_db.doSelect(sql_model,(self.month,self.phone))
        if len(code_sms)>0:
            res = '(?<=验证码:).*?(?=，5分钟)'
            code = re.findall(res,code_sms[0][0])[0]
            if code:
                log.info( "查询的验证码为： " + code)
            else:
                log.warning("发生了异常")
        else:
            log.warning("无查询到短信")

if __name__ == '__main__':
    sc = GetSmsCode()
    sc.get_sms_code()