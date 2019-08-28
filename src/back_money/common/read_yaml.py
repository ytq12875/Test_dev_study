#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import os

import yaml

class YamlParser:
    def __init__(self,file,path):
        if ".yaml" in file:
            yaml_file = path + "\\" + file
        else:
            yaml_file =path + "\\" + file +".yaml"
        # 打开yaml文件
        file = open(yaml_file, 'r', encoding="utf-8")
        self.file_data = file.read()
        file.close()

    def get_yaml_load_all(self):
        all_data = yaml.load_all(self.file_data, Loader=yaml.FullLoader)
        for data in all_data:
            return data

    def get_yaml_data(self,key):
        all_data = yaml.load_all(self.file_data, Loader=yaml.FullLoader)
        for data in all_data:
            if  key in data.keys():
                return data[key]
            else:
                return


if __name__ == '__main__':

    parser = YamlParser("\\dbconfig",os.path.dirname(os.getcwd())+"\\config")
    print(parser.get_yaml_data("uat_pay_db"))
    # file = "./"