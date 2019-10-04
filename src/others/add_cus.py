#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json
import random

import requests

from src.utils.random_name_phone import get_phone, get_name, get_post
from src.utils.random_id_card import RandomIdCard

add_cus_url = "http://10.91.138.150:53013/zugou-management/gateway/preloan.service.cust.CustService.personalSave"
login_url = "http://10.91.138.150:53013/zugou-management/gateway/general.service.LoginService.staffLogin"
json_value = '{"body":{"birthday":"1987-06-17","company":"四十大盗","companyAddress":"延吉街14号-8-10","companyPhone":"07544563214","contacts":[{"contactAddress":"啊实打实","contactName":"阿达","phone":"18565594511","relation":"R5"},{"contactAddress":"阿达","contactName":"阿达打","phone":"18369895624","relation":"R7"}],"customerName":"厉紫荷","earns":"50000","education":"L20","homeAddress":"发给分 发飞飞额","homePhone":"11012451245","houseType":"T11","household":"H1","householdAddress":"不知道那个地方","identifyNo":"54252419870617868X","identifyType":"T0","marry":"S10","phoneNumber":"18963321445","position":"软件工程师","sex":"G2","workYear":"20","alipay":"","alipayType":"","credit":"","qq":"","taobao":"","webchat":"14541545441","webchatType":"1","remark":"","_channel_id":"30","logonId":"0120171000001451"}}'
login_data = '{"body":{"userName":"0120171000001451","loginPwd":"YENxcmLdEJQ3FVrRiL9rsnggnd/MCupqNPCmgHndklFVYsmXKQ81amCYi+RjfqBaf8FjSol+hlGl49vQm0i34P/KSgCBtS0OEzYbaAE1BfVd83FZajIX7uzjo/os/Bb+xqVR/RtzZZG8/B8Spoh8GAmL9Gv3pt2UdDGIs7ONaL3Bvzya9jTA2OFOxDSEkMxp09WJkPzxgX6I1CEunU63zjPd09ig5xe1DgyJavacQ86dzi1VhYFJEDiUgkPNSZEks83H59l4Il4/n5aSssm+L2irmIv7CyTjwobfKSWvAMhgABYMS+CdVtaXN45Wk227QB9/1zh2m2IAxZUxjPPcWg==","_channel_id":"30"}}'
headers = {"Content-Type": "application/json;charset=utf-8"}
check_data = '{"body":{"customerName":"李世明1","identifyType":"T0","identifyNo":"411201199602222491","_channel_id":"30","logonId":"0120171000001451"}}'
check_url = 'http://10.91.138.150:53013/zugou-management/gateway/preloan.service.cust.CustService.personalExist'

def get_contact():
    dic_contact = {}
    dic_contact["contactAddress"] = "深圳市龙华区"
    dic_contact["contactName"] = get_name()
    dic_contact["phone"] = get_phone()
    dic_contact["relation"] = random.choice(("R5", "R7"))
    return dic_contact


def get_contacts():
    contact_list = []
    for i in range(2):
        contact = get_contact()
        contact_list.append(contact)
    return contact_list

def get_id_items():
    card_id = RandomIdCard().get_id_card()
    id = card_id[0]
    birth = id[6:10]+"-"+id[10:12]+"-"+id[12:14]
    if int(id[-2])%2 == 1:
        sex = "G1"
    else:
        sex = "G2"
    return id,birth,sex

def replace_char(string,char,index):
    string = list(string)
    string[index] = char
    return ''.join(string)

def get_wec_and_alipay():
    wec = random.choice(("",random.randint(1000000,99999999)))
    if wec:
        alipay =random.choice(("",random.randint(1111111111,99999999999)))
        if alipay:
            wec_type = str(random.choice((0, 1)))
            alipay_type = str(random.choice((0, 1)))
        else:
            wec_type = str(random.choice((0, 1)))
            alipay_type = ""
    else:
        alipay = random.randint(1111111111,99999999999)
        alipay_type = str(random.choice((0,1)))
        wec_type = ""
    return wec,wec_type,alipay,alipay_type

def pakage_check(idmsg,name):
    '''{"body":{"customerName":"李世明1","identifyType":"T0","identifyNo":"411201199602222491","_channel_id":"30","logonId":"0120171000001451"}}'''
    dic = {}
    dic_son = {}
    dic_son["identifyType"] = "T0"
    dic_son["_channel_id"] = "30"
    dic_son["logonId"] = "0120171000001451"
    dic_son["customerName"] = name
    dic_son["identifyNo"] = idmsg[0]
    dic["body"] = dic_son
    return json.dumps(dic,ensure_ascii=False,separators=(',', ':')).encode("utf-8")

def get_cus_info():
    id_msg = get_id_items()
    name = get_name()
    wec, wec_type, alipay, alipay_type = get_wec_and_alipay()
    cus_info = {}
    cus_info["companyPhone"] = "075445" + str(random.randint(10000,63214))
    cus_info["contacts"] = get_contacts()
    cus_info["companyAddress"] = "延吉街%s号-8-%s" %(random.randint(1,999),random.randint(1,99))
    cus_info["company"] = "企鹅有限公司"
    cus_info["earns"] = str(random.randint(0,999999))
    cus_info["education"] = random.choice(("L10","L20","L30","L40","L50","L60","L70","L80","L90","L99"))
    cus_info["homeAddress"] =  "龙华区清湖街道%s号-%s-%s" %(random.randint(1,999),random.randint(1,99),random.randint(1,99))
    cus_info["homePhone"] = "0755" + str(random.randint(11111111,99999999))
    cus_info["household"] = random.choice(("H1","H2"))
    cus_info["houseType"] = random.choice(("T5", "T10","T11","T13"))
    cus_info["householdAddress"] = "龙华区清湖街道%s-%s号"%(random.randint(1,999),random.randint(1,99))
    cus_info["identifyType"] = "T0"
    cus_info["identifyNo"] = id_msg[0]
    cus_info["birthday"] =  id_msg[1]
    cus_info["sex"] = id_msg[2]
    cus_info["customerName"] = name
    cus_info["phoneNumber"] = replace_char(get_phone(),str(random.choice((0,1,2))),1)
    cus_info["webchat"] = wec
    cus_info["webchatType"] = wec_type
    cus_info["alipay"] = alipay
    cus_info["alipayType"] = alipay_type
    cus_info["workYear"] = str(random.randint(0,50))
    cus_info["position"] = get_post()
    cus_info["marry"] = random.choice(("S10","S20","S21","S22","S23","S30","S40","S90"))
    cus_info["credit"] = ""
    cus_info["qq"] = ""
    cus_info["taobao"] = ""
    cus_info["remark"] =""
    cus_info["_channel_id"] ="30"
    cus_info["logonId"] = "0120171000001451"
    return cus_info

def get_json_value():
    dic_json_value = {}
    dic_json_value["body"] = get_cus_info()
    return json.dumps(dic_json_value,ensure_ascii=False,separators=(',', ':')).encode("utf-8")


if __name__ == '__main__':
    # s = requests.Session()
    # ret = s.request('POST', url=login_url, data=login_data, headers=headers)
    # print(ret.text)
    # ret1 = s.request('POST', url=add_cus_url, data=get_json_value(), headers=headers,)
    # print(ret1.text)
    # print(pakage_check(get_cus_info()["identifyNo"],get_cus_info()["customerName"]))
    print(json_value.encode("utf-8"))
    print(get_json_value())
    pass
