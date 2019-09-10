import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class Role(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "角色")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip('跳过')
    def test_role01(self):
        '''查询角色'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询角色')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_role02(self):
        '''停用角色'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '停用角色')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_role03(self):
        '''启用角色'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '启用角色')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_role04(self):
        '''保存角色权限配置'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '保存角色权限配置')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    def test_role05(self):
        '''查询角色权限'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询角色权限')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip('跳过')
    # def test_role06(self):
    #     '''编辑角色'''
    #     self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '编辑角色')
    #     self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)


    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()