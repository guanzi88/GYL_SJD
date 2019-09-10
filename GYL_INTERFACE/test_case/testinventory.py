import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class Inventory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "盘点类型")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip
    def test_01(self):
        '''查询盘点类型'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询盘点类型')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_02(self):
        '''查询盘点类型详情'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询盘点类型详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_03(self):
        '''查询停用状态的盘点类型'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询停用状态的盘点类型')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_04(self):
        '''查询启用状态的盘点类型'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询启用状态的盘点类型')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()