# -*- coding: utf-8 -*-

from enum import Enum
import matplotlib.pyplot as plt
from nationaldata.get import get_data, get_data_by_name, print_data
from nationaldata.process import filter_data, sort_data_order_by_year, split_year_num_by_list


class Plot(Enum):
    marker = 1
    line = 2
    bar = 3


def show_data(url, title, is_filter=True, filter_num=0, filter_mode="g", is_sort_by_year=True, sort_by_year_mode=1,
              show_title=True, color="r", plot_style=Plot.marker, marker="+", line_style="-",
              xlabel_show=True, xlabel="年份", ylabel_show=True, ylabel=None):
    data = get_data(url)
    if data is None:
        print("show_data 函数获取数据失败")
        return None
    if is_filter:
        if type(filter_num) != int and type(filter_num) != float:
            print("show_data 函数输入的过滤条件 {0} 类型为{1}不为数字".format(filter_num, type(filter_num)))
            return None
        if len(filter_mode) == 2 and filter_mode[1] != "e":
            print("show_data 函数输入的过滤模式 {0} 错误".format(filter_mode))
            return None
        filter_data(data, filter_num, filter_mode)
    data_list, unit = get_data_by_name(data, title, get_unit=True)
    if not data_list:
        print("show_data 函数获取不到名为 {0} 的字段数据".format(title))
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
    if plot_style == 1:
        plt.scatter(x, y, color=color, marker=marker)
    elif plot_style == 2:
        plt.plot(x, y, color=color, linestyle=line_style)
    elif plot_style == 3:
        plt.bar(x, y, color=color)
    else:
        print("show_data 函数画图模式传入参数 {0} 不存在该值，将默认绘制".format(plot_style))
        plt.scatter(x, y, color=color, marker=marker)
    plt.show()
