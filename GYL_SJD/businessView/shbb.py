#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Shbb(Common):

    sha = (By.ID, 'com.yhbc.purchase:id/iv_grid')      # 收货报表入口
    shb = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')
    shc = (By.ID, 'com.yhbc.purchase:id/tv_date_arr') # 查询时间
    shd = (By.ID, 'com.yhbc.purchase:id/item_select_name') # 查询本月
    she = (By.ID, 'com.yhbc.purchase:id/suppliers_select_tv') # 查询本月
    def shbb(self):
        logging.info('进入收货报表')
        self.driver.find_elements(*self.sha)[10].click()
        time.sleep(1)
        self.driver.find_element(*self.shc).click()
        self.driver.find_elements(*self.shd)[3].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("19收货物品列表")
        self.driver.find_elements(*self.she)[0].click()
        time.sleep(1)
        c.getScreenShot("20物品收货详情")
        self.driver.find_element(*self.shb).click()
        self.driver.find_element(*self.shb).click()





