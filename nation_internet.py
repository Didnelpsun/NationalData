# -*- coding: utf-8 -*-
# 爬取地址：
# https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X
# https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0Z
# 爬取结果：中国互联网相关指数
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests方式过滤SSL不安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

default_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "_trs_uv=kj4gd4hn_6_h5ld; JSESSIONID=7iCamhpmDETtsD7gqF6uCz2TpywVXKaNqXwCgarZdmDIVSQlC-67!1550732730; u=1",
        "Host": "data.stats.gov.cn",
        "Referer": "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
}


def get_data(url, headers=default_headers):
    # 使用了反爬虫所以必须加上完整请求头
    with requests.get(url, verify=False, headers=headers) as response:
        return json.loads(response.text)


class NationDictData:
    def __init__(self, name, exp, unit, data):
        self.name = name
        self.exp = exp
        self.unit = unit
        self.data = data


class NationData:
    def __init__(self, year, data):
        self.year = year
        self.data = data


def re_data(url):
    data = get_data(url)
    diction = {}
    wordlist = data['returndata']['wdnodes'][0]['nodes']
    for item in wordlist:
        diction[item['code']] = NationDictData(item['name'], item['exp'], item['unit'], [])
    datalist = data['returndata']['datanodes']
    for item in datalist:
        diction[item['wds'][0]['valuecode']].data += [NationData(item['wds'][1]['valuecode'], item['data']['data'])]
    return diction


def show_data(data):
    for item in data:
        nation_dict = data[item]
        print("项目名：{0}：".format(nation_dict.name))
        if format(nation_dict.exp).strip() != "":
            print("说明: {0}：".format(nation_dict.exp))
        print("单位: {0}：".format(nation_dict.unit))
        print("数据：")
        for i in nation_dict.data:
            print("{0}：{1}".format(i.year, i.data))
        print('\n')


def show_bare_data(data):
    for item in data:
        nation_dict = data[item]
        print("项目名：{0}：".format(nation_dict.name))
        index = 0
        print("数据：")
        for i in nation_dict.data:
            print(i.data)
            index += 1
        print("时间：", end='')
        print("{0}~{1}".format(nation_dict.data[index-1].year, nation_dict.data[0].year))
        print('\n')


if __name__ == "__main__":
    # 网页采用Ajax获取数据，如果需要获取数据直接根据ajax连接进行请求
    # https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X
    url1 = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1608972269113&h=1"
    # https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0Z
    url2 = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1608970698012&h=1"
    result1 = re_data(url1)
    result2 = re_data(url2)
    show_data(result1)
    print('\n')
    show_bare_data(result2)
