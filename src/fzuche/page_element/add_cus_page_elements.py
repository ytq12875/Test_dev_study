#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午2:09
# @Author  : ytq
# @FileName: add_cus_page_elements.py
# @Software: PyCharm
class AddCusPageElements:
    iframe = 'selector_selector=>.tab-iframe .active'
    cus_name = 'name=>customerName'
    cus_id_type = 'name=>identifyType'
    cus_id_num = 'name=>identifyNo'
    check_btn = 'selector_selector=>.btn-title-wrap .btn-green'
    msg_info = 'selector_selector=>.point-pop-wrap'
    msg_btn = 'selector_selector=>.msgBtn'
    cus_house_hold = 'name=>household'
    cus_marry = 'name=>marry'
    cus_mobile = 'name=>phoneNumber'
    cus_education = 'name=>education'
    cus_householdAddress = 'name=>householdAddress'
    cus_company = 'name=>company'
    cus_workYear = 'name=>workYear'
    cus_position = 'name=>position'
    cus_earns = 'name=>earns'
    cus_companyPhone = 'name=>companyPhone'
    cus_companyAddress = 'name=>companyAddress'
    cus_webchat = 'name=>webchat'
    cus_webchatType = 'name=>webchatType'
    cus_alipay = 'name=>alipay'
    cus_alipayType = 'name=>alipayType'
    cus_houseType = 'name=>houseType'
    cus_homePhone = 'name=>homePhone'
    cus_homeAddress = 'name=>homeAddress'
    contact_names = 'xpath=>//Input[contains(@ng-model, "item.contactName")]'
    contact_phones = 'xpath=>//Input[contains(@ng-model, "item.phone")]'
    contact_ships = 'xpath=>//select[contains(@ng-model, "item.relation")]'
    contact_adds = 'xpath=>//Input[contains(@ng-model, "item.contactAddress")]'
    add_contact_btn = 'xpath=>//button[contains(text(), "增加")]'
    add_cus_btn = 'xpath=>//input[@class="btn btn-green"and@value= "新增"]'
