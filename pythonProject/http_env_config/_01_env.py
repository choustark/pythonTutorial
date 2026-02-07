'''
环境变量是操作系统级别存储的键值对，用于配置应用程序的运行环境。
│                                                     │
│  • API 密钥和敏感信息                                │
│  • 数据库连接字符串                                  │
│  • 应用配置参数                                      │
│  • 环境标识（开发/测试/生产）                          |
'''
import os

all_env=os.environ
# 查询所有环境变量
print("\n查询所有环境变量")
print(f"\n共有{all_env}环境变量")

# 查询指定环境变量
print("\n查询指定环境变量")
print(f"\nPATH:{os.getenv('PATH')}")
print(f"\nHOME:{os.getenv('HOME')}")

# 遍历所有环境变量
print("\n遍历所有环境变量")
for key, value in all_env.items():
    print(f"{key}:{value}")

print("-----------"*60)
print("环境变量的获取")
# 方式一
try:
    value: str = os.environ['MY_VAR']
except KeyError:
    print("环境变量不存在")

# 方式二
value: str = os.environ.get('MY_VAR','default_value')
print(value)

print("-----------"*60)
print("设置环境变量{临时}")
os.environ['MY_VAR'] = 'test_value'
# 获取临时变量
print(os.getenv("MY_VAR"))

# ======删除环境变量======
if 'MY_VAR' in os.environ:
    del os.environ['MY_VAR']