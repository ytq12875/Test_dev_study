#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 下午4:50
# @Author  : ytq
# @FileName: white_list.py
# @Software: PyCharm
import os

from src.utils.log_utils import LogUtils
from src.utils.mysql_connect_utils import MysqlConnect

path = os.path.dirname(os.getcwd()) + "/back_money/config"
log = LogUtils()

class WhiteList:
    def __init__(self):
        env = input("请输入要插入白名单的环境：\n1.===>融合测试环境\n2.===>预发布环境\n其他===>体验环境\n")
        if str(env) == "1":
            self.db_env = "uat"
        elif str(env) == "2":
            self.db_env = "pre"
        else:
            self.db_env = "ex"
        self.pay_db = MysqlConnect(self.db_env + "_pay_db", path)
        self.cus_db = MysqlConnect(self.db_env + "_cus_db", path)

    def add_white_list(self,phone):
        if len(phone) == 11:
            cus_no = self.get_cus_no(phone)
        elif len(phone) == 17:
            cus_no = phone
        else:
            cus_no = None
        if cus_no:
            sql_model = '''INSERT INTO pcenter.pay_catalog (`group_name`, `item_value`, `item_title`, `seq_no`, `date_created`, `date_updated`,
                                     `create_by`, `update_by`)
    VALUES ('test_white_list', '%s', '测试白名单', '1', NULL, NULL, NULL, NULL)'''
            flag = self.pay_db.doChange(sql_model,cus_no)
            if flag == 1:
                log.info('客户手机/客户号'+ phone + '白名单插入成功')
            elif "PRIMARY" in str(flag):
                log.warning('客户手机/客户号'+ phone + '白名单插入失败： 白名单已经存在！')
            else:
                log.error('客户手机/客户号'+ phone + '白名单插入失败： ' + str(flag))
        else:
            log.warning('客户手机/客户号'+ phone + '客户不存在！')

    def get_cus_no(self,phone):
        sql_model = '''select um_no from um.um_user_info_base where mobile_phone = '%s' '''
        cus_rst = self.cus_db.doSelect(sql_model,phone)
        if cus_rst:
            return cus_rst[0][0]

    def do_insert_white(self):
        phone_list:list = input("请输入要插入白名单的手机或者客户号：（以英文的逗号分割）\n").strip().split(",")
        for phone in phone_list:
            self.add_white_list(phone)



if __name__ == '__main__':
    do = WhiteList()
    do.do_insert_white()