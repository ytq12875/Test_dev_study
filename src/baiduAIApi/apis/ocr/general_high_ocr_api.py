#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午3:31
# @Author  : ytq
# @FileName: general_ocr_api.py
# @Software: PyCharm
import base64

import requests

from src.baiduAIApi.common.get_action_url import ActionUrl
from src.baiduAIApi.common.get_token import TokenUtil


class GeneralHighOcr:

    def __init__(self):
        ocr_base_url = ActionUrl().get_ocr_url("general_high")
        access_token = TokenUtil().get_ocr_token()
        self.url = ocr_base_url + "?access_token=" + access_token
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def package_data(self, pic):
        file = open(pic, 'rb')
        img = base64.b64encode(file.read())
        self.ocr_data = {}
        self.ocr_data["image"] = img

    def discern(self,pic):
        self.package_data(pic)
        res = requests.request("post",self.url,headers=self.headers,data = self.ocr_data)
        rst_list = res.json()["words_result"]
        for rst in rst_list:
            print(rst["words"])


if __name__ == '__main__':
    go = GeneralHighOcr()
    go.discern("screenshot.png")