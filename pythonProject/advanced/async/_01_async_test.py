import asyncio
import time

'''
三个关键字
async def -> 定义异步函数
await     -> 等待异步操作完成
asyncio.run -> 运行异步程序
'''


async def hello():
    print("\n 1. 开始")
    # 暂停两秒
    await asyncio.sleep(2)
    print("\n 2. 结束")


# 运行异步函数
# asyncio.run(hello())


print("\n-----" * 10)
print("同步和异步对比")


# 同步
def sync_hello():
    print("\n 同步. 开始")
    time.sleep(2)
    print("\n 同步. 结束")


# 异步
async def async_hello():
    print("\n 异步. 1.开始")
    await asyncio.sleep(10)
    print("\n 异步. 2.结束")


# 运行
print("========同步执行=======")
# sync_hello()
# 异步
print("========异步执行=======")
# asyncio.run(async_hello())

print("-----" * 10)


async def task(name: str, delay: int):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 结束")


async def main():
    results = await asyncio.gather(
        task("任务1", 10),
        task("任务2", 5),
        task("任务3", 7),
        task("任务4", 9),
        task("任务5", 6),
    )
    print(f"所有任务执行完成:{results}")


# asyncio.run(main())

print("-----" * 10)


# 异步上下文管理器 (async with)

class AsyncContextManager:
    async def __aenter__(self):
        print("__aenter__")
        await asyncio.sleep(1)  # 模拟打开耗时
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("__aexit__")  # 模拟关闭耗时
        await asyncio.sleep(1)


async def use_resource():
    async with AsyncContextManager() as resource:
        print("使用资源")
        await asyncio.sleep(2)


asyncio.run(use_resource())


# 异步迭代器
async def async_counter(n: int):
    '''异步生成器'''
    for i in range(n):
        await asyncio.sleep(10)
        yield i


async def main1():
    async for i in async_counter(5):
        print(f'数字：{i}')

asyncio.run(main1())
