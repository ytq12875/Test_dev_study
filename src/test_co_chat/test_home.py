#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:32
# @Author  :ytq
import random

import pytest

from src.test_co_chat.contact_page import ContactPage
from src.utils.common_str import CommonStr


@pytest.mark.usefixtures("init_driver")
class TestHome:
    def test_contact(self,init_driver):
        name = CommonStr().get_cn_char(3)
        rd_phone = str(random.randint(13000000000, 13900000000))
        tel_phone = str(random.randint(20000000, 88888888))
        contact = ContactPage(init_driver)
        tips = contact.add_member(name,rd_phone,tel_phone)
        print(tips)
        assert "保存成功" in tips
