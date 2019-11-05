# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午3:00
# @Author  : YTQ
# @FileName: wework.py
# @Software: PyCharm

from src.wework_request.api.base_api import BaseApi


class WeWork(BaseApi):

    def __init__(self):
        super().__init__()
        self.get_token_url = self.url + self.ur.get_api("wework","token")

    def get_token(self, corpid, corpsecret):
        self.set_request_method(mode="http",method="get")
        self.set_url_params(corpid=corpid,corpsecret=corpsecret)
        r = self.do_request(self.get_token_url).json()
        self.access_token = r["access_token"]
        return self.access_token