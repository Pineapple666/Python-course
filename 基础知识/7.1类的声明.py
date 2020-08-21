#类的构造
'''
Python使用class关键词来声明一个类

类名一般首字母要大写

类的成员中必须有self参数：
    用于引用类中的成员函数或属性
    self参数永远是第一个参数

'''
#定义类之后，需要定义具体的对象才可以访问对象的成员方法或属性
class Cat:
    def voice(self):
        return '喵'

cat=Cat()#创建一个猫的具体对象cat
print(cat.voice())

'''
类有一个特殊的方法，构造函数__init__()

构造函数__init__()为对象的属性或方法进行初始化

创建对象的时候，新的对象会自动调用__init__()方法

如果在类中没有定义__init__()，Python会提供默认的构造函数

'''

#初始化对象猫的年龄、眼睛颜色
class Cat2:
    def __init__(self,age,eye_color):
        self.age=age
        self.eye_color=eye_color
    def voice(self):
        return '喵'

cat2=Cat2(1,'blue')
print('年龄：',cat2.age)
print('眼睛颜色：',cat2.eye_color)