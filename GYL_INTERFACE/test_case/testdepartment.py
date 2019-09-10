import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class DeparTment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "部门")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip('跳过')
    def test_department01(self):
        '''查询部门'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询部门')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_department02(self):
        '''根据部门所属组织查询部门'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据部门所属组织查询部门')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_department03(self):
        '''根据部门类型查询部门'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list,
                                                                                          '根据部门类型查询部门')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_department04(self):
        '''根据部门状态查询部门'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list,
                                                                                          '根据部门状态查询部门')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_department05(self):
        '''根据部门名称查询部门'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list,
                                                                                          '根据部门名称查询部门')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_department06(self):
        '''查询部门详情'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list,
                                                                                          '查询部门详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()