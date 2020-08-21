# 类的继承与超类
'''
在Python中可以让一个类去继承另一个类
    无毛猫类可以继承猫类

被继承的类成为父类，超类或基类，继承的类成为子类

Python支持多继承，允许一个子类有多个父类

'''

# Cat为父类，无毛猫Hairless为子类


# 父类
class Cat:
    def __init__(self, age):
        self.age = age


# 子类
class Hairless(Cat):
    def __init__(self, age, name):  # 如果子类定义了__init__方法，有可能会导致错误
        # AttributeError: 'Hairless' object has no attribute 'age'
        Cat.__init__(self, age)  # 在子类的构造函数中调用了父类的构造函数
        self.name = name


# Hairless为子类，自动继承父类的方法，自动继承Cat的构造函数
cat = Cat(3)
print(cat.age)

hairless = Hairless(4,"miao")
print(hairless.age)



# 如果子类想要调用父类的方法，使用Cat.__init__()的方式，父类名.方法()，也可以使用super()函数
hairless = Hairless(2, 'kitty')
print(hairless.age)


# 类的多态性--------------------------------------------------------------------------------------------
class Dog:
    def hair(self):
        return '大多数狗都有毛'


class Hairless(Dog):
    def hair(self):
        return '无毛狗没有毛'


class Rex(Dog):
    def hair(self):
        return '卷毛狗的毛为卷毛'


# 定义一个函数hair_type()，来体现狗类的多态性
def hair_type(dog_type):
    return dog_type.hair()  # 输入一个狗的类，并返回此类的hair()成员方法结果

dog=Dog()
hairless=Hairless()
rex=Rex()
for dog_type in [dog,hairless,rex]:
    print(hair_type(dog_type))