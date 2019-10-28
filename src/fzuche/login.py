#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午12:36
# @Author  : ytq
# @FileName: login.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver

_path = "/home/ytq/webdriver/78.0.3904.70/chromedriver"
_com_url = "http://10.90.136.105:23024/zugou-management/login.html"
driver = webdriver.Chrome(_path)
driver.get(_com_url)
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_name("j_username").send_keys("0120171000001451")
driver.find_element_by_name("j_password").send_keys("ldy001451")
driver.find_element_by_name("ok").click()
sleep(5)
print(driver.find_element_by_css_selector("#link-user").text)
driver.find_element_by_css_selector(".dropdown-toggle").click()
driver.quit()
