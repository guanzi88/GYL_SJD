import random
import requests


def getheader():

    data = '{"phone": "17856062978","password": "123456"}'
    headers = {
        "accept": "application/json, ""text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "invoke_source": "2233",
        "out_request_no": "EYRYZ5tVIB",
        "token": "null"
    }

    res = requests.request("POST", 'http://scm.blibao.com/api/v1/scm-system/common/login', data=data, headers=headers)
    token = res.json()["data"]["token"]
    rd = ''.join(random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], 10))
    headers = {
        "accept": "application/json, ""text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "invoke_source": "2233",
        "out_request_no": rd,
        "token": token
    }
    return headers
def getheadermd():

    data = '{"phone": "17856062911","password": "123456"}'
    headers = {
        "accept": "application/json, ""text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "invoke_source": "2233",
        "out_request_no": "EYRYZ5tVIB",
        "token": "null"
    }

    res = requests.request("POST", 'http://scm.blibao.com/api/v1/scm-system/common/login', data=data, headers=headers)
    token = res.json()["data"]["token"]
    rd = ''.join(random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], 10))
    headers = {
        "accept": "application/json, ""text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "invoke_source": "2233",
        "out_request_no": rd,
        "token": token
    }
    return headers


if __name__ == '__main__':

    print(getheader())
    print(getheadermd())