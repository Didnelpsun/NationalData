# -*- coding: utf-8 -*-

# 函数说明：
# 过滤所有数据
# 参数列表：
# data[dict[string:NationDictData]]：源数据
# num[int/float]：过滤数值
# mode[str]：过滤模式，g表示大于，l表示小于，e表示等于，ge表示大于等于，le表示小于等于
# 返回值：
# None：程序有误
# 0：程序无误
# 注释说明：
# 默认获得大于0数据，在源数据上过滤
def filter_data_dict(data, num=0, mode="g"):
    if data is None:
        print("filter_data_dict 函数传入参数data为空值")
        return None
    if type(num) != int and type(num) != float:
        print("filter_data_dict 函数输入的过滤条件 {0} 类型为{1}不为数字".format(num, type(num)))
        return None
    if len(mode) == 2 and mode[1] != "e":
        print("filter_data_dict 函数输入的过滤模式 {0} 错误".format(mode))
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
        print("filter_data 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 过滤数据列表
# 参数列表：
# data[list[NationData]]：源数据
# num[int/float]：过滤数值
# mode[str]：过滤模式，g表示大于，l表示小于，e表示等于，ge表示大于等于，le表示小于等于
# 返回值：
# None：程序有误
# 0：程序无误
# 注释说明：
# 默认获得大于0数据，在源数据上过滤
def filter_data_list(data, num=0, mode="g"):
    if data is None:
        print("filter_data_list 函数传入参数data为空值")
        return None
    if type(num) != int and type(num) != float:
        print("filter_data_list 函数输入的过滤条件 {0} 类型为{1}不为数字".format(num, type(num)))
        return None
    if len(mode) == 2 and mode[1] != "e":
        print("filter_data_list 函数输入的过滤模式 {0} 错误".format(mode))
        return None
    try:
        for i in range(len(data) - 1, -1, -1):
            data_value = data[i].data
            if mode[0] == "g":
                if len(mode) == 2:
                    if data_value < num:
                        del data[i]
                else:
                    if data_value <= num:
                        del data[i]
            elif mode[0] == "l":
                if len(mode) == 2:
                    if data_value > num:
                        del data[i]
                else:
                    if data_value >= num:
                        del data[i]
            elif mode[0] == "e":
                if data_value != num:
                    del data[i]
            else:
                print("filter_data_list 函数输入的过滤模式 {0} 错误".format(mode))
                return None
        return 0
    except TypeError as e:
        print("filter_data_list 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 替换数据
# 参数列表：
# data[list[NationData]]：源数据
# source[int/float/None]：修改源值
# target[int/float/None]：修改目标值
# 返回值：
# None：程序错误
# 0：程序无误
# 注释说明：
# 默认将数据0替换为None，在源数据上替换
def replace_data(data, source=0, target=None):
    if type(source) != int and type(source) != float and source is not None:
        print("replace_data 函数输入的替换源 {0} 类型为{1}不为数字".format(source, type(source)))
        return None
    if type(target) != int and type(target) != float and target is not None:
        print("replace_data 函数输入的替换目标 {0} 类型为{1}不为数字".format(target, type(target)))
        return None
    try:
        for item in data:
            data_item = data[item].data
            for i in range(len(data_item) - 1, -1, -1):
                data_value = data_item[i].data
                if data_value == source:
                    data_item[i].data = target
        return 0
    except TypeError as e:
        print("replace_data 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 根据年份检查NationData列表数据顺序
# 参数列表：
# data[list[NationData]]：源数据
# 返回值：
# None：错误
# -1：倒序
# 1：正序
# 0：乱序
# 2：无序（无法判断，列表元素少于2个或全部相等）
def check_data_order_by_year(data):
    if data is None:
        print("check_data_order_by_year 函数传入参数data为空值")
        return None
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
        print("check_data_order_by_year 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


# 函数说明：
# 根据年份对NationData列表数据排序
# 参数列表：
# data[list[NationData]]：源数据
# mode[int]：排序方式，-1倒序，1正序
# 返回值：
# None：程序出错
# 0：程序正确
# 注释说明：
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
            print("sort_data_order_by_year 函数数据不可迭代，", end='')
            print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
            return None


# 函数说明：
# 将处理过的list列表拆分为year和num两个部分
# 参数列表：
# data[list[NationData]]：源数据
# 返回值：
# None：程序有误
# []：无数据
# list[year], list[num]：对应名称的时间数据列表与数字数据列表
def split_year_num_by_list(data):
    years = []
    nums = []
    if data is None:
        print("split_year_num_by_list 函数传入参数data为空值")
        return None
    try:
        for item in data:
            years.append(item.year)
            nums.append(item.data)
        return years, nums
    except TypeError as e:
        print("split_year_num_by_list 函数数据不可迭代，", end='')
        print("报错位置在文件{0}的第{1}行".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno))
        return None


if __name__ == "__main__":
    pass
