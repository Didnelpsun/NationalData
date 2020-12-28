# -*- coding: utf-8 -*-
import json
import requests
from nationaldata.data_class import NationDictData, NationData, header
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests方式过滤SSL不安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 获取list格式的ajax数据
def get_bare_data(url, cookies):
    headers = header(cookies)
    # 使用了反爬虫所以必须加上完整请求头
    with requests.get(url, verify=False, headers=headers) as response:
        return json.loads(response.text)


# 规范化数据格式：
# return[dict]--code_key[string]:value[NationDictData]--name[string]
#      |--------code_key...                    |--------exp[string]
#                                              |--------unit[string]
#                                              |--------data[list]--NationData--year[string]
#                                                         |-----NationData...|--data[float]
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
        print("数据格式字典不存在对应键：{0}，".format(str(e)), end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None
    except IndexError as e:
        print("数据格式错误导致索引越界，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None
    return diction


# 根据数据字段中文名获取NationData列表，返回值None表示程序有误
def get_data_by_name(data, name):
    if data is None:
        print("get_data_by_name 函数传入参数data为空值")
        return None
    else:
        try:
            for item in data:
                if str.strip(data[item].name) == str.strip(name):
                    return data[item].data
        except TypeError as e:
            print("数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
            return None


# 打印数据
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
            print("数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
            return None


# 打印纯粹的数据
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
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
            return None


if __name__ == "__main__":
    pass
