# 迭代器
'''
可迭代对象：实现迭代器协议的对象，字符串、列表等

使用for循环句来查看元素

'''
from itertools import *
for i in [1, 3, 5, 7, 9]:
    print(i)

'''
迭代协议：提供next方法，返回迭代器的下一项，如果没有下一项，则抛出StopIteration，并终止迭代

内置函数iter接受可迭代对象并返回迭代器

迭代器指可实现next方法的对象

迭代器是访问迭代对象成员的一种方式

迭代器只能向前迭代，不能后退

迭代器无法复制

'''

# 创建迭代器--------------------------------------------------------------------------------------------
# 使用内置函数inter()进行创建

lst = [1, 3, 5, 7, 9]
lsts_iter = iter(lst)
print(type(lsts_iter))  # <class 'list_iterator'>


# 迭代器元素的访问-----------------------------------------------------------------------------------------
# 使用next()对迭代器的元素访问，如果没有下一项，则终止迭代

print(next(lsts_iter))
print(next(lsts_iter))
print(next(lsts_iter))
print(next(lsts_iter))
print(next(lsts_iter))

# 可以使用try...except避免终止迭代的异常抛出
try:
    while True:
        print(next(lsts_iter))
except StopIteration:
    pass


# 迭代器内部执行过程----------------------------------------------------------------------------------------
# 自己定义一个迭代器：
class Factorial(object):
    def __init__(self, end):
        self.pre = 1
        self.cur = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur > self.end:
            raise StopIteration
        else:
            Value = self.pre*self.cur
            self.pre = Value
            self.cur += 1
            return Value


f = Factorial(5)


# 迭代器的函数-------------------------------------------------------------------------------------------
print(dir(iter))


# 使用isinstance()判断对象是否是迭代器，从collections包里导入Iterator


print(list(f))  # list():将迭代器中的成员以列表形式输出
print(sum(Factorial(5)))  # 计算成员总和
print(sorted(Factorial(5), reverse=True))  # 排序

'''
Python中一些内置模块的函数可实现高效的迭代器创建

itertools模块的count、cycle、和islice函数

'''

# count(start, step): 无限迭代，start开始的每个元素上step值
counter = count(5, 10)

for i in range(10):
    print(next(counter), end=" ")
print('\n')


# cycle(p):无限迭代，循环迭代p中的成员
cycle_i = cycle(['Are', 'you', 'Hungry'])
for i in range(5):
    print(next(cycle_i), end=" ")


# islice(seq,start,stop,step):生成优先序列
finite_i = islice(counter, 0, 10, 3)
print('\n', list(finite_i))
