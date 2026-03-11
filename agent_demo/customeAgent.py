import asyncio
import os
from typing import Any
from dotenv import load_dotenv
from agentscope.agent import AgentBase
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
from agentscope.model import DashScopeChatModel


class MyAgent(AgentBase):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Friday"
        self.sys_prompt = "你是一个名为Friday的助手"
        self.model = DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=False
        )
        self.formatter = DashScopeChatFormatter()
        self.memory = InMemoryMemory()

    async def reply(self, msg: Msg | list[Msg] | None) -> Msg:
        """
        Agent 的核心响应方法
        agent 的核心逻辑方法，会根据输入生成响应消息。所有子类都需要实现这个方法，用于处理输入并生产回复
        """
        await self.memory.add(msg)

        # 准备提示词
        prompt = await self.formatter.format(
            [
                Msg("system", self.sys_prompt, "system"),
                *await self.memory.get_memory()
            ],
        )

        # 调用模型
        response = await self.model(prompt)

        msg = Msg(
            name=self.name,
            content=response.content,
            role="assistant",
        )

        # 在记忆中记录响应
        await self.memory.add(msg)

        # 打印消息
        await self.print(msg)
        return msg

    async def observe(self, msg: Msg | list[Msg] | None) -> Msg:
        """
        被动接受消息
        作用：让 Agent 被动接收消息但不产生回复。这用于以下场景：
          - 订阅模式：Agent 作为订阅者，监听其他 Agent 的输出
          - 多 Agent 协作：通过 MsgHub，一个 Agent 的回复会广播给所有订阅者的 observe 方法
          - 仅观察：需要感知信息但不响应的情况
        """
        await self.memory.add(msg)

    async def handle_interrupt(
            self,
            *args: Any,
            **kwargs: Any,
    ) -> Msg:
        """
        处理中断
        作用：当 Agent 的回复过程被中断时的处理逻辑。
        """
        # 以固定响应为例
        return Msg(
            name=self.name,
            content="我注意到您打断了我的回复，我能为你做些什么？",
            role="assistant",
        )


# 加载配置
load_dotenv()


async def run_custom_agent() -> None:
    agent: AgentBase = MyAgent()
    msg: Msg = Msg(
        name="user",
        content="今天东莞长安镇天气如何",
        role="user",
    )
    await agent(msg)


asyncio.run(run_custom_agent())
