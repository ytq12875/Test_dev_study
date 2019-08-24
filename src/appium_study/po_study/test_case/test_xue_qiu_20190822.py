#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/22 20:27
# @Author  :ytq
from time import sleep

import pytest

from src.appium_study.po_study.page_active.optional_search_page import OptionalSearchPage


@pytest.mark.usefixtures("init_appium_driver")
class TestXueQiu0822:

    def test_add_optional(self,init_appium_driver):
        optional = OptionalSearchPage(init_appium_driver)
        optional.search_optional("alibaba")