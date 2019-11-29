#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 上午8:27
# @Author  : ytq
# @FileName: request_api.py
# @Software: PyCharm
import json

import requests


def test_demo_api():
    base_url = 'http://localhost:9091'
    data = {"authRequest": {
        "userName": "user01",
        "password": "pwd"
    }}
    ret = requests.request('post', url=base_url + '/api/v1/user/login', data=json.dumps(data))
    access_token = ret.json()['access_token']
    headers = {'access_token': access_token}
    lst = requests.request('get', url=base_url + '/api/v1/menu/list', headers=headers)
    print(lst.json())
