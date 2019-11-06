#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 下午3:30
# @Author  : ytq
# @FileName: test_mem.py
# @Software: PyCharm
import pytest

from src.utils.log_utils import LogUtils
from src.wework_request.api.member import Member

log = LogUtils()

class TestMem:

    def setup_class(self):
        self.mem = Member()

    @pytest.mark.parametrize("userid,username,department,mobile,email",[("Aaaaaaaaaaa8","王麻子1","4","13800000007","")])
    def test_add_member(self,userid,username,department,mobile,email):
        ret = self.mem.add_member(userid,username,department,mobile=mobile,email= email)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid,username,department,mobile,email",[("Aaaaaaaaaaaa","李四","4","13800000000","")])
    def test_update_member(self,userid,username,department,mobile,email):
        ret = self.mem.update_member(userid,username,department,mobile=mobile,email= email)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid",[("Aaaaaaaaaaaa"),("Aaaaaaaaaaa1"),("Aaaaaaaaaaa2")])
    def test_get_single_info(self,userid):
        ret = self.mem.get_single_info(userid)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid,username,department,mobile,email",[("Aaaaaaaaaaa3","李四1","4","13800000003","")])
    def test_del_member(self,userid,username,department,mobile,email):
        add_ret = self.mem.add_member(userid,username,department,mobile=mobile,email= email)
        if add_ret["errcode"] == 0:
            ret = self.mem.del_member(userid)
            assert ret["errcode"] == 0