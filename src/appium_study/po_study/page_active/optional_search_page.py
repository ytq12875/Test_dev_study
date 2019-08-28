#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/24 19:45
# @Author  :ytq
from src.appium_study.po_study.page_active.optional_page import OptionalPage
from src.appium_study.po_study.page_element.search_page_element import SearchPageElement


class OptionalSearchPage(OptionalPage,SearchPageElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.goto_search()

    def search_optional(self,name):
        self.send_value(self.search_form,name)
        self.click_el(self.first_choose)

    def add_optional(self):
        pass