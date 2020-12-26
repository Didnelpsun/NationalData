# -*- coding: utf-8 -*-
# 定义类来规范保存数据
class NationDictData:
    def __init__(self, name, exp, unit, data):
        self.name = name
        self.exp = exp
        self.unit = unit
        self.data = data


class NationData:
    def __init__(self, year, data):
        self.year = year
        self.data = data
