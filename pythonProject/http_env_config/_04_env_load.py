"""
 .env 文件管理,使用python-dotenv加载配置文件
"""
import os
from dotenv import load_dotenv


def load_env(environment="development"):
    """
    根据环境加载配置
    """

    # 首先加载默认配置
    load_dotenv(".env", override=False)

    # 加载指定环境
    env_file = f'.env.{environment}'
    load_dotenv(env_file, override=True)

    # 加载本地配置
    load_dotenv(".env.local", override=True)

    #设置当前环境标识
    os.environ["ENVIRONMENT"] = environment


# 使用
load_env(environment="development")
print(f'当前环境：{os.getenv("ENVIRONMENT")}')
