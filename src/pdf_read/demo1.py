#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

# sec = ["天津","重庆","南京","沈阳","武汉","成都","西安","杭州","大连","青岛","宁波","厦门","哈尔滨","济南","长春","郑州","长沙","福州","乌鲁木齐","昆明","兰州","苏州","无锡","南昌","贵阳","南宁","合肥","太原","石家庄","呼和浩特","扬州","佛山 ","东莞","烟台","温州","淄博","三亚","海口"]
#
# while True:
#     find = input()
#     if find in sec:
#         print("IN")
#     else:
#         print("No")
import json

import requests
login_url = "http://10.91.138.102:53013/fzuche-oper/los/fzuche-intf-login.staffLogin"
sb_url = "http://10.91.138.102:53013/fzuche-oper/los/fzuche-intf-vehicle.saveWithholdInstall"
pload = {"custName":"江南","applyNo":"ZGSQ2019072300010","stopWithholdDateStart":"","stopWithholdDateEnd":"","withholdInstallType":"2","withholdAmount":"0.01","realtimeWithholdType":"21","withholdAmountType":"01","_channel_id":"66","logonId":"0120170200000406"}
data={
    'userName':(None, "0120170200000406"),
    'loginPwd': (None, "ZMAlef6DOCSsddQUQVF2HGuej23HgWqxYjc%2BkS8ThWWrkRoXqarLzdn7q2TqTaWfm%2B9EK%2FN%2FSO1VctoX0QQwQBUXPrdjIyVWyB88HJNzWDpkTW%2BPlWy%2FbxNt%2BjK9rzlu6Kmr8kqLcNAJUEzyL%2B%2BWE1x4sjHi8D66umaGwuW9fsr62EGvzNmpLVg7Al3G0x1FlZhRc0yxlKjfM2k6FD1PdKdC7piVBXmJ0eyoriJkGqexiOhI9ukDei2vp1XtYc1sE4ehHKjNeE28YxS5g99eAGI90ENrXywkhOMEgrDDTEAdrsem8BttF0XipOevhvjT%2BR4hEj8e4SpGxFAM0TM5Ug%3D%3D"),
    '_channel_id': (None, "66"),
}
query_url = "http://10.91.138.102:53013/fzuche-oper/los/fzuche-intf-vehicle.queryCurrentAmount"
query_data = {"applyNo":"ZGSQ2019072300010","custName":"江南","realtimeWithholdType":"21","withholdAmountType":"01","_channel_id":"66","logonId":"0120170200000406"}
s = requests.session()
ret = s.request("POST",login_url,files=data)

print(ret.request.url)
print(ret.request.body)
print(ret.json())

# ret2 = s.post(query_url,json.dumps(query_data,ensure_ascii=False, separators=(',', ':')).encode("utf-8"))
# print(ret2.text)
# ret1 = s.post(sb_url,json.dumps(pload,ensure_ascii=False, separators=(',', ':')).encode("utf-8"))
# print(ret1.text)