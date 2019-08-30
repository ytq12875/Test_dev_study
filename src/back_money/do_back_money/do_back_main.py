#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json

from src.back_money.do_back_money.selenium_utils import SeleniumUtils
from src.utils.mysql_connect_utils import MysqlConnect


class DoBackMoney:

    def __init__(self):
        pass

    def get_will_back_value(self, cust_no, date, db_env):
        _sql = "select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s'  and order_date ='%s' and refundable_amount > 0)"
        get_value_sql = _sql % (cust_no, date)
        db = MysqlConnect(db_env)
        rst = db.doSelect(get_value_sql)
        return list(rst)


    def make_json_list(self, cust_no, date, db_env):
        '''{
    "payChannelNo": "1002",
    "bsmJnlNo": "100220190726160036ST90100022"
    }   '''
        rtn_list = []
        for value in self.get_will_back_value(cust_no, date, db_env):
            if value[0] and value[1] in ("1001", "1002"):
                dic = {}
                dic["payChannelNo"] = value[1]
                dic["bsmJnlNo"] = value[0]
                rtn_list.append(json.dumps(dic))
        return rtn_list


    def do_back_money(self, user_env, cust_no, date, db_env, user="testUser", psw="1234abcd"):
        _selenium = SeleniumUtils(user_env)
        json_list = self.make_json_list(cust_no, date, db_env)
        _selenium.do_selenium(user, psw, json_list)


if __name__ == '__main__':
    do = DoBackMoney()
    user_env = "uat"
    db_env = "uat_pay_db"
    cust_no = "30020190802003752"
    date = "20190820"
    do.do_back_money(user_env, cust_no, date, db_env)
