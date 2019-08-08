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
        pic_path = "E:/pic/demo.png"
        self.driver_wait_vist(ContactPageElements.add_member_contact_menu)
        self.click_by_selector(ContactPageElements.add_member_contact_menu)
        self.driver_wait_vist(ContactPageElements.add_member_contact_list)
        self.click_by_selector(ContactPageElements.add_member_button)
        # 上传头像
        self.click_by_selector(ContactPageElements.add_member_title_form)
        self.send_value(ContactPageElements.add_member_select_pic,pic_path)
        self.driver_wait_vist(ContactPageElements.add_member_reupload)
        self.click_by_selector(ContactPageElements.add_member_save_pic)
        # 等待上传头像窗口消失
        self.driver_wait_no_vist(ContactPageElements.add_member_reupload)
        # 输入各input框
        self.send_value(ContactPageElements.add_member_mem_name,name)
        self.send_value(ContactPageElements.add_member_mem_english_name,name+"别名")
        self.send_value(ContactPageElements.add_member_mem_acctid,rd_phone+"qq.com")
        # 把所有选择radio放入selects变量中
        selects = self.get_elements(ContactPageElements.add_member_radio)
        self.click_element(random.choice(selects[:2]))
        self.send_value(ContactPageElements.add_member_mem_phone,rd_phone)
        self.send_value(ContactPageElements.add_member_mem_telephone,"0755" + tel_phone)
        self.send_value(ContactPageElements.add_member_mem_email,rd_phone + "@qq.com")
        self.send_value(ContactPageElements.add_member_mem_address,self.comm_str.get_cn_char(8))
        self.send_value(ContactPageElements.add_member_mem_title,get_post())
        self.click_element(random.choice(selects[2:4]))
        self.click_element(random.choice(selects[4:6]))
        # 判断如果选择了自定义则输入自定义的职位
        try:
            self.driver_wait_vist(ContactPageElements.add_member_mem_other_title)
            self.send_value(ContactPageElements.add_member_mem_other_title,get_post())
        except:
            pass
        self.click_by_selector(ContactPageElements.add_member_save)

    def get_contact_tips(self):
        return self.get_tips(ContactPageElements.add_member_tips)