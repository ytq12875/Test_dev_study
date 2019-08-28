#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/22 20:27
# @Author  :ytq
import time

import pytest

from src.appium_study.po_study.common.appium_driver import AppiumDriver


@pytest.fixture
def init_appium_driver():
    comm = AppiumDriver()
    driver = comm.driver
    yield driver
    time.sleep(2)
    comm.quit_driver()