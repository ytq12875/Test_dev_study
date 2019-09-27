#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/9/27 22:12
# @Author  :ytq
# @File    :
import os

from src.sqlite_db import model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(r'sqlite:///D:\Users\ytq\PycharmProjects\TestHome\src\sqlite_db\MySqlite.db')
Session = sessionmaker(bind=engine)
session = Session()
sql = session.query(model.UserDatum).filter_by(env='uat_pay_db')
data = session.query(model.UserDatum).filter_by(env='uat_pay_db').all()
print(sql)
print(data)
def to_dict(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}
for i in data:
    data_dict = to_dict(i)
    print(data_dict)
# data = model.UserDatum.