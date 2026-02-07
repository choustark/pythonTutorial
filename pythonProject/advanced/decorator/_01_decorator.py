def greeting(name: str) -> str:
    """
    打招呼
    :param name: 姓名
    :return: 打招呼信息
    """
    return f"Hello, {name}"


def log_decorator(func: callable):
    def wrapper(*args, **kwargs):
        print(f"\n开始执行{func.__name__}进行了前置操作")
        func(*args, **kwargs)
        print(f"结束执行{func.__name__}进行了后置操作")

    return wrapper


@log_decorator
def greeting(name: str):
    print(f"Hello, {name}")


# 调用函数
## greeting("张三")

print("------" * 80)
print("装饰器的工作原理")


def sample_decorator(func: callable):
    print(f"1、装饰器被的调用：接受函数：{func.__name__}")

    def wrapper():
        print(f"3、包装函数被调用：接受函数：{func.__name__}")
        result = func()
        print(f"5、包装函数返回：接受函数：{func.__name__}")
        return result

    print("2、wrapper装饰器函数创建")
    return wrapper


print("==定义函数==")


@sample_decorator
def sample_function():
    print("4、被装饰的函数执行")
    return "Hello World"


print("==调用函数==")
sample_function()

print("==再次调用函数==")
sample_function()
