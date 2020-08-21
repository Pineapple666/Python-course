# 内置函数
# 内置函数dir，列出模块的属性和方法
import importlib
import math
import random
import tushare

print(dir(math))
# print(help((dir)))


# globals()函数和locals()函数
'''
globals()和locals()函数的调用地方不一样

提供访问全局作用域和局部作用域中变量的方式

以字典的数据结构展现

三种命名空间：
    
    局部命名空间：当前函数或类的方法
    
    全局命名空间：当前模块

    内置命名空间：对所有模块都是全局

当引用某个变量的值时，Python会按着局部命名空间、全局命名空间、内置命名空间的顺序搜索

locals()返回局部命名空间信息，是只读的

globals()返回全局命名空间的信息，非只读

'''

# locals()函数---------------------------------------------------------------------------------------
# 返回函数里的局部变量及对应值


def callmemaby(string):
    locals()
    if string is None:
        print('There is no name being printed')
    else:
        digit = random.randint(1, 5)
        choice = random.choice(['Maybe', string])
        print('Call me %s %d times' % (choice, digit))
    return locals()


ans = callmemaby('Lady')
print(ans)


# globals()函数--------------------------------------------------------------------------------------
# globals()返回的信息是可以改变的
first = 'Sunday'
second = 'Monday'
third = 'Tuesday'

globals()['first'] = 'Friday'
globals()['third'] = 'No Day'

print('first day is', first)
print('second day is', second)
print('third day is', third)


# reload()函数---------------------------------------------------------------------------------------
# 函数reload()用于重新加载之前载入的模块

importlib.reload(math)


# Python的第三方包
'''
Python中的包可以自己创建定义，Tushare是其中的一个例子

Tushare可以实现金融数据的采集、清洗和储存

数据覆盖范围广，接口调用简单，响应快速

'''

print(tushare.__file__)
