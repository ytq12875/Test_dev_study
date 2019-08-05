#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/5 23:32
# @Author  :ytq
# @File    :
import pytest

@pytest.mark.usefixtures("init_driver")
class TestA:
    def test_one(self,init_driver):
        print("This is ClassA func1")

if __name__ == '__main__':
    pytest.main(["-vs"])