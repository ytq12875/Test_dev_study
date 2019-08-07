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
        "wwrtx.vst": "z5MPCJhGiUIYWLX-bNupDcZgPS9okqBw9QN8Tb4OQcbr3u7MGORPLoyFoHdF1yOgYLaMC6j9gekp5xXOZ0774uYId-YqSlonh2oSJeAsi6c1NQZ-XPlrvaKQjuiFIDyf8Zbu-tVhz6-j5cZUNyCE9IY2taNIbbV3y4-gG_POjMx7ss5S_kO7eYg8dqH_dblQYv4u86xJtpA94l4Ta9PkDHwrt7ZVDGiAjClSEbh7DXLozfkIeVMjEMn6Yhqpg9VTziJKfvkUiweEeXLtG1L3Mw",
        "wwrtx.d2st": "a3206199",
        "wwrtx.sid": "bI84_UY69ZZEAv63EF98PURkGCRy_oHAIxhOEMzrylxsRzT-YmbWXnQi9ARqTb2j",
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