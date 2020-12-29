# -*- coding: utf-8 -*-
# 爬取地址：
# https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X
# https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0Z
# 爬取结果：中国互联网相关指数
from nationaldata.get import get_data, print_data, get_bare_data, get_data_by_name
from nationaldata.show import show_data, Plot
from nationaldata.process import filter_data_list

if __name__ == "__main__":
    # 网页采用Ajax获取数据，如果需要获取数据直接根据ajax连接进行请求
    # show_data(url, '网站数(万个)', plot_style=1)
    # print_data(get_data(url))
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0R03&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609243967017"
    show_data(base_url, data_url, '射击创世界纪录人数', plot_style=Plot.bar)
    # data_list = get_data_by_name(get_data(base_url, data_url), "射击创世界纪录人数")
    # filter_data_list(data_list)
    # for item in data_list:
    #     print(item.data)
    # print_data(get_data(base_url, data_url))
