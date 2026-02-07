"""
函数和模块
"""

print('-------' * 10 + '使用函数' + '-------' * 10)


def calculate(num: int) -> int:
    result: int = 1
    for n in range(1, num):
        result += n
    return result


print('-------' * 10 + '使用函数(可变参数)' + '-------' * 10)


def add(*nums: int) -> int:
    total: int = 0
    for value in nums:
        if type(value) in (int, float):
            total += value
    return total


print(f'第一次使用函数计算结果是：{add()}')
print(f'第二次使用函数计算结果是：{add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')
print(f'第三次使用函数计算结果是：{add(1, 2, 4)}')


## 可变参数并且是键值对
def foo(*num, **info):
    print(num)
    print(info)


foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name='张三', age=18)

print('-------' * 10 + '使用模块管理函数' + '-------' * 10)
