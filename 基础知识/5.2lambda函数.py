# lambda函数

'''
lambda函数又称为匿名函数，是一种简单快速的函数定义方式，与其他函数的定义方式不一样。

'''
# lambda函数的结构--------------------------------------------------------------------------------------
'''
以lambda作为开头，可接收多个参数，只返回一个表达式的值，不包含多个表达式。
lambda arg1 arg2 : expression

'''


# 单个参数的lambda函数：
def sqrt_two(x): return x**(1/2)


print(sqrt_two(4))  # 2.0


# 多个参数的lambda函数：
def triangle(x, y): return (x**2+y**2)**(1/2)


print(triangle(3, 4))  # 5.0

# lambda函数的 使用场景-----------------------------------------------------------------------------------
''' 表达式返回一个函数对象'''

# 可以直接作为列表的元素
f_l = [lambda x:x*2]
print(f_l)  # [<function <lambda> at 0x00000170D006DF70>]
print(f_l[0](2))  # 4


# 作为字典的成员
f_d = {'man': lambda x, y: (x+y)/2, 'difference': lambda x, y: x-y}
# {'man': <function <lambda> at 0x00000170D0074040>, 'difference': <function <lambda> at 0x00000170D00740D0>}
print(f_d)
print(f_d['man'](5, 3))  # 4.0


# 实现列表元素的排序，eg：按嵌套列表中每一个成员列表的第一个元素进行排序
example_list = [[1, 4], [7, 6], [90, 2], [7, 8], [10, 24], [89, 95]]
print(sorted(example_list, key=lambda x: x[0]))


#实现字典成员的排序，eg：exmple_dict中的键为一篇文章出现单词的英文单词，值对应的是英文单词出现的次数
example_dict={'do':10,'I':40,'make':23,'hard':5,'science':1,'learn':9}
print(sorted(example_dict.items(),key=lambda x:x[0]))#按字典中的键排序
print(sorted(example_dict.items(),key=lambda x:x[1]))#按字典中的值排序


#函数对象作为函数的返回值，eg：power()返回数值x的次方
def power(n):
    return lambda x:x**n
power_five=power(5)
print(power_five(3))#返回3的5次方
