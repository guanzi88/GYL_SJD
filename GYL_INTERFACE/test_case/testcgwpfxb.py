import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class Cgdwpfxb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "采购物品分析表")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip('跳过')
    def test_01(self):
        '''查询库存'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据时间查询采购物品分析表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_02(self):
        '''查询库存'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据物品分类查询采购物品分析表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_03(self):
        '''查询库存'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据物品名称查询采购物品分析表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_04(self):
        '''查询库存'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询采购物品分析表详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_05(self):
        '''查询库存'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据门店查询采购物品分析表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)
    def test_06(self):
        '''查询库存'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据供应商查询采购物品分析表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)


    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()