# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午9:52
# @Author  : YTQ
# @FileName: my_driver.py
# @Software: PyCharm
from selenium import webdriver


def browser(browser):
    try:
        if browser == "chrome":
            # path = "/home/ytq/webdriver/78.0.3904.70/chromedriver"
            path = "D:/webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            return driver
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path="geckodriver")
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        else:
            print("Not found this browser, You can enter 'chrome','firefox' or 'ie'")
    except Exception as msg:
        print ("%s" % msg)


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % self.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

if __name__ == '__main__':

    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(v1+v2)