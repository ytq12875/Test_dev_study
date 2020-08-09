#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import datetime
import os
import random


class RandomIdCard:

    def __init__(self):
        cur_path = os.path.dirname(os.path.dirname(__file__))
        csv_path = cur_path + "/utils/area.csv"
        self.filename = csv_path

    # 功能：从csv文件中读取一个区域编码字典
    # 输入：文件名称
    def __areaCodeDict(self):
        dataDict = {}
        key = 0
        value = 1
        dataLine = open(self.filename, encoding='GBK').read().splitlines()
        for line in dataLine:
            tmpLst = line.split(",")
            dataDict[tmpLst[key]] = tmpLst[value]
        return dataDict

    # 功能：随机生产一个区域码

    def __areaCode(self, Dict):
        codeList = []
        for key in Dict.keys():
            codeList.append(key)
        lenth = len(codeList) - 1
        i = random.randint(0, lenth)
        return codeList[i]

    # 功能：随机生成1930年之后的出生日期
    def __birthDay(self):
        # d1 = datetime.datetime.strptime('1930-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # d2 = datetime.datetime.now()
        d1 = datetime.datetime.strptime('1960-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        d2 = datetime.datetime.strptime('1995-12-31 00:00:00', '%Y-%m-%d %H:%M:%S')
        delta = d2 - d1
        dys = delta.days
        i = random.randint(0, dys)
        dta = datetime.timedelta(days=i)
        bhday = d1 + dta
        return bhday.strftime('%Y%m%d')

    # 功能：随机生成3位序列号

    def __ordrNum(self):
        odNum = random.randint(0, 999)  # 随机生成0到999之间的数据
        sex = odNum % 2
        return (str(odNum).zfill(3), sex) #返回3位补零的序列号和性别

    # 功能：生成校验码

    def __check(self, id_num):
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id_num)):
            count = count + int(id_num[i]) * weight[i]
        return checkcode[str(count % 11)]  # 算出校验码

    def get_id_card(self):
        areaCodeDt = self.__areaCodeDict()  # 调用生成字典
        areaCd = self.__areaCode(areaCodeDt)  # 生成区域码
        areaCdName = areaCodeDt[areaCd]  # 获取区域名称
        birthDy = self.__birthDay()  # 生成出生日期
        (ordNum, sex) = self.__ordrNum()  # 生成顺序号和性别
        checkcode = self.__check((areaCd + birthDy + ordNum))  # 生产校验码
        id_card = areaCd + birthDy + ordNum + checkcode  # 拼装身份证号
        return id_card, areaCdName

    def check_is_id_card(self, id_num):
        id_str = str(id_num)
        last_code = id_str[-1]
        true_code = self.__check(id_str[:-1])
        areaCodeDt = self.__areaCodeDict()  # 调用生成字典
        if last_code != true_code:
            return "您查询的号码 " + id_str + " 不符合身份证规则"
        else:
            prov = areaCodeDt[id_str[:6]]
            birth = id_str[6:10] + "年" + id_str[10:12] + "月" + id_str[12:14] + "月"
            return "您查询的号码 " + id_str + " 符合身份证规则。此人来自于：" + prov + " 出生于：" + birth + " 。"


if __name__ == '__main__':
    mk = RandomIdCard()
    card = mk.get_id_card()
    print(card)
    print(mk.check_is_id_card(card[0]))
