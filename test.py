# -*- coding: utf-8 -*-
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests方式过滤SSL不安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1609174756265&h=1"

cookies = ""
with requests.get(url, verify=False) as response:
    for item in response.cookies:
        cookies += item.name + "=" + item.value + "; "

print(cookies)