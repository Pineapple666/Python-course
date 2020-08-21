# 模块的搜索路径
'''
模块被导入时，Python解释器首先根据模块名字搜索内置模块

如果没有找到，则根据sys.path变量给出的目录进行搜索

sys.path是一个字符串列表

sys.pqth包含当前目录、PYTHONPATH(环境变量)和安装决定的默认目录

'''

import sys
import numpy
import site

print(sys.path)


# 模块的路径修改------------------------------------------------------------------------------------------
'''
通过sys.path.append进行路径添加
    sys.path列表的特性允许对它进行修改
    如果需要导入的模块的路径不在搜索路径里，用append()可以进行路径添加

    sys.path.append('/Users/xxx/anaconda/lib/newfolder')

通过.pth文件修改搜索路径
    在安装第三方模块时，有可能需要将安装路径添加到sys.pyh中
    可以通过.pth作为扩展名创建路径配置文件，并且放到site-package包目录下
    由site.getsitepackages()函数获取site-packages目录

'''


# 模块被导入路径
# 通过__file__查看模块所在的路径

print(numpy.__file__)

print(site.getsitepackages())
