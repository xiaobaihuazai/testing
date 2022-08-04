# -*- coding: utf-8 -*-
# @Time : 2022/7/23 15:11
# @Author : Aries
# @Site : 
# @File : test_api.py
# @Software: PyCharm
import pytest


class ATestApi:

    @pytest.mark.parametrize("name", ["python", "pytest", "request"])
    def test_api(self, name):
        print('测试学习:' + name)

    @pytest.mark.parametrize("time", [["python",10], [ "pytest", 30], ["request", 50]])
    def test_api2(self, time):
        print('测试学习时间:' + str(time))
