# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午9:52
# @Author  : YTQ
# @FileName: my_driver.py
# @Software: PyCharm
from selenium import webdriver


def browser(browser):
    try:
        if browser == "chrome":
            path = "/home/ytq/webdriver/78.0.3904.70/chromedriver"
            driver = webdriver.Chrome(path)
            return driver
        elif browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        else:
            print("Not found this browser, You can enter 'chrome','firefox' or 'ie'")
    except Exception as msg:
        print ("%s" % msg)