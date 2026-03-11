# GPT-SoVITS 语音克隆集成指南

本项目集成了 GPT-SoVITS 语音克隆功能，允许 Agent 使用你上传的语音样本进行语音合成。

## 功能特性

- **声音克隆**：仅需 5-30 秒语音样本即可克隆音色
- **多语言支持**：中文、英文、日文、粤语
- **参数可调**：语速、多样性、温度等参数可配置
- **AgentScope 集成**：无缝集成到 ReActAgent 工具链

## 快速开始

### 1. 部署 GPT-SoVITS 服务

首先需要部署 GPT-SoVITS 本地服务：

```bash
# 克隆仓库
git clone https://github.com/RVC-Boss/GPT-SoVITS.git
cd GPT-SoVITS

# 安装依赖
pip install -r requirements.txt

# 启动 API 服务
python api_v2.py -a 0.0.0.0 -p 9880 -c configs/tts_infer.yaml
```

服务启动后访问 http://localhost:9880/docs 查看 Swagger 文档。

### 2. 安装项目依赖

```bash
# 在 agent_demo 项目目录下
uv sync
```

### 3. 准备参考音频

将你的语音样本放入 `voice_samples/` 目录：

**参考音频要求：**
- 格式：WAV
- 时长：建议 5-30 秒
- 要求：清晰无背景音，单人语音
- 命名：例如 `my_voice.wav`

```
voice_samples/
├── .gitkeep
└── my_voice.wav  # 你的语音样本
```

### 4. 运行语音 Agent

```bash
python voice_agent.py
```

## API 参数说明

### gpt_sovits_text_to_audio

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `text` | str | 必填 | 要合成的文本内容 |
| `ref_audio_path` | str | 必填 | 参考音频文件路径 |
| `prompt_text` | str | 必填 | 参考音频对应的文本内容 |
| `text_lang` | "zh"\|"en"\|"ja"\|"yue" | "zh" | 合成文本的语言 |
| `prompt_lang` | "zh"\|"en"\|"ja"\|"yue" | "zh" | 参考音频的语言 |
| `api_url` | str | "http://localhost:9880" | GPT-SoVITS API 地址 |
| `speed` | float | 1.0 | 语速控制 (0.5-2.0) |
| `top_k` | int | 5 | 采样参数，控制多样性 |
| `top_p` | float | 0.8 | 核采样参数 |
| `temperature` | float | 0.8 | 温度参数，控制随机性 |

## 使用示例

### 基础用法

```python
from tools.gpt_sovits_tts import gpt_sovits_text_to_audio

response = gpt_sovits_text_to_audio(
    text="你好，这是一个测试。",
    ref_audio_path="./voice_samples/my_voice.wav",
    prompt_text="这是参考音频的文本内容",
)

# response.content[0] 包含 AudioBlock
```

### 在 Agent 中使用

```python
from agentscope.agent import ReActAgent
from agentscope.tool import Toolkit
from tools.gpt_sovits_tts import gpt_sovits_text_to_audio

toolkit = Toolkit()
toolkit.register_tool_function(gpt_sovits_text_to_audio)

agent = ReActAgent(
    name="Jarvis",
    sys_prompt="你是一个智能助手。当用户要求语音回复时，使用 gpt_sovits_text_to_audio 工具。",
    toolkit=toolkit,
    # ... 其他配置
)
```

## 常见问题

### Q: 连接失败怎么办？

**错误信息：** `无法连接到 GPT-SoVITS API`

**解决方法：**
1. 确认 GPT-SoVITS 服务已启动
2. 检查服务地址是否正确（默认 `http://localhost:9880`）
3. 使用浏览器访问 http://localhost:9880/docs 确认服务可用

### Q: 合成效果不理想？

**优化建议：**
1. 使用更高质量的参考音频（清晰、无背景音）
2. 参考音频时长建议 10-30 秒
3. 调整 `temperature` 和 `top_p` 参数
4. 确保 `prompt_text` 与参考音频内容完全匹配

### Q: 支持哪些音频格式？

**支持格式：** WAV（推荐）

**格式转换：**
```bash
# 使用 ffmpeg 转换
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

## 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                      agent_demo 项目                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────┐      ┌──────────────────┐                  │
│  │ ReActAgent  │─────▶│ GPTSoVITS Tool   │                  │
│  │  (Jarvis)   │      │  (自定义工具)    │                  │
│  └─────────────┘      └────────┬─────────┘                  │
│                                │                             │
│                                ▼                             │
│                        ┌──────────────┐                      │
│                        │ HTTP API     │                      │
│                        │ localhost:9880│                    │
│                        └──────┬───────┘                      │
│                               │                              │
└───────────────────────────────┼──────────────────────────────┘
                                │
                                ▼
                        ┌──────────────────┐
                        │  GPT-SoVITS      │
                        │  本地服务        │
                        └──────────────────┘
```

## 参考资料

- [GPT-SoVITS GitHub](https://github.com/RVC-Boss/GPT-SoVITS)
- [GPT-SoVITS API 文档](https://m.blog.csdn.net/weixin_42596246/article/details/156244872)
- [10分钟上手！WSL2极速部署](https://m.blog.csdn.net/gitblog_00860/article/details/152100921)

## 许可证

本项目遵循 MIT 许可证。
