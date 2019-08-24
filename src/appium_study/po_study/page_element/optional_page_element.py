#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/23 22:13
# @Author  :ytq
from src.appium_study.po_study.page_element.main_page_element import MainPageElement


class OptionalPageElement(MainPageElement):
    optional_search = 'id=>action_search'
    optional_shares_list = 'id=>portfolio_stockName'
    snb_tip_wrapper = 'id=>snb_tip_text'
    optional_list = 'id=>portfolio_stockName'