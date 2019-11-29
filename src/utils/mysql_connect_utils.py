#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import os

import pymysql

from src.back_money.common.read_yaml import YamlParser

path = os.path.dirname(os.getcwd()) + "/back_money/config"


class MysqlConnect(object):

    def __init__(self, db, give_path, schema=None):
        dbconfig_file = YamlParser("dbconfig", give_path)
        config = dbconfig_file.get_yaml_data(db)
        self.host = config.get("host")
        self.port = config.get("port")
        self.user = config.get("user")
        self.passwd = config.get("passwd")
        self.schema = schema

    def doConnect(self):
        """获取数据库连接"""
        connect = pymysql.Connect(
            host=self.host,
            port=int(self.port),
            user=self.user,
            passwd=self.passwd,
            db=self.schema,
            charset='utf8'
        )
        return connect

    def doClose(self):
        """关闭数据库连接"""
        self.doConnect().close()

    def doSelect(self, sql, condition=''):
        """查询"""
        try:
            conn = self.doConnect()
            cur = conn.cursor()
            if condition:
                cur.execute(sql % condition)
            else:
                cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as msg:
            print(msg)
            return msg
        finally:
            cur.close()
            self.doClose()


    # 增删改
    def doChange(self, sql, cond):
        flag = 0
        conn = self.doConnect()
        cur = conn.cursor()
        try:
            cur.execute(sql % cond)
            conn.commit()
            flag = 1
            return flag
        except Exception as msg:
            conn.rollback()
            return msg
        finally:
            cur.close()
            self.doClose()



if __name__ == '__main__':
    mc = MysqlConnect("uat_pay_db",path)
    rst = mc.doSelect(
        "select bsm_jnl_no,cap_channel_no from pcenter.pay_consume_jnl where cust_no = '30020190802003752'")
    print(rst)
