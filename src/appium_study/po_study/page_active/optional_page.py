#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/23 22:12
# @Author  :ytq

from src.appium_study.po_study.page_active.main_page import MainPage
from src.appium_study.po_study.page_element.optional_page_element import OptionalPageElement


class OptionalPage(MainPage,OptionalPageElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.goto_optional()
        try:
            self.tap_in_cor(400,600) #处理蒙层
        except:
            pass

    def goto_search(self):
        self.click_el(self.optional_search)

    def get_optional_values(self):
        list = self.find_elements(self.optional_list)
        for i in list:
            print(i.text)