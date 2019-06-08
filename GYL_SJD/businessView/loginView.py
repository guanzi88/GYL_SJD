import logging
import time
from common.desired_caps import appium_desired
from common.common_fun import Common, By
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):
    # 登录界面元素

    username_type = (By.ID, 'com.yhbc.purchase:id/login_phone_et')
    password_type = (By.ID, 'com.yhbc.purchase:id/login_password_et')
    loginBtn = (By.ID, 'com.yhbc.purchase:id/login_btn')
    qxgx = (By.ID, 'com.yhbc.purchase:id/cancel_tv')

    def loginview(self, username, password):

        self.driver.find_element(*self.username_type).send_keys(username)
        self.driver.find_element(*self.password_type).send_keys(password)
        time.sleep(0.5)
        c = Common(self.driver)
        c.getScreenShot("0登录页")
        self.driver.find_element(*self.loginBtn).click()
        logging.info('登录商家端')
        time.sleep(5)
        c.getScreenShot("1首页")
        # 检查是否更新，如检测到更新那么就取消更新
        try:
            cancelBtn = self.driver.find_element(*self.qxgx)  # 取消更新
        except NoSuchElementException:
            logging.info("未检测到更新")
        else:
            cancelBtn.click()
            logging.info("取消更新")

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