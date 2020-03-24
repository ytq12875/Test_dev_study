#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午2:00
# @Author  : ytq
# @FileName: get_token.py
# @Software: PyCharm
import os

import requests

from src.baiduAIApi.utils.read_yaml import YamlParser


class TokenUtil:

    def __init__(self):
        cur_path = os.path.dirname(os.path.dirname(__file__))
        file_path = cur_path + '/config'
        self.config = YamlParser('acount_info.yaml',file_path)
        self.token_url = "https://aip.baidubce.com/oauth/2.0/token"

    def get_ocr_token(self):
        self.ocr_config = self.config.get_yaml_data("ocrStudy")
        post_data = {}
        post_data["grant_type"] = "client_credentials"
        post_data["client_id"] = self.ocr_config["API Key"]
        post_data["client_secret"] = self.ocr_config["Secret Key"]
        res = requests.request("post",self.token_url,data=post_data)
        return res.json()["access_token"]


if __name__ == '__main__':
    tk = TokenUtil()
    print(tk.get_ocr_token())