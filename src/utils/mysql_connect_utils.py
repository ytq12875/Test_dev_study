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

    def doSelect(self, sql, condition=None):
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

    def execute_sql_file(self,file):
        conn = self.doConnect()
        cur = conn.cursor()
        try:
            ##读取SQL文件,获得sql语句的list
            with open(file, 'r+') as f:
                sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
                sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
            ##执行sql语句，使用循环执行sql语句
            for sql_item in sql_list:
                cur.execute(sql_item)
        except pymysql.Error as e:
            print(e)
        finally:
            cur.close()
            conn.commit()
            self.doClose()


if __name__ == '__main__':
    mc = MysqlConnect("uat_pay_db", path)
    sql_moude = ''' select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s') and biz_no not like 'TK%%'  '''
    sql_moude1 = ''' select bsm_jnl_no, cap_channel_no from pcenter.pay_consume_jnl where pay_order_no in (select pay_order_no from pcenter.pay_consume_order where cust_no = '%s') and biz_no not like 'TK_'  '''
    sql = sql_moude % "30020191102033004"
    sql1 = sql_moude1 % "30020191102033004"
    rst = mc.doSelect(sql)
    rst1 = mc.doSelect(sql1)
    print(rst)
    print(rst1)
    md = MysqlConnect("uat_cus_db", path)
    md.execute_sql_file('/home/ytq/data/03_mileage_insert.sql')
