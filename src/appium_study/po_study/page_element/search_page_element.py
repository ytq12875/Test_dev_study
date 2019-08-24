#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/22 20:27
# @Author  :ytq
from src.appium_study.po_study.page_element.main_page_element import MainPageElement


class SearchPageElement(MainPageElement):
    search_form = 'id=>search_input_text'
    cancel_button = 'xpath=>//*[@text="取消"]'
    first_choose = 'id=>name'
    search_result_list = ''
