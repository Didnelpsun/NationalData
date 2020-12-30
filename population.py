# -*- coding: utf-8 -*-
# 人口数据

import matplotlib.pyplot as plt
from nationaldata.get import get_data, get_year_num_by_name
from nationaldata.process import float_list_sub
from nationaldata.show import show_data, show_data_list, Plot

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0301&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609320175967"
    data = get_data(base_url, data_url)
    show_data(base_url, data_url, '年末总人口', plot_style=Plot.line)
    show_data_list(base_url, data_url, ['男性人口', '女性人口'], title="男女人口")
    man_x, man_y = get_year_num_by_name(data, "男性人口")
    woman_x, woman_y = get_year_num_by_name(data, "女性人口")
    plt.plot(man_x, float_list_sub(man_y, woman_y))
    plt.title('男女人数差值')
    plt.ylabel("万人")
    plt.show()
    show_data_list(base_url, data_url, ['城镇人口', '乡村人口'], title="城镇与乡村人口")
    plt.show()
