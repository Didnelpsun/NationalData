# -*- coding: utf-8 -*-
# 图形化展示数据

from enum import Enum
import matplotlib.pyplot as plt
from nationaldata.get import get_data, get_data_by_name, get_year_num_by_name
from nationaldata.process import filter_data_list, sort_data_order_by_year, split_year_num_by_list, filter_data_dict, \
    replace_data


# 类说明：
# 定义绘制数据的可选形式
# 字段列表：
# marker[1]：点
# line[2]：线
# bar[3]：条柱
class Plot(Enum):
    marker = 1
    line = 2
    bar = 3


# 函数说明：
# 对于某个数据字段绘图
# 参数列表：
# base_url[str]：查询数据的URL
# data_url[str]：获取数据的URL
# title[str]：选取数据的中文字段
# is_filter[bool]：是否对数据进行过滤
# filter_num[int/float]：过滤数值
# filter_mode[g/l/e/ge/le]：过滤模式
# is_sort_by_year[bool]：是否根据时间排序
# sort_by_year_mode[-1/1]：排序模式
# show_title[bool]：是否显示标题
# color[str]：绘图颜色
# plot_style[enum[Plot]]：绘图模式
# marker[str]：点样式
# line_style[str]：线样式
# xlabel_show[bool]：是否显示X轴说明
# xlabel[str]：X轴说明
# ylabel_show[bool]：是否显示Y轴说明
# ylabel[str]：Y轴说明
# 返回值：
# None：程序有误
# 0：程序无误
def show_data(base_url, data_url, title, is_filter=True, filter_num=0, filter_mode="g", is_replace=False,
              replace_source=0, replace_target=None, is_sort_by_year=True, sort_by_year_mode=1,
              show_title=True, color="r", plot_style=Plot.line, marker="+", line_style="-",
              xlabel_show=True, xlabel="年份", ylabel_show=True, ylabel=None):
    data = get_data(base_url, data_url)
    if data is None:
        print("show_data 函数获取数据失败")
        return None
    data_list, unit = get_data_by_name(data, title, get_unit=True)
    if is_filter:
        if type(filter_num) != int and type(filter_num) != float:
            print("show_data 函数输入的过滤条件 {0} 类型为{1}不为数字".format(filter_num, type(filter_num)))
            return None
        if len(filter_mode) == 2 and filter_mode[1] != "e":
            print("show_data 函数输入的过滤模式 {0} 错误".format(filter_mode))
            return None
        filter_data_list(data_list, filter_num, filter_mode)
    if not data_list:
        print("show_data 函数获取不到名为 {0} 的字段数据".format(title))
        return None
    if is_replace:
        replace_data(data_list, source=replace_source, target=replace_target)
    if is_sort_by_year:
        if sort_by_year_mode != 1 and sort_by_year_mode != -1:
            print("show_data 函数输入的排序模式 {0} 错误".format(sort_by_year_mode))
            return None
        if data is None:
            print("show_data 函数获取的数据列表为空值")
            return None
        sort_data_order_by_year(data_list, sort_by_year_mode)
    x, y = split_year_num_by_list(data_list)
    plt.figure()
    if show_title:
        plt.title(title)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    if xlabel_show:
        plt.xlabel(xlabel)
    if ylabel_show:
        if ylabel is None:
            plt.ylabel(unit)
        else:
            plt.ylabel(ylabel)
    if plot_style == Plot.marker or plot_style == 1:
        plt.scatter(x, y, color=color, marker=marker)
    elif plot_style == Plot.line or plot_style == 2:
        plt.plot(x, y, color=color, linestyle=line_style)
    elif plot_style == Plot.bar or plot_style == 3:
        plt.bar(x, y, color=color)
    else:
        print("show_data 函数画图模式传入参数 {0} 不存在该值，将默认绘制".format(plot_style))
        plt.scatter(x, y, color=color, marker=marker)
    plt.show()
    return 0


# 函数说明：
# 对于某个数据字段绘图，并循环绘制多个
# 参数列表：
# base_url[str]：查询数据的URL
# data_url[str]：获取数据的URL
# title_list[list[str=]：选取数据的中文字段列表
# plot_style[enum[Plot]]：绘图模式
# 返回值：
# None：程序有误
# 0：程序无误
def show_datas(base_url, data_url, title_list, plot_style=Plot.line):
    for title in title_list:
        show_data(base_url, data_url, title, plot_style=plot_style)
    return 0


# 函数说明：
# 对于某些数据字段绘图，并合并为一张图
# 参数列表：
# base_url[str]：查询数据的URL
# data_url[str]：获取数据的URL
# title_list[list[str=]：选取数据的中文字段列表
# title[str]：图像标题
# is_filter[bool]：是否对数据进行过滤
# filter_num[int/float]：过滤数值
# filter_mode[g/l/e/ge/le]：过滤模式
# is_sort_by_year[bool]：是否根据时间排序
# sort_by_year_mode[-1/1]：排序模式
# show_title[bool]：是否显示标题
# color[str]：绘图颜色
# plot_style[enum[Plot]]：绘图模式
# marker[str]：点样式
# line_style[str]：线样式
# xlabel_show[bool]：是否显示X轴说明
# xlabel[str]：X轴说明
# ylabel_show[bool]：是否显示Y轴说明
# ylabel[str]：Y轴说明
# 返回值：
# None：程序有误
# 0：程序无误
def show_data_list(base_url, data_url, title_list, title=None, is_filter=True, filter_num=0, filter_mode="g",
                   is_replace=False, replace_source=0, replace_target=None,
                   is_sort_by_year=True, sort_by_year_mode=1, plot_style=Plot.line, marker="+", line_style="-",
                   xlabel_show=True, xlabel="年份", ylabel_show=True, ylabel=None, is_figure=True, loc="upper left"):
    data = get_data(base_url, data_url)
    if data is None:
        print("show_data_list 函数获取数据失败")
        return None
    if len(title_list) == 0:
        print("show_data_list 函数参数展示值列表为空")
        return None
    if is_filter:
        if type(filter_num) != int and type(filter_num) != float:
            print("show_data_list 函数输入的过滤条件 {0} 类型为{1}不为数字".format(filter_num, type(filter_num)))
            return None
        if len(filter_mode) == 2 and filter_mode[1] != "e":
            print("show_data_list 函数输入的过滤模式 {0} 错误".format(filter_mode))
            return None
        filter_data_dict(data, num=filter_num, mode=filter_mode)
    if is_replace:
        replace_data(data, source=replace_source, target=replace_target)
    if sort_by_year_mode != 1 and sort_by_year_mode != -1:
        print("show_data_list 函数输入的排序模式 {0} 错误".format(sort_by_year_mode))
        return None
    plt.figure()
    if title is not None:
        plt.title(title)
    _, unit = get_data_by_name(data, title_list[0], get_unit=True)
    for index in range(0, len(title_list)):
        x, y = get_year_num_by_name(data, title_list[index], is_sort=is_sort_by_year, sort_mode=sort_by_year_mode)
        if len(y) == 0:
            del title_list[index]
            break
        if plot_style == Plot.marker or plot_style == 1:
            plt.scatter(x, y, marker=marker)
        elif plot_style == Plot.line or plot_style == 2:
            plt.plot(x, y, linestyle=line_style)
        else:
            print("show_data 函数画图模式传入参数 {0} 错误，将默认绘制".format(plot_style))
            plt.scatter(x, y, marker=marker)
    if is_figure:
        plt.legend(title_list, loc=loc)
    if xlabel_show:
        plt.xlabel(xlabel)
    if ylabel_show:
        if ylabel is None:
            plt.ylabel(unit)
        else:
            plt.ylabel(ylabel)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    plt.show()
    return 0
