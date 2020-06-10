# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午8:55
# @Author  : YTQ
# @FileName: test_demo.py
# @Software: PyCharm
from time import sleep

import pytest
import yaml

from src.wrapper_demo.my_wrapper import Screen
from selenium import webdriver


class TestMy:

    # def setup(self):
    #
    #     self.drive = webdriver.Chrome()
    #
    # # @Screen()
    # # def test_1(self):
    # #     print("hhahaha")
    # #     sleep(1)
    # #     print("完了～～")

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("tstdt.yaml",'r', encoding='UTF-8' )))
    def test_data(self,a,b):
        # print(yaml.safe_load(open("tstdt.yaml",'r', encoding='UTF-8' )))
        print(a+b)


