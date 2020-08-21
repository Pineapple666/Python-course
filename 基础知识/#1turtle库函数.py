#turtle库需要import 作为保留字来进行调用
import turtle
turtle.circle(100,100)

from turtle import *
circle(100,80)

import turtle as t
t.circle(100,80)



setup(1000,800,0,0)


#turtle函数：
turtle.penup()
turtle.pu()
#将?抬起来

turtle.pendown()  
turtle.pd()
#将?落下

turtle.pensize(width)  
turtle.width(width)
#设置画笔宽度

turtle.color()

'''
turtle.color(colorstring)  设置画笔颜色，colorstring表示颜色的字符串，"purple","red".
turtle.color((r,g,b))或turtle.color(r,g,b)画笔颜色 对应RGB的01数值
turtle.color(colorstr1,colorstr2) 画笔颜色colorstr1，背景颜色colorstr2
turtle.pencolor(colorstring) 或turtle.pencolor((r,g,b))或turtle.pencolor(r,g,b)
只设置画笔颜色
'''

turtle.begin_fill()
#绘制带有填充色彩图形之前调用，表示填充开始。

turtle.fillcolor("red") or turtle.fillcolor(255,0,0)
#绘制图形的填充颜色  颜色名，	RGB三元组，颜色编码

turtle.end_fill()
#绘制有填充色彩之后调用，表示填充结束

turtle.filling()
#返回当前是否在填充状态

turtle.forward(distance) 
turtle.fd(distance)
#向画笔当前行进方向前进distance距离

turtle.backward(distance) 
turtle.bk(distance)
#向画笔当前行进反方向行进distance距离

turtle.right(60)
turtle.rt(60)
#以当前行进角度为原点，行进方向向右改变60度

turtle.left(60)
turtle.lt(60)
#向前进的方向向左改变60度

turtle.goto(0,0)
#将画笔移动到绝对位置（0,0)处。

turtle.circle(60,-360)
#根据半径60绘制extent角度的弧形

turtle.setx(0)
#将Turtle的x坐标移动到指定位置

turtle.sety(0)
#将Turtle的y坐标移动到指定位置

turtle.setheading(0)
#将Turtle的方向设定为固定角度，0-东，90-北，180-西，270-南

turtle.home()==goto(0,0)
#将Turtle移动到（0,0）位置和向东


turtle.dot(60,color)
#绘制一个指定直径、颜色的点

turtle.undo()
#撤销最后一个图形操作
