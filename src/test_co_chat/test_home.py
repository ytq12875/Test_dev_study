#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:32
# @Author  :ytq
# @File    :
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("init_driver")
class TestA:
    def test_one(self,init_driver):
        WebDriverWait(init_driver, 50).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="menu_index"]/span')))
        init_driver.find_element(By.ID, "menu_contacts").click()
        WebDriverWait(init_driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "member_list")))
        init_driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
        sleep(5)

if __name__ == '__main__':
    pytest.main(["-vs"])