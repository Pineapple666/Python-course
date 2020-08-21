'''
字符串
Python使用'string'的方式创建字符串

'''
a = 'A student'
print(type(a))  # <class 'str'>

'''
Python使用索引或者切片的方式获取字符串
编号对应方式为：

's' 't' 'u' 'd' 'e' 'n' 't'
-7  -6  -5  -4  -3  -2  -1
 0   1   2   3   4   5   6

 使用[]对字符串进行索引可获取一个元素
 使用[:]对字符串索引可获取连续几个元素

'''
print(a[0])  # 's'
print(a[0:5])  # 'stude'  注意：不包括最后一个字符

'''使用+可以将多个字符串合为一个'''

print('go'+'to')  # 'goto'

'''反斜杠\表示转义字符'''

print('[[1,2,3,],\n[4,5,6,],\n[7,8,9]]')  # '\n'为换行

'''格式化符号'''

print('Hello,%s' % 'World')  # 'Hello,World'

'''
%c  格式化字符及其ASCII码

%s  格式化字符串

%d  格式化整数

%u  格式化无符号整型

%o  格式化无符号八进制数

%x  格式化无符号十六进制数

%X  格式化无符号十六进制数（大写）

%f  格式化浮点数字，可指定小数点后的精度

%e  用科学计数法格式化浮点数

%E  上同

%g  %f和%e的简写

%G  %f和%E的简写

%p  用十六进制数格式化变量的地址

'''

'''特有数据类型，复数型：complex  如2+3i'''

a = complex(1, 3)
print(type(a))  # <class 'complex'>

'''布尔型bool只有True和False两个值，常用逻辑判断'''

a = True
b = False
print(type(a))
print(type(b))  # 均为<class 'bool'>

'''处理字符串的内置函数'''

x = "好好学习，天天向上"
print(len(x))  # 返回字符串a的长度

print(str(125))  # 将任意类型a转换成字符串类型

print(str(3+5))

print(chr(100), chr(101))  # 返回Unicode编码为a的字符

print(ord('/'), ord('+'), ord(' '))  # 返回字符a的Unicode编码制

print(hex(62))  # 将整数a转换成十六进制数，并返回其小写字符串形式

print(oct(62))  # 将整数a转换成八进制数，并返回其小写字符串形式

'''
（一）字符串查找类方法：find()、rfind()、index()、rindex()、count()
'''

# find()和rfind()方法分别用来查找一个字符串在另一个字符串指定范围
# （默认是整个字符串）中首次出现和最后一次出现的位置，如果不存在则返回-1

s = "bird,fish,monkey,rabbit"
print(s.find('fish'))

# index()和rindex()方法同find()，如果不存在则抛出异常

print(s.index('monkey'))

# count()方法用来返回一个字符串在另一个字符串中出现的次数，不存在则返回0

print(s.count('i'))

'''
（二）字符串分隔类方法：split()、rsplit()、partition()、rpartition()
'''
# split()和rsplit()方法分别用来以指定字符为分隔符，
# 从原字符串左端和右端开始将其分隔成多个字符串，并包含分隔结果的列表

s = "bird,fish,monkey,fish,rabbit"
print(s.split(','))  # ['bird', 'fish', 'monkey', 'fish', 'rabbit']
s = "I am a boy"
print(s.split())  # ['I', 'am', 'a', 'boy']

'''
（三）字符串链接方法：join()
'''
# 将列表中多个字符串进行链接，并在相邻两个字符串之间插入指定字符，返回新的字符串
li = ['apple', 'banana', 'pear', 'peach']
print(':'.join(li))  # apple:banana:pear:peach
print('-'.join(li))  # apple-banana-pear-peach

'''
（四）大小写字符串转换方法：lower()、upper()、capitalize()、title()、swapcase()
'''
s = "I have two big eyes."
print(s.lower())  # 返回小写字符串，i have two big eyes.
print(s.upper())  # 返回大写字符串，I HAVE TWO BIG EYES.
print(s.capitalize())  # 首字母大写，I have two big eyes.
print(s.title())  # 每个单词首字母大写，I Have Two Big Eyes.
print(s.swapcase())  # 大小写互换，i HAVE TWO BIG EYES.

'''
（五）字符串替换方法：replace()
'''
# 用于替换字符串中指定字符或子字符串，每次只能替换一个字符或子串。
# 不是修改原字符串，而是返回一个新的字符串

s = "i am pineapple"
print(s.replace("pineapple", "菠萝"))  # 你是我的small苹果儿

'''
（六）删除字符串两端，右端或左端连续空白和指定字符：strip()、rstrip()、lstrip()
'''
s = "     abc     "
print(s.strip())  # 删除两端空白字符，abc
print(s.rstrip())  # 删除右端空白字符，    abc
print(s.lstrip())  # 删除左端空白字符，abc
s = "====Mike===="
print(s.strip('='))  # 删除指定字符 "="，'Mike'

'''
（七）判断字符串是否以指定字符开始或结束方法：startwith()、endswith()
'''
s = "Python程序设计.py"
print(s.startswith("Python"))  # 判断字符串是否以 Python 开始，True
print(s.endswith("py"))  # 判断字符串是否以 py 结束，True

'''
（八）判断字符串类型的方法：isupper()、islower()
'''
s = 'years'
print(s.islower())  # 是否全为小写，True
print(s.isupper())  # 是否全为大写，False

s = "20001009"
print(s.isdigit())  # 是否全为数字，True

s = "He is 10 years old"
s = s.replace(" ", "")  # 去掉空格
print(s.isalnum())  # 是否为数字或字母，True
print(s.isalpha())  # 是否为全字母，False
s = "-+/*"
print(s.isascii())  # 是否是字符，True

'''
（九）字符串排版方法：center()、ljust()、rjust()、zfill()
'''
s = "Hello Mike"
print(s.center(30, "="))  # 字符串居中对齐，输出宽度为30，不足的以 "=" 填充
# ==========Hello Mike==========
print(s.ljust(20, "*"))  # 字符串左对齐，输出宽度为20，不足的以 "*" 填充
# Hello Mike**********
print(s.rjust(20, "*"))  # 字符串居右对齐，输出宽度为20，不足的以 "*" 填充
# **********Hello Mike
print(s.zfill(20))  # 输出宽度为20，在字符串左侧以字符 "0" 填充
# 0000000000Hello Mike

'''
format 格式化方法

在 "{}" 中首先输入 ":" ，":" 称为格式引导符

":" 之后分别设置 <填充字符> <对齐方式> <宽度>

     设置项                          可选值
   
   <填充字符>       "*"，"="，"-"等，但只能是一个字符，默认为空格
   
   <对齐方式>           ^(居中)，< (左对齐)，> (右对齐)
     
     <宽度>          一个整数，指格式化后整个字符串的字符个数
'''
print("{:*^20}".format("Mike"))  # 宽度20，居中对齐， "*" 填充
print("{:=<20}".format("Mike"))  # 宽度20，左对齐， "=" 填充
print("{:.2f}".format(3.1415926))  # 保留2位小数
print("{:.4f}".format(3.1415926))  # 保留4位小数
print("{:5d}".format(24))  # 宽度5，右对齐，空格填充，整数形式输出
print("{:x>5d}".format(24))  # 宽度5，右对齐，'x'填充，整数形式输出
