# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午4:24
# @Author  : YTQ
# @FileName: test_department.py
# @Software: PyCharm
from src.utils.log_utils import LogUtils
from src.wework_request.api.department import Department

log = LogUtils()

class TestDepartment:

    def setup_class(self):
        self.dp = Department()

    def test_add_department(self):
        ret = self.dp.add_department("测试添加8","1","10","40")
        log.info(ret)
        assert ret["errcode"] == 0


    def test_del_department(self):
        add_ret =self.dp.add_department("测试添加4","1","10","36")
        if add_ret["errcode"] == 0:
            dp_id = add_ret["id"]
            ret = self.dp.del_department(dp_id)
            assert ret["errcode"] == 0