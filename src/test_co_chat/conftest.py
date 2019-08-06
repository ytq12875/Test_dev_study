#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:29
# @Author  :ytq
# @File    :
import time

import pytest
from src.test_co_chat.page_driver import PageDriver

@pytest.fixture
def init_driver():
    comm = PageDriver()
    driver = comm.driver
    yield driver
    time.sleep(2)
    comm.quit_driver()