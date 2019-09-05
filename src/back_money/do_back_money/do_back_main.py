#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json

from src.back_money.do_back_money.data_collection import DataCollection
from src.back_money.do_back_money.selenium_utils import SeleniumUtils
from src.utils.common_str import CommonStr
from src.utils.log_utils import LogUtils
from src.utils.mysql_connect_utils import MysqlConnect

log = LogUtils()

class DoBackMoney:

    def __init__(self):
        self.mydb = DataCollection()
        pass

    def get_all_back_value(self, cust_no, db_env,date=None):
        if date:
            _sql = "select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s' and order_date ='%s')"
            get_value_sql = _sql % (cust_no,date)
        else:
            _sql = "select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s')"
            get_value_sql = _sql % (cust_no)
        db = MysqlConnect(db_env)
        rst = db.doSelect(get_value_sql)
        return list(rst)

    def insert_will_back_value(self,cust_no,db_env,date=None):
        insert_data = []
        for value in self.get_all_back_value(cust_no, db_env, date):
            if value[0] and value[1] in ("1001", "1002"):
                insert_data.append(value)
        try:
            self.mydb.insert_data(insert_data,db_env)
        except:
            pass


    def make_json_list(self,db_env):
        '''{
    "payChannelNo": "1002",
    "bsmJnlNo": "100220190726160036ST90100022"
    }   '''
        rtn_list = []
        for value in self.mydb.fetchall(db_env):
            dic = {}
            dic["payChannelNo"] = value[1]
            dic["bsmJnlNo"] = value[0]
            rtn_list.append(json.dumps(dic))
        return rtn_list

    def update_stutus(self,jsonlist,db_env):
        update_lis = []
        for json_value in jsonlist:
            tup_a = (CommonStr().get_time_vale(),json.loads(json_value)["bsmJnlNo"],db_env)
            update_lis.append(tup_a)
        self.mydb.update(update_lis)


    def do_back_money(self, env, cust_no, user="testUser", psw="1234abcd"):
        if env =='uat':
            user_env = "uat"
            db_env = "uat_pay_db"
        else :
            user_env = "pre"
            db_env = "pre_db"
        self.insert_will_back_value(cust_no, db_env)
        try:
            json_list = self.make_json_list(db_env)
            if json_list:
                _selenium = SeleniumUtils(user_env)
                _selenium.do_selenium(user, psw, json_list)
                self.update_stutus(json_list,db_env)
        except:
            log.info("无可退还的支付数据")


if __name__ == '__main__':
    do = DoBackMoney()
    user_env = "uat"
    cust_no = "30020190802003752"

    # user_env = "pre"
    # cust_no = "30020190800470254"

    # date = "20190904"

    do.do_back_money(user_env, cust_no)
