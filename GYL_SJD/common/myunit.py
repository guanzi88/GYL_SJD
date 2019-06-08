import unittest
from common.common_fun import Common, By
from common.desired_caps import appium_desired
import logging
from send_reports import yj_fujian
import warnings
import time

class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        warnings.simplefilter('ignore',ResourceWarning)
        self.driver=appium_desired()
        c = Common(self.driver)
        for x in range(3):
            c.swipeLeft()
        time.sleep(1)
        self.driver.find_element_by_id('com.yhbc.purchase:id/tv_start_login').click()

    @classmethod
    def tearDownClass(self):
        logging.info('关闭供应链商家端')
        self.driver.close_app()
        yj_fujian.send_mail()