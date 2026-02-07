'''

可以处理带参数函数的装饰器

'''
from functools import wraps


def log_decorator(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n开始执行{func.__name__}进行了前置操作")
        print(f'\n 位置参数：{args}')
        print(f'\n 关键字参数：{kwargs}')
        result = func(*args, **kwargs)
        print(f"结束执行{func.__name__}进行了后置操作")
        print(f'返回结果：{result}')
        return result

    return wrapper


@log_decorator
def add(a: int, b: int) -> int:
    return a + b


@log_decorator
def say_hello(name: str, greeting: str = 'hello'):
    print(f"{greeting}, {name}!")


print(add(1, 2))
print(say_hello('张三'))
print(say_hello('Bob', 'Hi'))
