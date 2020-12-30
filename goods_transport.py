# -*- coding: utf-8 -*-
# 各铁路线货运量

from nationaldata.show import show_data_list

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0E03&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609341509725"
    line = ["京哈线货运量", "京广线货运量", "京沪线货运量", "京九线货运量", "京包线货运量", "滨洲线货运量", "滨绥线货运量", "大秦线货运量",
            "石太线货运量", "石德线货运量", "北同蒲线货运量", "南同蒲线货运量", "包兰线货运量", "新石线货运量", "太焦线货运量",
            "焦柳线货运量", "胶济线货运量", "陇海线货运量", "沪昆线货运量", "宝成线货运量", "南昆线货运量", "成昆线货运量", "兰新线货运量",
            "青藏线货运量"]
    show_data_list(base_url, data_url, line, is_filter=False, is_replace=True, is_figure=False, title="铁路主干线货运量")
