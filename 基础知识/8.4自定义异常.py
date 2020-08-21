# 自定义异常
# 如果用户要使用的一场类型不是Python自带的，就要自定义异常
# 自定义异常继承自Exception类


class MyError(Exception):
    pass


#raise MyError('There is an Error!')  # __main__.MyError: There is an Error!


# 自定义NotIntError和InvalidScoreError异常处理这两种无效的值
score = [80, 59, 64, 94, 103, -10, '78']


class NotIntError(Exception):
    pass


class InvalidScoreError(EOFError):
    pass


# 将score列表中的分数加起来，捕捉到异常时，打印异常类型并打印分数合
try:
    total = 0
    for i in score:
        if (i < 0) | (i > 100):
            raise InvalidScoreError('Invalid Score!')
        elif not isinstance(i, int):
            raise NotIntError('Not Int Type')
        total+=i
except (InvalidScoreError, NotIntError):
    print('invalid:', i)  # 捕捉到任何一个异常，打印出导致异常的分数
finally:
    print('total score:', total)
