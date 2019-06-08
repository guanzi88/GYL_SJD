#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Kcyj(Common):

    kca = (By.ID, 'com.yhbc.purchase:id/iv_grid')      #库存查询入口
    kcc = (By.ID, 'com.yhbc.purchase:id/tv_title_back_text')
    def kcyj(self):
        logging.info('进入库存预警')
        self.driver.find_elements(*self.kca)[9].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("18库存预警列表")
        self.driver.find_element(*self.kcc).click()





