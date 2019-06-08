#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Pd(Common):

    pda = (By.ID, 'com.yhbc.purchase:id/iv_grid')      #盘点入口
    pdb = (By.ID, 'com.yhbc.purchase:id/check_type_start')     #开始盘点
    pdc = (By.ID, 'com.yhbc.purchase:id/commit_tv')     #点击盘点
    pdd = (By.ID, 'com.yhbc.purchase:id/confirm_tv')     #确认盘点
    pde = (By.ID, 'com.yhbc.purchase:id/check_tv')     #继续盘点
    pdf = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')     #继续盘点

    def pd(self):
        logging.info('进入盘点')
        self.driver.find_elements(*self.pda)[6].click()
        self.driver.find_elements(*self.pdb)[0].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("14盘点详情")
        self.driver.find_element(*self.pdc).click()
        self.driver.find_element(*self.pdd).click()
        self.driver.find_element(*self.pde).click()
        self.driver.find_element(*self.pdf).click()




