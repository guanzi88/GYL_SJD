#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Dfh(Common):

    dfha = (By.ID, 'com.yhbc.purchase:id/ll_item')      #待发货入口
    dfhb = (By.ID, 'com.yhbc.purchase:id/indent_send_receiver_dept')      #待发货详情
    dfhc = (By.ID, 'com.yhbc.purchase:id/batch_apply_tv')      #待发货详情
    dfhd = (By.ID, 'com.yhbc.purchase:id/img_title_bar_back')      #待发货详情
    dfhe = (By.ID, 'com.yhbc.purchase:id/tv_title_back_text')      #待发货详情
    dfhf = (By.ID, 'com.yhbc.purchase:id/tv_title_right_select')      #待发货详情
    dfhg = (By.ID, 'com.yhbc.purchase:id/tv_date_arr')      #待发货详情
    dfhh = (By.ID, 'com.yhbc.purchase:id/item_select_name')      #待发货详情
    dfhi = (By.ID, 'com.yhbc.purchase:id/goods_send_receiver_name')      #待发货详情
    dfhj = (By.ID, 'com.yhbc.purchase:id/tv_title_left_select')      #待发货详情
    dfhk = (By.ID, 'com.yhbc.purchase:id/batch_apply_tv')      #待发货详情
    dfhl = (By.ID, 'com.yhbc.purchase:id/send_receiver_all_cb')      #待发货详情
    dfhm = (By.ID, 'com.yhbc.purchase:id/date_tv')      #待发货详情
    dfhn = (By.ID, 'com.yhbc.purchase:id/send_receiver_confirm')      #待发货详情


    def dfh(self):
        logging.info('进入待发货')
        self.driver.find_elements(*self.dfha)[2].click()
        logging.info('进入物品维度')
        self.driver.find_element(*self.dfhf).click()
        logging.info('选择明日')
        self.driver.find_element(*self.dfhg).click()
        time.sleep(1)
        self.driver.find_elements(*self.dfhh)[1].click()
        time.sleep(1)
        c = Common(self.driver)
        c.getScreenShot("10待发货物品列表")
        self.driver.find_elements(*self.dfhi)[1].click()
        time.sleep(1)
        c.getScreenShot("10待发货物品详情")
        self.driver.find_element(*self.dfhk).click()
        self.driver.find_element(*self.dfhl).click()
        self.driver.find_element(*self.dfhn).click()
        self.driver.find_element(*self.dfhd).click()

        logging.info('进入订单维度')
        self.driver.find_element(*self.dfhj).click()
        self.driver.find_element(*self.dfhm).click()
        self.driver.find_elements(*self.dfhh)[1].click()
        time.sleep(1)
        c.getScreenShot("10待发货订单列表")
        self.driver.find_elements(*self.dfhb)[0].click()
        time.sleep(1)
        c.getScreenShot("11待发货订单详情")
        self.driver.find_element(*self.dfhc).click()
        self.driver.find_element(*self.dfhd).click()
        self.driver.find_element(*self.dfhe).click()




