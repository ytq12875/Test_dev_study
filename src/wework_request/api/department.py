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
        corpid = "ww75abb8519b57cec6"
        conct_secret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"
        self.access_token = WeWork().get_token(corpid=corpid,corpsecret=conct_secret)

    def department_list(self,_id = None):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {"access_token": self.access_token, "id": _id}
        ret = requests.request("get", url=url, params=params, headers=self.headers).json()
        return ret

    def add_department(self,name,parentid,order,_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {"access_token":self.access_token}
        dic = {}
        dic["name"] = name
        dic["parentid"] = parentid
        dic["order"] = order
        dic["id"] = _id
        ret = requests.request("post",url=url,params =params, data=json.dumps(dic),headers = self.headers).json()
        log.info(ret)
        return ret

    def del_department(self,_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params = {"access_token": self.access_token,"id":_id}
        ret = requests.request("get", url=url, params=params,headers=self.headers).json()
        return ret