#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json
import random

import requests

from src.utils.log_utils import LogUtils
from src.utils.random_name_phone import get_phone, get_name, get_post
from src.utils.random_id_card import RandomIdCard

log = LogUtils()

add_cus_url = "http://10.91.138.150:53013/zugou-management/gateway/preloan.service.cust.CustService.personalSave"
login_url = "http://10.91.138.150:53013/zugou-management/gateway/general.service.LoginService.staffLogin"
check_url = 'http://10.91.138.150:53013/zugou-management/gateway/preloan.service.cust.CustService.personalExist'
headers = {"Content-Type": "application/json;charset=utf-8"}
login_data = '{"body":{"userName":"%s","loginPwd":"e8ZM6a48N3u/niiLrEu+7IfNquDqxglfbJeGE03/GL7LNAFm4e11AEL0BXwh1iYz9mhUnSD3xp7XYaT3GmoQic8xHjnCCwZYZyj+U5X21aKfbw9WOtjIRJ/dLnpm1lEyG+VlDYt35amHNZry3hBvhdz7RzEQULFOn4pYf/8Y5kKbAUiV+lSYA6q6iQqrqlZnoyyCB3RbIy5Z8exnnNMOnxmR7U87bHQ+GIdkh/cO5Q4vGz8QY5PLXTLY85IaLHDkvFtQE9dTFE38wOblp2PtR1Y3/LM+zfKibV4blX5Rjg/nl82izd9gnM5BG71hqCF0xP67gdpV/nPuzrOWrgvBvA==","_channel_id":"30"}}'
json_data = '{"body":{"birthday":"2018-10-01","company":"四十大盗","companyAddress":"延吉街14号-8-10","companyPhone":"07544563214","contacts":[{"contactAddress":"啊实打实","contactName":"阿达","phone":"18565594511","relation":"R5"},{"contactAddress":"阿达","contactName":"阿达打","phone":"18369895624","relation":"R7"}],"customerName":"厉荷","earns":"50000","education":"L20","homeAddress":"发给分 发飞飞额","homePhone":"11012451245","houseType":"T11","household":"H1","householdAddress":"不知道那个地方","identifyNo":"450902201810015324","identifyType":"T0","marry":"S10","phoneNumber":"11386023421","position":"软件工程师","sex":"G2","workYear":"20","alipay":"","alipayType":"","credit":"","qq":"","taobao":"","webchat":"14541545441","webchatType":"1","remark":"","_channel_id":"30","logonId":"0120171000001451"}}'


class AddCuster:

    def __init__(self, userid):
        self.use_id = userid
        pass

    def get_contact(self, i):
        dic_contact = {}
        dic_contact["contactAddress"] = "深圳市龙华区%s" % random.choice(("民治街道", "清湖", "观澜", "龙华街道"))
        dic_contact["contactName"] = get_name()
        dic_contact["phone"] = get_phone()
        if i == 0:
            dic_contact["relation"] = random.choice(("R6", "R7"))
        else:
            dic_contact["relation"] = random.choice(("R4", "R5", "R8", "R11"))
        return dic_contact

    def get_contacts(self):
        contact_list = []
        for i in range(2):
            contact = self.get_contact(i)
            contact_list.append(contact)
        return contact_list

    def get_id_items(self):
        card_id = RandomIdCard().get_id_card()
        id = card_id[0]
        birth = id[6:10] + "-" + id[10:12] + "-" + id[12:14]
        if int(id[-2]) % 2 == 1:
            sex = "G1"
        else:
            sex = "G2"
        return id, birth, sex

    def replace_char(self, string, char, index):
        string1 = list(string)
        string1[index] = char
        return ''.join(string1)

    def get_wec_and_alipay(self):
        wec = str(random.choice(("", random.randint(1000000, 99999999))))
        if wec:
            alipay = str(random.choice(("", random.randint(1111111111, 99999999999))))
            if alipay:
                wec_type = str(random.choice((0, 1)))
                alipay_type = str(random.choice((0, 1)))
            else:
                wec_type = str(random.choice((0, 1)))
                alipay_type = ""
        else:
            alipay = str(random.randint(1111111111, 99999999999))
            alipay_type = str(random.choice((0, 1)))
            wec_type = ""
        return wec, wec_type, alipay, alipay_type

    def pakage_check(self, idmsg, name):
        '''{"body":{"customerName":"李世明1","identifyType":"T0","identifyNo":"411201199602222491","_channel_id":"30","logonId":"0120171000001451"}}'''
        dic = {}
        dic_son = {}
        dic_son["identifyType"] = "T0"
        dic_son["_channel_id"] = "30"
        dic_son["logonId"] = "0120171000001451"
        dic_son["customerName"] = name
        dic_son["identifyNo"] = idmsg[0]
        dic["body"] = dic_son
        return json.dumps(dic, ensure_ascii=False).encode("utf-8")

    def get_cus_info(self):
        ''' '{"body":{"birthday":"2018-10-01","company":"四十大盗","companyAddress":"延吉街14号-8-10","companyPhone":"07544563214","contacts":[{"contactAddress":"啊实打实","contactName":"阿达","phone":"18565594511","relation":"R5"},{"contactAddress":"阿达","contactName":"阿达打","phone":"18369895624","relation":"R7"}],"customerName":"厉荷","earns":"50000","education":"L20","homeAddress":"发给分 发飞飞额","homePhone":"11012451245","houseType":"T11","household":"H1","householdAddress":"不知道那个地方","identifyNo":"450902201810015324","identifyType":"T0","marry":"S10","phoneNumber":"11386023421","position":"软件工程师","sex":"G2","workYear":"20","alipay":"","alipayType":"","credit":"","qq":"","taobao":"","webchat":"14541545441","webchatType":"1","remark":"","_channel_id":"30","logonId":"0120171000001451"}}' '''
        id_msg = self.get_id_items()
        name = get_name()
        wec, wec_type, alipay, alipay_type = self.get_wec_and_alipay()
        cus_info = {}
        cus_info["companyPhone"] = "075445" + str(random.randint(10000, 63214))
        cus_info["contacts"] = self.get_contacts()
        cus_info["companyAddress"] = "%s%s号-8-%s" % (
            random.choice(("延吉街", "庆丰街道", "解放街")), random.randint(1, 999), random.randint(1, 99))
        cus_info["company"] = "%s有限公司" % random.choice(("企鹅", "苹果", "芒果", "万科", "富通"))
        cus_info["earns"] = str(random.randint(0, 999999))
        cus_info["education"] = random.choice(("L10", "L20", "L30", "L40", "L50", "L60", "L61"))
        cus_info["homeAddress"] = "龙华区清湖街道%s号-%s-%s" % (
            random.randint(1, 999), random.randint(1, 99), random.randint(1, 99))
        cus_info["homePhone"] = "0755" + str(random.randint(11111111, 99999999))
        cus_info["household"] = random.choice(("H1", "H2"))
        cus_info["houseType"] = random.choice(("T5", "T10", "T11", "T13"))
        cus_info["householdAddress"] = "龙华区清湖街道%s-%s号" % (random.randint(1, 999), random.randint(1, 99))
        cus_info["identifyType"] = "T0"
        cus_info["identifyNo"] = id_msg[0]
        cus_info["birthday"] = id_msg[1]
        cus_info["sex"] = id_msg[2]
        cus_info["customerName"] = name
        cus_info["phoneNumber"] = self.replace_char(get_phone(), str(random.choice((0, 1, 2))), 1)
        cus_info["webchat"] = wec
        cus_info["webchatType"] = wec_type
        cus_info["alipay"] = alipay
        cus_info["alipayType"] = alipay_type
        cus_info["workYear"] = str(random.randint(0, 50))
        cus_info["position"] = get_post()
        cus_info["marry"] = random.choice(("S10", "S20", "S30", "S91"))
        cus_info["credit"] = ""
        cus_info["qq"] = ""
        cus_info["taobao"] = ""
        cus_info["remark"] = ""
        cus_info["_channel_id"] = "30"
        cus_info["logonId"] = self.use_id
        return cus_info

    def get_json_value(self):
        dic_json_value = {}
        dic_json_value["body"] = self.get_cus_info()
        # separators=(',', ':')参数能进行json的默认，与：后面的空格消除
        return json.dumps(dic_json_value, ensure_ascii=False).encode("utf-8")

    def login(self):
        self.s = requests.Session()
        ret = self.s.request('POST', url=login_url, data=login_data % self.use_id, headers=headers)
        if ret.json()["responseCode"] == "000000":
            log.info("用户登录成功。")
        else:
            log.error(ret.json())
            log.warning("用户登录失败！")

    def do_add(self):
        do_json_value = self.get_json_value()
        cus_name = json.loads(do_json_value)["body"]["customerName"]
        log.info("使用 " + cus_name + " 进行客户新增")
        ret1 = self.s.request('POST', url=add_cus_url, data=do_json_value, headers=headers)
        if ret1.json()["responseCode"] == "000000":
            log.info("客户 " + cus_name + " 新增成功")
        else:
            log.error(ret1.json())
            log.warning("客户 " + cus_name + " 新增失败")

    def query_cus(self):
        url = 'http://10.91.138.150:53013/zugou-management/gateway/preloan.service.cust.CustService.personalView'
        data = '{"body":{"customerId":"30020191002018148","_channel_id":"30","logonId":"0120171000001451"}}'
        return self.s.request('POST', url=url, data=data, headers=headers)


if __name__ == '__main__':
    # 0120170600000924,0120171000001451
    add = AddCuster("0120170600000924")
    try:
        add.login()
        for i in range(2):
            add.do_add()
    except:
        pass
