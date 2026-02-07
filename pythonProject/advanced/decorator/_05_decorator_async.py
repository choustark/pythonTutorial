'''

异步装饰器

'''
import time
from functools import wraps
import asyncio
import random
import inspect


def async_time(func: callable):
    '''
    计算异步函数的执行时间
    :param func:
    :return:
    '''

    @wraps(func)
    async def wrapper(*arg, **kwargs):
        import time
        start: float = time.time()
        result = await func(*arg, **kwargs)
        end: float = time.time()
        print(f'{func.__name__}函数耗时{end - start:.2f}秒')
        return result

    return wrapper


@async_time
async def download(file_name):
    """
    下载文件
    :param file_name: 文件名
    :return:
    """
    print(f"\n开始下载文件{file_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"\n下载文件{file_name}完成")


# asyncio.run(download('test.txt'))

# 同步和异步装饰器
def uinversal(func: callable):
    """
    同步和异步装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        """
        同步装饰器
        :param args:
        :param kwargs:
        :return:
        """
        start: float = time.time()
        result = func(*args, **kwargs)
        end: float = time.time()
        print(f'{func.__name__}函数耗时:{end - start:.2f}秒')
        return result

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        """
        异步装饰器
        :param args:
        :param kwargs:
        :return:
        """
        start: float = time.time()
        result = await func(*args, **kwargs)
        end: float = time.time()
        print(f'{func.__name__}函数耗时:{end - start:.2f}秒')
        return result

    # 根据函数类型返回不同的wrapper
    if inspect.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper

@uinversal
def sync_download(file_name):
    """
    同步下载文件
    :param file_name: 文件名
    :return:
    """
    print(f"\n开始下载文件{file_name}")
    time.sleep(random.randint(1, 5))
    print(f"\n下载文件{file_name}完成")

@uinversal
async def async_download(file_name):
    """
    异步下载文件
    :param file_name: 文件名
    :return:
    """
    print(f"\n开始下载文件{file_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"\n下载文件{file_name}完成")

sync_download('test.txt')
asyncio.run(async_download('test.txt'))
