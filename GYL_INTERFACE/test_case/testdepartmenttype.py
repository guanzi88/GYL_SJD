import unittest
import requests

from tool.get_header import getheader
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class DeparTmenttype(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "部门分类")  # 读取该测试类所有用例数据
        cls.headers = getheader()

    # @unittest.skip
    def test_departmenttype01(self):
        '''查询部门分类'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '查询部门分类')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)


    def test_departmenttype02(self):
        '''根据部门分类名称查询'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '根据部门分类名称查询')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()