'''

带参数的装饰器

'''
from functools import wraps


def repeat(times: int):
    """
    重复执行装饰器
    :param times: 重复的次数
    :return:
    """

    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


@repeat(times=3)
def say_hello(name: str):
    """
    打招呼
    :param name: 姓名
    :return: 打招呼信息
    """
    print(f"hello {name}")


say_hello("chou")

def hello():
    print("hello")

hello = repeat(times=3)(hello)
print(hello.__name__)