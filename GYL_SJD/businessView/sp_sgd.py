#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Sp_Sgd(Common):

    dsp = (By.ID, 'com.yhbc.purchase:id/ll_item')             #待审批入口
    sgdxq = (By.ID, 'com.yhbc.purchase:id/un_apply_item_order_number')  #申购单详情
    quanxuan = (By.ID, 'com.yhbc.purchase:id/apply_all_select')   #全选物品
    sptg = (By.ID, 'com.yhbc.purchase:id/apply_pass')   #审批通过
    qrsp = (By.ID, 'com.yhbc.purchase:id/confirm_tv')   #确认审批通过
    fh1 = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')   #返回
    fh2 = (By.ID, 'com.yhbc.purchase:id/tv_title_back_text')   #返回

    def sp_sgd(self):
        logging.info('进入待审批')
        self.driver.find_elements(*self.dsp)[0].click()
        c = Common(self.driver)
        c.swipeDown()
        time.sleep(1)
        c.getScreenShot("3待审批申购单列表")
        self.driver.find_elements(*self.sgdxq)[0].click()
        self.driver.find_element(*self.quanxuan).click()
        self.driver.find_element(*self.sptg).click()
        self.driver.find_element(*self.qrsp).click()
        time.sleep(1)
        c.getScreenShot("4审批通过详情")
        self.driver.find_element(*self.fh1).click()
        self.driver.find_element(*self.fh2).click()



