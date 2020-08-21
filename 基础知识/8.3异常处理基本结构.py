# 异常处理基本结构
'''
try关键字内为要检测的语句

except后的名字为异常类型

如果在try内检测到这种异常类型，则执行except关键字内的代码

try:
    <语句>
except <异常类型>
    <发现异常时执行的语句>

'''

try:
    # 2/0
    2/2
except ZeroDivisionError:
    print('ZeroDivisionError')  # ZeroDivisionError
else:
    print('There is no ZeroDivisionError')  # There is no ZeroDivisionError


# 如果抛出的异常不是捕捉的异常，仍会抛出错误
# 不在except关键字后制定特定的一场类型，仍会捕捉到异常，但不知道异常的类型
try:
    1+'1'
except:
    print('There is a Error')

try:
    1+'1'
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')  # TypeError


'''
finally子句为异常处理的另一种常用结构

无论是否检测到异常，都会执行finally语句内的代码

try:
    <语句>
except <一场类型>
    <发现异常时执行的语句>
else:
    <未发现异常时执行的语句>
finally:
    <不管是否检测到异常都要执行的语句>

'''

try:
    1+'1'
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')
finally:
    print('finished')  # TypeError,finished


# 我们可以通过raise来主动抛出一个异常，raise的用法如下
'''
raise [Exception [, args [, traceback]]]

Exception位异常类型

args是自己提供的异常参数

traceback是跟踪异常对象

raise TypeError('There is a TyprError')

'''
#raise也可以在try/except结构中使用