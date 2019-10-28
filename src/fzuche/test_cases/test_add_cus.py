#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午1:23
# @Author  : ytq
# @FileName: test_add_cus.py
# @Software: PyCharm
from time import sleep

import pytest

from src.fzuche.pages.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestAddCus:

    @pytest.mark.parametrize("id,psw", [('0120171000001451', 'ldy001451')])
    def test_add_cus(self,init_driver,id,psw):
        login = LoginPage(init_driver, id, psw)
        add_cus = login.jump_to_main().go_to_add_cus()
        add_cus.add_cus()
        assert "成功" in add_cus.get_msg()