#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 下午2:58
# @Author  : ytq
# @FileName: member.py
# @Software: PyCharm
import json

from src.utils.log_utils import LogUtils
from src.wework_request.api.base_api import BaseApi
from src.wework_request.api.wework import WeWork

log = LogUtils()

class Member(BaseApi):

    def __init__(self):
        super().__init__()
        self.mem= self.ur.get_api("wework", "member")
        conct_secret = self.sr.get_secret_id("my_cor", "conct")
        self.access_token = WeWork().get_token(corpid=self.corpid, corpsecret=conct_secret)
        self.add_url = self.url + self.ur.get_api_by_parent("mem_add", self.mem)
        self.singe_info_url = self.url + self.ur.get_api_by_parent("mem_info", self.mem)
        self.update_mem_url = self.url + self.ur.get_api_by_parent("mem_update", self.mem)
        self.del_url = self.url + self.ur.get_api_by_parent("mem_del", self.mem)
        self.del_batch_url = self.url + self.ur.get_api_by_parent("mem_del_bacth",self.mem)
        self.list_simple_url = self.url + self.ur.get_api_by_parent("mem_list_simple", self.mem)
        self.list_details_url = self.url + self.ur.get_api_by_parent("mem_list_details", self.mem)
        self.use2open_url = self.url + self.ur.get_api_by_parent("mem_use2open", self.mem)
        self.open2use_url = self.url + self.ur.get_api_by_parent("mem_open2use", self.mem)
        self.invite_url = self.url + self.ur.get_api_by_parent("mem_invite", self.mem)
        self.qrcode_url = self.url + self.ur.get_api_by_parent("mem_get_qrcode", self.mem)

    def add_member(self,userid,name,department,mobile="",email=""):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token=self.access_token)
        men_dic = {}
        men_dic["userid"] = userid
        men_dic["name"] = name
        men_dic["department"] = department
        men_dic["mobile"] = mobile
        men_dic["email"] = email
        ret = self.do_request(self.add_url, data=men_dic).json()
        log.info(ret)
        return ret

    def update_member(self,userid,name,department,mobile="",email=""):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token=self.access_token)
        men_dic = {}
        men_dic["userid"] = userid
        men_dic["name"] = name
        men_dic["department"] = department
        men_dic["mobile"] = mobile
        men_dic["email"] = email
        ret = self.do_request(self.update_mem_url, data=men_dic).json()
        log.info(ret)
        return ret

    def get_single_info(self,userid):
        self.set_request_method(mode="http", method="get")
        self.set_url_params(access_token=self.access_token,userid=userid)
        ret = self.do_request(self.singe_info_url).json()
        log.info(ret)
        return ret

    def del_member(self,userid):
        self.set_request_method(mode="http", method="get")
        self.set_url_params(access_token=self.access_token, userid=userid)
        ret = self.do_request(self.del_url).json()
        log.info(ret)
        return ret

    def del_member_batch(self,user_list):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token=self.access_token)
        will_del_batch ={}
        will_del_batch["useridlist"] = user_list
        ret = self.do_request(self.del_batch_url,data=will_del_batch).json()
        log.info(ret)
        return ret

    def get_department_member_simple(self,department_id,fetch_child = "0"):
        self.set_request_method(mode="http", method="get")
        self.set_url_params(access_token=self.access_token, department_id=department_id,fetch_child = fetch_child)
        ret = self.do_request(self.list_simple_url).json()
        log.info(ret)
        return ret

    def get_department_member_details(self,department_id,fetch_child = "0"):
        self.set_request_method(mode="http", method="get")
        self.set_url_params(access_token=self.access_token, department_id=department_id,fetch_child = fetch_child)
        ret = self.do_request(self.list_details_url).json()
        log.info(ret)
        return ret

    def userid_to_openid(self,userid):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token=self.access_token)
        will_chage_user={}
        will_chage_user["userid"] = userid
        ret = self.do_request(self.use2open_url,data=will_chage_user).json()
        log.info(ret)
        return ret

    def openid_to_userid(self,openid):
        self.set_request_method(mode="http", method="post")
        self.set_url_params(access_token=self.access_token)
        will_chage_user={}
        will_chage_user["openid"] = openid
        ret = self.do_request(self.open2use_url,data=will_chage_user).json()
        log.info(ret)
        return ret