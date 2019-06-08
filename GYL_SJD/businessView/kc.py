#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Kc(Common):

    kca = (By.ID, 'com.yhbc.purchase:id/iv_grid')      #库存查询入口
    kcb = (By.ID, 'com.yhbc.purchase:id/stash_total_price')     #物品库存列表
    kcc = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')     #物品库存详情

    def kc(self):
        logging.info('进入库存查询')
        self.driver.find_elements(*self.kca)[7].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("15物品库存列表")
        self.driver.find_elements(*self.kcb)[0].click()
        time.sleep(1)
        c.getScreenShot("16物品库存详情")
        self.driver.find_element(*self.kcc).click()
        self.driver.find_element(*self.kcc).click()





