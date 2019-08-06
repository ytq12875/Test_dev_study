#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 0:20
# @Author  :ytq
# @File    :
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject:

    def __init__(self,driver):
        self.driver = driver

    def driver_wait_vist(self,*args):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.visibility_of_element_located(*args))

    def driver_wait_no_vist(self,*args):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.invisibility_of_element_located(*args))