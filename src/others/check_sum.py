#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

import itertools
import random

alipay = [5,2,0]
age = [1,5,10,7,3]
study = [5,4,3,1,1,1,1]
sex = [2,4]
prove = [5,3]
marry = [3,5,1,1]
house = [2,10,8,6,4]
wechat = [5,2,0]
first = [5,3,2,0]
product = [3,6,3,3,4,3,3,4,6]
long = [5,4,3,3,2]
charge = [6,4,3,1]
workyear = [4,3,2,1]
commonmen = [10,0]
tianchuang = [0,1,3,5,5]
pengyuan = [7,3,0]
tongdun = [8,3,1,0]
lis = []
lis.append(alipay)
lis.append(age)
lis.append(study)
lis.append(sex)
lis.append(prove)
lis.append(marry)
lis.append(house)
lis.append(wechat)
lis.append(first)
lis.append(product)
lis.append(long)
lis.append(charge)
lis.append(workyear)
lis.append(commonmen)
lis.append(tianchuang)
lis.append(pengyuan)
lis.append(tongdun)

def min(lis):
    sum = 0
    for lis_a in lis:
        lis_a.sort()
        sum+=lis_a[0]
    return sum
def max(lis):
    sum = 0
    for lis_a in lis:
        lis_a.sort()
        sum +=lis_a[-1]
    return sum

def choose(lis,chos):
    sum1 = 0
    sum2 = 0
    i = 1
    msg = ''
    for lis_a in lis:
        lis_a.sort()
        if len(lis_a) > int(chos):
            msg = str(i) +"表中的第 "+ str(chos) + " 个元素；"
            sum1 +=lis_a[int(chos)]
            msg += msg
        else:
            msg = str(i) + "表中的第 " + str(chos) + " 个元素；"
            num = random.choice((0,1,-1,-2))
            sum2 += lis_a[num]
            msg += msg
        i += 1
    return sum1+sum2,msg


# print(min(lis))
# print(max(lis))
list_a = []
for i in range(10):
    for j in range(6):
        list_a.append(choose(lis,j))
print(list_a)