#异常的介绍
'''
Python中至少有两种错误，语法错误和异常

语法错误是书写、输入的错误

异常是在代码语法正确的情况下，运行时出现的错误

'''
print(2/0)  # ZeroDivisionError: division by zero

'''
在Python中异常存在层级关系

BaseException               所有异常的基类
{
    Exception
    {
        StopIeration
        StandardError
        {
            ImportError
            LookupError
            NameError
            SyntaxError
            ValueError      传入的参数无效
            .
            '
            '
            '
            '
        }
        Warning
    }
    SystemExit              Python解释器退出
    KeyboradInterrupt       键盘中断
    GeneratorExit           生成器对象被销毁
}

'''

