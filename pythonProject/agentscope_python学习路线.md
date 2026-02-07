# AgentScope Python 学习路线

> 基于 AgentScope 开发多智能体应用所需掌握的 Python 核心知识点

---

## 📋 目录

- [1. Python 基础](#1-python-基础)
- [2. 异步编程](#2-异步编程)
- [3. 面向对象编程](#3-面向对象编程)
- [4. 装饰器](#4-装饰器)
- [5. 类型注解](#5-类型注解)
- [6. 上下文管理器](#6-上下文管理器)
- [7. 生成器和迭代器](#7-生成器和迭代器)
- [8. 环境变量和配置](#8-环境变量和配置)
- [9. HTTP 和 API 调用](#9-http-和-api-调用)
- [10. 工具函数注册](#10-工具函数注册)
- [学习路线建议](#学习路线建议)
- [快速验证](#快速验证)

---

## 1. Python 基础

### 必须掌握

| 知识点 | 说明 | AgentScope 中的应用 |
|--------|------|-------------------|
| **Python 3.10+ 语法** | 框架最低要求 | match-case 语句等新特性 |
| **变量和数据类型** | 基础语法 | 字符串、数字、布尔值 |
| **控制流** | 程序逻辑 | if/else、for/while 循环 |
| **函数定义** | 代码复用 | def、参数、返回值 |
| **列表和字典** | 数据结构 | 存储配置、消息等 |
| **模块导入** | 代码组织 | import、from...import |

### 代码示例

```python
# 基础语法示例
def greet(name: str) -> str:
    """简单的问候函数"""
    return f"Hello, {name}!"

# 使用
message = greet("AgentScope")
print(message)
```

---

## 2. 异步编程 ⭐ 重点！

这是 AgentScope 的**核心**，几乎所有示例都使用 `async/await`。

### 需要学习的内容

- `async def` 定义异步函数
- `await` 等待异步操作完成
- `asyncio.run()` 运行异步程序
- 异步上下文管理器 (`async with`)
- 异步迭代器 (`async for`)
- 并发任务 (`asyncio.gather`)

### AgentScope 代码示例

```python
import asyncio
from agentscope.agent import ReActAgent
from agentscope.model import DashScopeChatModel

async def main():
    """AgentScope 标准异步入口"""
    agent = ReActAgent(
        name="assistant",
        model=DashScopeChatModel(...),
    )

    # await 等待异步响应
    response = await agent("Hello!")
    print(response)

# 运行异步程序
asyncio.run(main())
```

### 学习要点

```python
# 异步函数定义
async def fetch_data():
    await asyncio.sleep(1)  # 模拟异步操作
    return "data"

# 异步上下文管理器
async with some_resource() as resource:
    await resource.process()

# 异步迭代
async for item in async_iterator:
    print(item)

# 并发执行多个任务
results = await asyncio.gather(
    fetch_data(),
    fetch_data(),
    fetch_data()
)
```

---

## 3. 面向对象编程 (OOP)

AgentScope 大量使用类和对象模式。

### 需要学习的内容

- 类的定义和实例化
- `__init__` 构造方法
- `__call__` 可调用对象
- 继承和多态
- 属性和方法

### AgentScope 代码示例

```python
from agentscope.agent import ReActAgent

# AgentScope 使用类定义 Agent
class ReActAgent:
    def __init__(self, name, model, sys_prompt=None):
        """初始化 Agent"""
        self.name = name
        self.model = model
        self.sys_prompt = sys_prompt

    def __call__(self, msg):
        """使对象可调用"""
        # 处理消息的逻辑
        return response

# 使用
agent = ReActAgent(name="Friday", model=...)
response = agent("Hello!")  # 调用 __call__ 方法
```

### 学习要点

```python
# 类的基本结构
class Agent:
    def __init__(self, name):
        self.name = name  # 实例属性

    def __call__(self, message):
        return f"{self.name}: {message}"

    def process(self, data):
        """普通方法"""
        pass

# 继承
class CustomAgent(Agent):
    def process(self, data):
        # 重写父类方法
        super().process(data)
```

---

## 4. 装饰器

AgentScope 使用装饰器注册生命周期钩子和查询函数。

### 需要学习的内容

- `@` 装饰器语法
- 装饰器的工作原理
- 带参数的装饰器
- 自定义装饰器

### AgentScope 代码示例

```python
from agentscope_runtime.engine import AgentApp
from agentscope_runtime.engine.schemas.agent_schemas import AgentRequest

agent_app = AgentApp(
    app_name="Friday",
    app_description="A helpful assistant",
)

# 初始化钩子
@agent_app.init
async def init_func(self):
    self.state_service = InMemoryStateService()
    await self.state_service.start()

# 关闭钩子
@agent_app.shutdown
async def shutdown_func(self):
    await self.state_service.stop()

# 查询处理函数
@agent_app.query(framework="agentscope")
async def query_func(self, msgs, request: AgentRequest = None, **kwargs):
    # 处理查询逻辑
    yield response, False
```

### 学习要点

```python
# 基础装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")
```

---

## 5. 类型注解

代码中大量使用类型提示以提高代码可读性。

### 需要学习的内容

- 类型注解语法
- `typing` 模块
- 泛型
- Optional、List、Dict 等

### AgentScope 代码示例

```python
from typing import Optional, List, Dict
from agentscope_runtime.engine.schemas.agent_schemas import AgentRequest

@agent_app.query(framework="agentscope")
async def query_func(
    self,
    msgs,                          # 参数
    request: AgentRequest = None,   # 带类型注解的参数
    **kwargs,
) -> None:                         # 返回类型注解
    """查询处理函数"""
    session_id: str = request.session_id
    user_id: str = request.user_id
```

### 学习要点

```python
# 基础类型注解
def add(a: int, b: int) -> int:
    return a + b

# typing 模块
from typing import List, Dict, Optional, Union

def process_data(
    items: List[str],
    config: Optional[Dict] = None
) -> Union[str, int]:
    if config is None:
        config = {}
    # 处理逻辑
    return "result"

# 泛型
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = T
```

---

## 6. 上下文管理器

用于资源管理，确保资源正确释放。

### 需要学习的内容

- `with` 语句
- `__enter__` 和 `__exit__` 方法
- 异步上下文管理器 (`async with`)

### AgentScope 代码示例

```python
from agentscope.pipeline import MsgHub
from agentscope.message import Msg

async def multi_agent_conversation():
    agent1 = ...
    agent2 = ...
    agent3 = ...

    # 使用上下文管理器管理多智能体对话
    async with MsgHub(
        participants=[agent1, agent2, agent3],
        announcement=Msg("Host", "Introduce yourselves.", "assistant")
    ) as hub:
        # 对话逻辑
        await hub.broadcast(Msg("Host", "Goodbye!", "assistant"))
```

### 学习要点

```python
# 自定义上下文管理器
class ResourceManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        # 清理资源

# 使用
with ResourceManager() as resource:
    # 使用资源
    pass

# 异步上下文管理器
class AsyncResourceManager:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 清理资源
        pass

async with AsyncResourceManager() as resource:
    # 使用资源
    pass
```

---

## 7. 生成器和迭代器

用于流式输出和数据处理。

### 需要学习的内容

- `yield` 关键字
- 生成器函数
- 生成器表达式
- `async for` 异步迭代

### AgentScope 代码示例

```python
from agentscope.pipeline import stream_printing_messages

@agent_app.query(framework="agentscope")
async def query_func(self, msgs, request: AgentRequest = None, **kwargs):
    agent = ReActAgent(...)

    # 流式输出响应
    async for msg, last in stream_printing_messages(
        agents=[agent],
        coroutine_task=agent(msgs),
    ):
        yield msg, last  # 生成器模式
```

### 学习要点

```python
# 生成器函数
def count_up_to(n):
    count = 0
    while count < n:
        yield count
        count += 1

# 使用
for i in count_up_to(5):
    print(i)

# 生成器表达式
squares = (x**2 for x in range(10))

# 异步生成器
async def async_counter(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async for value in async_counter(5):
    print(value)
```

---

## 8. 环境变量和配置

管理 API 密钥和配置信息。

### 需要学习的内容

- `os` 模块
- `os.environ` 和 `os.getenv()`
- `.env` 文件管理
- `python-dotenv` 库

### AgentScope 代码示例

```python
import os

# 获取环境变量
api_key = os.getenv("DASHSCOPE_API_KEY")

# 在 AgentScope 中使用
agent = ReActAgent(
    name="Friday",
    model=DashScopeChatModel(
        model_name="qwen-max",
        api_key=os.environ["DASHSCOPE_API_KEY"],  # 从环境变量读取
        stream=True,
    ),
)
```

### 学习要点

```python
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 获取环境变量
api_key = os.getenv("API_KEY")

# 设置环境变量
os.environ["MY_VAR"] = "value"

# 获取所有环境变量
all_env = os.environ
```

### .env 文件示例

```bash
# .env
DASHSCOPE_API_KEY=your_api_key_here
OPENAI_API_KEY=your_openai_key
MODEL_NAME=qwen-max
```

---

## 9. HTTP 和 API 调用

与外部服务和模型 API 交互。

### 需要学习的内容

- REST API 概念
- JSON 数据处理
- `requests` 库或 `httpx`
- OpenAI SDK

### AgentScope 代码示例

```python
# 使用 OpenAI SDK 调用 AgentScope 部署的服务
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:8091/compatible-mode/v1")

response = client.responses.create(
    model="any_name",
    input="杭州天气如何？"
)

print(response)
```

### 学习要点

```python
import requests
import httpx
import json

# 使用 requests
response = requests.get("https://api.example.com/data")
data = response.json()

# 使用 httpx (支持异步)
async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com/data")
    data = response.json()

# POST 请求
response = requests.post(
    "https://api.example.com/chat",
    json={"message": "Hello"},
    headers={"Authorization": "Bearer token"}
)
```

---

## 10. 工具函数注册

将函数注册为 Agent 可调用的工具。

### 需要学习的内容

- 函数作为对象
- 可调用对象 (`callable`)
- 函数签名 (`inspect` 模块)
- 函数装饰器

### AgentScope 代码示例

```python
from agentscope.tool import Toolkit

# 定义工具函数
def execute_python_code(code: str) -> str:
    """执行 Python 代码"""
    result = exec(code)
    return str(result)

# 创建工具包并注册
toolkit = Toolkit()
toolkit.register_tool_function(execute_python_code)

# 将工具包绑定到 Agent
agent = ReActAgent(
    name="Friday",
    toolkit=toolkit,  # 绑定工具
    ...
)
```

### 学习要点

```python
import inspect

# 函数作为对象
def greet(name):
    return f"Hello, {name}!"

# 将函数赋值给变量
my_func = greet
print(my_func("World"))  # Hello, World!

# 检查是否可调用
print(callable(greet))  # True

# 获取函数签名
sig = inspect.signature(greet)
print(sig)  # (name)

# 获取函数信息
print(greet.__name__)   # greet
print(greet.__doc__)    # 文档字符串
```

---

## 📅 学习路线建议

### 第 1 周：Python 基础

- [ ] 安装 Python 3.10+
- [ ] 变量和数据类型
- [ ] 控制流（if/else、循环）
- [ ] 函数定义和调用
- [ ] 列表、字典操作

### 第 2 周：面向对象编程

- [ ] 类的定义
- [ ] `__init__` 构造方法
- [ ] `__call__` 可调用对象
- [ ] 继承和多态

### 第 3 周：异步编程 ⭐

- [ ] `async def` 和 `await`
- [ ] `asyncio.run()`
- [ ] 异步上下文管理器
- [ ] 异步迭代器

### 第 4 周：高级特性

- [ ] 装饰器
- [ ] 上下文管理器
- [ ] 生成器

### 第 5 周：实用技能

- [ ] 类型注解
- [ ] 环境变量
- [ ] HTTP API 调用
- [ ] JSON 处理

### 第 6 周：AgentScope 实战

- [ ] 安装 AgentScope
- [ ] 创建第一个 Agent
- [ ] 注册工具函数
- [ ] 多智能体对话

---

## ✅ 快速验证

测试你是否准备好开始 AgentScope：

```python
import asyncio
import os
from agentscope.agent import ReActAgent
from agentscope.model import DashScopeChatModel
from agentscope.memory import InMemoryMemory
from agentscope.formatter import DashScopeChatFormatter

async def test_agentscope():
    """验证 AgentScope 基础代码理解"""

    # 1. 创建 Agent（需要理解类实例化）
    agent = ReActAgent(
        name="Test",
        sys_prompt="You are a helpful assistant.",
        model=DashScopeChatModel(
            model_name="qwen-turbo",
            api_key=os.getenv("DASHSCOPE_API_KEY"),  # 需要理解环境变量
        ),
        memory=InMemoryMemory(),
        formatter=DashScopeChatFormatter(),
    )

    # 2. 调用 Agent（需要理解异步和 __call__）
    response = await agent("Hello, AgentScope!")
    print(response)

    return response

# 3. 运行异步函数
if __name__ == "__main__":
    asyncio.run(test_agentscope())
```

**如果你能理解上面这段代码的每个部分，就可以开始学习 AgentScope 了！**

---

## 📚 推荐资源

### 官方文档

- [AgentScope GitHub](https://github.com/agentscope-ai/agentscope)
- [AgentScope 文档](https://doc.agentscope.io/)
- [AgentScope Runtime 文档](https://runtime.agentscope.io/)

### Python 学习

- [Python 官方文档](https://docs.python.org/3.10/)
- [Real Python](https://realpython.com/)
- [ asyncio 官方教程](https://docs.python.org/3.10/library/asyncio.html)

---

## 🎯 学习检查清单

完成以下检查项，确认你已准备好：

- [ ] 我可以使用 async/await 编写异步代码
- [ ] 我理解类和对象的基本概念
- [ ] 我可以使用装饰器修改函数行为
- [ ] 我理解上下文管理器（with 语句）
- [ ] 我可以使用生成器处理数据流
- [ ] 我知道如何读取环境变量
- [ ] 我可以发送 HTTP 请求并处理 JSON
- [ ] 我理解类型注解的用途
- [ ] 我已安装 Python 3.10 或更高版本
- [ ] 我已安装 AgentScope (`pip install agentscope`)

---

**祝你学习顺利！🚀**
