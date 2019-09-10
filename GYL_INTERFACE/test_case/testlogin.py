import unittest
import requests
from tool.print_log import log_case_info
from tool.read_xls import excel_to_list, get_test_data


class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data_list = excel_to_list("../data/test_user_data.xls", "登录")  # 读取该测试类所有用例数据
        cls.headers = {
            "accept": "application/json, "
            "text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "invoke_source": "2233",
            "out_request_no": "EYRYZ5tVIB",
            "token": "null"
            }

    # @unittest.skip
    def test_normal(self):
        '''正常登陆'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '正常登陆')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip
    def test_normal01(self):
        '''密码错误'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '密码错误')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    # @unittest.skip
    def test_normal02(self):
        '''用户名不存在'''
        self.case_name, self.url, self.method, self.data, self.expect_res = get_test_data(self.data_list, '用户名不存在')
        self.res = requests.request(self.method, self.url, data=self.data, headers=self.headers)

    def tearDown(self):

        self.assertIn(self.expect_res, self.res.text)
        log_case_info(self.case_name, self.url, self.method, self.headers, self.data, self.expect_res, self.res)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()