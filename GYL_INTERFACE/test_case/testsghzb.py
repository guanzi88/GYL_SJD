import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class Sghzb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "部门申购汇总表")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip('跳过')
    def test_01(self):
        '''根据时间查询部门申购汇总表'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据时间查询部门申购汇总表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_02(self):
        '''根据门店查询申购部门汇总表'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据门店查询申购部门汇总表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_03(self):
        '''根据部门查询部门申购汇总表'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据部门查询部门申购汇总表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_04(self):
        '''根据物品分类查询部门申购汇总表'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据物品分类查询部门申购汇总表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def test_05(self):
        '''根据物品名称查询部门申购汇总表'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据物品名称查询部门申购汇总表')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)


    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()