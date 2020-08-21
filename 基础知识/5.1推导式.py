# 推导式(comprehension)

# 列表推导式--------------------------------------------------------------------------------------------

'''
列表的可变性对数据的存储及运用提供了很大的便利

列表推导式为列表的创建提供了一种非常简便的方式

与循环控制方法相比，列表推导式的效率更加高效

'''
# 列表推导式需要用到for循环语句，用 [] 包括起来
# [表达式 for 变量 in 列表]

list1 = [i*2 for i in [1, 2, 3]]
print(list1)

# if语句也能被用到
# [ 表达式 for 变量 in 列表 if 判断条件]

list1 = [i*2 for i in [1, 2, 3] if i > 1]
print(list1)

# 多个for循环语句和if条件语句
# [表达式 for 变量1 in 列表1 if 判定条件1
#        for 变量2 in 列表2 if 判断条件2
#          .....]

list1 = [i+j for i in [1, 3, 5] if i % 2 != 0
         for j in [2, 4, 6] if j % 2 == 0]
print(list1)  # [3, 5, 7, 5, 7, 9, 7, 9, 11]

# 多重语句可以实现两个列表中满足一定条件的元素的两两自由组合

x = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5, 6]
list1 = [(i, j) for i in x if i not in 'ae'
         for j in y if j % 3 == 0]
print(list1)  # [('b', 3), ('b', 6), ('c', 3), ('c', 6), ('d', 3), ('d', 6)]

list1 = [{item: item+1} for item in [0, 2, 3, 4, 5, 6]]
print(list1)  # [{0: 1}, {2: 3}, {3: 4}, {4: 5}, {5: 6}, {6: 7}]

# 嵌套列表推导式
# 创建一个由数字1-10组成的3*3矩阵

list1 = [[k for k in range(column, column+3)] for column in range(1, 10, 3)]
print(list1)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

temp1 = []
temp2 = []
for i in range(1, 10, 3):
    for j in range(i, i+3):
        temp1.append(j)
    temp2.append(temp1)
    temp1 = []
print(temp2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 嵌套列表降维

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = [j for i in matrix for j in i]
print(list1)

result = []
for i in matrix:
    for j in i:
        result.append(j)
print(result)

# 字典推导式-------------------------------------------------------------------------------------------

# 利用for循环语句建立
# dict1={(key expression:value expression for (key,value) in dict.items())}

# if条件句与zip()函数也常在推导式中出现

# 字典推导式可以实现键值的快速交换

team_players = {'Stephen Curry': 'GSW', 'Paul Millsap': 'DEN',
                'LeBron James': 'CLE', 'Gordon Hayward': 'BOS', 'Blake Griffin': 'DET'}
dict1 = {value: key for key, value in team_players.items()}
print(dict1)
# {'GSW': 'Stephen Curry', 'DEN': 'Paul Millsap', 'CLE': 'LeBron James', 'BOS': 'Gordon Hayward', 'DET': 'Blake Griffin'}

# 如果有重复的值，交换后的值只有一个

rep = {'1': 'a', '2': 'p', '3': 'p', '4': 'l', '4': 'e'}
print({v: k for k, v in rep.items()})  # {'a': '1', 'p': '3', 'e': '4'}

# 集合推导式--------------------------------------------------------------------------------------------

# 使用 {} 对元素进行包裹
# 集合元素没有重复值

teams_list = ['GSW', 'CLE', 'DEN', 'BOS',
              'DET', 'TOR', 'OKC', 'MEM', 'HOU', 'TOR']
print({team for team in teams_list})
# 没有重复的元素{'TOR', 'GSW', 'BOS', 'HOU', 'OKC', 'DEN', 'DET', 'MEM', 'CLE'}
