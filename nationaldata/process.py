# -*- coding: utf-8 -*-

# 过滤数据，默认获得大于0数据
# num表示过滤数值，mode表示过滤模式，g表示大于，l表示小于，e表示等于，ge表示大于等于，le表示小于等于，返回值为None表示程序有误，0表示无误
def filter_data(data, num=0, mode="g"):
    if len(mode) == 2 and mode[1] != "e":
        print("filter_data 函数输入的过滤模式 {0} 错误".format(mode))
        return None
    if type(num) != int and type(num) != float:
        print("filter_data 函数输入的过滤条件 {0} 类型为{1}不为数字".format(num, type(num)))
        return None
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
                    return None
        return 0
    except TypeError as e:
        print("数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 根据年份检查NationData列表数据顺序，返回值-1倒序，1正序，0乱序，2无序（无法判断，情况有列表元素少于2个，全部相等），None错误
def check_data_order_by_year(data):
    if data is None:
        print("check_data_order_by_year 函数传入参数data为空值")
    else:
        try:
            length = len(data)
            if length <= 1:
                return 2
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
                    order = 2
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
            return None


# 根据年份对NationData列表数据排序，mode为排序方式，-1倒序，1正序
# 当data顺序与目标一致或者data无序则直接返回0，如果正好相反则反转，如果乱序则一个个调整
def sort_data_order_by_year(data, mode=-1):
    if mode != 1 and mode != -1:
        print("sort_data_order_by_year 函数输入的排序模式 {0} 错误".format(mode))
        return None
    if data is None:
        print("sort_data_order_by_year 函数传入参数data为空值")
        return None
    else:
        list_mode = check_data_order_by_year(data)
        try:
            if list_mode == mode or list_mode == 2:
                return 0
            elif list_mode == mode * -1:
                data.reverse()
                return 0
            else:
                if mode == -1:
                    data.sort(key=lambda x: x['year'], reversed=True)
                elif mode == 1:
                    data.sort(key=lambda x: x['year'])
        except TypeError as e:
            print("数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
            return None


if __name__ == "__main__":
    pass
