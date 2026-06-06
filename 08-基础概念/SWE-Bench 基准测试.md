---
tags:
  - 基准测试
  - 软件工程
  - AI编码
  - 评测
aliases:
  - SWE-Bench
  - SWE-Bench Verified
  - 软件工程基准
---

# SWE-Bench 基准测试


![[assets/swe-bench.jpg]]

## 一句话理解

> SWE-Bench 是衡量 AI 在真实开源代码库中自主修复 Bug 能力的标准基准——Claude Opus 4.6 以 80.8% 的成绩登顶，意味着每 5 个真实 Bug 它能独立修掉 4 个，这是评判 AI 编码能力最有说服力的指标之一。

## 核心概念

### 什么是 SWE-Bench

SWE-Bench（Software Engineering Benchmark）从 12 个主流 Python 开源项目（Django、scikit-learn、Flask 等）中收集真实的 GitHub Issue 和对应的 Pull Request，要求 AI 模型独立完成：

1. **理解 Issue 描述**（有时模糊、不完整）
2. **定位相关代码文件**（在大型代码库中搜索）
3. **编写修复代码**（生成 patch）
4. **通过原有测试**（不能破坏已有功能）

### SWE-Bench Verified

SWE-Bench 的人工验证子集，过滤掉了模糊或有争议的测试用例，被视为更可靠的评测标准。

### 2026 年竞争格局演进

**2026 年 2 月（16 天内三大模型发布）：**

| 模型 | SWE-Bench Verified | 发布日期 | 核心强项 |
|------|-------------------|---------|---------|
| **Claude Opus 4.6** | **80.8%**（当时最高） | 2026.2.5 | 精准生产 Bug 修复 |
| **Gemini 3.1 Pro** | 80.6% | 2026.2.19 | 最佳性价比（Opus 的 1/7.5） |
| **GPT-5.3 Codex** | 80.0% | 2026.2.5 | Terminal-Bench 77.3% |

**2026 年 6 月最新排名（截至 2026.06.02）：**

| 排名 | 模型 | SWE-Bench Verified | SWE-Bench Pro | 说明 |
|------|------|-------------------|---------------|------|
| 1 | **Claude Mythos Preview** | **93.9%** | — | 网络安全专用，未公开 |
| 2 | **Claude Opus 4.8** | **88.6%** | **69.2%** | Pro 榜全模型最高 |
| 3 | **GPT-5.5** | **88.7%** | 58.6% | Verified 接近 Opus 4.8 |
| 4 | **Claude Opus 4.7** | 87.6% | 64.3% | — |
| 6 | **DeepSeek V4-Pro-Max** | 80.6% | — | 开源最高 |

注意：OpenAI 已停止提交 Verified 分数，转推 SWE-bench Pro 基准（担忧训练数据污染）。目前总榜已有 97 个模型参评。

从 2025 年初 ~65% 到 2026 年中 ~89%，SWE-Bench Verified 的天花板在 15 个月内提升了近 25 个百分点。

### 与 OpenClaw 的关系

[[OpenClaw 是什么|OpenClaw]] 本身不参与 SWE-Bench 评测，但这个基准直接关系到其核心体验：

- OpenClaw 的 [[模型无关架构]] 意味着用户可以选择 SWE-Bench 成绩最好的模型
- [[Claude Code 的技术架构|Claude Code]] 凭借 Opus 4.8 的 88.6%（Verified）和 69.2%（Pro）在编码领域领先
- OpenClaw 的优势在编码之外：24/7 生活自动化

## 应用与影响

- **AI 编码能力标杆**：近 89% 意味着 AI 修 Bug 的能力已逼近专业开发者水平
- **Claude Code 年化营收 $25 亿**的基础：SWE-Bench 成绩直接支撑 Anthropic 的商业估值
- **多模型路由策略**：实际工程中，用 Gemini 处理高吞吐任务（成本低），用 Opus 处理高风险审计和重构（成绩高）——没有单一模型在所有场景都赢
- **局限性**：SWE-Bench 只测试 Python 项目的 Bug 修复，不覆盖新功能开发、架构设计、跨语言项目等场景

## 关键洞察

SWE-Bench Verified 接近 89% 是一个里程碑，但也容易被误读。它证明了 AI 能在**已知代码库中修复已知类型的 Bug**，但 SWE-Bench Pro 上最高分仅 69.2%（Opus 4.8），说明在更复杂的企业级工程任务上仍有显著差距。正如 Mercor 的 APEX-Agents 基准所示，在投行、咨询和法律的真实长程任务中，最好的模型首次完成率仍不到 25%。SWE-Bench 是窄领域的深度突破，不代表通用 Agent 能力的广度突破。OpenAI 停止提交 Verified 分数并转推 Pro 基准，也暗示了对数据污染问题的担忧——基准测试本身的可信度也在接受审视。

## 双链导航

- [[Claude 模型系列]] — Opus 4.6 的 80.8% 成绩
- [[Claude Code 的技术架构]] — SWE-Bench 成绩的直接受益者
- [[OpenClaw 是什么]] — 通过模型无关架构间接受益
- [[模型无关架构]] — 让用户选择最优 SWE-Bench 模型
- [[Agentic Coding]] — SWE-Bench 衡量的核心能力
- [[AI 代码生成宏观数据]] — 更广泛的 AI 编码数据
