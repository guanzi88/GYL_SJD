import logging
import time
from businessView.loginView import LoginView
from common.desired_caps import appium_desired
from common.common_fun import Common,By

class LogOut(Common):
    # 个人中心界面元素
    grzxBtn = (By.ID, 'com.yhbc.purchase:id/home_center_tv')
    logoutBtn = (By.ID, 'com.yhbc.purchase:id/log_out_bt')
    qcsjh = (By.ID, 'com.yhbc.purchase:id/phone_clear')

    def logout(self):
        C = Common(self.driver)
        C.swipeRight()
        time.sleep(0.5)
        C = Common(self.driver)
        C.getScreenShot("9个人中心")
        logging.info('退出商家端')
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.qcsjh).click()

if __name__ == '__main__':
    driver = appium_desired()
    c = Common(driver)
    c.swipeLeft()
    c.swipeLeft()
    c.swipeLeft()
    c.swipeLeft()
    L = LoginView(driver)
    csv_file = '../data/account.csv'
    data=c.get_csv_data(csv_file,1)
    L.loginview(data[0], data[1])