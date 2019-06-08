#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Bzqyj(Common):

    kca = (By.ID, 'com.yhbc.purchase:id/iv_grid')      #保质期预警入口
    kcc = (By.ID, 'com.yhbc.purchase:id/tv_title_back_text')
    def bzqyj(self):
        logging.info('进入保质期浴巾')
        self.driver.find_elements(*self.kca)[8].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("17保质期预警列表")
        self.driver.find_element(*self.kcc).click()





