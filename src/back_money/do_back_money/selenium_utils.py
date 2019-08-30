#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.back_money.common.read_yaml import YamlParser


class SeleniumUtils:

    def __init__(self,env):
        env_path = "D:\\Test_dev\\src\\back_money\\config"
        user_env_file = YamlParser("user_env", env_path)
        url = user_env_file.get_yaml_data(env).get("url")
        path = "D:/webdriver/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(url)

    def login(self,user,psw):
        self.driver.find_element(By.ID,"loginName").send_keys(user)
        self.driver.find_element(By.ID,"loginPwd").send_keys(psw)
        self.driver.find_element(By.CSS_SELECTOR,".ant-btn-lg").click()

    def goto_service(self):
        self.driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > aside > div.menu > ul > li:nth-child(3) > div > span").click()
        self.driver.find_element(By.XPATH,'//a[contains(text(),"Service")]').click()
        self.driver.find_element(By.ID,"gearNameLike").send_keys("zuche-paycloud-core")
        self.driver.find_element(By.ID,"serviceNameLike").send_keys("zuche-paycloud-core.channel.testSpecialRefund")
        self.driver.find_element(By.CSS_SELECTOR,".ant-col-lg-offset-1 .ant-btn-primary").click()
        self.driver.find_element(By.XPATH,'//a[text()="调用"]').click()


    def set_value_for_back(self,value):
        self.driver.find_element(By.ID, "jsonArgs").clear()
        self.driver.find_element(By.ID,"jsonArgs").send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR,".ant-modal-footer .ant-btn.ant-btn-primary.ant-btn-lg").click()
        sleep(5)

    def get_rst(self):
        # todo: print(self.driver.find_element(By.CSS_SELECTOR, "textarea .ant-input .ant-input-lg").text)
        # return self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div/span/textarea").text
        pass

    def quit_driver(self):
        self.driver.quit()

    def do_selenium(self,user,psw,json_list):
        try:
            self.login(user, psw)
            self.goto_service()
            for json_value in json_list:
                self.set_value_for_back(json_value)
                # print(self.get_rst())
        except Exception as e:
            print(e)
        finally:
            self.quit_driver()


if __name__ == '__main__':
    sel = SeleniumUtils("uat")
    user = "testUser"
    psw = "1234abcd"
    json_list = ['{"payChannelNo": "1002","bsmJnlNo": "100220190827144849ST90100367"}','{"payChannelNo": "1002","bsmJnlNo": "100220190827144229ST90100357"}']
    sel.do_selenium(user,psw,json_list)