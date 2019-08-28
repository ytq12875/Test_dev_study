#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/22 20:27
# @Author  :ytq
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        self.screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高

    def find_element(self, selector):
        '''查找元素，返回单个element'''
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._get_ele_selector(selector)))
        return self.driver.find_element(*self._get_ele_selector(selector))

    def find_elements(self, selector):
        '''查找元素集合，返回element列表'''
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._get_ele_selector(selector)))
        return self.driver.find_elements(*self._get_ele_selector(selector))

    def send_key_board(self, keys):
        '''发送按键'''
        sleep(2)
        self.driver.keyevent(keys)

    def click_el(self, selector):
        '''点击指定的selector'''
        self.find_element(selector).click()

    def long_press_el(self, selector, dur=2500):
        '''长按指定的selector'''
        TouchAction(self.driver).long_press(self.find_element(selector), duration=dur).perform()

    def send_value(self, selector, msg):
        '''向指定的selector输送值'''
        self.find_element(selector).send_keys(msg)

    def tap_in_cor(self, x, y):
        '''点击指定坐标'''
        sleep(3)
        TouchAction(self.driver).tap(x=x, y=y).perform().release()

    def swipe_up(self, t=500, n=1):
        '''向上滑动屏幕'''
        x1 = self.screen_width * 0.5  # x坐标
        y1 = self.screen_height * 0.75  # 起始y坐标
        y2 = self.screen_height * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        '''向下滑动屏幕'''
        x1 = self.screen_width * 0.5  # x坐标
        y1 = self.screen_height * 0.25  # 起始y坐标
        y2 = self.screen_height * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t=500, n=1):
        '''向左滑动屏幕'''
        x1 = self.screen_width * 0.75
        y1 = self.screen_height * 0.5
        x2 = self.screen_width * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500, n=1):
        '''向右滑动屏幕'''
        x1 = self.screen_width * 0.25
        y1 = self.screen_height * 0.5
        x2 = self.screen_width * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def _get_ele_selector(self, selector):
        '''解析selector 返回By，select元组'''
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
