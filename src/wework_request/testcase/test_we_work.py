# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 下午3:20
# @Author  : YTQ
# @FileName: test_we_work.py
# @Software: PyCharm
from src.utils.log_utils import LogUtils
from src.wework_request.api.wework import WeWork

log = LogUtils()


class TestWeWork:

    def test_get_token(self):
        fo = WeWork()
        token = fo.get_token("","")
        log.info(token)
        assert token is not None
