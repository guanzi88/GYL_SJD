# coding=utf-8
from appium import webdriver
import logging
import logging.config
import yaml
import os
import time

# 引用配置表
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
def appium_desired():
    # 读取yaml配置文件
    with open('../config/desired_caps.yaml', 'r',encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    # 创建appium会话，告诉appium你自动化的一些配置
    desired_caps={}
    # 指定手机操作系统
    desired_caps['platformName']=data['platformName']

    # 获取安装包存放地址
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    # 指定安装包地址
    desired_caps['app']=app_path
    # 指定包名
    desired_caps['appPackage']=data['appPackage']
    # 指定安装包首个活动页
    desired_caps['appActivity']=data['appActivity']

    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    # 模拟器设备

    desired_caps['platformVersion'] = data['platformVersion']  # 指定手机系统版本
    desired_caps['deviceName'] = data['deviceName']  # 指定手机型号或模拟器地址

    # meizu 15 plus 真机
    # desired_caps['platformVersion'] = data['platformVersion']
    # desired_caps['deviceName'] = data['deviceName']
    # desired_caps['udid'] = data['udid']

    logging.info('开始启动商家端')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    logging.info('商家端启动完成')
    logging.info('等待中')
    time.sleep(6)
    driver.implicitly_wait(2)
    return driver
if __name__ == '__main__':
    appium_desired()