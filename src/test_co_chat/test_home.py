#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:32
# @Author  :ytq
import random
import sys

import pytest

from src.test_co_chat.contact_page import ContactPage
from src.test_co_chat.profile_page import ProfilePage
from src.utils.log_utils import LogUtils
from src.utils.random_name_phone import get_name, get_phone

log = LogUtils()


@pytest.mark.usefixtures("init_driver")
class TestHome:

    def test_contact(self, init_driver):
        test_name = self.__class__.__name__ + "." + sys._getframe().f_code.co_name
        log.info("执行测试：" + test_name)
        name = get_name()
        rd_phone = get_phone()
        tel_phone = str(random.randint(20000000, 88888888))
        contact = ContactPage(init_driver)
        contact.add_member(name, rd_phone, tel_phone)
        tips = contact.get_contact_tips()
        assert "保存成功" in tips
        log.info(test_name + " 执行成功")

    @pytest.mark.parametrize("rd_phone,tel_phone", [(get_phone(), str(random.randint(20000000, 88888888)))])
    def test_profile_edit(self, init_driver, rd_phone, tel_phone):
        edit_member = ProfilePage(init_driver)
        edit_member.edit_member(rd_phone, tel_phone)
        tips = edit_member.get_edit_tips()
        assert "保存成功" in tips

    def test_unused_member(self, init_driver):
        unuse = ProfilePage(init_driver)
        rst = unuse.unused_member()
        if rst:
            assert "用户不是正常状态！" in rst
        else:
            tips = unuse.get_edit_tips()
            assert "禁用成功" in tips

    def test_used_member(self, init_driver):

        unuse = ProfilePage(init_driver)
        rst = unuse.used_member()
        if rst:
            assert "用户不是禁用状态！" in rst
        else:
            tips = unuse.get_edit_tips()
            assert "启用成功" in tips


if __name__ == '__main__':
    pytest.main(["-sv"])
