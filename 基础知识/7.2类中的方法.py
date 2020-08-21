# 类中的方法
'''
在Python的类中有很多内置的方法

内置方法的名字开头和结尾都有两个下划线"__"
    构造函数__init__()也是类的内置方法，用于初始化
    析构函数__del__()可以进行一些释放资源的操作，删除对象时被调用

内置方法__str__()用于打印对象

使用print语句时被调用，或者使用函数str()

可以将创建的实例的某个属性打印出来

'''


class Cat:
    def __init__(self, age, eye_color):
        self.age = age
        self.eye_color = eye_color

    def __str__(self):  # 定义 __str__函数
        return '猫的年龄：%d周岁' % (self.age)  # 打印猫的年龄


cat = Cat(1, 'blue')
print(cat)

'''
类中还有用于比较不同对象的内置函数：返回布尔值
    __gt__(self,other):self对象是否比other对象大
    __eg__(self,other):等于
    __le__(self,other):小于等于

'''

# 对象的封装性-------------------------------------------------------------------------------------------
'''
Python的语言风格不强调封装性，但依然可以实现对象的封装

在属性名称前加上两个下划线"__"来防止从外部访问内部的属性

'''


class Cat2:
    def __init__(self, age, eye_color):
        self.__age = age  # age私有化
        self.eye_color = eye_color


cat = Cat2(1, 'blue')
# print(cat.__age)  # AttributeError: 'Cat2' object has no attribute '__age'

# 但是，Python没有严格意义上的封装性
# 成员私有化只是提高了访问的门槛，并不能完全阻止从外部访问成员

cat.__age = 2
print(cat.__age)
