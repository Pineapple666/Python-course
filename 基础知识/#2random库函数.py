from random import *

m = ['a', 'b', 'c', 'd', 'e']

# for i in range(0,10):
print("\nrandom():返回区间[0.0,1.0)中的一个随机浮点数")
print(random())

print("\nuniform(a,b):返回下限a到上限b的随机浮点数")
print(uniform(0,10))

print("\nrandrange(n),randrange(m,n),randrange(m,n,d):返回给定区间的一个随机整数")
print(randrange(0, 5))

print("\nrandint(m,n):相当于randrange(m,m+1)")
print(randint(0, 5))

print("\nchoice(s):从序列s里随机选择一个元素")
print(choice(m))

print("\nsample(pop,k):从pop类型中随机选取k个元素，以列表类型返回")
print(sample(m, 3))

print("\nshuff(s):将序列类型中的元素随机排列，返回打乱后的序列")
print(shuffle(m))
print(m)

print("\nseed(n):用整数n重置随机数生成器。seed()利用系统当时的时间重置随机数生成器，调用seed函数，相当于要求重新开始一个随机序列。")
print(seed(125))

print("\ngauss(mu,sigma):正态分布，mu是均值，sigma是标准差")
print(gauss(0,1))

print("\nuniform(m,n):均匀分布，生成一个[m,n]之间的随机小数")
print(uniform(0, 5))

print("\nbetavariate(alpha,beta):beta分布")#alpha>0 beta>0
print(betavariate(1,1))

print("\ngammavariate(alpha,beta)")#alpha>0 beta>0
print(gammavariate(1,1))