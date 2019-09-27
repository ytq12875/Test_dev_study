#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

import redis

pool = redis.ConnectionPool(host='10.91.19.114', port=6611)
r = redis.Redis(connection_pool=pool)
for key in r.keys():
    key_str = str(key, encoding = "utf-8")
    if "SESSION" not in key_str:
        print(key_str)