#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import os
import sqlite3

from src.utils.log_utils import LogUtils

log = LogUtils()


class SqliteUtils:
    SHOW_SQL = True

    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = 'test.db'

    def get_conn(self):
        """
               获取数据库连接
               """
        try:
            conn = sqlite3.connect(self.path)

            """
            该参数是为了解决一下错误：
            ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str).
            It is highly recommended that you instead just switch your application to Unicode strings.
            """
            # conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
            conn.text_factory = str
            if os.path.exists(self.path) and os.path.isfile(self.path):
                log.info('本地数据库:[{}]'.format(self.path))
                return conn
        except sqlite3.OperationalError as e:
            log.error("Error:%s" % e)

    def get_cursor(self, conn):
        """
        该方法是获取数据库的游标对象，参数为数据库的连接对象
        """
        if conn is not None:
            return conn.cursor()
        else:
            return self.get_conn().cursor()

    def close_all(self, conn, cu):
        """
        关闭数据库游标对象和数据库连接对象
        """
        try:
            cu.close()
            conn.close()
        except sqlite3.OperationalError as e:
            log.info("Error:%s" % e)

    def create_table(self, sql, uni=None):
        """
        创建数据库表
        """
        if sql is not None and sql != '':
            conn = self.get_conn()
            cu = self.get_cursor(conn)
            if self.SHOW_SQL:
                log.info('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            if uni:
                cu.execute(uni)
            conn.commit()
            log.info('创建数据库表成功!')
            self.close_all(conn, cu)
        else:
            log.error('the [{}] is empty or equal None!'.format(sql))

    def drop_table(self, table):
        """
        如果表存在,则删除表
        """
        if table is not None and table != '':
            sql = 'DROP TABLE IF EXISTS ' + table
            if self.SHOW_SQL:
                log.info('执行sql:[{}]'.format(sql))
            conn = self.get_conn()
            cu = self.get_cursor(conn)
            cu.execute(sql)
            conn.commit()
            log.info('删除数据库表[{}]成功!'.format(table))
            cu.close()
            conn.close()
            # self.close_all(conn, cu)
        else:
            log.error('the [{}] is empty or equal None!'.format(table))

    def insert(self, sql, data):
        """
        插入数据
        """
        if sql is not None and sql != '':
            if data is not None:
                conn = self.get_conn()
                cu = self.get_cursor(conn)
                for d in data:
                    try:
                        if self.SHOW_SQL:
                            log.info('执行sql:[{}],参数:[{}]'.format(sql, d))
                        cu.execute(sql, d)
                        conn.commit()
                    except Exception as e:
                        log.error(e)
                self.close_all(conn, cu)
        else:
            log.error('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self, sql):
        """
        查询所有数据
        """
        if sql is not None and sql != '':
            conn = self.get_conn()
            cu = self.get_cursor(conn)
            if self.SHOW_SQL:
                log.info('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                # for e in range(len(r)):
                #     print(r[e])
                # return r[e]
                return r
            self.close_all(conn, cu)
        else:
            log.error('the [{}] is empty or equal None!'.format(sql))

    def fetchone(self, sql, data):
        """
        查询一条数据
        """
        if sql is not None and sql != '':
            if data is not None:
                # Do this instead
                d = (data,)
                conn = self.get_conn()
                cu = self.get_cursor(conn)
                if self.SHOW_SQL:
                    log.info('执行sql:[{}],参数:[{}]'.format(sql, data))
                cu.execute(sql, d)
                r = cu.fetchall()
                if len(r) > 0:
                    # for e in range(len(r)):
                    #     print(r[e])
                    return r
                self.close_all(conn, cu)
            else:
                log.error('the [{}] equal None!'.format(data))
        else:
            log.error('the [{}] is empty or equal None!'.format(sql))

    def update(self, sql, data):
        """
        更新数据
        """
        if sql is not None and sql != '':
            if data is not None:
                conn = self.get_conn()
                cu = self.get_cursor(conn)
                for d in data:
                    if self.SHOW_SQL:
                        log.info('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            log.error('the [{}] is empty or equal None!'.format(sql))

    def delete(self, sql, data):
        """
        删除数据
        """
        if sql is not None and sql != '':
            if data is not None:
                conn = self.get_conn()
                cu = self.get_cursor(conn)
                for d in data:
                    if self.SHOW_SQL:
                        log.info('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            log.error('the [{}] is empty or equal None!'.format(sql))


if __name__ == '__main__':
    dbfile = 'MySqlite.db'
    mydb = SqliteUtils(dbfile)
    # create_table_sql = '''CREATE TABLE Product1
    #             (
    #             ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #             Name NVARCHAR(100) NOT NULL)'''
    # mydb.create_table(create_table_sql)
    # sql = '''INSERT INTO Product1 VALUES(?, ?)'''
    # data = [(None, 'Dave'),
    #         (None, 'cndba'),
    #         (None, 'oracle'),
    #         (None, 'Python')]
    # mydb.insert(sql, data)
    # mydb.drop_table('Product')
    fech_sql = '''SELECT * FROM Product1 where ID >?'''
    print(mydb.fetchone(fech_sql, 0))
