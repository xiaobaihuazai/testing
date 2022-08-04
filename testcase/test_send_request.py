# -*- coding: utf-8 -*-
# @Time : 2022/7/21 16:06
# @Author : Aries
# @Site : 
# @File : test_send_request.py
# @Software: PyCharm


# 发送get请求
import re

import pytest
import requests

from common.requests_util import RequestsUtil
from common.yaml_utl import YamlUtl


class TestSendRequest:
    # csfr_token = ""
    # cks = ''
    # session = requests.session()
    # access_token = ""

    def test_get_token(self):
        # 获取鉴权码
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        date = {
            "grant_type": "client credential",
            "appid": "wx6db11b3efd1cdc690",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        rep = requests.request('get', url=url, params=date)
        # print(rep.json())
        # # 保存全局变量方式
        # TestSendRequest.access_token = rep.json()['access_token']
        # 保存至yaml文件的方式
        print(rep.json())
        access_token = rep.json()['errmsg']
        YamlUtl().write_extract_yaml({"access_token": access_token})
        # 断言
        assert 'errmsg' in rep.json()

    # @pytest.mark.parametrize("casedate", YamlUtl().read_testcase_date_yaml("get_token.yml"))
    # def test_get_token2(self, casedate):
    #     # 获取鉴权码
    #     url = casedate["request"]["url"]
    #     method = casedate.get("request").get("method")
    #     date = casedate.get("request").get("date")
    #     rep = RequestsUtil().send_requests(method=method, url=url, params=date)
    #     result = rep.json()
    #     print(result)
    #     if "errmsg" in result:
    #         YamlUtl().write_extract_yaml({"access_token": result["errmsg"]})
    #         # 断言
    #         assert 'errmsg' in rep.json()
    #     else:
    #         print(casedate.get("name") + ":功能未通过")

    # def test_edit_flag(self):
    #     url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token' + TestSendRequest.access_token
    #     date = {"tag": {"id": 132, "name": "广东人"}}
    #     rep = requests.request("post", url=url, json=date)
    #     print(rep.json())
    #
    # def test_file_upload(self):
    #     # # 使用全局变量的方式
    #     # url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token' + TestSendRequest.access_token
    #     # 使用yaml文件读取的方式
    #     access_token = YamlUtl().read_extract_yaml("access_token")
    #     url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token' + access_token
    #     date = {
    #         "media": open(r"./misg/shu.png", "rb")
    #     }
    #     rep = requests.request('post', url=url, files=date)
    #     print(rep.json())

    """
    1、获取cookie放在类全局变量中
    2、获取session放在全局变量中，请求使用全局变量的session访问
    """

    # 使用带cookie关联的接口测试
    # def test_strat(self):
    #     url = "http://47.107.116.139/phpwind"
    #     rep = self.session.request("get", url=url)
    #     # print(rep.text)
    #     # # 保存全局变量方式
    #     # TestSendRequest.csfr_token = re.search('csrf_token" value="(.*?)"/', rep.text)[1]
    #     # 保存至yaml文件的方式
    #     csrf_token = re.search('csrf_token" value="(.*?)"/', rep.text)[1]
    #     print(csrf_token)
    #     YamlUtl().write_extract_yaml({"csrf_token": csrf_token})
    #     # print(TestSendRequest.csfr_token)
    #     # TestSendRequest.cks = rep.cookies
    #
    # # 将该用例分组为smoki组中
    # # @pytest.mark.smoki
    # def test_login(self, conn_database):
    #     csfr_token = YamlUtl().read_extract_yaml("csfr_token")
    #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     date = {
    #         "username": "addmind",
    #         "password": "addmind",
    #         # "csfr_token": TestSendRequest.csfr_token,
    #         "csfr_token": csfr_token,
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     headers = {
    #         "Accept": "application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     # rep = requests.request("post", url=url, json=date, headers=headers, cookies=TestSendRequest.cks)
    #     # 使用session访问时不再需要cookie参数
    #     rep = self.session.request("post", url=url, json=date, headers=headers)
    #     print(rep.json())
