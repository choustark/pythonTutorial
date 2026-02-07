"""
  配置管理的最加实践配置类模式
"""
import os
from dataclasses import dataclass
from typing import Optional

from _04_env_load import load_env


# 先加载环境变量
load_env(environment="development")



@dataclass
class DataBaseConfig:
    """数据库配置"""
    url: str
    pool_size: int = 20
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
    database: DataBaseConfig
    api: APIConfig
    debug: bool = False
    log_level: str = "INFO"

    @classmethod
    def load(cls):
        """加载所有配置"""
        return cls(
            database=DataBaseConfig.from_env(),
            api=APIConfig.from_env(),
            debug=os.getenv("DEBUG", "False").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )

    def validate(self):
        """验证配置"""
        if not self.api.dashscope_key:
            raise ValueError("DASHSCOPE_API_KEY is required")
        print("配置验证通过")


# 使用
config = AppConfig.load()
config.validate()
print(f"Database: {config.database.url}")
print(f"Model: {config.api.model_name}")
