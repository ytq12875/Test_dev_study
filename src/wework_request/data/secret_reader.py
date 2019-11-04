# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 下午10:16
# @Author  : YTQ
# @FileName: secret_reader.py
# @Software: PyCharm
import os

from src.wework_request.utils.read_yaml import ReadYaml


class SecretReader:

    def __init__(self):
        self.path = os.path.dirname(os.getcwd()) + "/config"
        self.file = "secret_id"
        self.ym_obj = ReadYaml(path=self.path,file=self.file)

    def get_cor_id(self,cor_name):
        cor_obj = self.ym_obj.get_yaml_data(cor_name)
        return cor_obj["cor_id"]

    def get_secret_id(self,cor_name,secret_name):
        cor_obj = self.ym_obj.get_yaml_data(cor_name)
        secret = secret_name + "_secret"
        return cor_obj[secret]

if __name__ == '__main__':
    sr = SecretReader()
    print(sr.get_cor_id("my_cor"))
    print(sr.get_secret_id("my_cor","conct"))