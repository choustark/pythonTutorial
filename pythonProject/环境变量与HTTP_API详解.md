# 环境变量与 HTTP API 完全指南

> 在 AgentScope 开发中必备的配置管理和 API 调用技能

---

## 📋 目录

- [第一部分：环境变量](#第一部分环境变量)
  - [1. 环境变量基础](#1-环境变量基础)
  - [2. os 模块](#2-os-模块)
  - [3. .env 文件管理](#3-env-文件管理)
  - [4. 配置管理最佳实践](#4-配置管理最佳实践)
- [第二部分：HTTP API](#第二部分http-api)
  - [5. HTTP 基础](#5-http-基础)
  - [6. requests 库](#6-requests-库)
  - [7. httpx 库（异步）](#7-httpx-库异步)
  - [8. API 客户端封装](#8-api-客户端封装)
- [第三部分：AgentScope 应用](#第三部分agentscope-应用)
- [9. 练习题及答案](#9-练习题及答案)
- [10. 最佳实践](#10-最佳实践)

---

## 第一部分：环境变量

## 1. 环境变量基础

### 1.1 什么是环境变量？

**环境变量**是操作系统级别存储的键值对，用于配置应用程序的运行环境。

```
┌─────────────────────────────────────────────────────┐
│                 环境变量的用途                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  • API 密钥和敏感信息                                │
│  • 数据库连接字符串                                  │
│  • 应用配置参数                                      │
│  • 环境标识（开发/测试/生产）                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 1.2 为什么使用环境变量？

**❌ 不好的做法：硬编码配置**

```python
# config.py
API_KEY = "sk-1234567890abcdef"  # 敏感信息暴露！
DATABASE_URL = "postgresql://user:pass@localhost/db"
DEBUG = True
```

**问题：**
- 敏感信息会提交到 Git
- 不同环境需要修改代码
- 难以管理多套配置

**✅ 好的做法：使用环境变量**

```python
# config.py
import os

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
```

**优点：**
- 敏感信息不进入代码仓库
- 不同环境使用不同配置
- 配置与代码分离

### 1.3 查看环境变量

```python
import os

# 获取所有环境变量
all_env = os.environ
print(f"共有 {len(all_env)} 个环境变量")

# 查看特定环境变量
print(f"PATH: {os.getenv('PATH')}")
print(f"HOME: {os.getenv('HOME')}")

# 遍历所有环境变量
for key, value in os.environ.items():
    if 'API' in key.upper():
        print(f"{key} = {value[:10]}...")  # 只显示前 10 个字符
```

---

## 2. os 模块

### 2.1 os.getenv()

```python
import os

# ========== 基本用法 ==========
# 读取环境变量
value = os.getenv("MY_VAR")

# 带默认值
value = os.getenv("MY_VAR", "default_value")

# 不存在时返回 None
value = os.getenv("NON_EXISTENT_VAR")
print(value)  # None


# ========== 类型转换 ==========
# 字符串
api_key = os.getenv("API_KEY", "")

# 整数
port = int(os.getenv("PORT", "8080"))

# 布尔值
debug = os.getenv("DEBUG", "False").lower() == "true"

# 列表（逗号分隔）
allowed_hosts = os.getenv("ALLOWED_HOSTS", "").split(",")
```

### 2.2 os.environ

```python
import os

# ========== 读取环境变量 ==========
# 方式 1：直接访问
try:
    value = os.environ["MY_VAR"]
except KeyError:
    print("环境变量不存在")

# 方式 2：使用 get()
value = os.environ.get("MY_VAR", "default")


# ========== 设置环境变量 ==========
# 在当前进程中设置（临时）
os.environ["MY_VAR"] = "my_value"
print(os.getenv("MY_VAR"))  # my_value


# ========== 删除环境变量 ==========
if "MY_VAR" in os.environ:
    del os.environ["MY_VAR"]


# ========== 检查是否存在 ==========
if "API_KEY" in os.environ:
    print("API_KEY 已设置")
```

### 2.3 完整示例

```python
import os

class Config:
    """从环境变量加载配置"""

    # API 配置
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    # 模型配置
    MODEL_NAME = os.getenv("MODEL_NAME", "qwen-turbo")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))

    # 服务配置
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8090"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # 数据库配置
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///local.db"
    )

    # 日志配置
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        """验证必需的配置"""
        required = [
            "DASHSCOPE_API_KEY",
        ]
        missing = [key for key in required if not getattr(cls, key)]
        if missing:
            raise ValueError(f"缺少必需的环境变量: {missing}")

        print("✅ 配置验证通过")

# 使用
try:
    Config.validate()
    print(f"Model: {Config.MODEL_NAME}")
    print(f"Host: {Config.HOST}:{Config.PORT}")
except ValueError as e:
    print(f"❌ 配置错误: {e}")
```

---

## 3. .env 文件管理

### 3.1 创建 .env 文件

```bash
# .env
# ========== API 配置 ==========
DASHSCOPE_API_KEY=your_dashscope_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# ========== 模型配置 ==========
MODEL_NAME=qwen-turbo
TEMPERATURE=0.7
MAX_TOKENS=2000

# ========== 服务配置 ==========
HOST=0.0.0.0
PORT=8090
DEBUG=True

# ========== 数据库配置 ==========
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# ========== 日志配置 ==========
LOG_LEVEL=INFO
```

### 3.2 使用 python-dotenv

```python
from dotenv import load_dotenv
import os

# ========== 加载 .env 文件 ==========
# 方式 1：加载默认 .env 文件
load_dotenv()

# 方式 2：指定文件路径
load_dotenv(".env.local")

# 方式 3：覆盖现有环境变量
load_dotenv(override=True)

# 方式 4：加载多个文件
load_dotenv(".env.shared")
load_dotenv(".env.local")

# ========== 使用环境变量 ==========
api_key = os.getenv("DASHSCOPE_API_KEY")
model_name = os.getenv("MODEL_NAME", "qwen-turbo")

print(f"API Key: {api_key[:10]}...")
print(f"Model: {model_name}")
```

### 3.3 多环境配置

```
项目结构：
├── .env                    # 默认配置（不提交）
├── .env.example            # 示例配置（提交）
├── .env.development        # 开发环境
├── .env.testing            # 测试环境
└── .env.production         # 生产环境
```

```python
from dotenv import load_dotenv
import os

def load_env(environment="development"):
    """根据环境加载配置"""

    # 首先加载默认配置
    load_dotenv(".env.shared", override=False)

    # 然后加载环境特定配置
    env_file = f".env.{environment}"
    load_dotenv(env_file, override=True)

    # 最后加载本地配置（不提交）
    load_dotenv(".env.local", override=True)

    # 设置当前环境标识
    os.environ["ENVIRONMENT"] = environment

# 使用
load_env(environment="development")
print(f"当前环境: {os.getenv('ENVIRONMENT')}")
```

### 3.4 .env.example

```bash
# .env.example
# 这是环境变量配置示例
# 复制此文件为 .env 并填入实际值

# ========== API 配置 ==========
DASHSCOPE_API_KEY=your_api_key_here
OPENAI_API_KEY=your_openai_key_here

# ========== 模型配置 ==========
MODEL_NAME=qwen-turbo
TEMPERATURE=0.7
MAX_TOKENS=2000

# ========== 服务配置 ==========
HOST=0.0.0.0
PORT=8090
DEBUG=True
```

### 3.5 安全最佳实践

```python
# ========== .gitignore ==========
# 忽略所有 .env 文件
.env
.env.local
.env.*.local

# 但保留示例文件
!.env.example
```

```python
# ========== 验证敏感信息不被提交 ==========
def check_env_security():
    """检查 .env 文件安全"""
    import os
    from pathlib import Path

    env_files = [".env", ".env.local"]

    for env_file in env_files:
        if Path(env_file).exists():
            print(f"⚠️  警告: {env_file} 文件存在")

            # 检查是否在 .gitignore 中
            with open(".gitignore", "r") as f:
                gitignore = f.read()
                if env_file not in gitignore:
                    print(f"  ❌ {env_file} 未在 .gitignore 中！")
```

---

## 4. 配置管理最佳实践

### 4.1 配置类模式

```python
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class DatabaseConfig:
    """数据库配置"""
    url: str
    pool_size: int = 10
    max_overflow: int = 20

    @classmethod
    def from_env(cls):
        return cls(
            url=os.getenv("DATABASE_URL", "sqlite:///default.db"),
            pool_size=int(os.getenv("DB_POOL_SIZE", "10")),
            max_overflow=int(os.getenv("DB_MAX_OVERFLOW", "20")),
        )

@dataclass
class APIConfig:
    """API 配置"""
    dashscope_key: str
    openai_key: Optional[str] = None
    model_name: str = "qwen-turbo"
    temperature: float = 0.7

    @classmethod
    def from_env(cls):
        return cls(
            dashscope_key=os.getenv("DASHSCOPE_API_KEY", ""),
            openai_key=os.getenv("OPENAI_API_KEY"),
            model_name=os.getenv("MODEL_NAME", "qwen-turbo"),
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
        )

@dataclass
class AppConfig:
    """应用总配置"""
    database: DatabaseConfig
    api: APIConfig
    debug: bool = False
    log_level: str = "INFO"

    @classmethod
    def load(cls):
        """加载所有配置"""
        return cls(
            database=DatabaseConfig.from_env(),
            api=APIConfig.from_env(),
            debug=os.getenv("DEBUG", "False").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )

    def validate(self):
        """验证配置"""
        if not self.api.dashscope_key:
            raise ValueError("DASHSCOPE_API_KEY is required")
        print("✅ 配置验证通过")

# 使用
config = AppConfig.load()
config.validate()
print(f"Database: {config.database.url}")
print(f"Model: {config.api.model_name}")
```

### 4.2 配置验证

```python
import os
from typing import List, Optional
from dataclasses import dataclass

class ValidationError(Exception):
    """配置验证错误"""
    pass

def validate_required(value: Optional[str], name: str):
    """验证必需字段"""
    if not value:
        raise ValidationError(f"{name} is required")

def validate_port(value: int):
    """验证端口号"""
    if not (1 <= value <= 65535):
        raise ValidationError(f"Invalid port: {value}")

def validate_bool(value: str) -> bool:
    """验证布尔值"""
    if value.lower() in ("true", "1", "yes"):
        return True
    elif value.lower() in ("false", "0", "no"):
        return False
    else:
        raise ValidationError(f"Invalid boolean: {value}")

@dataclass
class ValidatedConfig:
    """带验证的配置"""

    @classmethod
    def from_env(cls):
        # API Key
        api_key = os.getenv("API_KEY")
        validate_required(api_key, "API_KEY")

        # 端口
        port = int(os.getenv("PORT", "8090"))
        validate_port(port)

        # 调试模式
        debug_str = os.getenv("DEBUG", "False")
        debug = validate_bool(debug_str)

        return cls(
            api_key=api_key,
            port=port,
            debug=debug,
        )

# 使用
try:
    config = ValidatedConfig.from_env()
    print("✅ 配置有效")
except ValidationError as e:
    print(f"❌ 配置错误: {e}")
```

### 4.3 配置优先级

```
配置优先级（从高到低）：

1. 命令行参数
2. 环境变量
3. 配置文件
4. 默认值
```

```python
import os
import argparse

class ConfigManager:
    """配置管理器"""

    def __init__(self):
        self.config = {}

    def load_defaults(self):
        """加载默认配置"""
        self.config.update({
            "host": "0.0.0.0",
            "port": 8090,
            "debug": False,
        })
        return self

    def load_from_file(self, filepath):
        """从文件加载配置"""
        import json
        try:
            with open(filepath) as f:
                file_config = json.load(f)
                self.config.update(file_config)
        except FileNotFoundError:
            pass
        return self

    def load_from_env(self):
        """从环境变量加载"""
        env_mapping = {
            "HOST": "host",
            "PORT": "port",
            "DEBUG": "debug",
        }
        for env_key, config_key in env_mapping.items():
            if env_key in os.environ:
                self.config[config_key] = os.environ[env_key]
        return self

    def load_from_args(self, args=None):
        """从命令行参数加载"""
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", default=self.config.get("host"))
        parser.add_argument("--port", type=int, default=self.config.get("port"))
        parser.add_argument("--debug", action="store_true")
        args = parser.parse_args(args)

        self.config.update({
            "host": args.host,
            "port": args.port,
            "debug": args.debug,
        })
        return self

    def build(self):
        """构建最终配置"""
        return type("Config", (), self.config)

# 使用
config = (ConfigManager()
    .load_defaults()
    .load_from_file("config.json")
    .load_from_env()
    .load_from_args(["--port", "9000"])
    .build())

print(f"Host: {config.host}")
print(f"Port: {config.port}")
print(f"Debug: {config.debug}")
```

---

## 第二部分：HTTP API

## 5. HTTP 基础

### 5.1 HTTP 请求方法

```
┌─────────────────────────────────────────────────────┐
│                 HTTP 请求方法                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  GET    - 获取资源                                  │
│  POST   - 创建资源                                  │
│  PUT    - 更新资源（完整）                           │
│  PATCH - 更新资源（部分）                            │
│  DELETE - 删除资源                                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 5.2 HTTP 状态码

```python
# ========== 常见状态码 ==========
status_codes = {
    # 成功响应
    200: "OK",
    201: "Created",
    204: "No Content",

    # 重定向
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",

    # 客户端错误
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    429: "Too Many Requests",

    # 服务器错误
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
}

# 状态码分类
def categorize_status(code):
    if 200 <= code < 300:
        return "成功"
    elif 300 <= code < 400:
        return "重定向"
    elif 400 <= code < 500:
        return "客户端错误"
    elif 500 <= code < 600:
        return "服务器错误"
```

### 5.3 HTTP 请求头

```python
# ========== 常见请求头 ==========
common_headers = {
    # 认证
    "Authorization": "Bearer <token>",
    "API-Key": "<key>",

    # 内容类型
    "Content-Type": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Type": "multipart/form-data",

    # 接受类型
    "Accept": "application/json",
    "Accept": "text/html",

    # 用户代理
    "User-Agent": "MyApp/1.0",

    # 其他
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}
```

---

## 6. requests 库

### 6.1 安装

```bash
pip install requests
```

### 6.2 GET 请求

```python
import requests

# ========== 基本 GET 请求 ==========
response = requests.get("https://api.github.com")

print(f"状态码: {response.status_code}")
print(f"内容: {response.text[:100]}...")

# ========== 带参数的 GET 请求 ==========
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
}
response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)
data = response.json()
print(f"找到 {data['total_count']} 个仓库")

# ========== 带请求头的 GET 请求 ==========
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json",
}
response = requests.get(
    "https://api.github.com/user",
    headers=headers
)
user = response.json()
print(f"用户: {user['login']}")

# ========== 处理响应 ==========
response = requests.get("https://api.github.com")

# 文本内容
text = response.text

# JSON 内容
json_data = response.json()

# 二进制内容
binary = response.content

# 响应头
headers = response.headers
print(f"Content-Type: {headers['Content-Type']}")

# ========== 错误处理 ==========
try:
    response = requests.get("https://api.github.com/invalid", timeout=5)
    response.raise_for_status()  # 非 2xx 状态码会抛出异常
except requests.Timeout:
    print("请求超时")
except requests.ConnectionError:
    print("连接错误")
except requests.HTTPError as e:
    print(f"HTTP 错误: {e}")
except requests.RequestException as e:
    print(f"请求异常: {e}")
```

### 6.3 POST 请求

```python
import requests

# ========== JSON POST 请求 ==========
url = "https://httpbin.org/post"
data = {
    "name": "Alice",
    "age": 30,
}

response = requests.post(url, json=data)
print(response.json())

# ========== 表单 POST 请求 ==========
url = "https://httpbin.org/post"
data = {
    "username": "alice",
    "password": "secret",
}

response = requests.post(url, data=data)
print(response.json())

# ========== 文件上传 ==========
url = "https://httpbin.org/post"
files = {
    "file": open("test.txt", "rb"),
}

response = requests.post(url, files=files)
print(response.json())
```

### 6.4 Session（会话）

```python
import requests

# ========== 使用 Session ==========
session = requests.Session()

# 设置会话级别的请求头
session.headers.update({
    "Authorization": "Bearer YOUR_TOKEN",
})

# 多个请求共享会话
response1 = session.get("https://api.example.com/users")
response2 = session.get("https://api.example.com/posts")

# Session 会自动处理 Cookies
session.get("https://example.com/login")
# Cookies 会自动保存在 session 中
response = session.get("https://example.com/profile")

# 关闭会话
session.close()

# ========== 使用 with 语句 ==========
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer TOKEN"})
    response = session.get("https://api.example.com/data")
```

---

## 7. httpx 库（异步）

### 7.1 安装

```bash
pip install httpx
# 带异步支持
pip install httpx[http2]
```

### 7.2 基本用法

```python
import httpx

# ========== 同步用法（类似 requests）==========
with httpx.Client() as client:
    response = client.get("https://api.github.com")
    print(response.json())
```

### 7.3 异步用法

```python
import asyncio
import httpx

# ========== 基本异步请求 ==========
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com")
        return response.json()

async def main():
    data = await fetch_data()
    print(data)

asyncio.run(main())

# ========== 并发请求 ==========
async def fetch_multiple():
    urls = [
        "https://api.github.com/users/octocat",
        "https://api.github.com/users/torvalds",
        "https://api.github.com/users/gvanrossum",
    ]

    async with httpx.AsyncClient() as client:
        # 并发执行多个请求
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            user = response.json()
            print(f"{user['login']}: {user['name']}")

asyncio.run(fetch_multiple())

# ========== 带参数的请求 ==========
async def search_repositories(query):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.github.com/search/repositories",
            params={
                "q": query,
                "sort": "stars",
                "per_page": 10,
            },
            headers={
                "Accept": "application/vnd.github.v3+json",
            },
            timeout=30.0,
        )
        return response.json()

asyncio.run(search_repositories("python"))
```

### 7.4 WebSocket 支持

```python
import asyncio
import httpx

async def websocket_example():
    async with httpx.AsyncClient() as client:
        async with client.websocket_connect("ws://localhost:8080/ws") as websocket:
            await websocket.send_text("Hello, WebSocket!")
            message = await websocket.receive_text()
            print(f"收到: {message}")

asyncio.run(websocket_example())
```

---

## 8. API 客户端封装

### 8.1 基础封装

```python
import httpx
from typing import Optional, Dict, Any

class APIClient:
    """HTTP API 客户端"""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        """异步上下文管理器入口"""
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self._get_headers(),
            timeout=self.timeout,
        )
        return self

    async def __aexit__(self, *args):
        """异步上下文管理器退出"""
        if self._client:
            await self._client.aclose()

    def _get_headers(self) -> Dict[str, str]:
        """获取请求头"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """GET 请求"""
        if not self._client:
            raise RuntimeError("Client not initialized. Use 'async with'.")

        response = await self._client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    async def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """POST 请求"""
        if not self._client:
            raise RuntimeError("Client not initialized. Use 'async with'.")

        response = await self._client.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()

# 使用
async def main():
    async with APIClient(
        base_url="https://api.example.com",
        api_key="your_api_key",
    ) as client:
        # GET 请求
        users = await client.get("/users")
        print(users)

        # POST 请求
        new_user = await client.post("/users", data={
            "name": "Alice",
            "email": "alice@example.com",
        })
        print(new_user)

asyncio.run(main())
```

### 8.2 带重试的客户端

```python
import asyncio
import httpx
from typing import Optional

class RetryableAPIClient:
    """带重试功能的 API 客户端"""

    def __init__(
        self,
        base_url: str,
        max_retries: int = 3,
        retry_delay: float = 1.0,
    ):
        self.base_url = base_url
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    async def request_with_retry(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ):
        """带重试的请求"""
        async with httpx.AsyncClient() as client:
            for attempt in range(self.max_retries):
                try:
                    response = await client.request(
                        method,
                        f"{self.base_url}{endpoint}",
                        **kwargs
                    )
                    response.raise_for_status()
                    return response.json()

                except (httpx.HTTPError, httpx.NetworkError) as e:
                    if attempt == self.max_retries - 1:
                        raise
                    print(f"请求失败，{self.retry_delay}秒后重试...")
                    await asyncio.sleep(self.retry_delay)

# 使用
async def main():
    client = RetryableAPIClient(
        base_url="https://api.example.com",
        max_retries=3,
    )

    data = await client.request_with_retry(
        "GET",
        "/users",
    )
    print(data)

asyncio.run(main())
```

---

## 第三部分：AgentScope 应用

## 9. AgentScope 中的配置管理

### 9.1 使用环境变量配置 Agent

```python
from dotenv import load_dotenv
import os
from agentscope.agent import ReActAgent
from agentscope.model import DashScopeChatModel
from agentscope.memory import InMemoryMemory

# 加载环境变量
load_dotenv()

# 从环境变量创建配置
def create_agent():
    """创建 Agent"""
    return ReActAgent(
        name=os.getenv("AGENT_NAME", "assistant"),
        sys_prompt=os.getenv("SYSTEM_PROMPT", "你是一个有用的助手"),
        model=DashScopeChatModel(
            model_name=os.getenv("MODEL_NAME", "qwen-turbo"),
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            stream=os.getenv("STREAM", "True").lower() == "true",
        ),
        memory=InMemoryMemory(),
    )

agent = create_agent()
```

### 9.2 完整的配置示例

```python
# .env
DASHSCOPE_API_KEY=your_key
MODEL_NAME=qwen-turbo
AGENT_NAME=assistant
SYSTEM_PROMPT=你是AgentScope助手
HOST=0.0.0.0
PORT=8090
```

```python
# config.py
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()

@dataclass
class AgentScopeConfig:
    """AgentScope 配置"""

    # API 配置
    dashscope_api_key: str
    model_name: str = "qwen-turbo"

    # Agent 配置
    agent_name: str = "assistant"
    system_prompt: str = "你是一个有用的助手"

    # 服务配置
    host: str = "0.0.0.0"
    port: int = 8090

    @classmethod
    def from_env(cls):
        return cls(
            dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
            model_name=os.getenv("MODEL_NAME", "qwen-turbo"),
            agent_name=os.getenv("AGENT_NAME", "assistant"),
            system_prompt=os.getenv("SYSTEM_PROMPT"),
            host=os.getenv("HOST", "0.0.0.0"),
            port=int(os.getenv("PORT", "8090")),
        )
```

### 9.3 调用 AgentScope 服务

```python
import httpx
import os

async def call_agentscope_service(message: str):
    """调用 AgentScope 部署的服务"""

    base_url = os.getenv("AGENTSCOPE_URL", "http://localhost:8091")
    endpoint = f"{base_url}/compatible-mode/v1"

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{endpoint}/responses",
            json={
                "model": "any",
                "input": message,
            }
        )
        response.raise_for_status()
        return response.json()

# 使用
asyncio.run(call_agentscope_service("你好"))
```

---

## 9. 练习题及答案

### 练习 1：环境变量配置

**题目：** 实现一个配置类，从环境变量读取数据库配置。

```python
import os
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str

    # TODO: 实现 from_env 方法
    @classmethod
    def from_env(cls):
        pass
```

<details>
<summary>查看答案</summary>

```python
@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str

    @classmethod
    def from_env(cls):
        return cls(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            database=os.getenv("DB_NAME", "mydb"),
            username=os.getenv("DB_USER", "user"),
            password=os.getenv("DB_PASSWORD", ""),
        )
```
</details>

---

### 练习 2：HTTP GET 请求

**题目：** 使用 httpx 实现 GitHub API 调用。

```python
import httpx
import asyncio

async def get_github_user(username: str):
    # TODO: 实现 GitHub 用户信息获取
    pass

asyncio.run(get_github_user("octocat"))
```

<details>
<summary>查看答案</summary>

```python
import httpx
import asyncio

async def get_github_user(username: str):
    url = f"https://api.github.com/users/{username}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

asyncio.run(get_github_user("octocat"))
```
</details>

---

### 练习 3：API 客户端

**题目：** 实现一个简单的 API 客户端。

```python
import httpx
from typing import Dict, Any

class SimpleAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    # TODO: 实现 get 方法
    async def get(self, endpoint: str) -> Dict[str, Any]:
        pass

    # TODO: 实现 post 方法
    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
```

<details>
<summary>查看答案</summary>

```python
import httpx
from typing import Dict, Any

class SimpleAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    async def get(self, endpoint: str) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()
            return response.json()

    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}{endpoint}",
                json=data
            )
            response.raise_for_status()
            return response.json()
```
</details>

---

## 10. 最佳实践

### 10.1 环境变量

```python
# ✅ 好的做法
# 1. 使用默认值
api_key = os.getenv("API_KEY", "default_key")

# 2. 类型转换
port = int(os.getenv("PORT", "8080"))

# 3. 验证必需变量
if not os.getenv("REQUIRED_VAR"):
    raise ValueError("REQUIRED_VAR is required")

# 4. 使用 .env.example
# 创建示例文件供其他开发者参考
```

### 10.2 HTTP API

```python
# ✅ 好的做法
# 1. 使用异步客户端
async with httpx.AsyncClient() as client:
    response = await client.get(url)

# 2. 设置超时
response = await client.get(url, timeout=30.0)

# 3. 处理错误
try:
    response.raise_for_status()
except httpx.HTTPError as e:
    print(f"请求失败: {e}")

# 4. 使用 Session 复用连接
async with httpx.AsyncClient() as client:
    response1 = await client.get(url1)
    response2 = await client.get(url2)
```

---

## ✅ 学习检查清单

### 环境变量
- [ ] 理解什么是环境变量
- [ ] 能够使用 `os.getenv()` 读取
- [ ] 能够使用 `os.environ` 操作
- [ ] 理解 `.env` 文件的作用
- [ ] 能够使用 `python-dotenv`
- [ ] 理解配置管理最佳实践

### HTTP API
- [ ] 理解 HTTP 请求方法
- [ ] 理解 HTTP 状态码
- [ ] 能够使用 `requests` 发送请求
- [ ] 能够使用 `httpx` 发送异步请求
- [ ] 能够处理响应和错误
- [ ] 能够封装 API 客户端

### AgentScope 应用
- [ ] 能够配置 API Key
- [ ] 能够调用部署的服务
- [ ] 理解配置与代码分离

---

**祝你学习顺利！🚀**
