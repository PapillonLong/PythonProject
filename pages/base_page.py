#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/03/02 14:55
# @Author  : liuxinbo
# @Email   : liuxinbo@cmcm.com
# @File    : base_page.py
import threading
import time
from base.base_def import BaseDef


class BasePage(BaseDef):
    """
    封装公共页面的基础操作
    """
    def hook_wx_method(self, method, selector):
        """
        封装hook wx API接口，获取对应回调
        :param method: 接口
        :param selector: 需要触发的选择器
        :return: 回调
        """
        # 信号量
        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args
        # hook wx API接口，获取回调后执行的callback
        self.mini.app.hook_wx_method(method, callback=callback)
        # 判断选择器是否存在，存在进行点击操作
        if selector:
            self.mini.page.get_element(selector).tap()
        is_called = called.acquire(timeout=10)
        # 释放hook
        self.mini.app.release_hook_wx_method(method)
        return is_called, callback_args

    def hook_nativate_method(self, attr_method, method=None, selector=None, value=None):
        """
        封装hook wx native处理原生控件弹窗，获取对应回掉信息
        :param attr_method: 处理弹窗的方法
        :param method: 原生控件方法
        :param selector: 需要触发的选择器
        :param value: 弹窗的参数值
        :return: 信号量，回调信息
        """
        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args
        # hook 小程序API，获取回调后执行callback
        if method:
            self.mini.app.hook_wx_method(method, callback=callback)
        # 判断选择器是否存在，存在进行点击操作
        if selector:
            self.get_element_selector(selector).tap()
        time.sleep(2)
        # 授权弹窗处理，例如self.native.allow_get_location()
        if value is None:
            getattr(self.mini.native, attr_method)()
        else:
            getattr(self.mini.native, attr_method)(value)

        is_called = called.acquire(timeout=10)
        # 释放hook 小程序API方法
        if method:
            self.mini.app.release_hook_wx_method(method)
        return is_called, callback_args

    def hook_current_page_method(self, attr_method, method=None, selector=None, **kwargs):
        """
        hook当前页面的方法，并获取回调
        :param attr_method: 操作方法
        :param method: 页面方法
        :param selector: 元素选择器
        :param value: 操作方法参数值
        :param param: 操作方法参数名
        :return: 信号量，回调信息
        """
        callback_args = None
        # 监听回调, 阻塞当前主线程
        callback_called = threading.Semaphore(0)

        def callback(args):
            nonlocal callback_args
            callback_args = args
            callback_called.release()

        # hook指定方法，监听事件
        if method:
            self.mini.app.hook_current_page_method(method, callback)
        if selector:
            ele = self.get_element_selector(selector)
            # 调用指定方法
            # 例如ele.scroll_to(top=40, left=0)
            getattr(ele, attr_method)(**kwargs)
        callback_called.acquire(timeout=10)
        # 释放当前方法hook
        if method:
            self.mini.app.release_hook_current_page_method(method)
        return callback_called, callback_args

    def mock_wx_method(self, method, expect_result):
        """
        mock wx API
        :param method: API接口
        :param expect_result: 预期的返回值
        :return: 返回值
        """
        # mock API
        self.mini.app.mock_wx_method(method=method, result=expect_result)
        # 获取回调信息
        info = self.mini.app.call_wx_method(method)
        # 去掉函数的mock
        self.mini.app.restore_wx_method(method)
        return info
