# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午4:24
# @Author  : YTQ
# @FileName: test_department.py
# @Software: PyCharm
import os

import pytest

from src.utils.log_utils import LogUtils
from src.wework_request.api.department import Department

log = LogUtils()

class TestDepartment:

    def setup_class(self):
        self.dp = Department()

    @pytest.mark.parametrize("dpt_name,parentid,order,_id", [("测试添加9","1","10","41")])
    def test_add_department(self,dpt_name,parentid,order,_id):
        ret = self.dp.add_department(dpt_name,parentid,order,_id)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("dpt_name,parentid,order,_id", [("测试添加8_改名","1","10","40")])
    def test_update_department(self,dpt_name,parentid,order,_id):
        ret = self.dp.update_department(dpt_name,parentid,order,_id)
        assert ret["errcode"] == 0

    @pytest.mark.parametrize("dpt_name,parentid,order,_id",[("测试添加4","1","10","36")])
    def test_del_department(self,dpt_name,parentid,order,_id):
        add_ret =self.dp.add_department(dpt_name,parentid,order,_id)
        if add_ret["errcode"] == 0:
            dp_id = add_ret["id"]
            ret = self.dp.del_department(dp_id)
            assert ret["errcode"] == 0
        else:
            log.error("部门新增失败！")

if __name__ == '__main__':
    pytest.main("--alluredir=test_result/allureReports")
    # pytest.main(['-s', '-q', '--alluredir', './report/xml/'])
    # rep_cmd = "allure generate report/xml -o report/html"
    # os.system(rep_cmd)