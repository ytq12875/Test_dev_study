#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
import json
import os
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.back_money.common.read_yaml import YamlParser
from src.utils.log_utils import LogUtils

log = LogUtils()


class SeleniumUtils:

    def __init__(self, env):
        env_path = os.path.dirname(os.getcwd()) + '/config/'
        user_env_file = YamlParser("user_env", env_path)
        user_file = YamlParser("login", env_path)
        url = user_env_file.get_yaml_data(env).get("url")
        self.user = user_file.get_yaml_data(env).get("login_name")
        self.psw = user_file.get_yaml_data(env).get("login_psw")
        # path = "D:/webdriver/chromedriver.exe"
        path = "/home/ytq/webdriver/78.0.3904.70/chromedriver"
        # 无头模式
        log.info("进入无头Chrome模式...")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        # self.driver = webdriver.Chrome(executable_path=path)
        # self.driver.maximize_window()
        self.driver.set_window_size(1366, 768)
        self.driver.implicitly_wait(30)
        self.driver.get(url)

    def login(self, user, psw):
        log.info("用户登录中...")
        self.driver.find_element(By.ID, "loginName").send_keys(user)
        self.driver.find_element(By.ID, "loginPwd").send_keys(psw)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-lg").click()

    def goto_service(self):
        log.info("进入zuche-paycloud-core.channel.testSpecialRefund服务...")
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#root > div > main > div > aside > div.menu > ul > li:nth-child(3) > div > span").click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Service")]').click()
        self.driver.find_element(By.ID, "gearNameLike").send_keys("zuche-paycloud-core")
        self.driver.find_element(By.ID, "serviceNameLike").send_keys("zuche-paycloud-core.channel.testSpecialRefund")
        self.driver.find_element(By.CSS_SELECTOR, ".ant-col-lg-offset-1 .ant-btn-primary").click()
        self.driver.find_element(By.XPATH, '//a[text()="调用"]').click()

    def set_value_for_back(self, value):
        self.driver.find_element(By.ID, "jsonArgs").clear()
        log.info("进行数据：" + value + "的退款操作...")
        self.driver.find_element(By.ID, "jsonArgs").send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-modal-footer .ant-btn.ant-btn-primary.ant-btn-lg").click()
        sleep(2)

    def get_rst(self):
        # 使用bs4从页面元素提取值

        # source = self.driver.page_source
        # doc = BeautifulSoup(source, "html.parser")
        # doc1_list = doc.find_all('textarea', class_="ant-input ant-input-lg")
        # for doc1 in doc1_list:
        #     if 'readonly' in str(doc1):
        #         return doc1.get_text()
                # return json.loads(rtn)["responseCode"]
        # 通过xpath定位元素并进行json转换
        rtn = self.driver.find_elements(By.XPATH,'//*[@class="ant-input ant-input-lg" and @type="textarea"]')[1].text
        return json.loads(json.dumps(rtn))

    def quit_driver(self):
        self.driver.quit()

    def do_selenium(self, json_list):
        try:
            self.login(self.user, self.psw)
            self.goto_service()
            rtn_json_list = []
            for json_value in json_list:
                self.set_value_for_back(json_value)
                retry = 0
                while retry < 10:
                    rtn = self.get_rst()
                    if rtn:
                        new_json = json.dumps({**json.loads(json_value), **{"rtn_msg": rtn}})
                        rtn_json_list.append(new_json)
                        break
                    elif retry < 10:
                        log.info("等待退款结果返回！")
                        sleep(1)
                        retry +=1
                    else:
                        log.error("10秒未得到返回,请重试！")
            return rtn_json_list
        except Exception as e:
            log.error("退款操作发生了异常"+str(e))
        finally:
            self.quit_driver()


if __name__ == '__main__':
    sel = SeleniumUtils("uat")
    json_list = ['{"payChannelNo": "1002","bsmJnlNo": "100220190827144849ST90100367"}',
                 '{"payChannelNo": "1002","bsmJnlNo": "100220190827144229ST90100357"}']
    sel.do_selenium(json_list)