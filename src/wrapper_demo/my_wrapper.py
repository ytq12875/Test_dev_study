# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午8:52
# @Author  : YTQ
# @FileName: my_wrapper.py
# @Software: PyCharm
from src.utils.log_utils import LogUtils

log = LogUtils()

class Screen:

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        def inner(*args, **kwargs):
            log.info("用例{}开始执行...".format(func.__name__))
            try:
                func(*args, **kwargs)
            except Exception as e:
                import time
                screenName = func.__name__
                log.error("用例{}执行报错{}".format(screenName, str(e)))
                nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("%s.png" % nowtime)
        return inner
