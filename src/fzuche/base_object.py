#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/6 0:20
# @Author  :ytq
# @File    :
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.utils.log_utils import LogUtils

class BaseObject:

    def __init__(self, driver):
        self.log = LogUtils()
        self.driver:WebDriver = driver

    def driver_wait_vist(self, selector):
        self.log.info("等待元素加载：")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._get_ele_selector(selector)))

    def driver_wait_clickable(self, selector):
        self.log.info("等待元素可被点击：")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self._get_ele_selector(selector)))

    def driver_wait_no_vist(self, selector):
        self.log.info("等待元素消失：")
        WebDriverWait(self.driver, 15).until(
            expected_conditions.invisibility_of_element_located(self._get_ele_selector(selector)))

    def get_element_from_parent(self,element,selector):
        self.log.info("从父元素中查询子元素：")
        return element.find_element(*self._get_ele_selector(selector))

    def get_element(self, selector):
        selector_tuple = self._get_ele_selector(selector)
        el = self.driver.find_element(*selector_tuple)
        if el:
            self.log.info("通过" + selector_tuple[0] + "方式定位元素：" + selector_tuple[1] + "成功")
            return el
        else:
            self.log.error("通过" + selector_tuple[0] + "方式定位元素：" + selector_tuple[1] + "失败")

    def get_elements(self, selector):
        selector_tuple = self._get_ele_selector(selector)
        els = self.driver.find_elements(*selector_tuple)
        if els:
            self.log.info("通过" + selector_tuple[0] + "方式定位元素：" + selector_tuple[1] + "成功")
            return els
        else:
            self.log.error("通过" + selector_tuple[0] + "方式定位元素：" + selector_tuple[1] + "失败")

    def send_value(self, selector,msg):
        el = self.get_element(selector)
        self.log.info("输入信息："+msg)
        return el.send_keys(msg)

    def send_value_by_element(self, element,msg):
        self.log.info("输入信息："+msg)
        return element.send_keys(msg)

    def send_new_value(self, selector,msg):
        el = self.get_element(selector)
        self.log.info("清空输入框：")
        el.clear()
        self.log.info("输入信息：" + msg)
        return el.send_keys(msg)

    def click_element(self, element):
        self.log.info("点击元素")
        element.click()

    def click_by_selector(self, selector):
        el = self.get_element(selector)
        self.log.info("点击元素")
        el.click()

    def get_tips(self, selector):
        self.driver_wait_vist(selector)
        el = self.get_element(selector)
        self.log.info("获取元素的文本信息：")
        tips = el.text
        return tips if tips else ""

    def scroll(self,num):
        # 50~10000
        jsCode = "var q=document.documentElement.scrollTop=%d"%num
        self.log.info("页面滑动%s"%str(num))
        self.driver.execute_script(jsCode)

    def get_tittle(self):
        self.log.info("获取页面标题：")
        return  self.driver.title

    def switch_to_iframe(self,num):
        self.log.info("切换iframe:%s"%str(num))
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[num])

    def get_source(self):
        self.log.info("获取页面：")
        return  self.driver.page_source

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
