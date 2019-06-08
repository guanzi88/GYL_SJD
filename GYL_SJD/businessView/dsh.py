#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Dsh(Common):

    dsha = (By.ID, 'com.yhbc.purchase:id/ll_item')      #待收货入口
    dshb = (By.ID, 'com.yhbc.purchase:id/receiver_tv')  #收货
    dshc = (By.ID, 'com.yhbc.purchase:id/confirm_receiver_tv')  #确认收货
    dshd = (By.ID, 'com.yhbc.purchase:id/tv_title_back_text')  #确认收货


    def dsh(self):
        logging.info('进入待收货')
        self.driver.find_elements(*self.dsha)[3].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("12待收货按部门详情")
        self.driver.find_element(*self.dshb).click()
        c.getScreenShot("13确认收货弹窗")
        self.driver.find_element(*self.dshc).click()
        self.driver.find_element(*self.dshd).click()
        time.sleep(2)




