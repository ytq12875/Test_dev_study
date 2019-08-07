#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 0:20
# @Author  :ytq
# @File    :
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject:

    def __init__(self, driver):
        self.driver = driver

    def driver_wait_vist(self, selector):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._get_ele_selector(selector)))

    def driver_wait_no_vist(self, selector):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.invisibility_of_element_located(self._get_ele_selector(selector)))

    def get_element(self, selector):
        return self.driver.find_element(*self._get_ele_selector(selector))

    def get_elements(self, selector):
        return self.driver.find_elements(*self._get_ele_selector(selector))

    def _get_ele_selector(self, selector):
        if '=>' not in selector:
            elc_method = By.ID
            selector_value = selector
        else:
            selector_by = selector.split('=>')[0]
            selector_value = selector.split('=>')[1]

            if selector_by == "i" or selector_by == "id":
                elc_method = By.ID
            elif selector_by == "n" or selector_by == 'name':
                elc_method = By.NAME
            elif selector_by == "c" or selector_by == 'class_name':
                elc_method = By.CLASS_NAME
            elif selector_by == "l" or selector_by == 'link_text':
                elc_method = By.LINK_TEXT
            elif selector_by == "p" or selector_by == 'partial_link_text':
                elc_method = By.PARTIAL_LINK_TEXT
            elif selector_by == "t" or selector_by == 'tag_name':
                elc_method = By.TAG_NAME
            elif selector_by == "x" or selector_by == 'xpath':
                elc_method = By.XPATH
            elif selector_by == "s" or selector_by == "selector_selector":
                elc_method = By.CSS_SELECTOR
            else:
                raise NameError("Please enter a valid type of targeting elements.")

        return elc_method, selector_value
