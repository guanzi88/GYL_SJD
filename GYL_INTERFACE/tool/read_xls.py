
import xlrd
import yaml


def excel_to_list(data_file, sheet):

    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_data(data_list, case_name):
    with open('../config/host.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    for case_data in data_list:

        if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
            url = case_data.get('url')
            url = data['host']+url  # 拼接URL
            method = case_data.get('method')
            data = case_data.get('data')
            data = data.encode("utf-8")
            # headers = case_data.get('headers')
            # headers = json.loads(headers)
            expect_res = case_data.get('expect_res')
            # 如果查询不到会返回None
            return case_name, url, method, data, expect_res


if __name__ == '__main__':

    data_list = excel_to_list("../data/test_user_data.xls", "登录")  # 读取excel，TestUserLogin工作簿的所有数据
    case_data = get_test_data(data_list, "正常登陆")  # 查找用例'test_user_login_normal'的数据
    print(case_data)