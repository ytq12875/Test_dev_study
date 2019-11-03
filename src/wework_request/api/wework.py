# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午3:00
# @Author  : YTQ
# @FileName: wework.py
# @Software: PyCharm
import requests


class WeWork:
    access_token = None
    corpid = "ww75abb8519b57cec6"
    conct_secret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"

    def __init__(self):
        pass

    def get_token(self, corpid=None, corpsecret=None):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        if self.access_token is None and corpid is None and corpsecret is None:
            r = requests.get(url, params={"corpid": self.corpid, "corpsecret": self.conct_secret}).json()
            self.access_token = r["access_token"]
        elif self.access_token is None and corpid and corpsecret:
            r = requests.get(url, params={"corpid": corpid, "corpsecret": corpsecret}).json()
            self.access_token = r["access_token"]
        return self.access_token
