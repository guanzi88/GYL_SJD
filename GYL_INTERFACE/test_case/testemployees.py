import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class Employees(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "员工")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip('跳过')
    def test_employees01(self):
        '''查询员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询员工')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees02(self):
        '''根据员工工号查询员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据员工工号查询员工')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees03(self):
        '''根据员工所属角色查询员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据员工所属角色查询员工')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees04(self):
        '''根据员工所属门店查询员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据员工所属门店查询员工')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees05(self):
        '''根据员工状态查询员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据员工状态查询员工')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees06(self):
        '''查看员工详情'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查看员工详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees07(self):
        '''停用员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查看员工详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_employees08(self):
        '''启用员工'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查看员工详情')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)


    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()