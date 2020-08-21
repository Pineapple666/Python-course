# 生成器
from itertools import *
'''
生成器被视为迭代器的一种，分为生成器函数和生成器表达式

生成器是返回可迭代对象的函数

生成器的优点：
            占用的CPU内存小
            只需较少的代码实现功能
            提高运算性能和效率

'''

# 生成器函数--------------------------------------------------------------------------------------------

'''
与普通函数创建相似

使用yield语句返回结果，而不是return语句
    yield语句可以是一个或多个
    生成器返回的是序列而不是单个元素
    每次执行yield语句时，函数会产生一个新的值
    当迭代结束时，会抛出StopIteration

'''


# 生成器函数的创建-----------------------------------------------------------------------------------------
# 创建一个阶乘的生成器函数
def fac():
    pre, cur = 1, 1
    while True:
        yield pre*cur  # 返回值
        pre, cur = pre*cur, cur+1


f = fac()  # 返回生成器对象
print(type(f))
print(list(islice(f, 0, 5)))


# 生成器函数的使用-----------------------------------------------------------------------------------------
# 当函数返回的是可迭代对象时，都可以用生成器函数替换


# 一般函数：
def ex_l():
    l = []
    for i in range(100):
        if i % 3 == 0 and i % 2 == 0:
            l.append(i)
    return l


l_ans = ex_l()
print(l_ans)


# 生成器函数
def ex_g():
    for i in range(100):
        if i % 3 == 0 and i % 2 == 0:
            yield i


ex_generator = ex_g()
print(next(ex_generator), end=" ")
print(next(ex_generator))
print(list(ex_generator))


# 当迭代器生成到末尾时，抛出StopIteration
# 以print_str生成器函数为例：从一数到三
def print_str():
    print('Count three:')
    for i in range(3):
        print('number:')
        yield i+1
    print('Finished counting!')


count = print_str()
for i in range(3):
    print(next(count))


# 生成器表达式-------------------------------------------------------------------------------------------
'''
生成器表达式与列表推导式的创建方法相似

生成器使用()，列表使用[]

生成器表达式返回一个生成器，列表推导式返回一个列表

(expression for var in iterbales)

'''


# 创建一个生成器，产生数字2至5的0次方、1次方以及2次方
gen = (x**n for x in range(2, 5) for n in range(3))
print(type(gen))
print(list(gen))


# 生成器的使用-------------------------------------------------------------------------------------------
def readmultiple(files):  # 读取多个文件，并返回每个文件的第一行
    for file in files:
        for line in open(file):
            yield line


def grep(lines, length):  # 返回字符串长度小于length的行
    return(line for line in lines if len(line) < length)


#读取NBA球员数据集，返回字符串长度小宇30的行
lines=readmultiple(['NBA_season1718_salary.csv'])
line=grep(lines,30)

print(next(line))
print(next(line))