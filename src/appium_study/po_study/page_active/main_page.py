#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/23 22:28
# @Author  :ytq
from src.appium_study.po_study.page_active.base_object import BaseObject
from src.appium_study.po_study.page_element.main_page_element import MainPageElement


class MainPage(BaseObject,MainPageElement):

    def goto_optional(self):
        self.click_el(self.optional_button)