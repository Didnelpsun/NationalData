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


if __name__ == "__main__":
    pass

