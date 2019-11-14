# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午8:55
# @Author  : YTQ
# @FileName: test_demo.py
# @Software: PyCharm
from time import sleep

from src.wrapper_demo.my_wrapper import Screen
from selenium import webdriver


class TestMy:

    def setup(self):

        self.drive = webdriver.Chrome()

    @Screen()
    def test_1(self):
        print("hhahaha")
        sleep(1)
        print("完了～～")