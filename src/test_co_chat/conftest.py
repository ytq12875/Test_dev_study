#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:29
# @Author  :ytq
# @File    :
import time

import pytest

from selenium import webdriver

_path = "D:/webdriver/chromedriver.exe"
_com_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
_cookies = {
    "wwrtx.vst":"c1PYtzMPFGO51fyUwiyOB9zdluxzdDyAFucTU1mTCfugwqFyJaE1TtxyLmAv7Jr9yUxQ959NjTZmDu4l5u36Yv6zwZKc855bkH-lvjQ9WgPiEoFinXkuAs2LuZTNZJFvwBfg1v5hL6LNnwepLxkXWmhR22FGUA3dtd1A9bL4tvfGbntz__81Y-egAeIZlZUMqJnlTuvNSkoSZlXT7XCqMEmTg7-B2_xildQIOtVe3wXJOYrxUGzQtG9YfUE0z64BvAud9VYplVdJpoXD1zc8yQ",
    "wwrtx.d2st": "a5511426",
    "wwrtx.sid": "bI84_UY69ZZEAv63EF98PeDT7MfcNn513_x7YceTVRvUw21C_lCip48A-LyF_Pt7",
    "wwrtx.ltype": "1",
    "wxpay.corpid": "1970324940078869",
    "wxpay.vid": "1688851793816595",
}


@pytest.fixture
def init_driver():
    driver = webdriver.Chrome(_path)
    driver.get(_com_url)
    for k, v in _cookies.items():
        driver.add_cookie({"name": k, "value": v})
    driver.get(_com_url)
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.quit()