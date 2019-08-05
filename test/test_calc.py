#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/7/14 16:32
# @Author  :ytq
#  @File    :${name}

from unittest import TestCase

from src.calc import Calc
from ddt import ddt,data,unpack

@ddt
class TestCalc(TestCase):
    calc = Calc()
    # def test_above(self):
    #     calc = Calc()
    #     result = calc.above(3,2)
    #     self.assertEqual(result,True)
    #
    #     result = calc.above(2, 3)
    #     self.assertEqual(result, False)
    #
    #     result = calc.above(3, 3)
    #     self.assertEqual(result, False)
    #
    #     result = calc.above(3, -2)
    #     self.assertEqual(result, True)
    #
    #     result = calc.above(-3, -2)
    #     self.assertEqual(result, False)
    #
    #     result = calc.above(3.2, 2)
    #     self.assertEqual(result, True)
    @data([3,2],[3.2,2],[3,-2])
    @unpack
    def test_above_pass(self,a,b):
        result = self.calc.above(a,b)
        self.assertEqual(result,True)

    @data([-3, -2], [3, 3], [2, 3])
    @unpack
    def test_above_fail(self, a, b):

        result = self.calc.above(a, b)
        self.assertEqual(result, False)