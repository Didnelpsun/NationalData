# -*- coding: utf-8 -*-
# 爬取地址：
# https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X
# https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0Z
# 爬取结果：中国互联网相关指数
from nationaldata.get import get_bare_data, get_data, print_data, get_names_in_data
from nationaldata.process import replace_data, sort_data_order_by_year

if __name__ == "__main__":
    # 网页采用Ajax获取数据，如果需要获取数据直接根据ajax连接进行请求
    url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609170169626"
    result1 = get_data(url)
    replace_data(result1)
    # print_data(result1)
    # result4 = get_data_by_name(result1, '文化办公用品类摊位数')
    # sort_data_order_by_year(result4, 1)
    # print_data(result4)
    result4 = get_names_in_data(result1)
    for item in result4:
        print(item)

    # get_bare_data(url)
