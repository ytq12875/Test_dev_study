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
        "wwrtx.vst": "Nq1Up4blYq_PiiV37S9Y53Vjd_qXrqVAAZmesrAwrAF8VvmJqNADsT_Hk890jSkZBdLB33qTjkGsUCE264eRvJdX5cqTbjfJ_nSAm4UWZFIfXvCubG_BDk-0OKiVGXGVemJkbpw2WTDAPWv7xOpLdEfD5pVJe4c1J4O6XMX-uf4V5_90XorWjiZO3ya_QXpwf5lHXJJOm2A4yTD2VwOrtESFH46ZRdk91mjV8AUsxP5nYVebKJj3B9UrC9dGthMaZnZDR6S4YdhAcPyCY29fvA",
        "wwrtx.d2st": "a1320545",
        "wwrtx.sid": "bI84_UY69ZZEAv63EF98PeFtW_oIfsQGXCLA8IB51oF2d8RO1orD0ekRDp_GPiZq",
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