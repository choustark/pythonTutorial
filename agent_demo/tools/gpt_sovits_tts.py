# -*- coding: utf-8 -*-
"""GPT-SoVITS text-to-speech tool for voice cloning."""
import base64
from typing import Literal

import requests

from agentscope.message import AudioBlock, TextBlock
from agentscope.tool import ToolResponse


def gpt_sovits_text_to_audio(
    text: str,
    ref_audio_path: str,
    prompt_text: str,
    text_lang: Literal["zh", "en", "ja", "yue"] = "zh",
    prompt_lang: Literal["zh", "en", "ja", "yue"] = "zh",
    api_url: str = "http://localhost:9880",
    speed: float = 1.0,
    top_k: int = 5,
    top_p: float = 0.8,
    temperature: float = 0.8,
) -> ToolResponse:
    """使用 GPT-SoVITS 将文本转换为语音，支持声音克隆。

    Args:
        text (str): 要合成的文本内容
        ref_audio_path (str): 参考音频文件路径（用于克隆声音）
        prompt_text (str): 参考音频对应的文本内容
        text_lang (Literal["zh", "en", "ja", "yue"], optional):
            合成文本的语言，默认为 "zh"（中文）
        prompt_lang (Literal["zh", "en", "ja", "yue"], optional):
            参考音频的语言，默认为 "zh"（中文）
        api_url (str, optional): GPT-SoVITS API 地址，默认为 "http://localhost:9880"
        speed (float, optional): 语速控制，范围 0.5-2.0，默认为 1.0
        top_k (int, optional): 采样参数，控制多样性，默认为 5
        top_p (float, optional): 核采样参数，默认为 0.8
        temperature (float, optional): 温度参数，控制随机性，默认为 0.8

    Returns:
        ToolResponse: 包含 AudioBlock 的响应，如果出错则包含错误信息

    Examples:
        >>> response = gpt_sovits_text_to_audio(
        ...     text="你好，这是一个测试。",
        ...     ref_audio_path="./voice_samples/sample.wav",
        ...     prompt_text="这是参考音频的文本内容",
        ... )
        >>> # response.content[0] 包含 AudioBlock
    """
    try:
        # 构建请求 payload
        payload = {
            "text": text,
            "text_lang": text_lang,
            "ref_audio_path": ref_audio_path,
            "prompt_text": prompt_text,
            "prompt_lang": prompt_lang,
            "speed": speed,
            "top_k": top_k,
            "top_p": top_p,
            "temperature": temperature,
        }

        # 调用 GPT-SoVITS API
        response = requests.post(
            f"{api_url}/tts",
            json=payload,
            timeout=60,
        )
        response.raise_for_status()

        # 处理返回的音频数据
        audio_data = response.content
        audio_base64 = base64.b64encode(audio_data).decode("utf-8")

        # 构建 AudioBlock
        audio_block = AudioBlock(
            type="audio",
            source={
                "type": "base64",
                "media_type": "audio/wav",
                "data": audio_base64,
            },
        )

        return ToolResponse(
            content=[audio_block],
            is_last=True,
        )

    except requests.exceptions.ConnectionError:
        return ToolResponse(
            content=[
                TextBlock(
                    type="text",
                    text=f"TTS 连接失败：无法连接到 GPT-SoVITS API ({api_url})。"
                    "请确保服务已启动（运行 `python api_v2.py -a 0.0.0.0 -p 9880`）。",
                )
            ],
            is_last=True,
        )
    except requests.exceptions.Timeout:
        return ToolResponse(
            content=[
                TextBlock(
                    type="text",
                    text=f"TTS 超时：请求在 {60} 秒后超时。请尝试缩短文本或检查服务器性能。",
                )
            ],
            is_last=True,
        )
    except requests.exceptions.HTTPError as e:
        return ToolResponse(
            content=[
                TextBlock(
                    type="text",
                    text=f"TTS HTTP 错误：{e.response.status_code} - {e.response.text}",
                )
            ],
            is_last=True,
        )
    except Exception as e:
        return ToolResponse(
            content=[TextBlock(type="text", text=f"TTS 错误: {str(e)}")],
            is_last=True,
        )
