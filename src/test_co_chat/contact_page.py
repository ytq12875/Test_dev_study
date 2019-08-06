#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 22:06
# @Author  :ytq
import random

from selenium.webdriver.common.by import By

from src.test_co_chat.BaseObject import BaseObject
from src.utils.common_str import CommonStr
from src.utils.random_name_phone import get_post


class ContactPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.comm_str = CommonStr()

    def add_member(self,name,rd_phone,tel_phone):
        self.driver_wait_vist((By.XPATH, '//*[@id="menu_index"]/span'))
        self.driver.find_element(By.ID, "menu_contacts").click()
        self.driver_wait_vist((By.ID, "member_list"))
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
        # 上传头像
        self.driver.find_element(By.ID, "js_upload_file").click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input').send_keys(
            "E:/pic/demo.png")
        self.driver_wait_vist((By.CSS_SELECTOR, ".js_file_reupload"))
        self.driver.find_element(By.CSS_SELECTOR, ".js_save").click()
        # 等待上传头像窗口消失
        self.driver_wait_no_vist((By.CSS_SELECTOR, ".js_file_reupload"))
        # 输入各input框
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys(name + "别名")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(rd_phone + "@qq.com")
        # 把所有选择radio放入selects变量中
        selects = self.driver.find_elements(By.CSS_SELECTOR, ".member_edit_item_right .ww_radio")
        random.choice(selects[:2]).click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(rd_phone)
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys("0755" + tel_phone)
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(rd_phone + "@qq.com")
        self.driver.find_element(By.ID, "memberEdit_address").send_keys(self.comm_str.get_cn_char(8))
        self.driver.find_element(By.ID, "memberAdd_title").send_keys(get_post())
        random.choice(selects[2:4]).click()
        random.choice(selects[4:6]).click()
        # 判断如果选择了自定义则输入自定义的职位
        try:
            self.driver_wait_vist((By.CSS_SELECTOR, ".util_d_n"))
            self.driver.find_element(By.CSS_SELECTOR, ".util_d_n").send_keys(get_post())
        except:
            pass
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        self.driver_wait_vist((By.ID, "js_tips"))
        return self.driver.find_element(By.ID, "js_tips").text