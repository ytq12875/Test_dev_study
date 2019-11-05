# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午4:23
# @Author  : YTQ
# @FileName: department.py
# @Software: PyCharm
import json

import requests

from src.utils.log_utils import LogUtils
from src.wework_request.api.base_api import BaseApi
from src.wework_request.api.wework import WeWork

log = LogUtils()

class Department(BaseApi):

    def __init__(self):
        super().__init__()
        self.dpt = self.ur.get_api("wework", "department")
        conct_secret = self.sr.get_secret_id("my_cor", "conct")
        self.access_token = WeWork().get_token(corpid=self.corpid,corpsecret=conct_secret)
        self.list_url = self.url + self.ur.get_api_by_parent("dpt_list", self.dpt)
        self.add_url = self.url + self.ur.get_api_by_parent("dpt_create", self.dpt)
        self.del_url = self.url + self.ur.get_api_by_parent("dpt_del", self.dpt)

    def department_list(self,_id = None):
        self.set_request_method(mode="http", method="get")
        self.set_url_params(access_token=self.access_token)
        ret = self.do_request(self.list_url).json()
        return ret

    def add_department(self,name,parentid,order,_id):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token = self.access_token)
        dic = {}
        dic["name"] = name
        dic["parentid"] = parentid
        dic["order"] = order
        dic["id"] = _id
        ret = self.do_request(self.add_url,data=json.dumps(dic)).json()
        log.info(ret)
        return ret

    def del_department(self,_id):
        self.set_request_method(mode="http", method="get")
        self.set_url_params(access_token = self.access_token,id=_id)
        ret = self.do_request(self.del_url).json()
        return ret