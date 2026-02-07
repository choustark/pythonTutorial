"""
Python 中的特色语法装饰器，一个是函数的递归调用。
Python 语言支持函数的嵌套定义
"""
import time
import random


def download(file_name):
    """
    下载文件
    :param file_name: 文件名
    :return:
    """
    print(f"开始下载文件{file_name}")
    time.sleep(random.randint(1, 5))
    print(f"下载文件{file_name}完成")


def upload(file_name):
    """
    上传文件
    :param file_name:
    :return:
    """

    print(f"开始上传文件{file_name}")
    time.sleep(random.randint(1, 5))
    print(f"上传文件{file_name}完成")


download("test.py")
upload("python从入门到精通.pdf")

"""
打印时间耗时
"""
start: float = time.time()
download("MySQL从删库到跑路.avi")
end: float = time.time()
print(f"下载文件耗时{end - start:.2f}秒")

start: float = time.time()
upload("python从入门到精通.pdf")
end: float = time.time()
print(f"上传文件耗时{end - start:.2f}秒")

"""
使用装饰器函数
def record_time(func):
    
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        
        return result
    
    return wrapper
"""


def record_time(func: callable):
    """
    记录函数执行耗时
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        """
        包装函数
        :param args:
        :param kwargs:
        :return:
        """
        # 在执行被装饰的函数之前记录开始时间
        start: float = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end: float = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f"函数{func.__name__}耗时{end - start:.2f}秒")
        # 返回被装饰函数的返回值
        return result

    return wrapper


download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

"""
使用python 内存的包装器
"""

import random
import time

from functools import wraps


def record_time(func):
    # 使用注解方式，语法糖
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰后的函数会记录执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')
