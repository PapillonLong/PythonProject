#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : page_test.py
from base.base_case import BaseCase
from base.base_def import BaseDef
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

    def test_1_get_red(self):
        """
        步数兑换红包
        """
        #进入我的页面
        self.BaseDef.switch_to_tabbar("/pages/me/me")
        current_path = self.BaseDef.mini.app.get_current_page().path
        self.logger.info(f"当前页面路径:{current_path}")
        if current_path == '/pages/me/me':
            self.logger.info("切换到我的页面")
            #点击步数换红包，进入步数换红包页面
            exchange_red = self.BaseDef.get_element_xpath("/page/view/scroll-view/view/view[2]/checkin-item//view/permission-button//button")
            if exchange_red:
                exchange_red.click()
                self.logger.info("进入步数兑换红包页")
            else:
                self.fail("进入步数兑换红包页失败")
            time.sleep(1)
            self.native.handle_modal(btn_text="允许")
            time.sleep(3)
            #点击立即兑换按钮，兑换红包
            exchange_btn = self.BaseDef.get_elements_selector("permission-button")
            self.assertIn("立即兑换", exchange_btn[0].text)
            if exchange_btn[0]:
                exchange_btn[0].click()
            else:
                self.fail("无红包可兑换")
            time.sleep(2)
            self.BaseDef.get_element_custom(".reedem_confirm_dialog_buton").click()
            self.logger.info("红包兑换成功")
        else:
            self.fail("切换到我的页面失败！") 


    def test_2_search_coupon(self):
        PageTest.search_coupon(self, "单店券")
    
    def te1st_3_buy_coupon(self):
        PageTest.search_coupon(self, "单店券")
        PageTest.buy_coupon(self)
    
    def search_coupon(self,coupon_name):
        try:
            self.BaseDef.switch_to_tabbar('/pages/home/home/index')
            ele = self.BaseDef.get_element_xpath("/page/view[1]/head-navigation//view/view[2]/view[1]/view[2]", 5)
            if ele:
                ele.click()
                self.logger.info("点击搜索框成功")
                time.sleep(3)
                self.native.input_text("单店券")
                self.logger.info("输入文本成功")
                search = self.BaseDef.get_element_xpath("/page/view/van-search/view",10)
                if search:
                    exit = self.BaseDef.mini.page.element_is_exists("/page/view/van-search/view")
                    if exit:
                        ##self.BaseDef.mini.page.get_element('.search_button').click()
                        self.BaseDef.get_element_custom('.search_button').click()
                        self.logger.info("点击搜索成功")
                    else:
                        self.fail("搜索按钮不存在")
                else:
                    self.fail("点击搜索失败")    
            else:
                self.fail("未找到搜索输入框")
            self.assertEqual("优惠券",self.BaseDef.get_element_xpath("/page/scroll-view/view[1]/view[1]/view").inner_text)
        except Exception as e:
            self.fail(f"出现异常：{e}")

    def buy_coupon(self):
        
        try:
            #点击优惠券进入优惠券详情页
            if(self.BaseDef.mini.page.element_is_exists("/page/view[2]/view/view")):
                self.logger.info("未找到优惠券")
            else:
                self.BaseDef.get_element_custom('.list-item-content-info-name').click()

            time.sleep(10)
            #判断立即购买按钮是否存在，若存在则点击按钮
            buy = self.BaseDef.mini.page.get_elements('permission-button>>>button')
            if buy:
                #如果按钮存在则点击按钮
                buy[1].click()
                self.logger.info("点击立即购买按钮成功")
                self.logger.info(buy[1].inner_text)
                self.assertIn("立即购买",buy[1].inner_text)
                self.assertIn("优惠后¥0",buy[1].inner_text,"优惠后非0元")
                heji = self.BaseDef.mini.page.get_element("/page/view/view[1]/view[1]/view[1]/view")
                self.logger.info("------%s",heji.inner_text)
                tjdd = self.BaseDef.get_element_selector('.tjdd')
                if tjdd:
                    tjdd.click()
                    self.native.handle_modal(btn_text="允许")
                    self.logger.info("点击提交订单按钮成功")
                else:
                    self.fail("提交订单按钮不存在")
                time.sleep(5)
                result = self.BaseDef.mini.page.get_element('.code-state-title')
                self.assertIn("购买成功",result.text)
            else:
                self.assertIn("立即购买", buy[1].text)
                self.fail("立即购买按钮未找到")        
            time.sleep(3)
        except Exception as e:
            self.fail(f"出现异常：{e}")

