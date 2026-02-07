"""
函数和模块
"""
from _11_function01_01 import calculate

# 输入m和n 计算组合数(m,n)的值
# m: int = int(input('请输入m的值：'))
# n: int = int(input('请输入n的值：'))
# # 计算m的阶乘
# fm: int = 1
# for i in range(1, m + 1):
#     fm *= i
#
# # 计算n的阶乘
# fn: int = 1
# for i in range(1, n + 1):
#     fn *= i
#
# # 计算(m-n) 的阶乘
# fk: int = 1
# for i in range(1, m - n + 1):
#     fk *= i
#
# print(f'组合数是：{fm // fn // fk}')

print('-------' * 10 + '使用函数' + '-------' * 10)


def calculate1(num: int) -> int:
    result: int = 1
    for n in range(2, num + 1):
        result *= n
    return result


m: int = int(input('请输入m的值：'))
n: int = int(input('请输入n的值：'))
print(f'使用函数计算得到(m,n)的组合数是：{calculate(m) // calculate(n) // calculate(m - n)}')

print('-------' * 10 + '使用函数(可变参数)' + '-------' * 10)


def add(*nums: int) -> int:
    total: int = 0
    for value in nums:
        if type(value) in (int,float):
            total += value
    return total

print(f'第一次使用函数计算结果是：{add()}')
print(f'第二次使用函数计算结果是：{add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')
print(f'第三次使用函数计算结果是：{add(1,2,4)}')


## 可变参数并且是键值对
def foo(*num,**info):
    print(num)
    print(info)
foo(1,2,3,4,5,6,7,8,9,10,name='张三',age=18)

print('-------' * 10 + '使用模块管理函数' + '-------' * 10)

print(f'使用模块管理函数调用函数的结果是：{calculate(10)}')

