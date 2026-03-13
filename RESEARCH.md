# Voice-to-Claude-Code 方案调研报告

## 1. 项目目标
在 Mac (M4/M3) 上实现通过语音转文字（STT）自动调用 Claude Code CLI。
- **核心触发**：全局快捷键（如 V 键）触发录音。
- **中文优化**：优先考虑阿里云（阿里大模型）的 ASR 服务。
- **自动化流**：语音 -> 文本 -> Claude Code 输入。

## 2. 语音转文字（STT）方案

### 2.1 阿里云智能语音交互（ASR）
- **推荐模型**：Qwen-ASR 或 Paraformer 实时语音识别。
- **优势**：针对中文深度优化，识别率极高，支持流式输出。
- **调用方式**：使用 `dashscope` Python SDK 或 WebSocket 接口。
- **M 系列芯片适配**：通过 Python 环境调用，无硬件兼容性问题。

### 2.2 本地替代方案（可选备选）
- **Whisper.cpp**：支持 Metal GPU 加速，M4/M3 上速度极快。
- **MLX-Audio**：Apple 官方为 Apple Silicon 优化的音频库。

## 3. Claude Code 调用方案
- **CLI 命令**：`claude`
- **非交互模式**：使用 `-p` (prompt) 参数。
  - 示例：`claude -p "帮我分析这段代码"`
- **Stdin 输入**：支持通过管道接收输入。
  - 示例：`echo "识别出的文本" | claude`

## 4. 全局快捷键触发方案 (macOS)

### 4.1 快捷指令 (Shortcuts) + AppleScript
- 创建一个“快捷指令”，绑定到快捷键。
- 使用 AppleScript 运行后台 Python 脚本进行录音和 ASR。

### 4.2 第三方工具 (推荐)
- **Keyboard Maestro**：最强大的 macOS 自动化工具，可绑定任意键（包括 V 键长按或双击）触发脚本。
- **Raycast / Alfred**：通过插件形式触发。
- **BetterTouchTool**：支持复杂的按键映射。

## 5. 技术架构设计
1. **监听层**：Keyboard Maestro 监听 V 键按下。
2. **录音层**：Python 脚本调用麦克风（PyAudio/SoundDevice）录制音频。
3. **识别层**：将音频流发送至阿里云 ASR API，获取文本。
4. **执行层**：将文本作为参数传递给 `claude -p`。
5. **反馈层**：通过 macOS 通知或浮窗显示识别状态。

## 6. 后续计划
1. 创建 GitHub 仓库。
2. 编写核心 Python 脚本示例。
3. 整理配置文档。
