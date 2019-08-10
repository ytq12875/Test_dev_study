#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import random

from src.test_co_chat.base_object import BaseObject
from src.test_co_chat.page_elements import ContactPageElements,ProfilePageElements
from selenium.webdriver.common.keys import Keys


class ProfilePage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)

    def __get_search(self):
        self.driver_wait_vist(ContactPageElements.add_member_contact_menu)
        self.click_by_selector(ContactPageElements.add_member_contact_menu)
        self.driver_wait_vist(ContactPageElements.add_member_contact_list)
        try:
            try:
                act_els = self.get_elements(ProfilePageElements.member_list_parent_name)
            except:
                act_els = []
            try:
                dis_act_els1 = self.get_elements(ProfilePageElements.member_list_parent_disable_name)
            except:
                dis_act_els1 = []
            els = act_els + dis_act_els1
            namelist=[]
            for el in els:
                namelist.append(self.get_element_from_parent(el, ProfilePageElements.member_list_son_name).get_attribute("title"))
            name = random.choice(namelist)
            self.send_value(ProfilePageElements.member_list_search,name)
            self.send_value(ProfilePageElements.member_list_search,Keys.ENTER)
            return self
        except:
            raise Exception("没有用户可以操作")


    def edit_member(self,rd_phone,tel_phone):
        self.__get_search()
        self.click_by_selector(ProfilePageElements.member_edit_button)
        self.driver_wait_vist(ProfilePageElements.member_edit_page)
        self.send_new_value(ProfilePageElements.member_edit_phone, rd_phone)
        self.send_new_value(ProfilePageElements.member_edit_telephone, "0755" + tel_phone)
        self.send_new_value(ProfilePageElements.member_edit_email, rd_phone + "@qq.com")
        self.click_by_selector(ProfilePageElements.member_edit_save)

    def unused_member(self):
        self.__get_search()
        self.driver_wait_no_vist(ProfilePageElements.member_edit_tips)
        try:
            status = self.get_element(ProfilePageElements.member_edit_status).text
            if status == "禁用":
                self.click_by_selector(ProfilePageElements.member_edit_status)
                self.click_by_selector(ProfilePageElements.member_edit_unused_do)
            else:
                return "用户不是正常状态！"
        except:
            return "操作失败"

    def used_member(self):
        self.__get_search()
        self.driver_wait_no_vist(ProfilePageElements.member_edit_tips)
        try:
            status = self.get_element(ProfilePageElements.member_edit_status).text
            if status == "启用":
                self.click_by_selector(ProfilePageElements.member_edit_status)
            else:
                return "用户不是禁用状态！"
        except:
            return "操作失败"

    def get_edit_tips(self):
        return self.get_tips(ProfilePageElements.member_edit_tips)