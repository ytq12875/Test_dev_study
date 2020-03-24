#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午2:50
# @Author  : ytq
# @FileName: get_action_url.py
# @Software: PyCharm
import os

from src.baiduAIApi.utils.read_yaml import YamlParser


class ActionUrl:

    def __init__(self):
        cur_path = os.path.dirname(os.path.dirname(__file__))
        file_path = cur_path + '/config'
        self.config = YamlParser('action_url.yaml', file_path)
        self.base_url = self.config.get_yaml_data("base")

    def get_ocr_url(self,action_method):
        self.orc_config = self.config.get_yaml_data("ocr")
        api = self.orc_config["api"]
        version = self.orc_config["version"]
        son_api = self.orc_config["apis"][action_method]
        return "/".join((self.base_url,api,version,son_api))

if __name__ == '__main__':
    au = ActionUrl()
    print(au.get_ocr_url("general"))
