#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

from rediscluster import RedisCluster

startup_nodes = [{"host": "10.91.19.114", "port": "6611"}]
rc = RedisCluster(startup_nodes=startup_nodes)
print(rc.get('alipay_nopwdpay_max_amount'))