---
title: GPT 模型系列
aliases: [GPT, OpenAI GPT, ChatGPT]
category: 模型分析
created: 2026-03-14
updated: 2026-06-06
tags: [OpenAI, GPT, LLM, ChatGPT]
---

# GPT 模型系列

> **一句话本质：** GPT（Generative Pre-trained Transformer）是 OpenAI 的旗舰大语言模型系列，从"能写文章的玩具"进化为"能操作电脑的全能智能体"，是当前商业化最成功的 LLM 家族。

## 演进时间线

| 版本 | 时间 | 里程碑意义 |
|------|------|-----------|
| GPT-3 | 2020.06 | 175B 参数，证明 scaling law |
| GPT-3.5 | 2022.11 | ChatGPT 发布，AI 出圈 |
| GPT-4 | 2023.03 | 多模态，通过律师/医生考试 |
| GPT-4o | 2024.05 | 原生多模态，语音实时对话 |
| GPT-5 | 2025 中 | 统一推理与生成，性能大幅提升 |
| GPT-5.2 | 2025 末 | 推理错误和幻觉显著减少，开源 gpt-oss-120b |
| GPT-5.3 Instant | 2026.03.03 | 400K 上下文，幻觉再降26.8% |
| GPT-5.4 | 2026.03.05 | 1M 上下文，原生 Computer Use，5级推理深度 |
| GPT-5.5 | 2026.04.23 | SWE-Bench Verified 88.7%，幻觉再降60%，MMLU 92.4% |
| GPT-5.5 Instant | 2026.05.05 | 替代 GPT-5.3 Instant 成为 ChatGPT 免费用户默认模型 |

## GPT-5.5：当前最新旗舰

GPT-5.5 是截至2026年6月 OpenAI 最强模型，于 2026 年 4 月 23 日发布，关键能力：

- **SWE-Bench Verified 88.7%**：超越 Claude Opus 4.7 的 87.6%，但在更难的 SWE-Bench Pro 上落后（58.6% vs Opus 4.7 的 64.3%）
- **MMLU 92.4%**：通用知识理解达到新高
- **幻觉降低 60%**：相比 GPT-5.4 大幅减少事实性错误
- **深度任务执行**：编写调试代码、在线研究、数据分析、创建文档和电子表格、操作软件等端到端任务

### GPT-5.5 Pro

$30/$180 每百万 token，使用更多计算资源进行深度推理，适合最高难度任务。

### GPT-5.5 Instant

2026 年 5 月 5 日发布，替代 GPT-5.3 Instant 成为 ChatGPT 所有用户（含免费用户）的默认模型。

## 定价与经济性

GPT-5.5 API 定价为 $5/$30 每百万 token（input/output），与 Claude Opus 4.8 的 $5/$25 接近。GPT-5.5 Pro 则为 $30/$180，面向高计算需求场景。性能相当的前提下，两家的成本差异已大幅缩小（详见 [[API 定价与成本分析]]）。

## 开源动作

OpenAI 发布了 **gpt-oss-120b**——117B 参数的 MoE 架构模型，MIT 许可证，性能接近 o4-mini。这是 OpenAI 在开源领域的重大转向，回应了 [[DeepSeek]] 等开源模型的竞争压力。

## 在 OpenClaw 中的集成

[[OpenClaw 是什么]] 通过 [[模型无关架构]] 支持 GPT 系列：

- GPT-5.5 适合需要全栈任务执行的复杂场景
- GPT-5.5 Instant 适合高频低延迟的批量任务
- OpenAI OAuth 仍支持第三方工具接入（与 Anthropic 封杀第三方 OAuth 形成对比）
- 通过统一的 API 抽象层切换，无需改动 Agent 逻辑
- 与 MCP 协议兼容的工具调用格式

## 遗留与淘汰

GPT-4o、GPT-4、GPT-3.5 已逐步淘汰。GPT-5.2 Thinking 已于 2026 年 6 月 5 日退役。GPT-5.3 Instant 被 GPT-5.5 Instant 替代。建议新项目直接使用 GPT-5.5。

## 延伸阅读

- [[DeepSeek]] — 开源竞争对手
