# 列表
'''
列表是最常用最基础的数据结构之一

列表为有序的序列类容器，可包含任意类型的元素。例如：1，'hello'，0.5，'d'等。

列表是可变的

列表还可进行一系列特定的操作。例如：序列相加、乘法、索引、切片等。

'''
# -------------------------------------------------------------------------------------------------
# 列表的创建

'''
列表里的元素用中括号'[]'包裹起来。例如['hello']

每个元素之间用逗号隔开','。例如：1,2

普通列表里的元素均为同类型元素

混合列表里的元素为不同类型元素

'''
# 创建含航班名称和机场名称的列表

names = ["Endeavor Air Inc.", "Southwest Georgia Regional"]

# 创建含取消航班数、转机航班数及延误航班数的列表

delay_n = [0, 1, 493]

# 创建含航班名称、机场名称及延误航班数等变量的列表

row1 = ["Endeavor Air Inc.", "Southwest Georgia Regional", 0, 1, 493]

'''通过python的内置函数list()进行创建列表'''

a = list('hello')  # 字符串的字符逐一迭代，返回给list
print(a)  # ['h', 'e', 'l', 'l', 'o']

# 结合list()和range()进行创建

a = list(range(5))  # 对范围进行迭代（0-4）
print(a)  # [0, 1, 2, 3, 4]

# -------------------------------------------------------------------------------------------------
# 多种列表

example1 = []
example2 = ['Kobe', 28, 2010, 'James', 32, 2016]
example3 = [['Chemistry', ['Lily', "A", 98], ['Mike', 60]]]
print(type(example1))  # 空列表
print(type(example2))  # 混合列表
print(type(example3))  # 嵌套列表

# -------------------------------------------------------------------------------------------------
# 列表访问
'''
列表访问可以通过列表索引、切片实现

一些特定函数也可以对列表进行查看和访问

列表里的元素都有其对应的编号（位置）

在python中，列表里从左边开始的第一个元素对应0，第二个元素为1，依次递增

列表里最后一个元素对应的编号为-1

'''

# -------------------------------------------------------------------------------------------------
# 列表索引

example1 = [1, 2, 3, 4, 5]
'''
编号对应如下：
 1   2   3   4   5   
 0   1   2   3   4   
-5  -4  -3  -2  -1
'''
print(example1[0])  # 1
print(example1[-1])  # 5

'''列表元素索引位置可以listname.index(element)实现'''

row1 = ["Endeavor Air Inc.", "Southwest Georgia Regional",
        0, 1, 493, 321, 14, 97, 0, 70]
print(row1.index("Southwest Georgia Regional"))  # 1
print(row1.index(0))  # 如果列表中有重复元素，则返回元素第一次出现的位置

# -------------------------------------------------------------------------------------------------
# 列表切片

'''
列表切片可以实现取多个列表元素
通过[:]得到多个所需元素（如果两个索引值为空，则默认从第一个元素到最后一个元素）
                       如： [start:end]
'''
print(row1[0:5])  # 取第一个到第五个元素   ['Endeavor Air Inc.', 'Southwest Georgia Regional', 0, 1, 493]
print(row1[2:])  # 取第三个到最后一个元素  [0, 1, 493, 321, 14, 97, 0, 70]
# 实现列表的逆序    [70, 0, 97, 14, 321, 493, 1, 0, 'Southwest Georgia Regional', 'Endeavor Air Inc.']
print(row1[::-1])
print(row1[::3])  # 间隔两个元素取一个元素（步长为3）

# -------------------------------------------------------------------------------------------------
# 求列表长度用函数len()

print(len(row1))  # 10

# -------------------------------------------------------------------------------------------------
# 列表元素检查

'''
检查某个元素是否在列表中可用in,not in实现

返回值类型为布尔型

in：如果元素存在于列表中，返回True；否则返回False

not in：与上相反

'''
carrier_name = ["Endeavor Air Inc.", "American Airlines Inc.",
                "Alaska Airlinees Inc.", "JetBlue Airways"]
print("Delta Air Lines Inc."in carrier_name)  # False
print(type("Delta Air Lines Inc."in carrier_name))  # <class 'bool'>

# -------------------------------------------------------------------------------------------------
# 列表元素出现次数

'''用count()可获得特定元素在列表中出现的次数'''

carrier_name_list = ["Endeavor Air Inc.", "Endeavor Air Inc.",
                     "Endeavor Air Inc.", "American Airlines Inc.", "Alaska Airlinees Inc."]
print(carrier_name_list.count("Endeavor Air Inc."))  # 3

# -------------------------------------------------------------------------------------------------
#  列表的修改

'''
列表示可以修改的

可替换单个或多个元素

还可以往列表中添加元素或者删除元素

'''
row2 = ["Delta Air Lines Inc.", "Tallahassee International",
        88, 0, 0, 1148, 0, 0, 0, 75]
row2[4] = 3
# ['Delta Air Lines Inc.', 'Tallahassee International', 88, 0, 3, 1148, 0, 0, 0, 75]
print(row2)

'''替换列表中多个元素可以通过切片实现'''

row2[2:5] = [1, 1, 1]
# ['Delta Air Lines Inc.', 'Tallahassee International', 1, 1, 1, 1148, 0, 0, 0, 75]
print(row2)

# -------------------------------------------------------------------------------------------------
#  列表元素添加

'''在列表末尾添加单个对象：listname.append(newelement)'''

example = [1, 2, 3, 4]
example0 = [5, 6, 7, 8]
example.append(example0)
print(example)  # [1, 2, 3, 4, [5, 6, 7, 8]]

'''在列表末尾添加多个元素：listname.extend(elementlist)'''

example = ['yellow', 'orange', 'blue']
example.extend(['green', 'yellow'])
print(example)  # ['yellow', 'orange', 'blue', 'green', 'yellow']

'''在列表中的指定位置插入元素：listname.insert(index,element)'''

example = ['red', 'orange', 'blue']
example.insert(1, 'new')
print(example)  # ['red', 'new', 'orange', 'blue']

# -------------------------------------------------------------------------------------------------
#  列表元素删除

'''列表删除指定位置元素：listname.pop(index)'''

example4 = [1, 2, 3, 4, 5, 6, 7, 8]
example4.pop(4)
print(example4)  # [1, 2, 3, 4, 6, 7, 8]
example4.pop()  # 不输入index时，默认删除最后一个元素

'''删除指定元素：listname.remove(element)'''

example5 = ['a', 'b', 'c', 'd', 'e', 'd']
example5.remove('d')
print(example5)  # ['a', 'b', 'c', 'e', 'd']，如果列表中有多个指定元素，则删除第一次出现的指定元素

# 列表删除,列表赋值的变量也被删除

del example5
# print(example5) # NameError: name 'example5' is not defined

'''还可以用del进行单个元素的删除'''

example5 = ['a', 'b', 'c', 'd', 'e']
del example5[0]
print(example5)  # ['b', 'c', 'd', 'e']

'''还可以用del进行多个元素的删除'''

del example5[1:2]
print(example5)  # ['b', 'd', 'e']

'''使用listname.clear()可删除列表里所有元素，得到一个空列表'''

example5.clear()  # clear不存在于python3以下版本
print(example5)  # []
# print(dir(list))

# -------------------------------------------------------------------------------------------------
#  列表的操作符

'''列表连接操作符 '+' 可以进行两个列表之间的拼接'''

example6 = [1, 2, 3, 4]
example7 = [5, 6, 7, 8]
print(example6+example7)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(example6)  # [1, 2, 3, 4] 列表没有改变

'''重复操作符 '*' 可重复列表中的元素'''

print(example6*2)  # 一个新的列表[1, 2, 3, 4, 1, 2, 3, 4]

'''
列表比较操作符 '>' '<' '>=' '<=' '==' 'is' 'is not' 
从第一个元素开始比较，只要一放所处同位置的元素大，则该列表大于另一列表

'''
example8 = [88, 3, 58]
example9 = [27, 2294, 66]
print(example8 > example9)  # True
example10 = [88, 3, 58]
print(example8 == example10)  # True，比较两个列表的值是否相同
print(example8 is example10)  # False，比较两个列表的引用对象是否相同
example9 = example8
print(example8 is example9)  # True

# -------------------------------------------------------------------------------------------------
#  列表内置函数

''' reverse 可以将列表元素反向排序，不返回值'''

player = ['Kobe', 'James', 'Curry', 'Durant']
player.reverse()
print(player)  # ['Durant', 'Curry', 'James', 'Kobe']

''' sort 可对列表元素进行排序，不返回值'''
grades = [98, 99, 100, 78, 89, 62, 67]
grades.sort()
print(grades)  # 排序后[62, 67, 78, 89, 98, 99, 100]

# -------------------------------------------------------------------------------------------------
# 列表的复制

'''
用等号 '=' 对列表进行复制，值与引用对象相同
一个列表改变，另一个列表也随之改变

'''
season = ['spring', 'winter']
season1 = season
season1.append('fall')
print(season)
print(season1)  # 均为['spring', 'winter', 'fall']

'''
用copy()对列表进行复制，值相同，引用对象不同
一个列表改变，另一个不影响

'''
season = ['spring', 'winter']
season2 = season.copy()
print(season2)  # ['spring', 'winter']
season.append('fall')
print(season1)  # ['spring', 'winter', 'fall']
print(season2)  # ['spring', 'winter']

'''
列表也可以通过切片进行复制
复制元素值，不复制应用对象

'''
season = ['spring', 'winter']
season_copy = season[:]
print(season_copy)  # ['spring', 'winter']
season.append('fall')
print(season_copy)  # ['spring', 'winter']

# -------------------------------------------------------------------------------------------------
# 列表的最大值和最小值

delta_mn = [40249, 16208, 1703, 9336, 233]
print(max(delta_mn))  # 40249
print(min(delta_mn))  # 233

# -------------------------------------------------------------------------------------------------
# 列表排序

''' sorted(listname) 返回升序后的列表'''

print(sorted(delta_mn))  # [233, 1703, 9336, 16208, 40249]

''' sorted(listname,reverse=True) 可返回降序后的列表'''

print(sorted(delta_mn, reverse=True))  # [40249, 16208, 9336, 1703, 233]

# -------------------------------------------------------------------------------------------------
# 嵌套列表

'''列表的元素可以为列表，从而得到一个高纬度的列表'''

example3 = [['Chemistry', ['Lily', "A", 98], ['Mike', 60]],
            ['Math', ['Lily', "B", 80], ['Mike', "A", 95]]]

'''嵌套列表的索引'''

print(example3[0])  # ['Chemistry', ['Lily', 'A', 98], ['Mike', 60]]
print(example3[0][1])  # ['Lily', 'A', 98]
print(example3[0][1][0])  # Lily

'''嵌套列表的切片'''

print(example3[1])  # ['Math', ['Lily', 'B', 80], ['Mike', 'A', 95]]
print(example3[1][1:])  # [['Lily', 'B', 80], ['Mike', 'A', 95]]
