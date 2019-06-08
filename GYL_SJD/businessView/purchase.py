#coding:utf-8
import logging
import time
from common.common_fun import Common,By

class Purchase(Common):
    # 创建申购单

    sg = (By.ID, 'com.yhbc.purchase:id/iv_grid')                  # 点击申购按钮

    sgbm = (By.ID, 'com.yhbc.purchase:id/department_select_tv')   # 申购部门
    xzbm = (By.ID, 'com.yhbc.purchase:id/item_select_name')       # 选择部门

    sgrq = (By.ID, 'com.yhbc.purchase:id/select_data_tv')         # 申购日期
    xzrq = (By.ID, 'com.yhbc.purchase:id/btnSubmit')             # 选择日期

    sgwp = (By.ID, 'com.yhbc.purchase:id/good_title')             # 申购物品
    xzfl = (By.CLASS_NAME, 'android.widget.TextView')             # 选择分类
    xzwp = (By.ID, 'com.yhbc.purchase:id/choose_goods_right_add')      # 选择物品
    qdwp = (By.ID, 'com.yhbc.purchase:id/choose_goods_bottom_confirm')    # 确认物品
    sgbz = (By.ID, 'com.yhbc.purchase:id/et_remark')              # 申购备注
    sgtj = (By.ID, 'com.yhbc.purchase:id/confirm_tv')             # 提交申购单
    qrwp = (By.ID, 'com.yhbc.purchase:id/label_keybord_btn_confim')             # 确认物品

    def purchase(self):
        bz = '我是申购备注'
        logging.info('创建申购单')
        self.driver.find_elements(*self.sg)[0].click()
        self.driver.find_element(*self.sgbm).click()
        self.driver.find_elements(*self.xzbm)[0].click()
        #选择申购日期
        #self.driver.find_element(*self.sgrq).click()
        #self.driver.find_element(*self.xzrq).click()
        self.driver.find_element(*self.sgwp).click()
        self.driver.find_elements(*self.xzfl)[0].click()
        #for i in range(9):
        for i in [0,1,2,6,7,10,12]:
            self.driver.find_elements(*self.xzwp)[i].click()
            self.driver.find_element(*self.qrwp).click()
        self.driver.find_element(*self.qdwp).click()
        self.driver.find_element(*self.sgbz).send_keys(bz)
        c = Common(self.driver)
        c.getScreenShot("2创建申购单")
        self.driver.find_element(*self.sgtj).click()


