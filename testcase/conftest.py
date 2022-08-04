# -*- coding: utf-8 -*-
# @Time : 2022/7/22 12:34
# @Author : Aries
# @Site : 
# @File : conftest.py
# @Software: PyCharm
import pytest

from common.yaml_utl import YamlUtl


@pytest.fixture(scope="function")
def conn_database():
    print("链接数据库")
    yield
    print("关闭数据库")


# 自动清楚每个会话后的yaml记录的信息
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtl().clear_extract_yaml()
