# -*- coding: utf-8 -*-

# 过滤数据，默认获得大于0数据
# num表示过滤数值，mode表示过滤模式，g表示大于，l表示小于，e表示等于，ge表示大于等于，le表示小于等于
def filter_data(data, num=0, mode="g"):
    if len(mode) == 2 and mode[1] != "e":
        print("filter_data 函数输入的过滤模式 {0} 错误".format(mode))
        return
    if not (type(num) == int or type(num) == float):
        print("filter_data 函数输入的过滤条件 {0} 类型为{1}不为数字".format(num, type(num)))
        return
    try:
        for item in data:
            data_item = data[item].data
            for i in range(len(data_item) - 1, -1, -1):
                data_value = data_item[i].data
                if mode[0] == "g":
                    if len(mode) == 2:
                        if data_value < num:
                            del data_item[i]
                    else:
                        if data_value <= num:
                            del data_item[i]
                elif mode[0] == "l":
                    if len(mode) == 2:
                        if data_value > num:
                            del data_item[i]
                    else:
                        if data_value >= num:
                            del data_item[i]
                elif mode[0] == "e":
                    if data_value != num:
                        del data_item[i]
                else:
                    print("filter_data 函数输入的过滤模式 {0} 错误".format(mode))
                    return
    except TypeError as e:
        print("数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))


# 根据年份检查NationData列表数据顺序，返回值-1倒序，1正序，0乱序，None无序（无法判断，情况有列表元素少于2个，全部相等）
def check_data_order_by_year(data):
    if data is None:
        print("check_data_order_by_year 函数传入参数data为空值")
    else:
        try:
            length = len(data)
            if length <= 1:
                return None
            else:
                if int(data[0].year) > int(data[1].year):
                    for i in range(0, length - 2):
                        if int(data[i].year) < int(data[i + 1].year):
                            return 0
                    return -1
                elif int(data[0].year) < int(data[1].year):
                    for i in range(0, length - 2):
                        if int(data[i].year) > int(data[i + 1].year):
                            return 0
                    return 1
                else:
                    order = None
                    for i in range(0, length - 2):
                        if int(data[i].year) > int(data[i + 1].year):
                            if order == 1:
                                order = 0
                                break
                            elif order is None:
                                order = -1
                        elif int(data[i].year) < int(data[i + 1].year):
                            if order == -1:
                                order = 0
                                break
                            elif order is None:
                                order = 1
                    return order
        except TypeError as e:
            print("数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))


# 根据年份对NationData列表数据排序，mode为排序方式，-1倒序，1正序
def sort_data_order_by_year(data, mode):
    if data is None:
        print("sort_data_order_by_year 函数传入参数data为空值")
    else:
        try:
        except TypeError as e:
            print("数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))


if __name__ == "__main__":
    pass
