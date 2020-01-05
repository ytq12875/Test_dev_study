#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 上午11:52
# @Author  : ytq
# @FileName: test_app_random_click.py
# @Software: PyCharm

import random
import time

import pymysql
from appium import webdriver

class  TestAPP12():

    def setup(self):
        desired_caps = {
            'platformName': 'Android',  # 系统
            # 'deviceName': '3HX0217311002113',  # 手机设备号；通过adb devices获得
            'deviceName' : '55057881',
            'platformVersion': 9,  # 安卓版本号
            'appPackage': "com.ldygo.qhzc",  # 包名
            'appActivity': 'ui.home.HomeActivity',  # 活动名（各个手机系统内可能不一样）
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'newCommandTimeout': 6000,
            "autoGrantPermissions": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 调起联动云租车
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def  test_123(self):

        self.driver.find_element_by_id("com.ldygo.qhzc:id/btn_pos").click()
        try:
            self.driver.find_element_by_id("com.ldygo.qhzc:id/iv_moregift_close").click()
        except:
            pass
        self.driver.find_element_by_id("com.ldygo.qhzc:id/iv_home_me").click()
        self.driver.find_element_by_id("com.ldygo.qhzc:id/phone_number").send_keys("17607660940")
        self.driver.find_element_by_id("com.ldygo.qhzc:id/login_btn").click()
        self.driver.find_element_by_id("com.ldygo.qhzc:id/tv_smscode_login").click()
        self.driver.find_element_by_id("com.ldygo.qhzc:id/et_register_code").send_keys("ljy17607660940")
        self.driver.find_element_by_id("com.ldygo.qhzc:id/login_btn").click()
        self.driver.find_element_by_id("com.ldygo.qhzc:id/iv_home_me").click()
        self.driver.find_element_by_id("com.ldygo.qhzc:id/rl_center_wallet").click()
        self.driver.find_element_by_id("com.ldygo.qhzc:id/bn_wallet_input").click()
        # todo: 循环点击或者输入
        fina = ""
        for i in range(10):
            # but_lis = ["50元","100元","200元","500元","1000元","2000元"]
            but_lis = ["5元","10元","20元","30元","50元","80元"]
            chose = random.choice(["1", "2"])
            if chose =="1":
                fina = self.xpath_name(but_lis)
            else:
                fina =self.put_in()
        print(fina)
        # self.driver.find_element_by_xpath('//*[@text="100元"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.ldygo.qhzc:id/payChannelsView"]/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()
        self.driver.find_element_by_id('com.ldygo.qhzc:id/tv_charge_money').click()
        self.driver.find_element_by_id('com.tencent.mm:id/m1').click()


    def xpath_name(self,lis:list):
        path =  random.choice(lis)
        path = "//[contains(text,'%s')]"% path
        # self.driver.find_element_by_xpath(path).click()
        self.driver.find_element_by_android_uiautomator(path).click()
        return path

    def put_in(self):
        money = str(random.randint(1,8000))
        self.driver.find_element_by_id('com.ldygo.qhzc:id/et_money').send_keys(money)
        # el.click()
        # time.sleep(1)
        # el.send_keys(money)
        return money

    def monkey_check(self, sql, host="10.91.19.100", port=3321, username='ldyop', password='Ldyop123@ldygo.com'):
            """select : sql
            输出：fetchall()"""
            db = pymysql.connect(
                host=host,
                port=port,
                user=username,
                password=password,
                # database='um',
                charset='utf8',
            )
            curcor = db.cursor()
            curcor.execute(sql)
            data = curcor.fetchall()
            db.close()
            return data


if __name__ == '__main__':
    pass
