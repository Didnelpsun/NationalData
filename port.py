
from nationaldata.show import show_data

if __name__ == "__main__":
    base_url = " https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0G0U&sj=2020"
    data_url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1625042754510"
    show_data(base_url, data_url, '快递量')
    show_data(base_url, data_url, '快递业务收入')
    