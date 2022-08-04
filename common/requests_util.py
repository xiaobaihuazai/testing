# -*- coding: utf-8 -*-
# @Time : 2022/7/23 16:26
# @Author : Aries
# @Site : 
# @File : requests_util.py
# @Software: PyCharm
import requests


class RequestsUtil:
    session = requests.session()

    def send_requests(self, method, url, **kwargs):
        rep = RequestsUtil.session.request( method, url, **kwargs)
        return rep
