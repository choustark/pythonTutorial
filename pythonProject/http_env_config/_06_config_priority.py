import os
import argparse
import json


class ConfigManager:
    """配置管理器"""

    def __init__(self):
        self.config: dict[str,str] = {}

    # 定义默认配置
    def load_default(self):
        self.config.update({
            "host": '0.0.0.0',
            "port": 8090,
            "debug": False
        })
        return self

    # 从文件加载配置
    def load_config_from_file(self, filePath):
        try:
            with open(filePath, encoding='utf-8-sig') as f:
                file_config = json.load(f)
                self.config.update(file_config)
        except FileNotFoundError:
            pass
        return self

    # 从配置文件加载配置
    def load_config_from_env(self):
        """从环境变量加载"""
        env_mapping: dict[str, str] = {
            "HOST": "host",
            "PORT": "port",
            "DEBUG": "debug",
        }
        for env_key, config_key in env_mapping.items():
            self.config[config_key] = os.getenv(env_key)
        return self

    # 从命令行参数加载配置
    def load_from_agrs(self, args=None):
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", default=self.config.get("host"))
        parser.add_argument("--port", type=int, default=self.config.get("port"))
        parser.add_argument("--debug", action="store_true")
        args = parser.parse_args(args)

        self.config.update({
            "host": args.host,
            "port": args.port,
            "debug": args.debug
        })
        return self

    def build(self):
        return type("Config", (), self.config)


config = (ConfigManager()
          .load_default()
          .load_config_from_file("config.json")
          .load_config_from_env()
          .load_from_agrs(["--port", "9000"])
          .build())

print(f"\nHost: {config.host}")
print(f"\nPort: {config.port}")
print(f"\nDebug: {config.debug}")
