#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 22:06
# @Author  :ytq
import random

from src.test_co_chat.BaseObject import BaseObject
from src.test_co_chat.contact_page_elements import ContactPageElements
from src.utils.common_str import CommonStr
from src.utils.random_name_phone import get_post


class ContactPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.comm_str = CommonStr()

    def add_member(self,name,rd_phone,tel_phone):
        self.driver_wait_vist(ContactPageElements.add_member_contact_menu)
        self.get_element(ContactPageElements.add_member_contact_menu).click()
        self.driver_wait_vist(ContactPageElements.add_member_contact_list)
        self.get_element(ContactPageElements.add_member_button).click()
        # 上传头像
        self.get_element(ContactPageElements.add_member_title_form).click()
        self.get_element(ContactPageElements.add_member_select_pic).send_keys("E:/pic/demo.png")
        self.driver_wait_vist(ContactPageElements.add_member_reupload)
        self.get_element(ContactPageElements.add_member_save_pic).click()
        # 等待上传头像窗口消失
        self.driver_wait_no_vist(ContactPageElements.add_member_reupload)
        # 输入各input框
        self.get_element(ContactPageElements.add_member_mem_name).send_keys(name)
        self.get_element(ContactPageElements.add_member_mem_english_name).send_keys(name + "别名")
        self.get_element(ContactPageElements.add_member_mem_acctid).send_keys(rd_phone + "@qq.com")
        # 把所有选择radio放入selects变量中
        selects = self.get_elements(ContactPageElements.add_member_radio)
        random.choice(selects[:2]).click()
        self.get_element(ContactPageElements.add_member_mem_phone).send_keys(rd_phone)
        self.get_element(ContactPageElements.add_member_mem_telephone).send_keys("0755" + tel_phone)
        self.get_element(ContactPageElements.add_member_mem_email).send_keys(rd_phone + "@qq.com")
        self.get_element(ContactPageElements.add_member_mem_address).send_keys(self.comm_str.get_cn_char(8))
        self.get_element(ContactPageElements.add_member_mem_title).send_keys(get_post())
        random.choice(selects[2:4]).click()
        random.choice(selects[4:6]).click()
        # 判断如果选择了自定义则输入自定义的职位
        try:
            self.driver_wait_vist(ContactPageElements.add_member_mem_other_title)
            self.get_element(ContactPageElements.add_member_mem_other_title).send_keys(get_post())
        except:
            pass
        self.get_element(ContactPageElements.add_member_save).click()
        self.driver_wait_vist(ContactPageElements.add_member_tips)
        return self.get_element(ContactPageElements.add_member_tips).text