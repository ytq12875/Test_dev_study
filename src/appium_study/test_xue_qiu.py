#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/15 22:12
# @Author  :ytq
# @File    :
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By


class TestXueQiu:

    def setup_method(self):
        server = 'http://localhost:4723/wd/hub'
        # app启动参数
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["autoGrantPermissions"] = True
        # 驱动
        self.driver = webdriver.Remote(server, desired_caps)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def goto_login_page(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/user_profile_icon").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/rl_login_phone").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_login_with_account").click()

    def test_wrong_phone(self):
        self.goto_login_page()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_account").send_keys("1225554555551154")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_password").send_keys("212242425")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/button_next").click()
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/md_content").text
        assert "手机号码填写错误" in text

    def test_wrong_password(self):
        self.goto_login_page()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_account").send_keys("13056886666")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_password").send_keys("212242425")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/button_next").click()
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/md_content").text
        assert "用户名或密码错误" in text

    @pytest.mark.parametrize("search,rst", [("alibaba", "阿里巴巴"), ("xiaomi", "小米"), ("google", "谷歌")])
    def test_search(self, search, rst):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys(search)
        self.driver.find_element(By.ID, "com.xueqiu.android:id/name").click()
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/stockName").text
        assert rst in text


if __name__ == '__main__':
    pytest.main()
