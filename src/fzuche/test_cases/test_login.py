#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 上午11:25
# @Author  : ytq
# @FileName: test_login.py
# @Software: PyCharm

import pytest

from src.fzuche.pages.login_page import LoginPage
from src.fzuche.pages.main_page import MainPage


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.parametrize("id,psw,log_name",[('0120171000001451','ldy001451','徐小川')])
    def test_login_success(self,init_driver,id,psw,log_name):
        login = LoginPage(init_driver,id,psw)
        main = login.jump_to_main()
        assert log_name ==main.get_login_user()
        main.logout()