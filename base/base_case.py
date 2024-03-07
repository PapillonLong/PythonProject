#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/02/22 15:30
# @Author  : liuxinbo
# @Email   : liuxinbo@cmcm.com
# @File    : base_case.py

import minium


class BaseCase(minium.MiniTest):
    """
    测试用例基础类，初始化Minium实例
    """
    @classmethod
    def setUpClass(cls):
        super(BaseCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        pass

    def tearDown(self):
        pass



