import unittest
import sys
from BeautifulReport import BeautifulReport
import time
from send_reports.yj_fujian import send_mail

path = 'D:\\GYL_INTERFACE\\'
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports'
now = time.strftime("%Y-%m-%d")
# report_name = now + '-测试报告.html'
report_name = '供应链接口测试报告.html'

test_suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
result = BeautifulReport(test_suite)
result.report(filename=report_name, description='供应链接口自动化测试报告', log_path=report_dir)

# send_mail()