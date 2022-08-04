# -*- coding: utf-8 -*-
# @Time : 2022/7/31 16:45
# @Author : Aries
# @Site : 
# @File : log.py
# @Software: PyCharm
"""日志器封装"""
import logging


class Log:
    def __init__(self, level="DEBUG"):
        # 日志器对象
        self.log = logging.getLogger("Testing")
        self.log.setLevel(level)

    def console_headle(self, level="INFO"):
        """控制台处理器"""
        console_headle = logging.StreamHandler()
        console_headle.setLevel(level)
        # 日志显示格式化
        console_headle.setFormatter(self.get_formater()[0])

        return console_headle
    
    def file_headle(self, level="INFO"):
        """文件处制器"""
        file_headle = logging.FileHandler("log/log.txt", mode='a', encoding="utf-8")
        file_headle.setLevel(level)
        file_headle.setFormatter(self.get_formater()[1])

        return file_headle

    def get_formater(self):
        """格式化显示"""
        console_fmt = logging.Formatter(fmt="## %(asctime)s ------》》%(levelname)-8s [%(filename)s:%(lineno)s]------》》%(message)s")
        file_fmt = logging.Formatter(fmt="### %(name)s ## %(asctime)s ------》》%(levelno)s------》》%(message)s")

        return console_fmt, file_fmt

    def get_log(self):
        """日志器添加处理器"""
        self.log.addHandler(self.console_headle())
        self.log.addHandler(self.file_headle())
        return self.log
