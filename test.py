# -*- coding: utf-8 -*-
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests方式过滤SSL不安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0I0A04&sj=2019"

cookies = ""
with requests.get(url, verify=False) as response:
    for item in response.cookies:
        cookies += item.name + "=" + item.value + "; "

print(cookies)