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

    @pytest.mark.parametrize("userid,username,department,mobile,email",[("Aaaaaaaaaaa2","王麻子","4","13800000002",""),("Aaaaaaaaaaa8","王麻子1","4","13800000007",""),("Aaaaaaaaaaa9","王麻子2","4","13800000008","")])
    def test_add_member(self,userid,username,department,mobile,email):
        ret = self.mem.add_member(userid,username,department,mobile=mobile,email= email)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid,username,department,mobile,email",[("Aaaaaaaaaaaa","李四","4","13800000000","")])
    def test_update_member(self,userid,username,department,mobile,email):
        ret = self.mem.update_member(userid,username,department,mobile=mobile,email= email)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid",("Aaaaaaaaaaaa","Aaaaaaaaaaa1","Aaaaaaaaaaa2"))
    def test_get_single_info(self,userid):
        ret = self.mem.get_single_info(userid)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid,username,department,mobile,email",[("Aaaaaaaaaaa3","李四1","4","13800000003","")])
    def test_del_member(self,userid,username,department,mobile,email):
        add_ret = self.mem.add_member(userid,username,department,mobile=mobile,email= email)
        if add_ret["errcode"] == 0:
            ret = self.mem.del_member(userid)
            assert ret["errcode"] == 0

    @pytest.mark.parametrize("user_list",(["Aaaaaaaaaaa2"],["Aaaaaaaaaaa8","Aaaaaaaaaaa9"]))
    def test_del_batch(self,user_list):
        ret = self.mem.del_member_batch(user_list)
        assert ret["errcode"] ==0

    @pytest.mark.parametrize("department_id,fetch_child",[("1",""),("2",""),("1","1")])
    def test_simple_list(self,department_id,fetch_child):
        ret = self.mem.get_department_member_simple(department_id,fetch_child)
        assert ret["errcode"] ==0

    @pytest.mark.parametrize("department_id,fetch_child", [("1", ""), ("2", ""), ("1", "1")])
    def test_details_list(self, department_id, fetch_child):
        ret = self.mem.get_department_member_details(department_id, fetch_child)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("userid", ["YangTieQiao"])
    def test_userid_to_openid(self,userid):
        ret = self.mem.userid_to_openid(userid)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("openid", ["oebUkw8WDm3_aPOXgBFx-X0TnuWo"])
    def test_openid_to_userid(self,openid):
        ret = self.mem.openid_to_userid(openid)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("user_list,party_list,tag_list", [(["Aaaaaaaaaaaa"],[""],[""]),(["Aaaaaaaaaaaa"],[2,3],[""])])
    def test_invite_member(self, user_list,party_list,tag_list):
        ret = self.mem.invite_member(user_list,party_list,tag_list)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("size",[1,2,3,4])
    def test_get_qrcode(self, size):
        ret = self.mem.get_qrcode(size)
        assert ret["errcode"] == 0