"""
函数的进阶应用
Python中的函数确实是一等函数（First-Class Functions），这意味着函数在Python中具有以下特性：
1、函数可以赋值给变量
2、函数可以作为参数传递
3、函数可以作为返回值
4、函数可以存储在数据结构中
"""


def calculate(*num, **kwargs) -> int:
    """
    输入任何数据进行求和操作
    :param num:
    :param kwargs:
    :return: 求和
    """
    tems: list = list(num) + list(kwargs.values())
    result = 0
    for item in tems:
        if type(item) in (int, float):
            result += item
    return result


def add(temp: int, item: int) -> int:
    return temp + item


def calculate2(default_value, op_func: callable, *num, **kwargs) -> int:
    """
    输入任何数据进行求和操作
    :param op_func: 运算方法
    :param default_value: 默认值
    :param num:
    :param kwargs:
    :return: 求和
    """
    tems: list = list(num) + list(kwargs.values())
    result = default_value
    for item in tems:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result


print(calculate2(100, add, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

import operator

print(calculate2(100, operator.add, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

old_nums: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_nums: list = [item + 1 for item in old_nums if item % 2 == 0]
print(new_nums)

"""
使用内置函数
"""


def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


new_nums_1: list = list(map(square, filter(is_even, old_nums)))

"""
Lambda函数（匿名函数）
lambda 函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值.
定义 lambda 函数的关键字是lambda，后面跟函数的参数，如果有多个参数用逗号进行分隔；冒号后面的部分就是函数的执行体，
通常是一个表达式，表达式的运算结果就是 lambda 函数的返回值，不需要写return 关键字。
"""

new_nums_2: list = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))

import functools

# 用一行代码实现计算阶乘的函数
fac: callable = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

is_prime: callable = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

"""
偏函数
偏函数是指固定函数的某些参数，
生成一个新函数这样就无需在每次调用函数时都传递相同的参数。在 Python 语言中，我们可以使用functools模块的partial函数来创建偏函数。
"""
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))  # 1001

print(int2('1001'))  # 9
print(int8('1001'))  # 513
print(int16('1001'))  # 4097
