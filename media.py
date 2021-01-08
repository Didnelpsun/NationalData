# -*- coding: utf-8 -*-
# 媒体数据

from nationaldata.show import show_data, Plot

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0T&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1610117974403"
    show_data(base_url, data_url, '函件数', plot_style=Plot.line)
    show_data(base_url, data_url, '报刊期发数', plot_style=Plot.line)
    show_data(base_url, data_url, '汇票业务', plot_style=Plot.line)
    show_data(base_url, data_url, '集邮业务量', plot_style=Plot.line)
