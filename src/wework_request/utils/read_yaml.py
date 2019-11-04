# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 下午10:12
# @Author  : YTQ
# @FileName: read_yaml.py
# @Software: PyCharm

import codecs

import yaml


class ReadYaml:

    def __init__(self,file,path):
        if ".yaml" in file:
            yaml_file = path + "/" + file
        else:
            yaml_file =path + "/" + file +".yaml"
        # 打开yaml文件
        # print(yaml_file)
        file1 = codecs.open(yaml_file, 'r')
        self.file_data = file1.read()
        file1.close()

    def get_yaml_load_all(self):
        all_data = yaml.load_all(self.file_data)
        for data in all_data:
            return data

    def get_yaml_data(self,key):
        all_data = yaml.load_all(self.file_data)
        for data in all_data:
            if  key in data.keys():
                return data[key]
            else:
                return