---
title: DeepSeek
aliases: [深度求索, DeepSeek AI, DeepSeek V3, DeepSeek R1]
tags: [DeepSeek, 开源, LLM, MoE, 中国AI, 性价比, OpenClaw]
created: 2026-03-15
updated: 2026-06-06
---

## 一句话总结

DeepSeek 是中国量化私募幻方量化孵化的开源大模型系列，用不到 OpenAI 十分之一的训练成本做出接近闭源前沿的效果——它是 OpenClaw 生态中性价比最高的模型选择。

## 核心功能

**模型矩阵**：

| 系列 | 参数 | 特点 |
|------|------|------|
| V3/V3.2 | 671B (MoE, 37B 激活) | 通用模型，免费使用，MLA + DeepSeekMoE |
| R1 | — | 推理专用，纯 RL 训练涌现推理能力，对标 o1 |
| R1-0528 | — | 幻觉减少 45-50%，接近 o3 和 Gemini 2.5 Pro |
| **V4-Pro** | 1.6T (MoE, 49B 激活) | 2026.04.24 发布，1M 上下文，CSA+HCA 混合注意力，SWE-bench Verified 80.6%（开源最高） |
| **V4-Flash** | 284B (MoE, 13B 激活) | 极致性价比，$0.14/$0.28 每百万 token，MIT 许可 |

**成本颠覆**：R1 推理 API 仅 $2.19/百万 token，OpenAI o1 要 $60——差距近 30 倍。训练成本约 $600 万 vs OpenAI 超 $1 亿。V4-Flash 更进一步将 API 成本压低至 $0.14/$0.28 每百万 token，Pro 也仅 $1.74/$3.48——开源 1M 上下文模型中无对手。

**技术创新**：
- Multi-head Latent Attention（MLA）：大幅降低 KV 缓存内存占用
- DeepSeekMoE：更细粒度的专家路由
- R1-Zero 路径：证明推理能力可不依赖人类标注数据涌现
- **V4 的 CSA+HCA 混合注意力**：Compressed Sparse Attention + Heavily Compressed Attention，在 1M token 上下文下仅需 V3.2 的 27% 推理 FLOPs 和 10% KV 缓存

## OpenClaw 中的应用

通过 [[模型无关架构]]，OpenClaw 可无缝切换到 DeepSeek：

| 场景 | 推荐模型 | 月费估算 |
|------|----------|----------|
| 成本敏感的日常 Agent | V3.2 | $13-18 |
| 需要深度推理 | R1 系列 | 按量计费 |
| 完全离线私有化 | 蒸馏小模型 via [[Ollama 本地模型运行|Ollama]] | $0 |

2026 年模型竞争格局中，DeepSeek V4-Pro-Max 以 SWE-bench Verified 80.6% 排名开源模型第一（总榜第6），证明了开源模型可以在编码任务上逼近闭源前沿。DeepSeek V3/R1/V4 在推理和编码任务上的持续突破是底层能力飞跃的重要组成。中国用户称其为"value for money"——OpenClaw 中国社区中 DeepSeek 是最受欢迎的模型之一，配合智谱 GLM-5、Kimi K2.5 等国产模型形成本土化部署方案。

DeepSeek 的成功还迫使 OpenAI 开源 gpt-oss-120b，推动了整个行业的开源转向，与 [[GPT 模型系列]] 和 [[Claude 模型系列]] 形成三足鼎立格局。

## 关键洞察

DeepSeek 改写了"做好 AI 必须烧大钱"的行业叙事。对 OpenClaw 生态而言，DeepSeek 的价值不仅是省钱——MIT 许可证的全面开源意味着企业和个人可以完全私有化部署，数据不出内网。这与 OpenClaw 的 [[AI 基础设施思维|本地优先哲学]] 完美契合。R1-Zero 的纯 RL 训练路径更是一个深远信号：如果推理能力可以在没有人类标注的情况下涌现，那么 AI Agent 的自主能力天花板可能比我们想象的更高。

## 相关笔记

- [[大语言模型]] — LLM 技术全景与对比
- [[模型无关架构]] — 为什么 Agent 框架不应绑死模型
- [[开源AI运动]] — 开源 vs 闭源的行业博弈
- [[Transformer 架构]] — DeepSeek 基于 Transformer 的 MoE 创新
- [[Ollama 本地模型运行]] — 本地运行 DeepSeek 蒸馏模型
- [[竞品成本对比]] — DeepSeek 的成本优势量化
