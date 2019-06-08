#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Sgd(Common):
    # 查看申购单

    sga = (By.ID, 'com.yhbc.purchase:id/icon')  #首页申购入口
    sgb = (By.ID, 'com.yhbc.purchase:id/canku') #点击卡片
    fh = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back') #退出详情页面
    def sgd(self):

        logging.info('查看申购单')
        self.driver.find_elements(*self.sga)[1].click()
        c = Common(self.driver)
        c.swipeDown()
        time.sleep(3)
        c.getScreenShot("5申购单列表")
        self.driver.find_elements(*self.sgb)[0].click()
        time.sleep(2)
        c.getScreenShot("6申购单详情")
        self.driver.find_element(*self.fh).click()
