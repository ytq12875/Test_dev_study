#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
from src.back_money.do_back_money.sqlite_utls import SqliteUtils
from src.utils.common_str import CommonStr
from src.utils.log_utils import LogUtils

log = LogUtils()

class DataCollection:

    def __init__(self):
        dbfile = 'MySqlite.db'
        self.mydb = SqliteUtils(dbfile)

    def create_table_data_table(self):
        create_table_sql = '''CREATE TABLE user_data
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        env NVARCHAR(100) NOT NULL,
                        bsm_jnl_no NVARCHAR(100) NOT NULL,
                        pay_channel_no NVARCHAR(100) NOT NULL,
                        has_used NVARCHAR(100) NOT NULL,
                        insert_time datetime,
                        update_time datetime)'''
        uni = 'CREATE UNIQUE INDEX udx_env_jnl ON user_data (env,bsm_jnl_no,pay_channel_no)'
        self.mydb.create_table(create_table_sql,uni=uni)

    def insert_data(self,lis,env):
        insert_sql = '''INSERT INTO user_data VALUES(?, ?, ?, ?, ?, ?, ?)'''
        new_list = []
        for i in lis:
            i = list(i)
            i.insert(0, None)
            i.insert(1, env)
            i.insert(4, '0')
            i.insert(5,CommonStr().get_time_vale())
            i.insert(6,'')
            i = tuple(i)
            new_list.append(i)
        self.mydb.insert(insert_sql, new_list)

    def update(self,lis):
        """s
        更新数据
        """
        log.info('更新已经使用过的数据状态...')
        update_sql = '''UPDATE user_data SET has_used = '1',update_time = ? WHERE bsm_jnl_no = ? and env = ? '''
        self.mydb.update(update_sql, lis)

    def fetchall(self,env):
        """
        查询所有数据
        """
        log.info('查询所有未进行退款数据...')
        fetchall_sql = '''SELECT bsm_jnl_no,pay_channel_no FROM user_data where has_used = '0' and env = ?'''
        return self.mydb.fetchone(fetchall_sql,env)

if __name__ == '__main__':
    do = DataCollection()
    do.create_table_data_table()