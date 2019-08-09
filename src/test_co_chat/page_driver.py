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
        "wwrtx.vst": "Xl490ntPOinUxbDnqm5peNdRgQgLc3CsH_6a3qC4UMLInFQCIVcwGit5YOT_IQLTnaJOKp6U8MZ_TFRq2l8JWkfGIpO4QOwt012XX7mdEtgjROQJfWJXWoIzTLkVHdQsXbGNUE9ECwstqMpBA7nQ3hYz0LZEM_H0CfZbjaQwT-Edvp7YcZKC2s-z5Hls3K3SpyL9b2v_woE64n0wjqSfJlBGeCxPG225g2WRDT_RHgYjSOw8FOrwn1db9eELR5Ln6t0ee7rgcHQn2qQghX3NMg",
        "wwrtx.d2st": "a4621756",
        "wwrtx.sid": "bI84_UY69ZZEAv63EF98PZ8jftV9qZlSmLRX3xrBhMYAQfgzConbN31MUIQJU7K9",
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