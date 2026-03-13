import asyncio
import os

from agentscope.agent import ReActAgent, UserAgent
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.model import DashScopeChatModel
from agentscope.tool import Toolkit, execute_shell_command, execute_python_code, view_text_file
from dotenv import load_dotenv

load_dotenv()

toolkit = Toolkit()
toolkit.register_tool_function(execute_shell_command)
toolkit.register_tool_function(execute_python_code)
toolkit.register_tool_function(view_text_file)


async def main() -> None:
    agent = ReActAgent(
        name="jarvis",
        sys_prompt="你是一个人工智能助手，协助用户执行命令和编写代码。",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            enable_thinking=False,
            stream=True
        ),
        formatter=DashScopeChatFormatter(),
        toolkit=toolkit,
        memory=InMemoryMemory()
    )
    user = UserAgent("User")

    msg = None
    while True:
        msg = await user(msg)
        if msg.get_text_content() == 'exit':
            break
        msg = await agent(msg)


if __name__ == "__main__":
    asyncio.run(main())
