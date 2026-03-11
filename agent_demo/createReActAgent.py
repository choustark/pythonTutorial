from dotenv import load_dotenv
from agentscope.agent import ReActAgent, AgentBase
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
from agentscope.model import DashScopeChatModel
import asyncio
import os

from agentscope.tool import Toolkit, execute_python_code

# 加载配置
load_dotenv()


# 创建智能体
async def create_chat_agent() -> None:
    """创建ReAct 智能体并执行一个简单的任务"""
    # 工具准备
    toolKit = Toolkit()
    toolKit.register_tool_function(execute_python_code)

    # 创建智能体
    jarvis = ReActAgent(
        name="Jarvis",
        sys_prompt="你是一个名为Jarvis的助手",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
            enable_thinking=False
        ),
        formatter=DashScopeChatFormatter(),
        toolkit=toolKit,
        memory=InMemoryMemory()
    )
    msg = Msg(
        name="user",
        content="你好！Jarvis,用python 运行Hello World",
        role="user"
    )

    # ReActAgent 实现了__call__可以自调用
    await jarvis(msg)

asyncio.run(create_chat_agent())
