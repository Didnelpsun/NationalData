# -*- coding: utf-8 -*-
# 互联网率数据

from nationaldata.show import show_datas, show_data_list

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0X&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609331743014"
    show_data_list(base_url, data_url, ['电话普及率(包括移动电话)', '移动电话普及率'])
    show_datas(base_url, data_url, ['每千人拥有公用电话数', '开通互联网宽带业务的行政村比重', '互联网普及率'])
