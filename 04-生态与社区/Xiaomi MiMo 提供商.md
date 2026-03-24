---
tags:
  - OpenClaw
  - 提供商
  - 小米
  - 中国
  - 2026年3月
aliases:
  - Xiaomi Provider
  - MiMo V2
  - 小米 MiMo
  - MiMo V2 Pro
  - MiMo V2 Omni
---

# Xiaomi MiMo 提供商

## 一句话理解

> 小米的大模型 MiMo V2 通过 v2026.3.22 正式进入 OpenClaw 生态——这不只是多了一个模型选项，更是中国消费电子巨头从"硬件制造商"向"AI 基础设施参与者"转型的信号。

## 技术实现

- 切换至 `/v1` OpenAI 兼容端点（简化集成复杂度）
- 支持 **MiMo V2 Pro** 和 **MiMo V2 Omni** 两个模型变体
- 由 @DJjjjhao 在 PR #49214 中贡献
- 通过 [[Provider-Plugin 架构]] 作为标准提供商插件注册

## MiMo V2 系列

| 模型 | 定位 |
|------|------|
| MiMo V2 Pro | 高性能通用推理 |
| MiMo V2 Omni | 多模态能力（文本+图像） |

## 中国 AI 生态意义

小米的加入与 [[Qwen DashScope 提供商|阿里 Qwen]]、[[Z.AI GLM 4.5-4.6 系列|智谱 GLM]] 共同构成了 OpenClaw 在中国模型生态的三足鼎立。结合 [[OpenClaw GitHub 数据更新 2026Q1|Tencent 和火山引擎的赞助]]，以及 [[飞书集成]] 的深度接入，OpenClaw 正在形成一个完整的中国 AI 基础设施适配层。

这呼应了 [[中国用户与 OpenClaw]] 中描述的市场热潮——社区中中国开发者已成为最活跃的贡献群体之一。

## 双链导航

- [[Provider-Plugin 架构]] — 提供商插件化架构
- [[Qwen DashScope 提供商]] — 阿里云模型提供商
- [[Z.AI GLM 4.5-4.6 系列]] — 智谱模型提供商
- [[中国用户与 OpenClaw]] — 中国市场热潮
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
