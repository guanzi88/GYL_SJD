import json
import logging.config

# 引用配置表

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def log_case_info(case_name, url, method, headers, data, expect_res, res):

    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    logging.info("测试用例：{0}".format(case_name))
    logging.info("url    ：{0}".format(url))
    logging.info("请求方式：{0}".format(method))
    logging.info("请求头  ：{0}".format(headers))
    logging.info("请求参数：{0}".format(data))
    logging.info("期望结果：{0}".format(expect_res))
    logging.info("实际结果：{0}".format(res.text))
    logging.info(" " * 80)


if __name__ == '__main__':

    log_case_info('case_name', 'url', 'method', 'headers', 'data', 'expect_res', 'res')