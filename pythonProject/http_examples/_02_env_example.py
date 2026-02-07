'''
 环境变量示例，从环境变量加载配置
'''
import os

class Config:
    #从环境变量中加载变量

    DASHSCOPE_API_KEY: str = os.getenv('DASHSCOPE_API_KEY')
    OPEN_API_KEY: str = os.getenv("OPEN_API_KEY")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY")

    # 模型配置
    MODEL_NAME: str = os.getenv("MODEL_NAME","qwen-turbo")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE",0,7))
    MAX_TOKEN: int = int(os.getenv("MAX_TOKEN",2000))

    # 服务器配置
    HOST: str = os.getenv("HOST","0.0.0.0")
    PORT: str = os.getenv("PORT","8080")
    DEBUG: str = os.getenv("DEBUG","Fals").lower() == 'true'


    # 数据库配置
    DATABASE_URL: str = os.getenv("DATABASE_URL","sqlite:///local.db")

    # 日志配置
    LOG_LEVEL: str = os.getenv("LOG_LEVEL","INFO")

    @classmethod
    def validate(cls):
        '''验证必须的配置'''
        required = [
            'DATABASE_URL'
        ]

