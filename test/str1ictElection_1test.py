from base.base_case import BaseCase
from base.base_def import BaseDef
import time

class strictElection_test(BaseCase):

    def setup(self) -> None:
        super().setUp()

    def __init__(self, methodName: str = "runTest") -> None:
        super(strictElection_test,self).__init__(methodName)
        self.BaseDef = BaseDef(self)

    def test_add_good(self):
        strictElection_test.empty_cart(self)
        strictElection_test.search_good(self, "测试商品222")
        strictElection_test.add_cart(self)
    
    def test_buy_good(self):
        strictElection_test.search_good(self, "测试商品222")
        strictElection_test.buy_good(self)

    def empty_cart(self):
        """
        删除购物车商品
        """
        try:
            self.BaseDef.switch_to_tabbar('/commercePages/cart/cart')
            clear = self.BaseDef.get_element_selector('.right_name')
            if clear:
                clear.click()
                delt = self.BaseDef.get_element_custom('van-button>>>button')
                self.logger.info(delt.inner_text)
                if delt.inner_text == '删除':
                    delt.click()
                    del2 = self.BaseDef.mini.page.get_element('van-overlay').get_elements('van-button')[1].get_element('button')
                    self.logger.info(del2.inner_text)
                    del2.click()
                else:
                    self.logger.info("按钮非删除状态")
            else:
                self.logger.info("无需清空购物车")
        except Exception as e:
            self.logger.error(f"发生异常：{e}")
            return
    
    def search_good(self,good_name):
        """
        根据商品名称查找商品
        """
        try:
            self.BaseDef.switch_to_tabbar("/commercePages/strictElection/strictElection")
            search_button = self.BaseDef.get_element_selector(".search",20)
            if search_button:
                search_button.click()
                time.sleep(5)
                self.native.input_text(good_name)
                self.BaseDef.get_element_xpath('/page/view[1]/view[2]').click()
            else:
                self.logger.info("商品搜索失败")
        except Exception as e:
            self.logger.error(f"发生异常：{e}")
            return

    def add_cart(self):
        """
        加购商品到购物车
        """
        try:
            good_pct = self.BaseDef.get_element_custom('hot-saleval>>>waterfall>>>waterfall-item>>>lazyload-image>>>image')
            if good_pct:
                #点击商品图片进入商品详情页
                good_pct.click()
                time.sleep(5)
                add_cart_btn = self.BaseDef.get_element_xpath('/page/view[2]/view[3]/permission-button[1]//button')
                self.logger.info(add_cart_btn)
                if add_cart_btn:
                    add_cart_btn.click()
                    det = self.BaseDef.mini.page.get_element('specifications').get_element('van-popup').get_element('permission-button')
                    det.click()
                else:
                    self.logger.info("加购按钮不存在")
                    
                self.BaseDef.switch_to_tabbar('/commercePages/cart/cart')
            else:
                self.logger.info("搜索商品结果不存在")
        except Exception as e:
            self.logger.error(f"发生异常：{e}")
            return

    def buy_good(self):
        """
        点击商品图片进入商品详情页，点击立即购买按钮，购买商品
        """
        try:
            good_pct = self.BaseDef.get_element_custom('hot-saleval>>>waterfall>>>waterfall-item>>>lazyload-image>>>image')
            if good_pct:
                good_pct.click()
                time.sleep(5)
                buy_btn = self.BaseDef.get_element_xpath('/page/view[2]/view[3]/permission-button[2]//button')
                if buy_btn:
                    buy_btn.click()
                    buy_btn_2 = self.BaseDef.mini.page.get_element('specifications').get_element('van-popup').get_element('permission-button')
                    buy_btn_2.click()
                    time.sleep(20)
                else:
                    self.logger.info('立即购买按钮不存在')
            else:
                self.logger.inf("无商品！！")
        except Exception as e:
            self.logger.error(f"出现异常：{e}")
            return