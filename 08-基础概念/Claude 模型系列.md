---
title: Claude 模型系列
aliases: [Claude, Anthropic Claude, Claude AI]
category: 模型分析
created: 2026-03-14
updated: 2026-06-06
tags: [Anthropic, Claude, LLM, Constitutional-AI]
---

# Claude 模型系列


![[assets/claude-models.jpg]]

> **一句话本质：** Claude 是 [[Anthropic 公司分析|Anthropic]] 打造的"安全优先"大语言模型家族，用三个尺寸（Haiku/Sonnet/Opus）覆盖从轻量到旗舰的全部场景，核心差异化在于 [[Constitutional AI]] 训练方法带来的可控性。

## 家族架构：三级火箭

| 层级 | 定位 | 典型用途 | 4.6版定价（每百万token） |
|------|------|----------|--------------------------|
| **Haiku** | 快速低成本 | 分类、摘要、批量处理 | ~$1/$5 |
| **Sonnet** | 平衡之选 | 日常编码、知识工作 | $3/$15 |
| **Opus** | 最强智能 | 复杂推理、研究、Agent | $5/$25 |

设计哲学：同代 Sonnet 的能力通常接近上一代 Opus，但成本只有三分之一。这让用户可以"按需选型"而非"一律用最贵的"。

## 版本演进关键节点

- **Claude 3**（2024.03）：确立 Opus/Sonnet/Haiku 三级体系，引入视觉能力
- **Claude 3.5 Sonnet**（2024.06）：小模型打败大模型，重塑行业认知
- **Claude 3.7 Sonnet**（2025.02）：Extended Thinking——混合推理模式，复杂问题质量跃升
- **Claude 4**（2025.05）：专业级编码能力，[[Claude Code 分析|Claude Code]] 成为开发者日常工具
- **Claude 4.5 Opus**（2025.11）：降价67%，高端智能平民化
- **Claude Opus 4.6**（2026.02）：Agent 团队协作、1M 上下文 GA、多 Agent 协调
- **Claude Sonnet 4.6**（2026.02）：Computer Use 准确率达94%，首次在编码评测中超越上代 Opus
- **Claude Opus 4.7**（2026.04.16）：SWE-bench Verified 87.6%、Pro 64.3%，复杂软件工程和视觉能力大幅提升
- **Claude Opus 4.8**（2026.05.28）：SWE-bench Verified 88.6%、Pro 69.2%，搭载 [[Dynamic Workflows]] 大规模 Agent 编排，4x 低于 4.7 的代码缺陷遗漏率，支持 Fast Mode（2.5x 吞吐）
- **Claude Mythos Preview**（2026.04.07）：网络安全专用旗舰模型，SWE-bench Verified 93.9%，通过 Project Glasswing 向 150+ 组织（15+ 国家）提供零日漏洞发现能力，尚未公开发布

## Constitutional AI：Claude 的灵魂

不同于 OpenAI 的 RLHF 路线，Anthropic 采用 Constitutional AI（CAI）：

1. 制定一套明确的"宪法"原则（如诚实、无害、有帮助）
2. 让模型先自我批评、自我修正
3. 再用 AI 反馈（RLAIF）替代部分人类标注

结果：Claude 在拒绝有害请求时更稳定，且推理过程更透明（Extended Thinking 可见思维链）。

## 在 OpenClaw 中的使用

OpenClaw 默认推荐 Claude 作为主力模型，原因：
- Extended Thinking 适合多步骤 Agent 任务
- 工具调用（Tool Use）原生支持，与 [[MCP 协议]] 深度集成
- 长上下文（1M tokens）支持全代码库分析
- 安全边界清晰，减少 Agent 失控风险

## 与 GPT 的差异化

| 维度 | Claude | GPT |
|------|--------|-----|
| 安全哲学 | Constitutional AI, 原则驱动 | RLHF, 人类反馈驱动 |
| 编码强项 | 长上下文理解、重构 | 广泛工具生态、Computer Use |
| 推理风格 | Extended Thinking（可见思维链） | 可配置推理深度（5级） |
| 开放程度 | 闭源 | 部分开源（gpt-oss-120b） |

## 延伸阅读

- [[OpenClaw 是什么]] — Agent 框架中的 Claude 角色
- [[Claude Code 2026年3月更新]] — v2.1.81 搭载 Opus 4.6（100万 token 上下文）
- [[Dynamic Workflows]] — Opus 4.8 搭载的大规模 Agent 编排能力
- [[ACP 协议]] — Claude Code 原生支持的编辑器-Agent 通信标准
