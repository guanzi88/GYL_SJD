from baseView.baseView import BaseView
from common.desired_caps import appium_desired
import logging.config
from selenium.webdriver.common.by import By
import os
import time
import csv

class Common(BaseView):
    def get_screenSize(self):
        # 获取屏幕尺寸
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

        # 左滑操作
    def swipeLeft(self):
        logging.info('屏幕左滑')
        pm = self.get_screenSize()
        y1 = int(pm[1] * 0.5)
        x1 = int(pm[0] * 0.8)
        x2 = int(pm[0] * 0.2)
        self.swipe(x1, y1, x2, y1, 200)
        time.sleep(0.5)

    def swipeRight(self):
        logging.info('屏幕右滑')
        pm = self.get_screenSize()
        y1 = int(pm[1] * 0.5)
        x1 = int(pm[0] * 0.01)
        x2 = int(pm[0] * 0.8)
        self.swipe(x1, y1, x2, y1, 200)

    def swipeUp(self):
        logging.info('屏幕上划')
        pm = self.get_screenSize()
        y1 = int(pm[1] * 0.6)
        x1 = int(pm[0] * 0.5)
        y2 = int(pm[1] * 0.3)
        self.swipe(x1, y1, x1, y2, 200)

    def swipeDown(self):
        logging.info('屏幕下划')
        pm = self.get_screenSize()
        y1 = int(pm[1] * 0.2)
        x1 = int(pm[0] * 0.5)
        y2 = int(pm[1] * 0.8)
        self.swipe(x1, y1, x1, y2, 200)

    def getTime(self):
        self.now = time.strftime("%m-%d")
        return self.now

    def getScreenShot(self, module):
        # time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s.png' % (module)

        logging.info('%s 截图' % module)
        # 若生成的文件文件名相同则会覆盖
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        param csv_file: csv文件路径
        param line: 数据行数
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row



if __name__ == '__main__':
    driver = appium_desired()
    c=Common(driver)
    # c.check_updateBtn()
    # # c.check_skipBtn()
    c.swipeLeft()
    # c.swipeLef()
    c.getScreenShot("启动商家端")