from agentscope.message import (
    Msg,
    TextBlock,
    ThinkingBlock,
    ImageBlock,
    AudioBlock,
    VideoBlock,
    ToolUseBlock,
    ToolResultBlock,
    Base64Source
)
import json

"""
消息是agentScope 中的核心概念，用于数据传输 （多模态数据，工具Api 信息存储/交换提示词的构建）。

"""

messageInfo: Msg = Msg(
    name="zhou",
    role="assistant",
    content="你好，我能怎么帮助你！"
)
print(f"\n发送者的名称: {messageInfo.name}")
print(f"\n发送者的角色: {messageInfo.role}")
print(f"\n消息的内容: {messageInfo.content}")


blockMsg: Msg = Msg(
    name="Jarvis",
    role="assistant",
    content= [
        TextBlock(
            type="text",
            text="这是一个包含 base64 编码数据的多模态消息。",
        ),
        ImageBlock(
            type="image",
            source=Base64Source(
                type="base64",
                media_type="image/jpeg",
                data="/9j/4AAQSkZ...",
            ),
        ),
        AudioBlock(
            type="audio",
            source=Base64Source(
                type="base64",
                media_type="audio/mpeg",
                data="SUQzBAAAAA...",
            ),
        ),
        VideoBlock(
            type="video",
            source=Base64Source(
                type="base64",
                media_type="video/mp4",
                data="AAAAIGZ0eX...",
            ),
        ),
    ]
)