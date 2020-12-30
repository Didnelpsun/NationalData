# -*- coding: utf-8 -*-
# 化妆品相关数据

from nationaldata.show import show_data, show_data_list

if __name__ == "__main__":
    shop_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0I0A01&sj=2019"
    shop_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609344918538"
    show_data(shop_base_url, shop_data_url, '化妆品类摊位数')
    trade_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0I0A02&sj=2019"
    trade_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609345025305"
    show_data(trade_base_url, trade_data_url, "化妆品类成交额")
    wholesale_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0I0A03&sj=2019"
    wholesale_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609345122413"
    show_data(wholesale_base_url, wholesale_data_url, "化妆品类批发市场成交额")
    retail_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0I0A04&sj=2019"
    retail_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609345738445"
    show_data(retail_base_url, retail_data_url, '化妆品类零售市场成交额')
    retail_price_index_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0906&sj=2019"
    retail_price_index_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609345521976"
    show_data(retail_price_index_base_url, retail_price_index_data_url, "化妆品类商品零售价格指数(上年=100)")
    urban_retail_price_index_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0907&sj=2019"
    urban_retail_price_index_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609346149084"
    show_data(urban_retail_price_index_base_url, urban_retail_price_index_data_url, '化妆品类城市商品零售价格指数(上年=100)')
    rural_retail_price_index_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0908&sj=2019"
    rural_retail_price_index_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609346264490"
    show_data(rural_retail_price_index_base_url, rural_retail_price_index_data_url, '化妆品类农村商品零售价格指数(上年=100)')
    trade_index_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A090305&sj=2019"
    trade_index_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609346500523"
    show_data_list(trade_index_base_url, trade_index_data_url, ["化妆美容用品类居民消费价格指数(上年=100)", "清洁化妆用品类居民消费价格指数(上年=100)"],
                   title="化妆用品类居民消费价格指数")
    urban_trade_index_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A090405&sj=2019"
    urban_trade_index_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609346684585"
    show_data_list(urban_trade_index_base_url, urban_trade_index_data_url, ["化妆美容用品类城市居民消费价格指数(上年=100)",
                                                                            "清洁化妆用品类城市居民消费价格指数(上年=100)"],
                   title="化妆用品类城市居民消费价格指数")
    rural_trade_index_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A090505&sj=2019"
    rural_trade_index_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609346909511"
    show_data_list(rural_trade_index_base_url, rural_trade_index_data_url, ["化妆美容用品类农村居民消费价格指数(上年=100)",
                                                                            "清洁化妆用品类农村居民消费价格指数(上年=100)"],
                   title="化妆用品类农村居民消费价格指数")
    in_base_url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0N1B&sj=2019"
    in_data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1609346992473"
    show_data_list(in_base_url, in_data_url, ["出入境食品及化妆品检验检疫批次", "出入境食品及化妆品检验检疫不合格批次"],
                   title="出入境食品及化妆品检验检疫批次")
    show_data_list(in_base_url, in_data_url, ["出入境食品及化妆品检验检疫货值", "出入境食品及化妆品检验检疫不合格货值"],
                   title="出入境食品及化妆品检验检疫货值")
