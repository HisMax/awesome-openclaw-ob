---
tags:
  - 成本
  - API
  - LLM
aliases:
  - LLM API 成本
  - 模型定价
---

# API 定价与成本分析

OpenClaw 的[[模型无关架构]]让用户可以灵活选择 LLM 提供商，成本差异显著。

## 成本档位

| 使用强度 | 月费 | 典型配置 |
|----------|------|----------|
| 轻度 | $1-5 | 本地模型 + Haiku |
| 中度 | $20-50 | VPS + Sonnet |
| 重度 | $100-200 | VPS + Opus |
| 极端 | $400-700+ | 多 Agent + 重度 API |

## 降低成本的方式

1. **本地模型**：通过 [[Ollama 本地模型运行]] 运行免费本地模型，零 API 成本（但需要硬件支持）——Ollama 零成本方案是 API 定价的颠覆性替代
2. **中国本土模型**：智谱 GLM-5、Kimi K2.5 等，接近闭源模型能力但成本极低
3. **OpenRouter 路由**：多模型路由服务，接入 400+ LLM 模型

## 对比参考

- Claude Code 年化营收 $25 亿+，Anthropic 整体 ARR $470 亿（[[Anthropic Series H 融资|Series H 时点]]），说明 AI 编码工具的付费市场规模巨大
- [[Cognition Series D 融资|Cognition（Devin）]]ARR $4.92 亿，AI 编码 Agent 的付费意愿强劲
- OpenClaw 的免费策略形成差异化竞争
- [[2026 前沿模型竞争格局]] 中三大模型的定价差异（Gemini 成本仅为 Opus 的 1/7.5）直接影响用户选型

## 相关笔记

- [[模型无关架构]]
- [[2026 前沿模型竞争格局]]
- [[竞品成本对比]]

## 外部链接

- [Anthropic](https://anthropic.com)
- [OpenAI](https://openai.com)
