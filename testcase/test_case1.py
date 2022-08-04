# -*- coding: utf-8 -*-
# @Time : 2022/7/21 15:56
# @Author : Aries
# @Site : 
# @File : test_case1.py
# @Software: PyCharm
import pytest
from ddt import ddt, data, unpack
from common.excel_utl import ExcelUtl
from log.log import Log




class TestCase:

    log = Log()
    logger = log.get_log()

    def testcase1(self, ):
        self.logger.info("执行测试用例")
        print("测试用例1:" )
        self.logger.info("结束测试用例")

#
# def test_get_num():
#     print("get num ceshi !!")
import os

from common.yaml_utl import YamlUtl
# #
# YamlUtl().write_extract_yaml({"shuzhi": 123})
# csfr_token = YamlUtl().read_extract_yaml("shuzhi")
# print(csfr_token)
# print(os.getcwd())

