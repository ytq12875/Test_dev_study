#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/8/3 0:19
# @Author  :ytq
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSeleniumEx:

    # 初始化，制定驱动路径并最大化浏览器和设置隐式等待
    def setup_method(self):
        path = "D:/webdriver/chromedriver.exe"
        # 电脑一直调不出来debug换端口啥都试过就是没法打开debug端口
        # options = Options()
        # options.add_experimental_option ("debuggerAddress", "127.0.0.1:9222")
        # self.driver = webdriver.Chrome(executable_path = path,options = options)
        _com_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        _cookies = {
            "wwrtx.vst": "Nq1Up4blYq_PiiV37S9Y53Vjd_qXrqVAAZmesrAwrAF8VvmJqNADsT_Hk890jSkZBdLB33qTjkGsUCE264eRvJdX5cqTbjfJ_nSAm4UWZFIfXvCubG_BDk-0OKiVGXGVemJkbpw2WTDAPWv7xOpLdEfD5pVJe4c1J4O6XMX-uf4V5_90XorWjiZO3ya_QXpwf5lHXJJOm2A4yTD2VwOrtESFH46ZRdk91mjV8AUsxP5nYVebKJj3B9UrC9dGthMaZnZDR6S4YdhAcPyCY29fvA",
            "wwrtx.d2st": "a1320545",
            "wwrtx.sid": "bI84_UY69ZZEAv63EF98PeFtW_oIfsQGXCLA8IB51oF2d8RO1orD0ekRDp_GPiZq",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324940078869",
            "wxpay.vid": "1688851793816595",
        }
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.get(_com_url)
        for k, v in _cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(_com_url)
        self.driver.implicitly_wait(5)

    # 清理，关闭驱动
    def teardown_method(self):
        self.driver.quit()

    def get_cn_char(self, num):
        rd_str = ""
        for i in range(num):
            _head = random.randint(0xb0, 0xf7)
            _body1 = random.randint(0xa1, 0xf9)
            val = f'{_head:x}{_body1:x}'
            name = bytes.fromhex(val).decode('GBK')
            rd_str += name
        return rd_str

    def test_weiXin_c(self):
        name = self.get_cn_char(3)
        rd_phone = str(random.randint(13000000000, 13900000000))
        tel_phone = str(random.randint(20000000, 88888888))
        WebDriverWait(self.driver, 50).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="menu_index"]/span')))
        self.driver.find_element(By.ID, "menu_contacts").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "member_list")))
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
        # 上传头像
        self.driver.find_element(By.ID, "js_upload_file").click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input').send_keys(
            "E:/pic/demo.png")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR, ".js_file_reupload")))
        self.driver.find_element(By.CSS_SELECTOR, ".js_save").click()
        # 等待上传头像窗口消失
        WebDriverWait(self.driver, 30).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_file_reupload")))
        # 输入各input框
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys(name + "别名")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(rd_phone + "@qq.com")
        # 把所有选择radio放入selects变量中
        selects = self.driver.find_elements(By.CSS_SELECTOR, ".member_edit_item_right .ww_radio")
        random.choice(selects[:2]).click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(rd_phone)
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys("0755" + tel_phone)
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(rd_phone + "@qq.com")
        self.driver.find_element(By.ID, "memberEdit_address").send_keys(self.get_cn_char(8))
        self.driver.find_element(By.ID, "memberAdd_title").send_keys(self.get_cn_char(6))
        random.choice(selects[2:4]).click()
        random.choice(selects[4:6]).click()
        # 判断如果选择了自定义则输入自定义的职位
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".util_d_n")))
            self.driver.find_element(By.CSS_SELECTOR, ".util_d_n").send_keys(self.get_cn_char(3))
        except:
            pass
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((
            By.ID, "js_tips")))
        rst = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" in rst


if __name__ == '__main__':
    pytest.main(["-s", "test_selenium_ex_0803.py"])
