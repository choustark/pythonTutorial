"""
函数的应用
"""

"""
设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
"""

import random
import string

ALL_CHARTS: str = string.digits + string.ascii_letters


def generate_code(length: int = 6) -> str:
    """
    生成指定长度的验证码
    :param length 生成验证码的长度
    :return: 返回验证码
    """
    return ''.join(random.sample(ALL_CHARTS, length))


generate_code()

"""
判断素数
"""


def is_prime(num: int) -> bool:
    """
    判断输入的数字是否是素数
    :param num: 被判断的数字
    :return: true or  false
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


"""
双色球随机选号码
1、红球 34个
2、篮球 16个
"""
RED_BALL: list = [i for i in range(1, 35)]
BLUE_BALL: list = [i for i in range(1, 17)]


def choose() -> list:
    """
    随机生成一组号
    :return: 保存的随机号码
    """
    selected_ball = random.sample(RED_BALL, 6)
    selected_ball.sort()
    return selected_ball.append(random.choice(BLUE_BALL))


"""
None 的含义
None 是 Python 中的一个特殊常量，表示空值或没有值。
主要特点
数据类型：属于 NoneType 类型
唯一性：Python 中只有一个 None 对象
表示含义：表示"无值"、"空"或"不存在"

"""


def display(balls: list) -> None:
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')


n: int = int(input('请输入要生成的组数：'))
for _ in range(n):
    display(choose())
