#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 21:48
# @Author  :ytq
# @File    :
from selenium import webdriver


class PageDriver:
    _path = "D:/webdriver/chromedriver.exe"
    _com_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    _cookies = {
        "wwrtx.vst": "dExeoXB4slzS37UoTRk1NlSj4vejhGwEU7uQ2wHAeojQulGuewaNI_lLmrtZc330zBBkX5PYw7nv7jFglmA3FNdP8JLX_soEepRYqSAzqcuoERzV1KRSDrWEDf_ENUdpJxuvBbwCGBD3jkxtuZaa-MsuXyp0Clm3MTLZ_F88ZcmiLLCiMJTAOGkS8cHNzMpQn4BpoO6SO4GdoWPl14NTAxss7hzpQKALAzOIuhbhCzw817QIVu_Ytxq1oh86nErQeIndyOuCU1Sk1V72pyHTFA",
        "wwrtx.d2st": "a9524691",
        "wwrtx.sid": "bI84_UY69ZZEAv63EF98PRRsBEtWnrohlRLQgxwNu_v2qmCZpYPjjStw7EyDTXxu",
        "wwrtx.ltype": "1",
        "wxpay.corpid": "1970324940078869",
        "wxpay.vid": "1688851793816595",
    }

    def __init__(self):
        self.driver = webdriver.Chrome(self._path)
        self.driver.get(self._com_url)
        self.driver.maximize_window()
        for k, v in self._cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(self._com_url)
        self.driver.implicitly_wait(5)


    def quit_driver(self):
        self.driver.quit()