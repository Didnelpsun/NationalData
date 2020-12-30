# -*- coding: utf-8 -*-
# 互联网基础数据

import matplotlib.pyplot as plt
from nationaldata.show import show_datas, show_data_list

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0Z&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609330715051"
    show_datas(base_url, data_url, ['互联网上网人数', '域名数', '网站数', '网页数', 'IPv4地址数', '互联网宽带接入端口',
                                    '互联网拨号用户', '移动互联网用户', '移动互联网接入流量'])
    show_data_list(base_url, data_url, ['互联网宽带接入用户', '城市宽带接入用户', '农村宽带接入用户'])
    plt.show()
