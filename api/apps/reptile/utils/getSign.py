import copy

import requests
from reptile.utils.hash import my_md5


def getSign(body=None, key="e38174983350a531e3183a8a7eefe325"):
    if body is None:
        body = {"appid": 17919}
    body_copy = copy.deepcopy(body)
    # 将参数的value值都转成str类型
    body_str = dict([(x, str(y)) for x, y in body_copy.items()])
    # 列表生成式，生成key=value格式，将参数拼接
    strData = ["".join(i) for i in body_str.items()]
    # 以首字母进行排序
    strData.append(key)
    strData.sort()
    # 用=!=进行拼接
    strJoinData = "".join(strData)
    # 通过md5进行加密
    sign = my_md5(strJoinData)
    body["sign"] = sign
    return body


if __name__ == "__main__":
    body = getSign()
    rsp = requests.get("https://grnx.api.storeapi.net/api/94/219", params=body)
    print(rsp.json())
    res = rsp.json()["retdata"]
    medium_risk = []
    high_risk = []
    for data in res:
        area_list = data["dangerousAreas"]["subList"]
        if len(area_list) != 0:
            for area in area_list:
                if area["level"] == "中风险":
                    medium_risk.append(area["xArea"])
                elif area["level"] == "高风险":
                    high_risk.append(area["xArea"])
    print(medium_risk)
    print(high_risk)
