#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午2:10
# @Author  : ytq
# @FileName: add_cus_page.py
# @Software: PyCharm
import random
from time import sleep

from selenium.webdriver.common.keys import Keys

from src.fzuche.base_object import BaseObject
from src.fzuche.page_element.add_cus_page_elements import AddCusPageElements
from src.utils.random_id_card import RandomIdCard
from src.utils.random_name_phone import get_name, get_phone, get_post
from src.fzuche.utils.commen_str import replace_char,get_wec_and_alipay


class AddCusPage(BaseObject, AddCusPageElements):
    def __init__(self, driver):
        super().__init__(driver)
        self.id_msg = RandomIdCard().get_id_card()
        self.ali_wech_tuple = get_wec_and_alipay()

    def check_has(self):
        name = get_name()
        self.switch_to_iframe(1)
        self.send_value(self.cus_name, name)
        self.send_value(self.cus_id_type, "身份证")
        self.send_value(self.cus_id_num, self.id_msg[0])
        self.click_by_selector(self.check_btn)
        if "此用户不存在" in self.get_msg():
            sleep(2)
            self.click_by_selector(self.msg_btn)
            self.name = name
            return True
        else:
            sleep(2)
            self.click_by_selector(self.msg_btn)
            return False

    def add_cus(self):
        if self.check_has():
            self.send_value(self.cus_house_hold,random.choice(("本地", "非本地")))
            self.send_value(self.cus_marry,random.choice(("未婚", "已婚", "离异", "丧偶")))
            self.send_value(self.cus_mobile,replace_char(get_phone(), str(random.choice((0, 1, 2))), 1))
            self.send_value(self.cus_education,random.choice(("研究生", "大学本科", "大学专科和专科学校", "中等专业学校或中等技术学校", "技术学校", "高中", "高中以下")))
            self.send_value(self.cus_householdAddress,self.id_msg[1])
            self.send_value(self.cus_company,"中国企鹅有限公司")
            self.send_value(self.cus_workYear,str(random.randint(0,55)))
            self.send_value(self.cus_position,get_post())
            self.send_value(self.cus_earns,str(random.randint(1000,9999999)))
            self.send_value(self.cus_companyPhone,str(random.randint(11111111,99999999)))
            self.send_value(self.cus_companyAddress,"深圳市龙华区清湖街道1109-1号")
            self.send_value(self.cus_webchat,self.ali_wech_tuple[0])
            self.send_value(self.cus_webchatType,self.ali_wech_tuple[1])
            self.send_value(self.cus_alipay, self.ali_wech_tuple[2])
            self.send_value(self.cus_alipayType, self.ali_wech_tuple[3])
            self.send_value(self.cus_houseType,random.choice(("自拥无贷款","自拥有贷款","与亲属同住","单位宿舍","租房")))
            self.send_value(self.cus_homePhone,"0755" + str(random.randint(11111111, 99999999)))
            self.send_value(self.cus_homeAddress,"龙华区清湖街道%s-%s号" % (random.randint(1, 999), random.randint(1, 99)))
            self.send_value_by_element(self.get_elements(self.contact_names)[0],get_name())
            self.send_value_by_element(self.get_elements(self.contact_phones)[0], get_phone())
            self.send_value_by_element(self.get_elements(self.contact_ships)[0],random.choice(("配偶","父亲","母亲")))
            self.send_value_by_element(self.get_elements(self.contact_adds)[0],"龙华区清湖街道%s-%s号" % (random.randint(1, 999), random.randint(1, 99)))
            self.click_by_selector(self.add_contact_btn)
            self.send_value_by_element(self.get_elements(self.contact_names)[1],get_name())
            self.send_value_by_element(self.get_elements(self.contact_phones)[1], get_phone())
            self.send_value_by_element(self.get_elements(self.contact_ships)[1],random.choice(("亲属","朋友","兄弟","姐妹","同事","同学")))
            self.send_value_by_element(self.get_elements(self.contact_adds)[1],"龙华区清湖街道%s-%s号" % (random.randint(1, 999), random.randint(1, 99)))
            self.click_by_selector(self.add_cus_btn)

    def get_msg(self):
        return self.get_tips(self.msg_info).strip()