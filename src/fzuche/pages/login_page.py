#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 上午11:30
# @Author  : ytq
# @FileName: login_page.py
# @Software: PyCharm
from src.fzuche.base_object import BaseObject
from src.fzuche.page_element.login_page_elements import LoginPageElements
from src.fzuche.pages import main_page
from src.fzuche.pages.main_page import MainPage


class LoginPage(BaseObject,LoginPageElements):
    def __init__(self, driver,id,psw):
        super().__init__(driver)
        self.id = id
        self.psw = psw

    def login_sys(self):
        self.driver_wait_vist(self.login_name)
        self.send_value(self.login_name,self.id)
        self.send_value(self.login_psw,self.psw)
        self.click_by_selector(self.login_btn)
        return main_page

    def jump_to_main(self):
        return self.login_sys().MainPage(self.driver)