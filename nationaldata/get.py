# -*- coding: utf-8 -*-
import json
import requests
from nationaldata.data_class import NationDictData, NationData, header
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests方式过滤SSL不安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 函数说明：
# 获取Dict式的AJAX数据
# 参数列表：
# url[str]：获取数据的URL
# 返回值：
# dict[]：保存数据的字典
def get_bare_data(url):
    cookies = ""
    with requests.get("https://data.stats.gov.cn", verify=False) as response:
        for item in response.cookies:
            cookies += item.name + "=" + item.value + "; "
    headers = header(cookies)
    requests.get("https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0I0A01&sj=2019", headers=headers, verify=False)
    # 使用了反爬虫所以必须加上完整请求头
    with requests.get(url, verify=False, headers=headers) as response:
        return json.loads(response.text)


# 函数说明：
# 规范化数据格式
# 参数列表：
# url[str]：获取数据URL
# 返回值：
# None：程序错误
# dict[string:NationDictData]：保存数据的字典
# 注释说明：
# 数据格式：
# return[dict]--code_key[string]:value[NationDictData]--name[string]
#      |--------code_key...                    |--------exp[string]
#                                              |--------unit[string]
#                                              |--------data[list]--NationData--year[string]
#                                                           |           |-------data[float]
#                                                           |
#                                                           |-------NationData...
#
def get_data(url):
    data = get_bare_data(url)
    diction = {}
    try:
        wordlist = data['returndata']['wdnodes'][0]['nodes']
        for item in wordlist:
            diction[item['code']] = NationDictData(item['name'], item['exp'], item['unit'], [])
        datalist = data['returndata']['datanodes']
        for item in datalist:
            diction[item['wds'][0]['valuecode']].data += [NationData(item['wds'][1]['valuecode'], item['data']['data'])]
    except KeyError as e:
        print("get_data 函数数据格式字典不存在对应键：{0}，".format(str(e)), end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None
    except IndexError as e:
        print("get_data 函数数据格式错误导致索引越界，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None
    return diction


# 函数说明：
# 根据数据字段中文名获取NationData列表
# 参数列表：
# data[dict[string:NationDictData]]：源数据
# get_unit[bool]：是否获取单位
# get_exp[bool]：是否获取备注
# 返回值：
# None：程序有误
# list[NationData], unit, exp：对应名称的数据列表，单位，备注
def get_data_by_name(data, name, get_unit=False, get_exp=False):
    if data is None:
        print("get_data_by_name 函数传入参数data为空值")
        return None
    try:
        data_list = []
        unit = ""
        exp = ""
        for item in data:
            if str.strip(data[item].name) == str.strip(name):
                data_list = data[item].data
        if get_unit is False and get_exp is False:
            return data_list
        elif get_unit is True and get_exp is False:
            return data_list, unit
        else:
            return data_list, unit, exp
    except TypeError as e:
        print("get_data_by_name 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 根据数据字段中文名获取时间列表与数据列表
# 参数列表：
# data[dict[string:NationDictData]]：源数据
# 返回值：
# None：程序有误
# []：无对应字段
# list[year], list[num]：对应名称的时间数据列表与数字数据列表
def get_year_num_by_name(data, name):
    years = []
    nums = []
    if data is None:
        print("get_year_data_by_name 函数传入参数data为空值")
        return None
    try:
        for item in data:
            if str.strip(data[item].name) == str.strip(name):
                for i in data[item].data:
                    years.append(i.year)
                    nums.append(i.data)
        return years, nums
    except TypeError as e:
        print("get_year_data_by_name 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 获取字典里的所有名称
# 参数列表：
# data[dict[string:NationDictData]]：源数据
# 返回值：
# None：程序错误
# []：数据字段为空
# list[str]：包含名称的列表
def get_names_in_data(data):
    names = []
    if data is None:
        print("get_names_in_data 函数传入参数data为空值")
        return None
    try:
        for item in data:
            names.append(data[item].name)
        return names
    except TypeError as e:
        print("get_names_in_data 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 打印数据
# 参数列表：
# data[dict[string:NationDictData]]：源数据
# 返回值：
# None：程序错误
# 0：程序无误
def print_data(data):
    if data is None:
        print("print_data 函数传入参数data为空值")
        return None
    else:
        try:
            for item in data:
                nation_dict = data[item]
                print("项目名：{0}".format(nation_dict.name))
                if format(nation_dict.exp).strip() != "":
                    print("说明: {0}".format(nation_dict.exp))
                print("单位: {0}".format(nation_dict.unit))
                print("数据：")
                for i in nation_dict.data:
                    print("{0}：{1}".format(i.year, i.data))
                print('\n')
            return 0
        except TypeError as e:
            print("print_data 数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
            return None


# 函数说明：
# 打印纯粹的数据
# 参数列表：
# data[dict[string:NationDictData]]：源数据
# 返回值：
# None：程序错误
# 0：程序无误
# 注释说明：
# 与print_data主要差别在于数据为纯粹的一列，方便复制粘贴
def print_bare_data(data):
    if data is None:
        print("print_bare_data 函数传入参数data为空值")
    else:
        try:
            for item in data:
                nation_dict = data[item]
                print("项目名：{0}".format(nation_dict.name))
                index = 0
                print("数据：")
                for i in nation_dict.data:
                    print(i.data)
                    index += 1
                print("时间：", end='')
                if index > 1:
                    print("{0}~{1}".format(nation_dict.data[0].year, nation_dict.data[index - 1].year))
                else:
                    print(nation_dict.data[0].year)
                print('\n')
            return 0
        except TypeError as e:
            print("数据不可迭代，", end='')
            print("print_bare_data 报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"],
                                                            e.__traceback__.tb_lineno))
            return None


if __name__ == "__main__":
    pass
