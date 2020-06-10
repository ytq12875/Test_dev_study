#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/22 20:27
# @Author  :ytq
from time import sleep

import pytest
from appium.webdriver.extensions.android.gsm import GsmCallActions

from src.appium_study.po_study.page_active.base_object import BaseObject
from src.appium_study.po_study.page_active.optional_search_page import OptionalSearchPage


@pytest.mark.usefixtures("init_appium_driver")
class TestXueQiu0822:

    def test_add_optional(self,init_appium_driver):
        optional = OptionalSearchPage(init_appium_driver)
        optional.search_optional("alibaba")

    def test_network(self,init_appium_driver):
        "GsmCallActions.CALL"
        base = BaseObject(init_appium_driver)
        base.send_sms("18129802968","hello~~")
        sleep(10)
        base.gsm_call("18129802968",GsmCallActions.CALL)
        pass