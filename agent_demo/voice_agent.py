# -*- coding: utf-8 -*-
"""Voice cloning agent example using GPT-SoVITS."""
import asyncio
import os

from agentscope.agent import ReActAgent
from agentscope.formatters import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
from agentscope.models import DashScopeChatModel
from agentscope.tool import Toolkit

from tools.gpt_sovits_tts import gpt_sovits_text_to_audio


async def main() -> None:
    """创建一个支持语音克隆的 ReAct 智能体并运行示例对话。"""
    # 准备工具
    toolkit = Toolkit()
    toolkit.register_tool_function(gpt_sovits_text_to_audio)

    # 创建 Agent
    jarvis = ReActAgent(
        name="Jarvis",
        sys_prompt=(
            "你是一个名为 Jarvis 的智能助手。"
            "当用户要求语音回复时，请使用 gpt_sovits_text_to_audio 工具生成语音。"
            "语音合成需要提供参考音频路径和对应的参考文本。"
        ),
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        formatter=DashScopeChatFormatter(),
        toolkit=toolkit,
        memory=InMemoryMemory(),
    )

    # 配置参考音频（用户上传的声音样本）
    ref_audio_path = "./voice_samples/my_voice.wav"
    prompt_text = "这是我的声音样本，用于语音克隆。"

    # 示例对话 1：简单语音合成
    msg1 = Msg(
        name="user",
        content=(
            f"请用我的声音说：你好，我是贾维斯，很高兴为您服务。"
            f"参考音频路径：{ref_audio_path}，参考文本：{prompt_text}"
        ),
        role="user",
    )

    print("=" * 50)
    print("示例 1：简单语音合成")
    print("=" * 50)
    await jarvis(msg1)

    # 示例对话 2：长文本语音合成
    msg2 = Msg(
        name="user",
        content=(
            f"请用我的声音朗读一段话："
            f"人工智能正在改变我们的生活方式，从智能助手到自动驾驶，"
            f"从医疗诊断到创意写作，AI 技术正日益融入我们的日常生活。"
            f"参考音频路径：{ref_audio_path}，参考文本：{prompt_text}"
        ),
        role="user",
    )

    print("\n" + "=" * 50)
    print("示例 2：长文本语音合成")
    print("=" * 50)
    await jarvis(msg2)


if __name__ == "__main__":
    asyncio.run(main())
