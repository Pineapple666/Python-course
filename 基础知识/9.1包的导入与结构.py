# 包的导入与结构
'''
Python模块(Module)即是包含Python程序代码的脚本文件

文件后缀的.py

一个Python程序是一个模块的系统

在Python中，第三方工具包(Package)和内置标准库都是模块

'''

# 模块的执行环境------------------------------------------------------------------------------------------
'''
模块中包含变量和函数

在一个模块中，可以导入其他模块

'''

#模块的导入--------------------------------------------------------------------------------------------
'''
使用import语句导入整个模块
    import module1
    import module2
    import module3

一行导入多个模块
    import module1, module2, module3,......

使用from...import语句导入特定模块属性
    from module import name1, name2, name3, ......

import...as或者from...import...as可替换模块的原始名称
    import module as m
    from module import name as n

'''

#包
'''
包是一个有层次的文件目录结构

由n个模块或n个子包组成的Python应用程序执行环境

有利于模块的识别和管理

'''
#包的目录结构-------------------------------------------------------------------------------------------
'''
包的目录结构与树状结构类似

每一个包的目录里都包含__init__.py的文件

PackageA                顶层包
{
    __init__.py         初始化PackageA
    module1.py          模块1
    module2.py          模块2
    
    PackageB            子包PackageB
    {
        __init__.py     初始化PackageB
        module1.py      模块1
    }
}

'''

#包的导入---------------------------------------------------------------------------------------------
'''
包的导入与模块类似，下面简单写一下不同的地方

import package.module1.name1                #导入包的模块1中的name1对象

from package.module import name1 as n1      #同上

'''

#常用的包---------------------------------------------------------------------------------------------
'''
数据科学领域中常用的Python包：

Numpy               科学计算基础包

Scikit-learn        机器学习

Pandas              处理类表格数据结构的数据分析

Scrapy              采集数据、数据爬虫

Statsmodels         搭建统计模型，进行统计检验

Matplotlib          平面绘图

'''