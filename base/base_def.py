#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/02/25 14:55
# @Author  : liuxinbo
# @Email   : liuxinbo@cmcm.com
# @File    : base_def.py


class BaseDef:
    """
    封装Minium元素定位、页面跳转方法
    """

    def __init__(self, mini):
        """
        初始化，Minium实例
        :param mini:
        """
        self.mini = mini

    def get_element_selector(self, selector, timeout=10):
        """
        基础标签元素定位
        :param selector: 元素
        :param timeout:超时时间
        :return: 返回节点
        """
        bol = self.mini.page.element_is_exists(selector, max_timeout=timeout)
        ret = None
        if bol:
            ret = self.mini.page.get_element(selector)
        return ret

    def get_element_selector_text(self, selector, inner_text, timeout=10):
        """
        基础标签元素带text定位
        :param selector: 元素
        :param inner_text: 内容
        :param timeout: 超时时间
        :return: 返回节点
        """
        bol = self.mini.page.element_is_exists(selector, max_timeout=timeout)
        ret = None
        if bol:
            ret = self.mini.page.get_element(selector, inner_text)
        return ret

    def get_element_xpath(self, xpath, timeout=10):
        """
        xpath定位
        :param xpath: xpath元素
        :param timeout: 超时时间
        :return: 返回节点
        """
        bol = self.mini.page.element_is_exists(xpath, max_timeout=timeout)
        ret = None
        if bol:
            ret = self.mini.page.get_element(xpath)
        return ret

    def get_element_custom(self, custom, timeout=10):
        """
        自定义组件定位
        :param custom: 自定义组件名
        :param timeout: 超时时间
        :return: 返回节点
        """
        bol = self.mini.page.element_is_exists(custom, max_timeout=timeout)
        ret = None
        if bol:
            ret = self.mini.page.get_element(custom)
        return ret

    def get_elements_selector(self, selector, timeout=10):
        """
        批量基础标签元素定位
        :param selector: 元素
        :param timeout: 超时时间
        :return: 返回节点
        """
        bol = self.mini.page.element_is_exists(selector, max_timeout=timeout)
        ret = None
        if bol:
            ret = self.mini.page.get_elements(selector)
        return ret

    def get_elements_selector_text(self, selector, inner_text, timeout=10):
        """
        批量基础标签元素带text定位
        :param selector: 元素
        :param inner_text: 内容
        :param timeout: 超时时间
        :return: 返回节点
        """
        bol = self.mini.page.element_is_exists(selector, max_timeout=timeout)
        ret = None
        if bol:
            ret = self.mini.page.get_elements(selector, inner_text)
        return ret

    def wait_page(self, route):
        """
        等待页面跳转成功
        :param route: 跳转路径
        :return: 返回True或False
        """
        ret = self.mini.app.wait_for_page(route)
        if ret:
            return True
        return False

    def navigate_to_page(self, route, params=None):
        """
        以导航的方式跳转到指定页面,不能跳转到tabbar页面
        支持相对路径和绝对路径,小程序中页面栈最多十层
        :param route: 页面路径
        :param params: 页面路径参数
        :return ret: 页面跳转结果，True或者False
        :return page: page对象
        """
        navigate_page = self.mini.app.navigate_to(route, params)
        ret = self.wait_page(route)
        print(navigate_page)
        print(ret)
        return ret, navigate_page

    def redirect_to_page(self, route, params=None):
        """
        关闭当前页面，重定向到应用内的某个页面,不能跳转到abbar页面
        :param route: 页面路径
        :param params: 页面路径参数
        :return ret: 页面跳转结果，True或者False
        :return page: page对象
        """
        redirect_page = self.mini.app.redirect_to(route, params)
        ret = self.wait_page(route)
        return ret, redirect_page

    def switch_to_tabbar(self, route):
        """
        跳转到tabBar页面,会关闭其他所有非tabBar页面
        :param route: 页面路径
        :return ret: 页面跳转结果，True或者False
        :return page: page对象
        """
        switch_page = self.mini.app.switch_tab(route)
        ret = self.wait_page(route)
        return ret, switch_page

