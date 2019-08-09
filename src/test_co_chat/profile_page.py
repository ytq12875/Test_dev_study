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
        els = self.get_elements(ProfilePageElements.member_list_parent_name)
        namelist=[]
        for el in els:
            namelist.append(self.get_element_from_parent(el, ProfilePageElements.member_list_son_name).get_attribute("title"))
        name = random.choice(namelist)
        self.send_value(ProfilePageElements.member_list_search,name)
        self.send_value(ProfilePageElements.member_list_search,Keys.ENTER)
        return self


    def edit_member(self):
        self.__get_search()
        pass

    def unused_member(self):
        pass

    def used_member(self):
        pass