---
tags:
  - 竞品对比
  - OpenClaw
  - Claude-Code
  - Remote-Control
aliases:
  - OpenClaw 对比 Remote Control
  - Claude Code Remote Control
---

# OpenClaw vs Claude Code Remote Control

> 2026.2.25 发布研究预览，仅限 Max 计划用户

| 维度 | [[OpenClaw 是什么|OpenClaw]] | [[Claude Code 分析|Claude Code]] Remote Control |
|------|----------|---------------------------|
| **发布** | 2026.1.30（更名后） | 2026.2.25 研究预览 |
| **架构** | 本地守护进程 + 消息应用桥接 | 纯出站 HTTPS，本地会话 → 手机/浏览器同步 |
| **本质** | 把 AI **内嵌到聊天 App** 里作为常驻助手 | 把**终端会话投射到手机上**远程操控 |
| **持久性** | 24/7 持续运行，关机才停 | 关闭终端即结束，网络断开 ~10 分钟超时 |
| **安全** | Docker 沙箱可选，密钥明文（[[OpenClaw 安全风险]]） | 纯出站 HTTPS，短期凭证，TLS 加密桥 |
| **模型** | 多模型自由切换 | 仅 Anthropic 模型 |

## 本质区别

- **Remote Control** 解决的是"离开电脑后继续操控编码会话"的问题，是 Agentic Coding 场景的延伸
- **OpenClaw** 解决的是"在日常聊天界面中拥有一个永不离线的 AI 助手"

二者目标场景完全不同，但都体现了 AI Agent 向更自主化方向的演进。

## 外部链接

- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code)

## 相关

- [[OpenClaw vs Claude Code]]
- [[Claude Code 分析]]
- [[竞品对比总览]]
- [[Claude Code 2026年Q2更新]] — Dynamic Workflows 进一步扩展远程操控价值
