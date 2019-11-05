#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 上午8:37
# @Author  : ytq
# @FileName: url_reader.py
# @Software: PyCharm
import os

from src.wework_request.utils.read_yaml import ReadYaml


class UrlReader:

    def __init__(self):
        self.path = os.path.dirname(os.getcwd()) + "/config"
        self.file = "urls"
        self.ym_obj = ReadYaml(path=self.path,file=self.file)

    def get_url(self,obj_name):
        url_obj = self.ym_obj.get_yaml_data(obj_name)
        return url_obj["url"]

    def get_api(self,obj_name,url_name):
        url_obj = self.ym_obj.get_yaml_data(obj_name)
        return url_obj[url_name]

    def get_api_by_parent(self,url_name,per_obj):
        return per_obj[url_name]

if __name__ == '__main__':
    ur = UrlReader()
    print(ur.get_url("wework"))
    print(ur.get_api("wework","token"))
    dpt = ur.get_api("wework","department")
    print(ur.get_api_by_parent("dpt_list",dpt))