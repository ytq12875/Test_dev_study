#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:29
# @Author  :ytq
# @File    :
import time

import pytest

from src.fzuche.driver.chrome_driver import PageDriver
from src.utils.log_utils import LogUtils

log = LogUtils()
@pytest.fixture
def init_driver():
    log.info("初始化driver...")
    comm = PageDriver()
    driver = comm.driver
    log.info("执行测试函数...")
    yield driver
    time.sleep(2)
    log.info("退出driver...")
    comm.quit_driver()