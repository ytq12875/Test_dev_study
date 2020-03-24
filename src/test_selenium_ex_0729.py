#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/7/29 21:52
# @Author  :ytq
import os
from time import sleep

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.my_driver import browser
from selenium.webdriver.chrome.webdriver import RemoteWebDriver
from src.utils.log_utils import LogUtils

log = LogUtils()
class TestSeleniumEx:

    # 初始化，制定驱动路径并最大化浏览器和设置隐式等待
    def setup(self):
        log.info("初始化chrome：")
        self.driver = browser("chrome")
        # chrome_options = Options()
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--user-data-dir')
        # chrome_options.add_argument('--dns-prefetch-disable')
        # chrome_options.add_argument('--lang=en-US')
        # chrome_options.add_argument('--disable-setuid-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # self.driver = RemoteWebDriver("http://localhost:5001/wd/hub")
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # 清理，关闭驱动
    def teardown_method(self):
        log.info("退出driver......")
        self.driver.quit()

    # 进入社区，测试查看最新发布的第一个帖子
    # @pytest.mark.skip
    def test_last_article(self):
        self.driver.find_element(By.LINK_TEXT, "社区").click()
        self.driver.find_element(By.LINK_TEXT, "最新发布").click()
        # 强行等待，不然会点击到首页的帖
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a').click()
        # 随意取一个参照点进行断言。。。
        sleep(3)
        assert "次阅读" in self.driver.page_source

    # 社区访问霍格沃兹测试学院，断言未登录是被拒绝的
    # @pytest.mark.skip
    @pytest.mark.parametrize("home", [("霍格沃兹测试学院")])
    def test_no_login_visit(self, home):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, home).click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/a').click()
        sleep(3)
        assert "访问被拒绝，你可能没有权限或未登录。" in self.driver.page_source

    # 错误用户名和密码登陆
    # @pytest.mark.skip
    @pytest.mark.parametrize("name,psw", [("lisi", "123456"), ("zhangsan", "454521")])
    def test_error_login(self, name, psw):
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.NAME, "user[login]").send_keys(name)
        self.driver.find_element(By.ID, "user_password").send_keys(psw)
        self.driver.find_element(By.NAME, "commit").click()
        sleep(3)
        assert "没有该用户，请您重新注册。" or "帐号或密码错误。" or "由于多次密码错误，您的帐号已被暂时锁定" or "Invalid Login" in self.driver.page_source

    # 搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的
    # @pytest.mark.skip
    @pytest.mark.parametrize("seek_text,rst_css,rst_text", [("测试媛", '[href="/topics/4331"]',"TesterHome 测试媛组织成立啦")])
    def test_query(self, seek_text, rst_css,rst_text):
        self.driver.find_element(By.NAME, "q").send_keys(seek_text)
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, rst_css).click()
        sleep(3)
        assert rst_text in self.driver.find_element(By.CSS_SELECTOR,
                                                    '.media-body .media-heading').text


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml/','--clean-alluredir'])
    # 拼接cmd命令并执行
    rep_path = os.getcwd()
    print(rep_path)

    rep_cmd = "allure generate report/xml -o report/html"
    command = 'cd {0} && {1}'.format(rep_path,rep_cmd)
    os.system(command)