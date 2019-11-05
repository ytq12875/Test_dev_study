# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午4:39
# @Author  : YTQ
# @FileName: base_api.py
# @Software: PyCharm
import requests

from src.utils.log_utils import LogUtils
from src.wework_request.data.secret_reader import SecretReader
from src.wework_request.data.url_reader import UrlReader

log = LogUtils()

class BaseApi:

    def __init__(self):
        self.sr = SecretReader()
        self.ur = UrlReader()
        self.headers = {"Content-Type": "application/json;charset=utf-8"}
        self.corpid = self.sr.get_cor_id("my_cor")
        self.url = self.ur.get_url("wework")

    def set_url_params(self,**kwargs):
        self.params = kwargs

    def set_request_method(self,mode = "http",method = None):
        self.mode = mode
        self.method = method

    def do_request(self,url,data =None):
        if self.mode == "http":
            if self.method:
                ret = requests.request(self.method, url= url,params=self.params,data =data, headers = self.headers)
                return ret
            else:
                log.error("http通讯方式method不能为空！")