# -*- coding: utf-8 -*-

# 类说明：
# 规范保存数据最外层的格式
# 字段列表：
# name[str]：数据中文说明
# exp[str]：数据备注
# unit[str]：数据对应的单位
# data[NationData]：源数据
# num[int/float]：过滤数值
class NationDictData:
    def __init__(self, name, exp, unit, data):
        self.name = name
        self.exp = exp
        self.unit = unit
        self.data = data


# 类说明：
# 规范最里面的数据格式，为时间日期键值对
# 字段列表：
# year[str]：时间日期
# data[int/float/None]：数据
class NationData:
    def __init__(self, year, data):
        self.year = year
        self.data = data


# 函数说明：
# 设置请求响应头
# 参数列表：
# cookie[str]：Cookies值
# 返回值：
# dict：响应头字典
def header(cookie, accept="application/json, text/javascript, */*; q=0.01", accept_encoding="gzip, deflate, br",
           accept_language="zh-CN,zh;q=0.9", connection="keep-alive", host="data.stats.gov.cn",
           referer="https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X",
           sec_fetch_dest="empty", sec_fetch_mode="cors", sec_fetch_site="same-origin",
           user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit" +
                      "/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
           x_requested_with="XMLHttpRequest"):
    return {
        "Accept": accept,
        "Accept-Encoding": accept_encoding,
        "Accept-Language": accept_language,
        "Connection": connection,
        "Cookie": str(cookie),
        "Host": host,
        "Referer": referer,
        "Sec-Fetch-Dest": sec_fetch_dest,
        "Sec-Fetch-Mode": sec_fetch_mode,
        "Sec-Fetch-Site": sec_fetch_site,
        "User-Agent": user_agent,
        "X-Requested-With": x_requested_with
    }
