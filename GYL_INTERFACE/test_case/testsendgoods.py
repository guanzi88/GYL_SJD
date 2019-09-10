import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class SendGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "集团发货")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip('跳过')
    def test_01(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据时间查询集团待发货订单')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_02(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据门店查询集团待发货订单')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_03(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据订单号查询集团待发货的订单')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_04(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询集团待发货订单')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_05(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据时间查询集团待发货物品')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_06(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据物品查询集团待发货物品')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_07(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据物品分类查询集团待发货物品')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_09(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据申购部门查询集团待发货物品')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_10(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据发货部门查询集团待发货物品')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_11(self):
        '''根据时间查询集团待发货订单'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询集团待发货物品详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)


    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()