---
tags:
  - OpenClaw
  - 产品定义
  - AI-Agent
aliases:
  - OpenClaw
  - OpenClaw 定义
  - OpenClaw 概览
---

# OpenClaw 是什么


![[assets/openclaw-what-is.jpg]]

OpenClaw 是一个**免费、开源的自主 AI Agent 框架**，运行在用户本地设备上，通过 WhatsApp、Telegram、Discord 等即时通讯应用作为交互界面，连接外部大语言模型（Claude、GPT、DeepSeek 等）来自主执行任务。

> "Your own personal AI assistant. Any OS. Any Platform. The lobster way."

## 产品定位

OpenClaw 将 AI Agent 视为**基础设施问题**而非仅仅是提示工程问题。LLM 负责智能，OpenClaw 负责操作系统层——会话管理、记忆系统、工具沙箱、访问控制和消息路由。

> "OpenClaw treats AI as an infrastructure problem. The LLM provides intelligence; OpenClaw provides the operating system."

## 核心能力

1. **多频道收件箱**：支持 13+ 通讯平台（WhatsApp、Telegram、Slack、Discord、Signal、iMessage、Teams 等）
2. **多代理路由**：不同频道/对话路由到隔离的 Agent 实例
3. **语音唤醒 + 对话模式**：macOS/iOS/Android 常驻语音，集成 ElevenLabs
4. **Live Canvas**：Agent 驱动的可视化工作空间（A2UI: Agent-to-UI）
5. **浏览器控制**：通过 Chrome DevTools Protocol 控制浏览器
6. **技能/插件系统**：ClawHub 上 13,000+ 个社区技能
7. **持久记忆**：SQLite + 向量嵌入的混合搜索记忆系统
8. **Heartbeat 主动监控**：每 30 分钟检查一次，主动通知用户

## 关键数据（截至 2026.6）

| 指标 | 数值 |
|------|------|
| GitHub Stars | **375,000+**（GitHub 历史最高 starred 项目） |
| Contributors | 1,200+ |
| 月活用户 | 320 万 |
| 开源许可 | MIT License |
| 主要语言 | TypeScript |
| npm 包名 | `openclaw`（周下载 77 万+） |
| 创建时间 | 2025年11月24日 |
| Discord 成员 | 176,000+ |

## 为什么重要

OpenClaw **没有发明新的 AI 技术**。它的创新在于**工程整合**：
1. 把 LLM 的能力包装成"操作系统"
2. 用聊天应用作为通用 UI（人人都会用 WhatsApp）
3. 持久记忆让 Agent 成为真正的"助理"而非"一次性工具"
4. 开源 + 模型无关 = 任何人都能定制

> 不是技术突破，而是**[[可及性突破]]**。

## 最新动态（2026年4-6月）

- **v2026.4**：从"可组装平台"迈向"持久化运行时"——[[OpenClaw v2026.4 版本更新|Durable TaskFlow]] 让工作流具备状态持久化能力，Memory-Wiki 赋予 Agent 结构化长期记忆，[[OpenClaw v2026.4 版本更新|Claw Chain 四漏洞修复]]暴露了沙箱安全的深层挑战，DeepSeek V4 Flash 成为新默认模型，运行时支持 6 种模型提供商热切换
- **v2026.5**：稳定性月——[[OpenClaw v2026.5 版本更新|十余个版本密集迭代]]，重心转向频道可靠性、启动性能瘦身、语音管道打磨（Google Meet + Twilio + Discord Voice Follow），核心安装瘦身将 WhatsApp/Slack/Bedrock 等移出默认安装
- **v2026.6**：治理月——[[OpenClaw v2026.6 版本更新|Auto Mode]] 用"策略→模型审核→人工兜底"三层架构替代粗暴的 YOLO 模式，[[Operator Install Policy]] 让运营者可配置安装策略，Skill Workshop 降低 Skill 创建门槛
- 安全方面仍需关注：[[RankClaw ClawHub 审计|RankClaw 审计]]发现 7.5% 恶意 Skills，[[Claw Chain 四漏洞链]] 等安全事件对生态构成持续压力

## 相关笔记

- [[OpenClaw 的起源与发展历程]]
- [[OpenClaw v2026.3 版本更新]] — 2026 年 3 月架构大变革
- [[OpenClaw v2026.4 版本更新]] — 持久化运行时转型
- [[OpenClaw v2026.5 版本更新]] — 稳定性与语音管道成熟
- [[OpenClaw v2026.6 版本更新]] — 治理与策略执行
- [[Dashboard 控制面板]] — Web 管理界面
- [[Provider-Plugin 架构]] — 模型提供商插件化
- [[可插拔沙箱后端]] — 可替换的执行环境
- [[Agent Execution Loop]]
- [[Agent-Flow-Loop 原理]]
- [[Tool Use 机制]]
- [[安全边界与风险（总览）]]
- [[Claude Code 的技术架构]]

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [Anthropic 官网](https://anthropic.com)
