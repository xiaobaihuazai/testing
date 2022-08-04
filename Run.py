# -*- coding: utf-8 -*-
# @Time : 2022/7/21 15:57
# @Author : Aries
# @Site : 
# @File : Run.py
# @Software: PyCharm
import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./teap -o ./reports --clean")
