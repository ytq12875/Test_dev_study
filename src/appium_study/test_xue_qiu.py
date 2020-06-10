#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/15 22:12
# @Author  :ytq
# @File    :
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestXueQiu:

    def setup_method(self):
        server = 'http://localhost:4723/wd/hub'
        # app启动参数
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "myDevice"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["autoGrantPermissions"] = True
        # desired_caps["dontStopAppOnReset"] = True
        # desired_caps["noReset"] = True
        desired_caps["skipServerInstallation"] = True
        desired_caps["skipDeviceInitialization"] = True
        # 驱动
        self.driver = webdriver.Remote(server, desired_caps)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def goto_login_page(self):
        self.driver.find_element(By.XPATH, "//*[@text='我的']").click()
        # self.driver.find_element(By.ID, "user_profile_icon").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_login_phone").click()
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
        print(self.driver.page_source)
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys(search)
        print(self.driver.page_source)
        self.driver.find_element(By.ID, "com.xueqiu.android:id/name").click()
        print(self.driver.page_source)
        self.driver.find_element(*self.text("加自选")).click()
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/stockName").text
        assert rst in text

    def text(self,key):
        return (By.XPATH,"//*[@text='%s']"%key)


if __name__ == '__main__':
    pytest.main()
