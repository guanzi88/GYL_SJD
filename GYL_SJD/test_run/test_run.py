import unittest
from BeautifulReport import BeautifulReport
import time
import sys
path='E:\\GYL_SJD\\'
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports'
now = time.strftime("%m-%d")
report_name = now + '-测试报告.html'

test_suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_all.py')
result = BeautifulReport(test_suite)
result.report(filename=report_name, description='供应链商家端测试报告', log_path='../reports')