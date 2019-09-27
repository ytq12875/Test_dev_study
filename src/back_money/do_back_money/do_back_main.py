#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json

from src.back_money.common.data_collection import DataCollection
from src.back_money.do_back_money.selenium_utils import SeleniumUtils
from src.utils.common_str import CommonStr
from src.utils.log_utils import LogUtils
from src.utils.mysql_connect_utils import MysqlConnect

log = LogUtils()


class DoBackMoney:

    def __init__(self):
        self.mydb = DataCollection()
        pass

    def get_all_back_value(self, cust_no, db_env, date=None):
        log.info("从服务器数据库中查询给定条件的退款数据...")
        if date:
            _sql = "select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s' and order_date ='%s')"
            get_value_sql = _sql % (cust_no, date)
        else:
            _sql = "select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s')"
            get_value_sql = _sql % (cust_no)
        db = MysqlConnect(db_env)
        log.info("服务器数据库执行sql：" + get_value_sql)
        rst = db.doSelect(get_value_sql)
        if len(rst) > 0:
            return list(rst)
        else:
            log.warning("服务端没有待退款的数据！")

    def insert_will_back_value(self, cust_no, db_env, date=None):
        insert_data = []
        log.info("从本地数据库读取待对比的数据...")
        db_has_data = self.mydb.fetchone(db_env, cust_no)
        for value in self.get_all_back_value(cust_no, db_env, date):
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
        '''{
    "payChannelNo": "1002",
    "bsmJnlNo": "100220190913174841ST90100625"
    }   '''
        rtn_list = []
        for value in self.mydb.fetchall(db_env, cus_no):
            dic = {}
            dic["payChannelNo"] = value[1]
            dic["bsmJnlNo"] = value[0]
            rtn_list.append(json.dumps(dic))
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

    def get_user_input(self):
        user_data = input("请输入待退款的信息：“环境（uat或者pre）,客户号,日期”，输入信息以英文的逗号隔开，如果要退客户名下全部支付金额则日期为空！\n")
        if user_data:
            data_list = user_data.split(",")
            if len(data_list) == 2 or len(data_list) == 3:
                if data_list[0] in ('uat', "pre"):
                    if len(data_list) == 3:
                        date = data_list[2]
                    else:
                        date = None
                    env = data_list[0]
                    if env == 'uat':
                        user_env = "uat"
                        db_env = "uat_pay_db"
                    else:
                        user_env = "pre"
                        db_env = "pre_db"
                    cust_no = data_list[1]
                    self.insert_will_back_value(cust_no, db_env, date)
                    return db_env, user_env, cust_no
                else:
                    log.error("输入的环境有误！")
            else:
                log.error("数据条件不满足，数据间由英文逗号分隔，至少输入环境和客户号，且最多输入环境、客户号、日期三项！")
        else:
            log.error("没有输入需要退还的数据！")

    def do_back_money(self, user="testUser", psw="1234abcd"):
        try:
            db_env, user_env, cust_no = self.get_user_input()
            try:
                json_list = self.make_json_list(db_env, cust_no)
                if json_list:
                    _selenium = SeleniumUtils(user_env)
                    rtn_json_list = _selenium.do_selenium(user, psw, json_list)
                    self.update_stutus(rtn_json_list, db_env)
            except:
                log.warning("无可退还的支付数据或组装json数据出现了问题！")
        except Exception as e:
            log.error(e)


if __name__ == '__main__':
    do = DoBackMoney()
    '''
    user_env = "uat"
    cust_no = "30020190802004051"
    cust_no = "30020190802003752"
    user_env = "pre"
    cust_no = "30020190800470254"
    date = "20190904"
    '''
    do.do_back_money()
