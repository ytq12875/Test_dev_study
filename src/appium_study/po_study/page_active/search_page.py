#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/22 20:27
# @Author  :ytq
from src.appium_study.po_study.page_active.base_object import BaseObject
from src.appium_study.po_study.page_element.search_page_element import SearchPageElement


class SearchPage(BaseObject,SearchPageElement):

    def search_thing(self,value):
        self.click_el(self.main_search)
        self.send_value(self.search_form,value)

    def get_rst(self):
        pass
