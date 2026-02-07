# 我的 AgentScope 学习计划（定制版）

> 已掌握：Python 基础语法、类和对象、已安装 Python 3.10+ 和 AgentScope

---

## 📊 当前进度

✅ 已掌握的内容：
- [x] Python 基本语法
- [x] 类和对象的基本概念
- [x] Python 3.10+ 已安装
- [x] AgentScope 已安装

---

## 🎯 需要学习的内容（按优先级排序）

### 优先级 1：异步编程 ⭐⭐⭐

这是 AgentScope 的**核心**，必须先掌握！

#### 学习清单

- [ ] `async def` 定义异步函数
- [ ] `await` 等待异步操作
- [ ] `asyncio.run()` 运行异步程序
- [ ] `async with` 异步上下文管理器
- [ ] `async for` 异步迭代

#### 快速练习

```python
import asyncio

# 练习1：基础异步函数
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# 练习2：运行异步函数
asyncio.run(say_hello())

# 练习3：异步上下文管理器
class AsyncResource:
    async def __aenter__(self):
        print("Resource opened")
        return self

    async def __aexit__(self, *args):
        print("Resource closed")

async def practice_context():
    async with AsyncResource() as r:
        print("Using resource")

# 练习4：异步迭代
async def async_counter(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def practice_iteration():
    async for num in async_counter(3):
        print(num)
```

#### 学习资源

- [Python asyncio 官方文档](https://docs.python.org/3.10/library/asyncio.html)
- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)

---

### 优先级 2：装饰器

AgentScope 用 `@agent_app.init`、`@agent_app.query` 等装饰器注册函数。

#### 学习清单

- [ ] `@` 装饰器语法
- [ ] 装饰器的工作原理
- [ ] 带参数的装饰器
- [ ] 类装饰器

#### 快速练习

```python
# 练习1：基础装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 完成")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

# 测试
print(greet("AgentScope"))

# 练习2：带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    return "Hi!"

# 测试
print(say_hi())  # ['Hi!', 'Hi!', 'Hi!']
```

---

### 优先级 3：上下文管理器 & 生成器

用于 AgentScope 的 `MsgHub` 和流式输出。

#### 学习清单

- [ ] `with` 语句和上下文管理器
- [ ] `__enter__` 和 `__exit__` 方法
- [ ] `yield` 生成器
- [ ] 异步生成器

#### 快速练习

```python
# 练习1：上下文管理器
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, *args):
        if self.file:
            self.file.close()

# 使用
with FileManager("test.txt") as f:
    f.write("Hello!")

# 练习2：生成器
def count_up_to(n):
    count = 0
    while count < n:
        yield count
        count += 1

for i in count_up_to(5):
    print(i)

# 练习3：异步生成器
async def async_count(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for num in async_count(3):
        print(num)

asyncio.run(main())
```

---

### 优先级 4：环境变量 & HTTP API

配置管理和 API 调用。

#### 学习清单

- [ ] `os.getenv()` 读取环境变量
- [ ] `.env` 文件和 `python-dotenv`
- [ ] `requests` 或 `httpx` 发送 HTTP 请求
- [ ] JSON 数据处理

#### 快速练习

```python
import os
import requests

# 练习1：读取环境变量
api_key = os.getenv("MY_API_KEY", "default_value")
print(f"API Key: {api_key}")

# 练习2：设置环境变量
os.environ["TEST_VAR"] = "test_value"
print(os.getenv("TEST_VAR"))

# 练习3：HTTP GET 请求
response = requests.get("https://api.github.com")
print(f"状态码: {response.status_code}")
print(f"JSON: {response.json()}")

# 练习4：HTTP POST 请求
data = {"message": "Hello from Python"}
response = requests.post(
    "https://httpbin.org/post",
    json=data
)
print(response.json())
```

---

### 优先级 5：类型注解

提高代码可读性（AgentScope 代码中大量使用）。

#### 学习清单

- [ ] 函数参数和返回值类型注解
- [ ] `typing` 模块
- [ ] Optional、List、Dict

#### 快速练习

```python
from typing import List, Dict, Optional, Union

# 练习1：基础类型注解
def add(a: int, b: int) -> int:
    return a + b

# 练习2：复杂类型注解
def process_items(
    items: List[str],
    config: Optional[Dict] = None
) -> Dict[str, Union[str, int]]:
    if config is None:
        config = {}
    return {"result": ",".join(items), "count": len(items)}

# 测试
result = process_items(["a", "b", "c"])
print(result)
```

---

### 优先级 6：AgentScope 工具注册

将函数注册为 Agent 可调用的工具。

#### 学习清单

- [ ] Toolkit 的使用
- [ ] `register_tool_function()` 方法
- [ ] 工具函数的定义规范

#### 快速练习

```python
from agentscope.tool import Toolkit

# 定义工具函数
def get_weather(city: str) -> str:
    """获取指定城市的天气

    Args:
        city: 城市名称

    Returns:
        天气信息字符串
    """
    return f"{city}今天天气晴朗，温度25°C"

# 创建工具包并注册
toolkit = Toolkit()
toolkit.register_tool_function(get_weather)

# 查看已注册的工具
print(f"已注册工具: {toolkit.tools}")

# 在 Agent 中使用
from agentscope.agent import ReActAgent

agent = ReActAgent(
    name="weather_assistant",
    toolkit=toolkit,
    ...
)
```

---

## 📅 定制学习计划（4 周）

### 第 1 周：异步编程（重中之重）

| 任务 | 内容 |
|------|------|
| Day 1-2 | async/await 基础语法 |
| Day 3-4 | asyncio 模块 |
| Day 5-6 | 异步上下文管理器和迭代器 |
| Day 7 | AgentScope 异步代码实践 |

### 第 2 周：装饰器 & 上下文管理器

| 任务 | 内容 |
|------|------|
| Day 1-3 | 装饰器（基础到进阶） |
| Day 4-5 | 上下文管理器 |
| Day 6-7 | 生成器和异步生成器 |

### 第 3 周：实用技能

| 任务 | 内容 |
|------|------|
| Day 1-2 | 环境变量和配置管理 |
| Day 3-4 | HTTP API 调用 |
| Day 5 | JSON 处理 |
| Day 6-7 | 类型注解 |

### 第 4 周：AgentScope 实战

| 任务 | 内容 |
|------|------|
| Day 1-2 | 工具函数注册 |
| Day 3-4 | 创建多智能体对话 |
| Day 5-6 | 部署 Agent 服务 |
| Day 7 | 完整项目实践 |

---

## ✅ 今日快速测试

验证你对已有知识的掌握，并开始学习异步编程：

```python
import asyncio
import os

# 测试1：类和对象（已掌握）
class Agent:
    def __init__(self, name):
        self.name = name

    def __call__(self, message):
        return f"{self.name}: {message}"

agent = Agent("Test")
print(agent("Hello"))  # 应该输出: Test: Hello

# 测试2：异步编程（开始学习）
async def async_test():
    print("开始")
    await asyncio.sleep(1)
    print("结束")

asyncio.run(async_test())

# 测试3：环境变量
os.environ["TEST"] = "value"
print(os.getenv("TEST"))  # 应该输出: value
```

---

## 🎓 下一步

1. **今天就开始**：学习异步编程（优先级1）
2. **复制上面的代码**：运行并理解每一行
3. **完成练习**：确保理解 async/await
4. **明天继续**：学习装饰器

准备好了吗？让我们从异步编程开始！ 🚀
