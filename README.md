# [国家统计局数据库爬虫程序](https://github.com/Didnelpsun/NationalData)

该程序用于爬取 [国家统计局数据库](https://data.stats.gov.cn/) 数据。

文件格式：

```
NationalData
     |---------nationaldata[爬虫程序包]
     |               |------------------__init__.py[包初始化]
     |               |------------------data_class.py[数据类型，为数据处理提供结构依赖]
     |               |------------------get.py[数据获取]
     |               |------------------process.py[数据处理]
     |               |------------------save.py[数据保存]
     |
     |---------.gitignore[git过滤文件]
     |---------README.md[说明文件]
     |---------work.py[示例文件]
```

**提示**：国家统计局采用AJAX传输数据，且需要使用cookies反爬，所以需要在使用时需要传入访问的cookies。
