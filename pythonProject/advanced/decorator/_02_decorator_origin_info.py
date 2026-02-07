from functools import wraps

'''
functools.wraps
'''


# 问题：丢失原函数信息


def my_decorator(func: callable):
    def wrapper():
        return func()

    return wrapper


@my_decorator
def say_hello():
    """
    打招呼
    :return: 打招呼信息
    """
    print("hello")


#print(say_hello.__name__)  # 输出 wrapper
#print(say_hello.__doc__)  # 输出 None


# 解决方法：使用 functools.wraps 解决函数信息丢失问题


def my_decorator(func: callable):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper



@my_decorator
def say_hello():
    """
    打招呼
    :return: 打招呼信息
    """
    print("有函数信息的 hello")



print(say_hello.__name__)
print(say_hello.__doc__)