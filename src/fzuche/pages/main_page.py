#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 上午11:52
# @Author  : ytq
# @FileName: main_page.py
# @Software: PyCharm
from time import sleep

from src.fzuche.base_object import BaseObject
from src.fzuche.page_element.main_page_elements import MainPageElements
from src.fzuche.pages import add_cus_page


class MainPage(BaseObject,MainPageElements):
    def __init__(self, driver):
        super().__init__(driver)

    def get_login_user(self):
        self.driver_wait_vist(self.user_msg)
        return self.get_tips(self.user_msg)

    def logout(self):
        self.driver_wait_vist(self.logout_btn)
        self.click_by_selector(self.logout_btn)
        self.click_by_selector(self.logout_qr_btn)
        return self

    def go_to_add_cus(self):
        self.driver_wait_clickable(self.manage_cus)
        while True:
            try:
                self.click_by_selector(self.manage_cus)
                self.click_by_selector(self.add_cus_link)
                return add_cus_page.AddCusPage(self.driver)
            except:
                self.log.warning("点击元素失败了，3秒后重试～")
                sleep(3)