#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午5:17
# @Author  : ytq
# @FileName: do_back_use_yaml.py
# @Software: PyCharm

import json
import os

from src.back_money.common.data_collection import DataCollection
from src.back_money.common.read_yaml import YamlParser
from src.back_money.do_back_money.do_back_main import DoBackMoney
from src.back_money.do_back_money.selenium_utils import SeleniumUtils
from src.utils.common_str import CommonStr
from src.utils.log_utils import LogUtils
from src.utils.mysql_connect_utils import MysqlConnect

log = LogUtils()

path = os.path.dirname(os.getcwd()) + "/config"


class DoBackMoney_yaml(DoBackMoney):

    def __init__(self):
        super().__init__()
        self.yaml_read = YamlParser("return_cus", os.getcwd())

    def main(self):
        uat_cus_list = self.yaml_read.get_yaml_load_all()["uat"]
        pre_cus_list = self.yaml_read.get_yaml_load_all()["pre"]
        ex_cus_list = self.yaml_read.get_yaml_load_all()["ex"]
        if uat_cus_list is None and pre_cus_list is None and ex_cus_list is None:
            log.warning("没有退款数据！")
        else:
            if uat_cus_list:
                self.do_back(uat_cus_list, "uat")
            if pre_cus_list:
                self.do_back(pre_cus_list, "pre")
            if ex_cus_list:
                self.do_back(ex_cus_list, "ex")

    def do_back_money_not_input(self,db_env, user_env, cust_no):
        try:
            while True:
                json_list = self.make_json_list(db_env, cust_no)
                if json_list:
                    try:
                        self._refund(json_list,user_env, db_env)
                    except:
                        log.info("正在重试。。。。")
                else:
                    log.info("退款完成。。。。")
                    break
        except:
            log.warning("无可退还的支付数据或组装json数据出现了问题！")

    def do_back(self, cus_list: list, env):
        if env == 'uat':
            user_env = "uat"
            db_env = "uat_pay_db"
        elif env == 'pre':
            user_env = "pre"
            db_env = "pre_pay_db"
        else:
            user_env = "ex"
            db_env = "ex_db"
        for cus in cus_list:
            if len(str(cus))>11:
                cus_no = cus
            else:
                cus_no = self.get_cus_from_phone(cus,user_env)
            self.insert_will_back_value(cus_no, db_env)
            self.do_back_money_not_input(db_env, user_env, cus_no)


if __name__ == '__main__':
    do = DoBackMoney_yaml()
    do.main()
