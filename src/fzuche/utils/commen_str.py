#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午1:54
# @Author  : ytq
# @FileName: commen_str.py
# @Software: PyCharm
import random

from src.utils.random_id_card import RandomIdCard
from src.utils.random_name_phone import get_name, get_phone


def get_id_items():
    card_id = RandomIdCard().get_id_card()
    id = card_id[0]
    birth = id[6:10] + "-" + id[10:12] + "-" + id[12:14]
    if int(id[-2]) % 2 == 1:
        sex = "G1"
    else:
        sex = "G2"
    return id, birth, sex

def get_wec_and_alipay():
    wec = str(random.choice(("", random.randint(1000000, 99999999))))
    if wec:
        alipay = str(random.choice(("", random.randint(1111111111, 99999999999))))
        if alipay:
            wec_type = random.choice(("实名", "非实名"))
            alipay_type = random.choice(("实名", "非实名"))
        else:
            wec_type = random.choice(("实名", "非实名"))
            alipay_type = "请选择"
    else:
        alipay = str(random.randint(1111111111, 99999999999))
        alipay_type = random.choice(("实名", "非实名"))
        wec_type = "请选择"
    return wec, wec_type, alipay, alipay_type

def get_contact(i):
    dic_contact = {}
    dic_contact["contactAddress"] = "深圳市龙华区%s" % random.choice(("民治街道", "清湖", "观澜", "龙华街道"))
    dic_contact["contactName"] = get_name()
    dic_contact["phone"] = get_phone()
    if i == 0:
        dic_contact["relation"] = random.choice(("R6", "R7"))
    else:
        dic_contact["relation"] = random.choice(("R4", "R5", "R8", "R11"))
    return dic_contact

def get_contacts():
    contact_list = []
    for i in range(2):
        contact = get_contact(i)
        contact_list.append(contact)
    return contact_list

def replace_char(string, char, index):
    string1 = list(string)
    string1[index] = char
    return ''.join(string1)

if __name__ == '__main__':
    co = get_contacts()
    print(co)