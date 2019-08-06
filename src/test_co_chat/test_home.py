#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:32
# @Author  :ytq
import random

import pytest

from src.test_co_chat.contact_page import ContactPage
from src.utils.random_name_phone import get_name, get_phone


@pytest.mark.usefixtures("init_driver")
class TestHome:
    def test_contact(self,init_driver):
        name = get_name()
        rd_phone = get_phone()
        tel_phone = str(random.randint(20000000, 88888888))
        contact = ContactPage(init_driver)
        tips = contact.add_member(name,rd_phone,tel_phone)
        print(tips)
        assert "保存成功" in tips
