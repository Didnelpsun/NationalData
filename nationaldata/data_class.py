# -*- coding: utf-8 -*-
# 定义类来规范保存数据
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


def header(cookie, accept="application/json, text/javascript, */*; q=0.01", accept_encoding="gzip, deflate, br", accept_language="zh-CN,zh;q=0.9"):
    return {
        "Accept": accept,
        "Accept-Encoding": accept_encoding,
        "Accept-Language": accept_language,
        "Connection": "keep-alive",
        "Cookie": str(cookie),
        "Host": "data.stats.gov.cn",
        "Referer": "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
