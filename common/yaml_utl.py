# -*- coding: utf-8 -*-
# @Time : 2022/7/22 12:07
# @Author : Aries
# @Site : 
# @File : yaml_utl.py
# @Software: PyCharm
import os

import yaml


class YamlUtl:

    # 读取yaml文件
    def read_extract_yaml(self, key):
        print("-------------》文件地址：" + os.getcwd()+"/extract.yml")
        with open(os.getcwd()+"/extract.yml", mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 写入yaml文件
    def write_extract_yaml(self, date):
        with open(os.getcwd()+"/extract.yml", mode="a", encoding="utf-8") as f:
            yaml.dump(date, stream=f, allow_unicode=True)

    # 清楚yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml", mode="w", encoding="utf-8") as f:
            f.truncate()

    # # 读取测试用例数据yaml文件
    # def read_testcase_date_yaml(self, yaml_name):
    #     print("-------------》文件地址：" + os.getcwd()+"/extract.yml")
    #     print(os.getcwd()+"/date/" + yaml_name)
    #     with open(os.getcwd()+"/testcase/date/" + yaml_name, mode="r", encoding="utf-8") as f:
    #         value = yaml.load(stream=f, Loader=yaml.FullLoader)
    #         return value
