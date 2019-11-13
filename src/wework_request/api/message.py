#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 上午11:48
# @Author  : ytq
# @FileName: message.py
# @Software: PyCharm
from src.wework_request.api.base_api import BaseApi
from src.wework_request.api.wework import WeWork


class Message(BaseApi):

    def __init__(self):
        super().__init__()
        self.msg = self.ur.get_api("wework", "message")
        msg_secret = self.sr.get_secret_id("my_cor", "send_msg")
        self.access_token = WeWork().get_token(corpid=self.corpid, corpsecret=msg_secret)
        self.send_msg_url = self.url + self.ur.get_api_by_parent("send_msg", self.msg)

    def send_msg(self,touser,toparty,totag):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token=self.access_token)
        text_msg={}
        text_msg["touser"] = touser
        text_msg["toparty"] = toparty
        text_msg["totag"] = totag
        text_msg["msgtype"] = "text"
