#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/9/27 22:12
# @Author  :ytq
# @File    :
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.sqlite_db.model import UserDatum as ud

cur_path = os.getcwd()
rootPath = cur_path[:cur_path.find("Test_dev_study/")+len("Test_dev_study/")]
sqlite_db_path = rootPath+"/src/sqlite_db/MySqlite.db"

def _to_dict(models):
    rtnList  = []
    if len(models) > 0:
        for model in models:
            user_dict =  {c.name: getattr(model, c.name) for c in model.__table__.columns}
            rtnList.append(user_dict)
        return rtnList
    else:
        return None

def _to_tuple(models):
    rtnList = []
    if len(models) > 0:
        for model in models:
            user_tuple = tuple(getattr(model, c.name) for c in model.__table__.columns)
            rtnList.append(user_tuple)
        return rtnList
    else:
        return None

class OrmDemo:
    def __init__(self,db_tb):
        self.engine = create_engine(r'sqlite:///%s'%sqlite_db_path)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.db_tb = db_tb

    def close_session(self):
        self.session.close()

    def fetch_as_dict(self,**kwargs):
        try:
            sql = self.session.query(self.db_tb).filter_by(**kwargs)
            data = self.session.query(self.db_tb).filter_by(**kwargs).all()
            print(sql)
            return _to_dict(data)
        except Exception as e:
            print(e)
        finally:
            self.close_session()

    def fetch_as_tuple(self,**kwargs):
        try:
            sql = self.session.query(self.db_tb).filter_by(**kwargs)
            data = self.session.query(self.db_tb).filter_by(**kwargs).all()
            print(sql)
            return _to_tuple(data)
        except Exception as e:
            print(e)
        finally:
            self.close_session()


if __name__ == '__main__':
    dic = dict()
    dic["env"] = "uat_pay_db"
    dic["cus_no"] = "30020161200000053"
    dic["has_used"] = "1"
    do_orm = OrmDemo(ud)
    data = do_orm.fetch_as_dict(**dic)
    print(data)