#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Dzhz(Common):
    dzhza = (By.ID, 'com.yhbc.purchase:id/iv_grid')      #保质期预警入口
    dzhzb = (By.ID, 'com.yhbc.purchase:id/number_tv')
    dzhzc = (By.ID, 'com.yhbc.purchase:id/goods_name_tv')
    dzhzd = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')
    def dzhz(self):
        logging.info('进入对账汇总')
        self.driver.find_elements(*self.dzhza)[12].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("21对账汇总列表")
        self.driver.find_element(*self.dzhzb).click()
        time.sleep(1)
        c.getScreenShot("22对账汇总明细")
        self.driver.find_element(*self.dzhzc).click()
        time.sleep(1)
        c.getScreenShot("23对账汇总明细的明细")
        self.driver.find_element(*self.dzhzd).click()
        self.driver.find_element(*self.dzhzd).click()
        self.driver.find_element(*self.dzhzd).click()





