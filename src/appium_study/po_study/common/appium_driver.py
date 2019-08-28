#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/18 14:59
# @Author  :ytq
from appium import webdriver


class AppiumDriver:
    _server = 'http://localhost:4723/wd/hub'
    _platformName = "Android"
    _platformVersion = "6.0.1"
    _deviceName = "127.0.0.1:7555"
    _appPackage= "com.xueqiu.android"
    _appActivity= ".view.WelcomeActivityAlias"

    def __init__(self):
        server = self._server
        # app启动参数
        desired_caps = {}
        desired_caps["platformName"] = self._platformName
        desired_caps["platformVersion"] = self._platformVersion
        desired_caps["deviceName"] = self._deviceName
        desired_caps["appPackage"] = self._appPackage
        desired_caps["appActivity"] = self._appActivity
        desired_caps["autoGrantPermissions"] = True
        # 驱动
        self.driver = webdriver.Remote(server, desired_caps)
        self.driver.implicitly_wait(15)

    def quit_driver(self):
        self.driver.quit()