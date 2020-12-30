# -*- coding: utf-8 -*-
# 航空相关数据

from nationaldata.show import show_data_list

if __name__ == "__main__":
    base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0R&sj=2019"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609342955511"
    show_data_list(base_url, data_url, ['民用航空航线数', '民用航空国际航线数', '民用航空国内航线数', '民用航空港、澳地区航线数'],
                   title="航空航线数")
    show_data_list(base_url, data_url, ['定期航班航线里程', '国际航线线路长度', '民用航空国内航线航线里程', '民用航空港、澳地区航线里程'],
                   title="国家铁路里程")
    show_data_list(base_url, data_url, ['民用飞机架数', '民用运输飞机架数', '民用大中型运输飞机架数'], title="国家公路里程")
    show_data_list(base_url, data_url, ['民用大中型波音747运输飞机架数', '民用大中型波音737运输飞机架数', '民用大中型波音757运输飞机架数',
                                        '民用大中型波音767运输飞机架数'], title="国家公路里程")
    show_data_list(base_url, data_url, ['民用大中型MD90运输飞机架数', '民用大中型MD82运输飞机架数', '民用大中型A320运输飞机架数'],
                   title="国家公路里程")
    show_data_list(base_url, data_url, ['民用小型运输飞机架数', '民用小型ARJ21-700运输飞机架数', '民用通用飞机架数',
                                        '民用教学校验飞机架数'], title="国家公路里程")
