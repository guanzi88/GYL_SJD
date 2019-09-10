import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class TestStores(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "店铺")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip
    def test_stores01(self):
        '''查询店铺'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询店铺')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_stores02(self):
        '''根据区域查询店铺'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据区域查询店铺')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_stores03(self):
        '''根据门店名称查询门店'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据门店名称查询门店')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_stores04(self):
        '''查看店铺详情'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查看店铺详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()