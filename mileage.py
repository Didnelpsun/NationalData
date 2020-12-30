# -*- coding: utf-8 -*-
# 里程数

from nationaldata.show import show_data_list

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G03&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609335172414"
    show_data_list(base_url, data_url, ['国家铁路营业里程', '国家铁路复线里程', '国家铁路自动闭塞里程'], title="国家铁路里程")
    show_data_list(base_url, data_url, ['公路里程', '等级公路里程'], title="国家公路里程")
    show_data_list(base_url, data_url, ['内河航道里程', '等级航道里程'], title="国家航道里程")
