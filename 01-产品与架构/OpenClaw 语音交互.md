---
tags:
  - 语音
  - 功能
  - OpenClaw
aliases:
  - TTS
  - 语音助手
---

# OpenClaw 语音交互

OpenClaw 支持多种语音交互方式，进一步降低使用门槛。

## 文字转语音（TTS）

- **ElevenLabs** 原生 TTS 支持，实现高质量语音输出
- Telegram 支持 **Opus 语音格式**（48kHz / 64kbps），语音消息清晰自然

## 语言学习 Skill

社区开发的语言学习技能：
- 支持 **30+ 主要语言**，包括普通话和粤语
- 用户通过语音对话练习外语，AI 实时纠正发音和语法
- 这类技能通过 ClawHub 发布，借助 [[Tool Use 机制]] 与外部语音 API 交互

详见 [[Skills 市场]]。

## Jupiter Voice

- **Apple Silicon 本地语音助手**
- 支持自定义唤醒词
- 在 Mac 上实现类似 Siri 的体验，但后端由 [[OpenClaw 是什么|OpenClaw]] Agent 驱动
- 通过 LLM 理解自然语言指令，结合自主决策循环执行复杂任务

## 2026 年 4-5 月语音管道成熟

v2026.4-5 标志着 OpenClaw 语音能力从"能用"变成"好用"：

- **v2026.4.25**：**Google Meet 集成**——Agent 作为参与者加入 Google Meet 会议，实时音频转写（基于 Gemini Live），Talk/Voice Call/Meet 三种语音场景统一为实时语音循环
- **v2026.5.4**：**Twilio Dial-in**——通过 Twilio 拨入 Google Meet 会话，带节奏的音频流和背压感知缓冲
- **v2026.5.20**：**Discord Voice Follow**——Agent 自动跟随用户加入 Discord 语音通话，语音上下文修复解决了误解口语指令的问题
- **v2026.5.22**：**Meeting Notes 插件**——自动启动会议捕获，手动转录导入，Discord 语音作为首个实时来源

详见 [[OpenClaw v2026.4 版本更新]] 和 [[OpenClaw v2026.5 版本更新]]。

## 意义

语音交互是编程民主化的进一步延伸——连文字输入都不需要，直接用语音与 AI Agent 对话。这也是可及性突破的重要组成部分。

## 相关笔记

- [[OpenClaw 是什么]]
- [[Tool Use 机制]]
- [[Skills 市场]]
- [[OpenClaw v2026.4 版本更新]] — Google Meet 集成与语音架构升级
- [[OpenClaw v2026.5 版本更新]] — Twilio、Discord Voice Follow 与 Meeting Notes

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [ElevenLabs](https://elevenlabs.io)
