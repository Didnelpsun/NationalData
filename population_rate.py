# -*- coding: utf-8 -*-
# 人口变化率

import matplotlib.pyplot as plt
from nationaldata.show import show_data_list

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0302&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609329910665"
    show_data_list(base_url, data_url, ['人口出生率', '人口死亡率', '人口自然增长率'])
    plt.show()
