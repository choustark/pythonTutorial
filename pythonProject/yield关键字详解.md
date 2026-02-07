# Python yield 关键字完全指南

> 从基础到实战，全面掌握 yield 和生成器

---

## 📋 目录

- [1. yield 是什么](#1-yield-是什么)
- [2. 普通生成器](#2-普通生成器)
- [3. 异步生成器](#3-异步生成器)
- [4. yield 工作原理](#4-yield-工作原理)
- [5. 对比：return vs yield](#5-对比return-vs-yield)
- [6. 实际应用场景](#6-实际应用场景)
- [7. AgentScope 中的应用](#7-agentscope-中的应用)
- [8. 高级特性](#8-高级特性)
- [9. 练习题及答案](#9-练习题及答案)
- [10. 最佳实践](#10-最佳实践)

---

## 1. yield 是什么

### 1.1 基本概念

`yield` 是一个关键字，用于将一个**函数变成生成器**。

```python
# 普通函数
def normal_function():
    return 1
    return 2  # 永远不会执行

# 生成器函数
def generator_function():
    yield 1
    yield 2  # 会执行
```

### 1.2 核心作用

```
yield 的三个核心作用：
┌─────────────────────────────────────────────────────┐
│                                                     │
│  1. 产出（Yield）                                    │
│     → 向调用者返回一个值                              │
│                                                     │
│  2. 暂停（Pause）                                    │
│     → 保存当前函数状态                                │
│     → 保存所有局部变量                                │
│     → 记住执行位置                                    │
│                                                     │
│  3. 恢复（Resume）                                   │
│     → 下次调用时从暂停处继续                          │
│     → 恢复保存的状态                                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 1.3 return vs yield 对比

| 关键字 | 作用 | 返回方式 | 函数状态 |
|--------|------|----------|----------|
| `return` | 函数结束，返回值 | 一次性返回所有结果 | 调用后函数结束 |
| `yield` | 函数暂停，返回一个值 | 逐步返回多个值 | 暂停并保存状态 |

### 1.4 简单示例

```python
def count_up_to(n):
    """生成器：逐个返回数字"""
    for i in range(n):
        yield i

# 使用
for num in count_up_to(5):
    print(num)

# 输出：
# 0
# 1
# 2
# 3
# 4
```

---

## 2. 普通生成器

### 2.1 基础示例对比

```python
# ========== 使用 return ==========
def get_numbers_return(n):
    """一次性返回所有数字"""
    result = []
    for i in range(n):
        result.append(i)
    return result

numbers = get_numbers_return(3)
print(numbers)  # [0, 1, 2]
print(type(numbers))  # <class 'list'>


# ========== 使用 yield ==========
def get_numbers_yield(n):
    """逐个返回数字"""
    for i in range(n):
        yield i

numbers_gen = get_numbers_yield(3)
print(numbers_gen)  # <generator object get_numbers_yield at 0x...>
print(type(numbers_gen))  # <class 'generator'>

# 通过迭代获取值
for num in numbers_gen:
    print(num)
# 输出：
# 0
# 1
# 2
```

### 2.2 执行流程详解

```python
def my_generator():
    """演示生成器的执行流程"""
    print("步骤 1: 第一次调用")
    yield 10
    print("步骤 2: 第二次调用")
    yield 20
    print("步骤 3: 第三次调用")
    yield 30
    print("步骤 4: 函数结束")

# 创建生成器
gen = my_generator()

# 第一次迭代
print("获取第一个值:", next(gen))
# 输出：
# 步骤 1: 第一次调用
# 获取第一个值: 10

# 第二次迭代
print("获取第二个值:", next(gen))
# 输出：
# 步骤 2: 第二次调用
# 获取第二个值: 20

# 第三次迭代
print("获取第三个值:", next(gen))
# 输出：
# 步骤 3: 第三次调用
# 获取第三个值: 30

# 第四次迭代（会抛出 StopIteration 异常）
try:
    print("获取第四个值:", next(gen))
except StopIteration:
    print("生成器已耗尽")
# 输出：
# 步骤 4: 函数结束
# 生成器已耗尽
```

### 2.3 生成器的状态

```python
def state_generator():
    """展示生成器如何保存状态"""
    counter = 0  # 局部变量
    multiplier = 2

    while counter < 5:
        print(f"  [内部] counter={counter}, multiplier={multiplier}")
        result = counter * multiplier
        counter += 1
        yield result

# 使用生成器
gen = state_generator()

print("第一次调用:")
value1 = next(gen)  # counter=0, result=0
print(f"  收到: {value1}\n")

print("第二次调用:")
value2 = next(gen)  # counter=1, result=2
print(f"  收到: {value2}\n")

print("第三次调用:")
value3 = next(gen)  # counter=2, result=4
print(f"  收到: {value3}\n")
```

**输出：**
```
第一次调用:
  [内部] counter=0, multiplier=2
  收到: 0

第二次调用:
  [内部] counter=1, multiplier=2
  收到: 2

第三次调用:
  [内部] counter=2, multiplier=2
  收到: 4
```

**关键点：** 生成器会保存 `counter` 和 `multiplier` 的状态，每次恢复时从上次停止的地方继续。

### 2.4 内存优势

```python
import sys

# ========== 使用 list ==========
def generate_list(n):
    """生成列表（占用大量内存）"""
    return [i for i in range(n)]

big_list = generate_list(1000000)
print(f"list 内存占用: {sys.getsizeof(big_list):,} 字节")
# 约 8,000,000 字节（8MB）


# ========== 使用 generator ==========
def generate_generator(n):
    """生成器（占用极少内存）"""
    for i in range(n):
        yield i

big_gen = generate_generator(1000000)
print(f"generator 内存占用: {sys.getsizeof(big_gen):,} 字节")
# 约 200 字节

# 对比：生成器内存占用是列表的 1/40000！
```

### 2.5 生成器的方法

```python
def demo_generator():
    """演示生成器的各种方法"""
    print("生成器创建")
    yield 1
    yield 2
    yield 3

gen = demo_generator()

# 1. next() - 获取下一个值
print(f"next(gen): {next(gen)}")  # 1

# 2. __next__() - 同 next()
print(f"gen.__next__(): {gen.__next__()}")  # 2

# 3. send() - 发送值到生成器
def receive_generator():
    """接收外部发送的值"""
    value = None
    while True:
        received = yield value
        if received is not None:
            value = received * 2

gen2 = receive_generator()
next(gen2)  # 启动生成器
print(f"gen2.send(5): {gen2.send(5)}")  # 10

# 4. throw() - 向生成器抛出异常
def error_generator():
    try:
        yield 1
        yield 2
    except ValueError:
        print("捕获到 ValueError")
        yield 3

gen3 = error_generator()
next(gen3)
print(f"gen3.throw(ValueError): {gen3.throw(ValueError)}")  # 3

# 5. close() - 关闭生成器
gen4 = demo_generator()
next(gen4)
gen4.close()
# 后续再调用 next(gen4) 会抛出 StopIteration
```

---

## 3. 异步生成器

### 3.1 基本语法

```python
import asyncio

# ========== 普通生成器 ==========
def counter(n):
    """普通生成器"""
    for i in range(n):
        yield i

# 使用
for num in counter(3):
    print(num)


# ========== 异步生成器 ==========
async def async_counter(n: int):
    """异步生成器"""
    for i in range(n):
        await asyncio.sleep(1)  # 异步等待
        yield i  # 异步产出值

# 使用（必须用 async for）
async def main():
    async for num in async_counter(3):
        print(f"数字: {num}")

asyncio.run(main())

# 输出：
# 数字: 0
# （等待1秒）
# 数字: 1
# （等待1秒）
# 数字: 2
```

### 3.2 异步生成器的特点

```python
import asyncio
import time

async def async_streaming_data(n):
    """异步流式生成数据"""
    for i in range(n):
        print(f"  [生成器] 正在生成第 {i} 个数据...")
        await asyncio.sleep(1)  # 模拟异步操作（如网络请求）
        yield i ** 2
        print(f"  [生成器] 第 {i} 个数据已发送")

async def process_stream():
    """处理异步流"""
    print("=== 开始处理流 ===")
    start_time = time.time()

    async for value in async_streaming_data(3):
        elapsed = time.time() - start_time
        print(f"  [消费者] 收到值: {value} (耗时: {elapsed:.1f}s)")

    print("=== 流处理完成 ===")

asyncio.run(process_stream())
```

**输出：**
```
=== 开始处理流 ===
  [生成器] 正在生成第 0 个数据...
  [消费者] 收到值: 0 (耗时: 1.0s)
  [生成器] 第 0 个数据已发送
  [生成器] 正在生成第 1 个数据...
  [消费者] 收到值: 1 (耗时: 2.0s)
  [生成器] 第 1 个数据已发送
  [生成器] 正在生成第 2 个数据...
  [消费者] 收到值: 4 (耗时: 3.0s)
  [生成器] 第 2 个数据已发送
=== 流处理完成 ===
```

### 3.3 async for 的等价写法

```python
import asyncio

async def async_counter(n):
    for i in range(n):
        await asyncio.sleep(1)
        yield i

async def main():
    gen = async_counter(3)

    # async for 的等价写法
    try:
        while True:
            # 获取下一个值（异步方式）
            i = await anext(gen)  # Python 3.10+
            print(f"值: {i}")
    except StopAsyncIteration:
        print("迭代结束")

asyncio.run(main())
```

### 3.4 异步生成器表达式

```python
import asyncio

# ========== 普通生成器表达式 ==========
# (x for x in range(10))

# ========== 异步生成器表达式 ==========
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

# 异步生成器表达式
async_gen = (x * 2 async for x in async_range(5))

async def main():
    async for value in async_gen:
        print(value)

asyncio.run(main())
```

---

## 4. yield 工作原理

### 4.1 状态机模型

```python
def state_machine_generator():
    """生成器本质上是一个状态机"""

    # 状态 1
    print("状态 1: 开始执行")
    yield "A"  # 暂点 1：保存状态，返回 "A"

    # 状态 2
    print("状态 2: 从暂停点恢复")
    yield "B"  # 暂点 2：保存状态，返回 "B"

    # 状态 3
    print("状态 3: 再次从暂停点恢复")
    yield "C"  # 暂点 3：保存状态，返回 "C"

    # 状态 4
    print("状态 4: 最后一次恢复，函数结束")

# 状态转换过程
gen = state_machine_generator()

print(">>> 第 1 次 next()")
value = next(gen)  # "A"
print(f"    返回: {value}\n")

print(">>> 第 2 次 next()")
value = next(gen)  # "B"
print(f"    返回: {value}\n")

print(">>> 第 3 次 next()")
value = next(gen)  # "C"
print(f"    返回: {value}\n")

print(">>> 第 4 次 next()")
try:
    next(gen)
except StopIteration:
    print("    StopIteration: 生成器已耗尽")
```

**输出：**
```
>>> 第 1 次 next()
状态 1: 开始执行
    返回: A

>>> 第 2 次 next()
状态 2: 从暂停点恢复
    返回: B

>>> 第 3 次 next()
状态 3: 再次从暂停点恢复
    返回: C

>>> 第 4 次 next()
状态 4: 最后一次恢复，函数结束
    StopIteration: 生成器已耗尽
```

### 4.2 执行流程可视化

```
┌──────────────────────────────────────────────────────────┐
│                    生成器执行流程                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  async def async_counter(3):                             │
│                                                          │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌──────┐ │
│  │ i = 0   │───>│ yield 0 │───>│ 暂停    │───>│ 等待 │ │
│  └─────────┘    └─────────┘    └─────────┘    └──────┘ │
│       │                              ↑                   │
│       │         ┌────────────┐       │                   │
│       └─────────│ 恢复执行    │───────┘                   │
│                 └────────────┘                           │
│                       │                                  │
│                       v                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│  │ i = 1   │───>│ yield 1 │───>│ 暂停    │              │
│  └─────────┘    └─────────┘    └─────────┘              │
│       │                      ↑                           │
│       └──────────────────────┘ (async for 继续请求)      │
│                       │                                  │
│                       v                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│  │ i = 2   │───>│ yield 2 │───>│ 暂停    │              │
│  └─────────┘    └─────────┘    └─────────┘              │
│                       │                                  │
│                       v                                  │
│                 ┌──────────┐                            │
│                 │ 循环结束  │                            │
│                 └──────────┘                            │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 4.3 保存的状态详解

```python
def detailed_state_generator():
    """详细展示生成器保存的状态"""

    # 局部变量 1
    counter = 0

    # 局部变量 2
    data_list = []

    # 局部变量 3
    multiplier = 2

    while counter < 4:
        print(f"\n[生成器内部]")
        print(f"  counter = {counter}")
        print(f"  data_list = {data_list}")
        print(f"  multiplier = {multiplier}")

        # 计算结果
        result = counter * multiplier

        # 更新状态
        data_list.append(result)
        counter += 1

        # 暂停并返回结果
        yield result

# 使用生成器
gen = detailed_state_generator()

print("=" * 50)
print("第 1 次调用 next(gen)")
print("=" * 50)
value1 = next(gen)
print(f"→ 返回值: {value1}")

print("\n" + "=" * 50)
print("第 2 次调用 next(gen)")
print("=" * 50)
value2 = next(gen)
print(f"→ 返回值: {value2}")

print("\n" + "=" * 50)
print("第 3 次调用 next(gen)")
print("=" * 50)
value3 = next(gen)
print(f"→ 返回值: {value3}")
```

**输出：**
```
==================================================
第 1 次调用 next(gen)
==================================================

[生成器内部]
  counter = 0
  data_list = []
  multiplier = 2
→ 返回值: 0

==================================================
第 2 次调用 next(gen)
==================================================

[生成器内部]
  counter = 1
  data_list = [0]
  multiplier = 2
→ 返回值: 2

==================================================
第 3 次调用 next(gen)
==================================================

[生成器内部]
  counter = 2
  data_list = [0, 2]
  multiplier = 2
→ 返回值: 4
```

### 4.4 调用栈对比

```python
# ========== 普通函数的调用栈 ==========
def normal_function_a():
    result = normal_function_b()
    return result

def normal_function_b():
    result = normal_function_c()
    return result

def normal_function_c():
    return 42

# 调用栈：A → B → C → 返回 → 返回 → 返回


# ========== 生成器的调用栈 ==========
def generator_a():
    yield from generator_b()

def generator_b():
    yield from generator_c()

def generator_c():
    yield 1
    yield 2
    yield 3

# 调用栈：
# 第 1 次 next：A → B → C → yield 1 → 暂停
# 第 2 次 next：从 C 恢复 → yield 2 → 暂停
# 第 3 次 next：从 C 恢复 → yield 3 → 暂停
# 第 4 次 next：从 C 恢复 → 结束 → 返回 B → 结束 → 返回 A → 结束
```

---

## 5. 对比：return vs yield

### 5.1 基本对比

```python
# ========== 使用 return ==========
def get_numbers_return(n):
    """一次性返回所有数据"""
    result = []
    for i in range(n):
        result.append(i)
    return result  # 函数结束，返回整个列表

numbers = get_numbers_return(3)
print(numbers)  # [0, 1, 2]
# 可以多次遍历
for num in numbers:
    print(num)
for num in numbers:  # 第二次遍历
    print(num)


# ========== 使用 yield ==========
def get_numbers_yield(n):
    """逐个返回数据"""
    for i in range(n):
        yield i  # 暂停，保持状态

numbers_gen = get_numbers_yield(3)
# 只能遍历一次
for num in numbers_gen:
    print(num)
# 再次遍历不会有输出（生成器已耗尽）
for num in numbers_gen:
    print(num)  # 什么都不输出
```

### 5.2 详细对比表

| 特性 | return | yield |
|:------|:-------|:-------|
| **返回方式** | 一次性返回所有值 | 逐个返回值 |
| **函数状态** | 调用后函数结束 | 暂停并保存状态 |
| **内存占用** | 需要存储所有结果 | 每次只生成一个值 |
| **可迭代性** | 返回列表/元组等 | 返回生成器对象 |
| **重新遍历** | 结果可多次遍历 | 只能遍历一次 |
| **惰性求值** | ❌ 立即计算 | ✅ 按需计算 |
| **无限序列** | ❌ 不可能 | ✅ 可以 |
| **适用场景** | 数据量小，需要多次访问 | 数据量大，流式处理 |

### 5.3 性能对比

```python
import time
import sys

# ========== return 版本 ==========
def fetch_all_data():
    """一次性获取所有数据"""
    print("开始获取所有数据...")
    time.sleep(3)  # 模拟耗时操作
    data = [i for i in range(1000000)]
    print("所有数据获取完成！")
    return data

def test_return():
    start = time.time()
    all_data = fetch_all_data()  # 等待 3 秒

    process_start = time.time()
    for item in all_data[:5]:  # 只处理前 5 个
        print(f"处理: {item}")
    process_end = time.time()

    total = time.time() - start
    process_time = process_end - process_start
    wait_time = total - process_time

    print(f"\n总耗时: {total:.2f} 秒")
    print(f"  等待数据: {wait_time:.2f} 秒")
    print(f"  处理数据: {process_time:.2f} 秒")
    print(f"内存占用: {sys.getsizeof(all_data):,} 字节")

test_return()

# 输出：
# 开始获取所有数据...
# 所有数据获取完成！
# 处理: 0
# 处理: 1
# 处理: 2
# 处理: 3
# 处理: 4
#
# 总耗时: 3.01 秒
#   等待数据: 3.00 秒
#   处理数据: 0.01 秒
# 内存占用: 8,000,056 字节


# ========== yield 版本 ==========
import asyncio

async def fetch_data_stream():
    """流式获取数据"""
    for i in range(1000000):
        if i == 0:
            await asyncio.sleep(0.01)  # 只在开始时等待
        if i < 5:
            yield i  # 只生成前 5 个

async def test_yield():
    start = time.time()

    count = 0
    async for item in fetch_data_stream():
        print(f"处理: {item}")
        count += 1
        if count >= 5:
            break

    total = time.time() - start
    print(f"\n总耗时: {total:.2f} 秒")
    print(f"  立即开始处理，无需等待所有数据")
    print(f"内存占用: 极小（生成器对象）")

asyncio.run(test_yield())

# 输出：
# 处理: 0
# 处理: 1
# 处理: 2
# 处理: 3
# 处理: 4
#
# 总耗时: 0.02 秒
#   立即开始处理，无需等待所有数据
# 内存占用: 极小（生成器对象）
```

### 5.4 用户体验对比

```python
import asyncio

# ========== return 版本：用户需要等待 ==========
async def chat_return():
    """一次性返回所有响应"""
    print("用户: 你好")
    await asyncio.sleep(3)  # 模拟生成响应
    print("Agent: 你好！我是AI助手，有什么可以帮助你的吗？")
    # 用户等待了 3 秒才看到响应

# ========== yield 版本：流式输出 ==========
async def chat_yield():
    """流式返回响应"""
    print("用户: 你好")
    print("Agent: ", end="", flush=True)

    response_parts = ["你好", "！", "我是", "AI", "助手", "，", "有什么", "可以", "帮助", "你的", "吗", "？"]

    for part in response_parts:
        await asyncio.sleep(0.25)  # 每个字的延迟
        print(part, end="", flush=True)  # 逐字输出

    print()  # 换行

asyncio.run(chat_yield())

# 用户体验：立即看到第一个字，逐字显示，类似 ChatGPT
```

---

## 6. 实际应用场景

### 6.1 大文件处理

```python
def read_large_file(filename):
    """逐行读取大文件，避免内存溢出"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()  # 每次只处理一行

# 使用
for line in read_large_file("huge_file.txt"):
    process(line)  # 处理每一行

# 优点：
# 1. 不需要一次性加载整个文件到内存
# 2. 可以处理超过内存大小的文件
# 3. 可以立即开始处理第一行
```

### 6.2 数据库查询

```python
def fetch_records_from_db(query, batch_size=1000):
    """从数据库分批获取记录"""
    offset = 0

    while True:
        # 每次只查询一批数据
        cursor = db.execute(
            query + f" LIMIT {batch_size} OFFSET {offset}"
        )
        batch = cursor.fetchall()

        if not batch:
            break

        for record in batch:
            yield record

        offset += batch_size

# 使用
for record in fetch_records_from_db("SELECT * FROM users"):
    process(record)

# 优点：
# 1. 不会一次性加载百万条记录到内存
# 2. 网络传输更平滑
# 3. 可以立即处理第一批数据
```

### 6.3 API 分页请求

```python
import asyncio
import aiohttp

async def fetch_all_pages(base_url, per_page=100):
    """异步获取所有分页数据"""
    page = 1

    async with aiohttp.ClientSession() as session:
        while True:
            print(f"获取第 {page} 页...")

            # 请求当前页
            url = f"{base_url}?page={page}&per_page={per_page}"
            async with session.get(url) as response:
                data = await response.json()

            if not data['items']:  # 没有更多数据
                break

            # 产出当前页的每条数据
            for item in data['items']:
                yield item

            page += 1
            await asyncio.sleep(0.1)  # 避免请求过快

async def main():
    """处理所有分页数据"""
    async for item in fetch_all_pages("https://api.example.com/data"):
        print(f"处理: {item}")

asyncio.run(main())
```

### 6.4 生产者-消费者模式

```python
import asyncio
import random

async def data_producer(name, n):
    """数据生产者"""
    for i in range(n):
        delay = random.uniform(0.1, 0.5)
        await asyncio.sleep(delay)
        print(f"  [生产者 {name}] 生产: 数据 {i}")
        yield i

async def data_consumer(source, name):
    """数据消费者"""
    async for data in source:
        delay = random.uniform(0.1, 0.3)
        await asyncio.sleep(delay)
        print(f"  [消费者 {name}] 消费: {data}")

async def producer_consumer_pipeline():
    """连接生产者和消费者"""
    producer = data_producer("P1", 5)
    await data_consumer(producer, "C1")

asyncio.run(producer_consumer_pipeline())
```

**输出：**
```
  [生产者 P1] 生产: 数据 0
  [消费者 C1] 消费: 0
  [生产者 P1] 生产: 数据 1
  [消费者 C1] 消费: 1
  [生产者 P1] 生产: 数据 2
  [消费者 C1] 消费: 2
  ...
```

### 6.5 无限序列

```python
# ========== 斐波那契数列 ==========
def fibonacci():
    """生成无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用：获取前 10 个
fib = fibonacci()
for i, num in zip(range(10), fib):
    print(num)

# 输出：0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# ========== 质数生成器 ==========
def primes():
    """生成无限质数"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 使用：获取前 10 个质数
prime_gen = primes()
for i, prime in zip(range(10), prime_gen):
    print(prime)

# 输出：2, 3, 5, 7, 11, 13, 17, 19, 23, 29


# ========== 异步无限数据流 ==========
async def sensor_data():
    """模拟传感器数据流"""
    while True:
        await asyncio.sleep(1)
        yield random.uniform(20, 30)  # 温度数据

async def monitor_sensor():
    """监控传感器"""
    threshold = 28
    async for temp in sensor_data():
        status = "⚠️  高温" if temp > threshold else "✅ 正常"
        print(f"温度: {temp:.1f}°C {status}")

asyncio.run(monitor_sensor())
```

### 6.6 数据管道

```python
def read_words(filename):
    """读取文件中的单词"""
    with open(filename) as f:
        for line in f:
            for word in line.split():
                yield word

def filter_stop_words(words, stop_words):
    """过滤停用词"""
    for word in words:
        if word.lower() not in stop_words:
            yield word

def count_words(words):
    """统计词频"""
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        yield word, word_count[word]

# 使用管道
stop_words = {'the', 'a', 'an', 'and', 'or', 'but'}

pipeline = count_words(
    filter_stop_words(
        read_words('text.txt'),
        stop_words
    )
)

for word, count in pipeline:
    print(f"{word}: {count}")
```

---

## 7. AgentScope 中的应用

### 7.1 流式输出响应

```python
from agentscope.pipeline import stream_printing_messages
from agentscope.agent import ReActAgent

async def query_agent(agent, user_message):
    """流式获取 Agent 响应"""

    # stream_printing_messages 是一个异步生成器
    async for msg, last in stream_printing_messages(
        agents=[agent],
        coroutine_task=agent(user_message),
    ):
        # msg: 当前消息片段
        # last: 是否是最后一条（True 表示结束）

        text = msg.get_text_content()
        print(text, end="", flush=True)

        if last:
            print("\n（响应完成）")
```

**工作原理：**

```
用户: "介绍一下 AgentScope"
    ↓
Agent 开始处理
    ↓
┌────────────────────────────────────────┐
│  yield "AgentScope 是"                  │ → 用户看到
├────────────────────────────────────────┤
│  yield "一个由"                          │ → 用户看到
├────────────────────────────────────────┤
│  yield "阿里巴巴"                        │ → 用户看到
├────────────────────────────────────────┤
│  yield "开发的"                          │ → 用户看到
├────────────────────────────────────────┤
│  yield "多智能体框架"                    │ → 用户看到
└────────────────────────────────────────┘
    ↓
响应完成
```

### 7.2 实现流式输出

```python
import asyncio

async def streaming_agent_response(prompt):
    """模拟 Agent 流式响应"""

    # 模拟分词或分段生成
    response_parts = [
        "你好！",
        "我是",
        "AgentScope",
        "助手。",
        "有什么",
        "可以帮助",
        "你的吗？"
    ]

    for part in response_parts:
        await asyncio.sleep(0.3)  # 模拟生成延迟
        yield part

async def chat_with_agent():
    """与 Agent 对话"""
    print("用户: 你好")
    print("Agent: ", end="", flush=True)

    async for chunk in streaming_agent_response("你好"):
        print(chunk, end="", flush=True)  # 逐字输出

    print()  # 换行

asyncio.run(chat_with_agent())
```

**输出：**
```
用户: 你好
Agent: 你好！我是AgentScope助手。有什么可以帮助你的吗？
（逐字显示，类似 ChatGPT）
```

### 7.3 完整的 AgentScope 查询示例

```python
from agentscope.agent import ReActAgent
from agentscope.pipeline import stream_printing_messages
from agentscope_runtime.engine import AgentApp

agent_app = AgentApp(
    app_name="MyAgent",
    app_description="流式响应的 AI 助手",
)

@agent_app.query(framework="agentscope")
async def query_func(self, msgs, request=None, **kwargs):
    """Agent 查询处理函数 - 流式输出版本"""

    # 1. 创建或获取 Agent
    agent = ReActAgent(
        name="assistant",
        model=self.model,
        memory=self.memory,
        ...

    # 2. 流式输出响应
    async for msg, last in stream_printing_messages(
        agents=[agent],
        coroutine_task=agent(msgs),
    ):
        # 每次生成一段就 yield 出去
        yield msg, last

        # last=False: 还有更多内容
        # last=True: 这是最后一段

    # 3. 保存状态（用于多轮对话）
    state = agent.state_dict()
    await self.state_service.save_state(
        user_id=request.user_id,
        session_id=request.session_id,
        state=state,
    )
```

### 7.4 多 Agent 流式对话

```python
from agentscope.pipeline import MsgHub
from agentscope.message import Msg

async def multi_agent_streaming_chat():
    """多智能体流式对话"""

    # 创建多个 Agent
    alice = ReActAgent(name="Alice", ...)
    bob = ReActAgent(name="Bob", ...)
    charlie = ReActAgent(name="Charlie", ...)

    # 使用 MsgHub 管理对话
    async with MsgHub(
        participants=[alice, bob, charlie],
        announcement=Msg("Host", "开始讨论", "assistant")
    ) as hub:
        # 每个 Agent 的响应都是流式的
        async for msg, last in hub.broadcast_streaming(
            Msg("Host", "请发表意见", "assistant")
        ):
            # 逐段显示每个 Agent 的响应
            print(f"[{msg.name}]: ", end="")
            print(msg.content, end="", flush=True)

            if last:
                print()  # 换行
```

---

## 8. 高级特性

### 8.1 yield from（委托生成器）

```python
# ========== 基础示例 ==========
def sub_generator():
    """子生成器"""
    yield 1
    yield 2

def main_generator():
    """主生成器"""
    yield from sub_generator()  # 委托给子生成器
    yield 3

for num in main_generator():
    print(num)

# 输出：1, 2, 3


# ========== 等价写法 ==========
def main_generator_manual():
    """手动实现 yield from 的功能"""
    for value in sub_generator():
        yield value
    yield 3


# ========== 实际应用 ==========
def flatten(nested_list):
    """展平嵌套列表"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # 递归展平
        else:
            yield item

nested = [1, [2, [3, 4]], 5, [6, [7, 8]]]
for item in flatten(nested):
    print(item, end=" ")

# 输出：1 2 3 4 5 6 7 8
```

### 8.2 生成器协程（send 方法）

```python
def interactive_generator():
    """可以接收输入的生成器"""
    received = None
    while True:
        received = yield received
        if received is None:
            received = 0

gen = interactive_generator()

# 必须先启动生成器
next(gen)  # 或 gen.send(None)

# 发送值到生成器
print(gen.send(10))  # 输出: 10
print(gen.send(20))  # 输出: 20
print(gen.send(30))  # 输出: 30
```

### 8.3 生成器异常处理（throw 方法）

```python
def error_handling_generator():
    """可以处理异常的生成器"""
    try:
        yield 1
        yield 2
    except ValueError as e:
        print(f"生成器捕获异常: {e}")
        yield 3
    finally:
        print("生成器清理")

gen = error_handling_generator()
print(next(gen))  # 1
print(gen.throw(ValueError, "测试异常"))  # 3
```

### 8.4 生成器关闭（close 方法）

```python
def cleanup_generator():
    """需要清理的生成器"""
    try:
        print("生成器启动")
        yield 1
        yield 2
        print("这行不会执行")
    finally:
        print("生成器清理完成")

gen = cleanup_generator()
print(next(gen))  # 1
gen.close()  # 关闭生成器
# 会执行 finally 块
```

---

## 9. 练习题及答案

### 练习 1：基础生成器

**题目：** 实现一个生成器，生成指定范围内的所有偶数。

```python
def even_numbers(start, end):
    """生成 [start, end] 范围内的所有偶数"""
    # TODO: 实现这个函数
```

**答案：**

```python
def even_numbers(start, end):
    """生成 [start, end] 范围内的所有偶数"""
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

# 测试
for num in even_numbers(1, 10):
    print(num)

# 输出：2, 4, 6, 8, 10
```

---

### 练习 2：斐波那契数列生成器

**题目：** 实现一个生成器，生成前 n 个斐波那契数。

```python
def fibonacci(n):
    """生成前 n 个斐波那契数"""
    # TODO: 实现这个函数
```

**答案：**

```python
def fibonacci(n):
    """生成前 n 个斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 测试
for num in fibonacci(10):
    print(num)

# 输出：0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

---

### 练习 3：异步计数器

**题目：** 实现一个异步生成器，每秒生成一个递增数字。

```python
import asyncio

async def async_counter(start, end, interval=1):
    """异步生成器，每 interval 秒生成一个数字"""
    # TODO: 实现这个函数
```

**答案：**

```python
import asyncio

async def async_counter(start, end, interval=1):
    """异步生成器，每 interval 秒生成一个数字"""
    for num in range(start, end + 1):
        await asyncio.sleep(interval)
        yield num

async def test():
    async for num in async_counter(1, 5, 0.5):
        print(f"数字: {num}")

asyncio.run(test())

# 输出：
# 数字: 1 (等待 0.5 秒)
# 数字: 2 (等待 0.5 秒)
# 数字: 3 (等待 0.5 秒)
# 数字: 4 (等待 0.5 秒)
# 数字: 5 (等待 0.5 秒)
```

---

### 练习 4：流式文件处理

**题目：** 实现一个生成器，逐行读取文件并过滤空行。

```python
def non_empty_lines(filename):
    """逐行读取文件，跳过空行"""
    # TODO: 实现这个函数
```

**答案：**

```python
def non_empty_lines(filename):
    """逐行读取文件，跳过空行"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # 非空行
                yield line

# 测试
for line in non_empty_lines("test.txt"):
    print(line)
```

---

### 练习 5：批量数据处理器

**题目：** 实现一个生成器，将数据分批处理。

```python
def batch_processor(data, batch_size):
    """将数据分批产出"""
    # TODO: 实现这个函数
```

**答案：**

```python
def batch_processor(data, batch_size):
    """将数据分批产出"""
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        yield batch

# 测试
data = list(range(10))
for batch in batch_processor(data, 3):
    print(f"批次: {batch}")

# 输出：
# 批次: [0, 1, 2]
# 批次: [3, 4, 5]
# 批次: [6, 7, 8]
# 批次: [9]
```

---

### 练习 6：异步流式 API 请求

**题目：** 实现一个异步生成器，模拟分页 API 请求。

```python
import asyncio

async def fetch_paginated_data(base_url, max_pages=3):
    """异步获取分页数据"""
    # TODO: 实现这个函数
```

**答案：**

```python
import asyncio

async def fetch_paginated_data(base_url, max_pages=3):
    """异步获取分页数据"""
    for page in range(1, max_pages + 1):
        print(f"获取第 {page} 页...")
        await asyncio.sleep(1)  # 模拟网络请求

        # 模拟 API 响应
        data = {
            'page': page,
            'items': [
                {'id': (page - 1) * 10 + i}
                for i in range(1, 6)
            ]
        }

        for item in data['items']:
            yield item

async def test():
    async for item in fetch_paginated_data("https://api.example.com/data"):
        print(f"处理: {item}")

asyncio.run(test())

# 输出：
# 获取第 1 页...
# 处理: {'id': 1}
# 处理: {'id': 2}
# 处理: {'id': 3}
# 处理: {'id': 4}
# 处理: {'id': 5}
# 获取第 2 页...
# 处理: {'id': 11}
# ...
```

---

### 练习 7：链式生成器

**题目：** 实现一个数据管道，包含多个处理阶段。

```python
def read_data(filename):
    """读取数据"""
    # TODO: 实现这个函数

def filter_data(data, threshold):
    """过滤数据"""
    # TODO: 实现这个函数

def transform_data(data):
    """转换数据"""
    # TODO: 实现这个函数
```

**答案：**

```python
def read_data(filename):
    """从文件读取数据"""
    with open(filename, 'r') as f:
        for line in f:
            yield int(line.strip())

def filter_data(data, threshold):
    """过滤大于阈值的数据"""
    for value in data:
        if value > threshold:
            yield value

def transform_data(data):
    """对数据进行平方运算"""
    for value in data:
        yield value ** 2

# 创建数据管道
def process_pipeline(filename, threshold):
    """完整的数据处理管道"""
    data = read_data(filename)
    filtered = filter_data(data, threshold)
    transformed = transform_data(filtered)
    return transformed

# 测试
# 假设 data.txt 内容：
# 1
# 5
# 10
# 15
# 20

for result in process_pipeline("data.txt", 5):
    print(result)

# 输出：
# 100 (10^2)
# 225 (15^2)
# 400 (20^2)
```

---

## 10. 最佳实践

### 10.1 何时使用生成器

```python
# ✅ 适合使用生成器的场景
def use_generator_when():
    """
    1. 处理大量数据（内存有限）
    2. 流式处理（边生成边消费）
    3. 无限序列（斐波那契、质数等）
    4. 复杂的数据管道
    5. 需要惰性求值
    """

# ❌ 不适合使用生成器的场景
def use_list_when():
    """
    1. 需要多次遍历同一数据
    2. 数据量很小（内存不是问题）
    3. 需要随机访问（索引访问）
    4. 需要获取长度（len()）
    """
```

### 10.2 生成器命名

```python
# ✅ 好的命名：清晰表明是生成器
def user_ids():
    """生成用户 ID"""
    yield from get_user_ids()

def prime_numbers():
    """生成质数"""
    ...

# ❌ 不好的命名：无法判断是否为生成器
def get_users():
    """看起来像返回列表，实际是生成器"""
    yield ...

def users():
    """意图不明确"""
    ...
```

### 10.3 文档字符串

```python
def fibonacci_sequence(n):
    """生成前 n 个斐波那契数。

    这是一个生成器函数，使用 yield 逐个返回值。

    Args:
        n: 要生成的斐波那契数的数量

    Yields:
        int: 斐波那契数列中的下一个数字

    Example:
        >>> for num in fibonacci_sequence(5):
        ...     print(num)
        0
        1
        1
        2
        3
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 10.4 资源清理

```python
# ✅ 好的做法：使用 try-finally 确保清理
def safe_file_reader(filename):
    """安全地读取文件"""
    f = None
    try:
        f = open(filename, 'r')
        for line in f:
            yield line.strip()
    finally:
        if f:
            f.close()

# ✅ 更好的做法：使用上下文管理器
def safe_file_reader_v2(filename):
    """使用上下文管理器"""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()
```

### 10.5 避免常见陷阱

```python
# ========== 陷阱 1：生成器只能遍历一次 ==========
gen = (x for x in range(3))

list1 = list(gen)  # [0, 1, 2]
list2 = list(gen)  # [] 生成器已耗尽

# 解决方案：如果需要多次遍历，先转为列表
data = list(x for x in range(3))
list1 = list(data)  # [0, 1, 2]
list2 = list(data)  # [0, 1, 2]


# ========== 陷阱 2：在生成器中修改可变状态 ==========
def buggy_generator(items):
    """在迭代过程中修改列表"""
    for item in items:
        if item == 2:
            items.append(4)  # 危险！可能导致无限循环
        yield item

# 解决方案：避免修改原始数据
def safe_generator(items):
    """创建副本或避免修改"""
    items_copy = items.copy()
    for item in items_copy:
        yield item


# ========== 陷阱 3：忘记启动生成器 ==========
def counter():
    """计数生成器"""
    count = 0
    while True:
        received = yield count
        if received is not None:
            count = received

gen = counter()
# gen.send(10)  # ❌ 错误！必须先启动生成器

next(gen)  # ✅ 先启动
gen.send(10)  # ✅ 现在可以发送了
```

### 10.6 性能优化

```python
# ========== 使用生成器表达式 ==========
# ✅ 更简洁，更高效
sum(x * 2 for x in range(1000))

# ❌ 创建不必要的列表
sum([x * 2 for x in range(1000)])


# ========== 链式生成器 ==========
def pipeline_optimized():
    """优化的数据管道"""

    # ❌ 不优化：每个阶段创建中间列表
    data = range(1000)
    filtered = [x for x in data if x % 2 == 0]
    transformed = [x ** 2 for x in filtered]
    result = sum(transformed)

    # ✅ 优化：使用生成器链
    data = range(1000)
    result = sum(
        x ** 2
        for x in data
        if x % 2 == 0
    )


# ========== 使用 itertools ==========
import itertools

# ✅ 使用标准库工具
def count_up_from(n):
    """从 n 开始计数"""
    yield from itertools.count(n)

def take(n, iterable):
    """获取前 n 个元素"""
    return itertools.islice(iterable, n)
```

---

## ✅ 学习检查清单

完成以下检查项，确认你已掌握 yield 和生成器：

### 基础理解
- [ ] 理解 `yield` 将函数变成生成器
- [ ] 理解 `yield` 暂停函数并保存状态
- [ ] 理解 `yield` 与 `return` 的区别
- [ ] 知道如何使用生成器

### 生成器操作
- [ ] 能够使用 `next()` 获取值
- [ ] 理解 `for` 循环与生成器的关系
- [ ] 了解 `send()`、`throw()`、`close()` 方法
- [ ] 理解生成器的内存优势

### 异步生成器
- [ ] 理解 `async def` + `yield` 的语法
- [ ] 能够使用 `async for` 遍历异步生成器
- [ ] 理解 `anext()` 的作用
- [ ] 能够实现异步生成器

### 实际应用
- [ ] 能够处理大文件（逐行读取）
- [ ] 能够实现数据管道
- [ ] 理解 AgentScope 中的流式输出
- [ ] 能够实现分页数据获取

### 高级特性
- [ ] 理解 `yield from` 的作用
- [ ] 能够创建嵌套生成器
- [ ] 理解生成器的异常处理
- [ ] 了解生成器的最佳实践

---

## 📚 记忆口诀

```
yield 的三重奏：

1. 产出（Yield）  - 返回值给调用者
2. 暂停（Pause）  - 保存当前状态
3. 恢复（Resume） - 从暂停处继续

---

return vs yield：

return: 一次性返回，函数结束
yield:  产出并暂停，等待恢复

return: 立刻给你整个蛋糕
yield:  一片一片切给你

---

何时使用 yield：

大数据 → 用 yield（省内存）
小数据 → 用 list（方便）

无限流 → 用 yield（可以）
有限集 → 看需求

一次遍历 → 用 yield
多次遍历 → 用 list
```

---

## 📚 参考资源

- [Python 生成器 - 官方文档](https://docs.python.org/3.10/howto/functional.html#generators)
- [PEP 255 - Simple Generators](https://peps.python.org/pep-0255/)
- [PEP 342 - Coroutines via Enhanced Generators](https://peps.python.org/pep-0342/)
- [PEP 492 - Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
- [AgentScope 官方文档](https://doc.agentscope.io/)

---

**祝你学习顺利！🚀**
