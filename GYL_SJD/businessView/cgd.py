#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Cgd(Common):

    cga = (By.ID, 'com.yhbc.purchase:id/icon')                # 首页采购入口
    cgb = (By.ID, 'com.yhbc.purchase:id/indent_orderNumber')  # 卡片单号
    fh = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')   # 退出详情页面

    def cgd(self):
        logging.info('查看采购单')
        self.driver.find_elements(*self.cga)[3].click()
        c = Common(self.driver)
        c.swipeDown()
        time.sleep(3)
        c.getScreenShot("7采购单列表")
        for i in range(2):
            self.driver.find_elements(*self.cgb)[i].click()
            time.sleep(0.5)
            c.getScreenShot("8采购单"+str(i))
            self.driver.find_element(*self.fh).click()


