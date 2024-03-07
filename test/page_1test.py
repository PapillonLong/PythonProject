#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : page_test.py
from base.base_case import BaseCase
from base.base_def import BaseDef
from pages.base_page import BasePage
import time

class PageTest(BaseCase):

    def setUp(self) -> None:
        super().setUp()
        # 页面跳转
        # self.HomePage.interface_page("page")

    def __init__(self, methodName='runTest'):
        """
        初始化PageTest类，初始化基础页、首页类
        """
        super(PageTest, self).__init__(methodName)
        self.BaseDef = BaseDef(self)

    def test1_get_home_city(self):
        """
        基础标签元素定位测试
        :return: 断言首页的北京市是否存在
        """
        ele = self.BaseDef.get_element_xpath("/page/view[1]/head-navigation//view/view[1]/view/view[2]", 5)
        if ele:
            self.logger.info(ele.inner_text)
        else:
            self.logger.info("未找到该元素")
        self.assertEqual("北京市",ele.inner_text)
    
    def test_get_tab_coupon(self):
        """
        切换到优惠券tab，检查搜索框下的热搜，分类区域和tab显示
        """
        self.BaseDef.switch_to_tabbar('/pages/new/find/find')
        time.sleep(3)
        hot_text = self.BaseDef.get_element_selector("/page/view[2]/view/view")
        if hot_text:
            self.logger.info(hot_text.inner_text)
        else:
            self.logger.info("热搜不存在")
        self.assertEqual("热搜:",hot_text.inner_text)

        tab1 = self.BaseDef.get_element_xpath('//*[@id="tab-header"]/view[1]')
        if tab1:
            self.logger.info(tab1.inner_text)
        else:
            self.logger.info("美食餐厅tab不存在")
        self.assertEqual("美食餐厅",tab1.inner_text)

        types = self.BaseDef.get_element_custom('gold-pos>>>view')
        if types:
            self.logger.info(types.inner_text)
        else:
            self.logger.info("分类区不存在")
        
        self.assertIn("烤肉",types.inner_text)