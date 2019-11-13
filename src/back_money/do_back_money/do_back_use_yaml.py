#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午5:17
# @Author  : ytq
# @FileName: do_back_use_yaml.py
# @Software: PyCharm

#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json
import os

from src.back_money.common.data_collection import DataCollection
from src.back_money.common.read_yaml import YamlParser
from src.back_money.do_back_money.selenium_utils import SeleniumUtils
from src.utils.common_str import CommonStr
from src.utils.log_utils import LogUtils
from src.utils.mysql_connect_utils import MysqlConnect

log = LogUtils()

path = os.path.dirname(os.getcwd()) + "/config"


class DoBackMoney:

    def __init__(self):
        self.mydb = DataCollection()
        self.yaml_read = YamlParser("return_cus",os.getcwd())

    def get_all_back_value(self, cust_no, db_env):
        log.info("从服务器数据库中查询给定条件的退款数据...")
        _sql = "select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s')"
        get_value_sql = _sql % (cust_no)
        db = MysqlConnect(db_env, path)
        log.info("服务器数据库执行sql：" + get_value_sql)
        rst = db.doSelect(get_value_sql)
        if len(rst) > 0:
            return list(rst)
        else:
            log.warning("服务端没有待退款的数据！")

    def insert_will_back_value(self, cust_no, db_env):
        insert_data = []
        log.info("从本地数据库读取待对比的数据...")
        db_has_data = self.mydb.fetchone(db_env, cust_no)
        service_list = self.get_all_back_value(cust_no, db_env)
        if service_list:
            for value in self.get_all_back_value(cust_no, db_env):
                if db_has_data:
                    if value[0] and value[1] in ("1001", "1002") and value not in db_has_data:
                        insert_data.append(value)
                else:
                    if value[0] and value[1] in ("1001", "1002"):
                        insert_data.append(value)
            if insert_data:
                try:
                    self.mydb.insert_data(insert_data, db_env, cust_no)
                except:
                    pass
            else:
                log.info("无需要插入本地数据库的数据！")

    def make_json_list(self, db_env, cus_no):
        rtn_list = []
        try:
            for value in self.mydb.fetchall(db_env, cus_no):
                dic = {}
                dic["payChannelNo"] = value[1]
                dic["bsmJnlNo"] = value[0]
                rtn_list.append(json.dumps(dic))
            return rtn_list
        except:
            log.error("客户 "+str(cus_no) +" 没有可还的数据！")
            return rtn_list

    def update_stutus(self, jsonlist, db_env):
        update_lis = []
        for json_value in jsonlist:
            '''
            返回值responseCode为000000时为处理成功状态，为664002时则是流水号不存在
            '''
            rtn_msg = json.loads(json_value)["rtn_msg"]
            rtn_code = json.loads(rtn_msg)["responseCode"]
            if rtn_code == "000000" or rtn_code == "664002":
                tup_a = (CommonStr().get_time_vale(), rtn_code, rtn_msg, json.loads(json_value)["bsmJnlNo"], db_env)
                update_lis.append(tup_a)
        self.mydb.update(update_lis)

    def main(self):
        uat_cus_list = self.yaml_read.get_yaml_load_all()["uat"]
        pre_cus_list = self.yaml_read.get_yaml_load_all()["pre"]
        ex_cus_list = self.yaml_read.get_yaml_load_all()["ex"]
        if uat_cus_list is None and pre_cus_list is None and ex_cus_list is None:
            log.warning("没有退款数据！")
        else:
            if uat_cus_list:
                self.do_back(uat_cus_list,"uat")
            if pre_cus_list:
                self.do_back(pre_cus_list, "pre")
            if ex_cus_list:
                self.do_back(ex_cus_list, "ex")

    def do_back(self,cus_list:list,env):
        json_list = []
        if env == 'uat':
            user_env = "uat"
            db_env = "uat_pay_db"
        elif env == 'pre':
            user_env = "pre"
            db_env = "pre_db"
        else:
            user_env = "ex"
            db_env = "ex_db"

        for uat_cus in cus_list:
            self.insert_will_back_value(uat_cus, db_env)
            json_list+=self.make_json_list(db_env, uat_cus)
            # print(json_list)
        if json_list:
            _selenium = SeleniumUtils(user_env)
            rtn_json_list = _selenium.do_selenium(json_list)
            self.update_stutus(rtn_json_list, db_env)
        else:
            log.warning("所有的客户都退款完成或者无可退还的数据！")



if __name__ == '__main__':
    do = DoBackMoney()
    do.main()