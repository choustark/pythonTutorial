'''
 .env 文件管理,使用python-dotenv加载配置文件
'''
import os
from dotenv import load_dotenv

# =======加载 .env 文件======
# 方式一：
load_dotenv()

# 方式二执行文件路径
load_dotenv(".env")

# 方式三：覆盖现有环境变量
load_dotenv(override=True)

# 方式四：加载多个文件
load_dotenv(".env.shared")
load_dotenv(".env.local")

# ========使用环境变量=========
api_key: str = os.getenv("DASHSCOPE_API_KEY")
model_name: str = os.getenv("MODEL_NAME","qwen-turbo")
print(f'\nAPI KEY:{api_key[:10]}...')
print(f'\nModel:{model_name}')

