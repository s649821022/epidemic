import requests
from reptile.utils.common import epidemic_url


def get_epidemic_data():
    """
    获取疫情数据和相关的疫情新闻
    """
    latest_data = {}
    resp = requests.get(epidemic_url).json()
    if resp and resp["code"] == 200:
        desc_dict = resp["newslist"][0]["desc"]
        latest_data.update(desc_dict)
        latest_data.pop("id")
        latest_data.pop("foreignStatistics")
        latest_data.pop("globalStatistics")
        latest_data.pop("createTime")
        latest_data.pop("modifyTime")
        return latest_data
    else:
        return "爬取数据失败，网络异常或接口次数已用完"


def get_epidemic_news():
    """
    获取疫情有关的新闻
    """
    latest_news = {}
    resp = requests.get(epidemic_url).json()
    if resp and resp["code"] == 200:
        latest_news["news"] = resp["newslist"][0]["news"]
        return latest_news
    else:
        return "爬取数据失败，网络异常或接口次数已用完"


def get_risk_area():
    """
    获取低中高风险地区数据
    """
    rsp = requests.get("https://diqu.gezhong.vip/api.php")
    res = rsp.json()
    area_dict = {"high_area": [], "medium_area": [], "low_area": []}
    low_risk = []
    medium_risk = []
    high_risk = []
    if res and res["msg"] == "查询成功":
        hcount = res["data"]["hcount"]
        mcount = res["data"]["mcount"]
        lcount = res["data"]["lcount"]
        for data in res["data"]["highlist"]:
            if data["communitys"]:
                for i in data["communitys"]:
                    high_risk.append({"xArea": i})
        for data in res["data"]["middlelist"]:
            if data["communitys"]:
                for i in data["communitys"]:
                    medium_risk.append({"xArea": i})
        for data in res["data"]["lowlist"]:
            if data["communitys"]:
                for i in data["communitys"]:
                    low_risk.append({"xArea": i})
    else:
        return "查询失败"
    area_dict["high_area"] = high_risk
    area_dict["medium_area"] = medium_risk
    area_dict["low_area"] = low_risk
    area_dict["hcount"] = hcount
    area_dict["mcount"] = mcount
    area_dict["lcount"] = lcount
    return area_dict


def get_latest_infected_number():
    """
    获取最近30天的感染人数
    """
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,cityStatis,provinceCompare"
    resp = requests.get(url)
    data = resp.json()
    number_data = {
        "date": [],
        "confirm": [],
        "nowConfirm": [],
        "noInfect": [],
        "dead": [],
        "heal": [],
    }
    resp = data["data"]["chinaDayList"][30:]
    for item in resp:
        number_data["date"].append(item["date"])
        number_data["confirm"].append(int(item["confirm"]))
        number_data["nowConfirm"].append(int(item["nowConfirm"]))
        number_data["noInfect"].append(int(item["noInfect"]))
        number_data["dead"].append(int(item["dead"]))
        number_data["heal"].append(int(item["heal"]))
    return number_data


if __name__ == "__main__":
    # print(get_epidemic_data())
    (get_risk_area())
    # print(get_latest_infected_number())
