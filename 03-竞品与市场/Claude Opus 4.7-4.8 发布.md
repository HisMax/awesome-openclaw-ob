---
tags:
  - Anthropic
  - Claude模型
  - 竞品动态
  - 2026年Q2
  - Opus
aliases:
  - Opus 4.7
  - Opus 4.8
  - Claude Opus 4.7
  - Claude Opus 4.8
---

# Claude Opus 4.7-4.8 发布

## 一句话理解

> 2026 年 Q2，Anthropic 连续发布两代 Opus 模型——4.7 在编码/推理/Agent 能力上全面超越 GPT-5.4，4.8 则以 SWE-Bench Pro 69.2% 和 Online-Mind2Web 84% 两项纪录确立了"最强编码+浏览器 Agent"地位，同时 Fast mode 将高端推理成本降至 1/3。

## 时间线

| 日期 | 事件 |
|------|------|
| 2026-04-16 | Opus 4.7 GA 发布 |
| 2026-04-23 | OpenAI 发布 [[GPT-5.5 发布\|GPT-5.5]]，直接竞争 |
| 2026-05-28 | Opus 4.8 GA 发布（史上最快 Opus 迭代间隔：42 天） |

两代 Opus 之间仅隔 42 天，远短于之前 70-75 天的典型迭代周期。这个节奏说明 Anthropic 在 GPT-5.5 发布后迅速做出了竞争性回应。

## Opus 4.7（2026-04-16）

### 编码与 Agent 能力全面提升

Opus 4.7 是一次"全面升级"——不是某个单项突破，而是在编码、推理、视觉、指令遵循等多个维度同时进步。

| Benchmark | Opus 4.6 | Opus 4.7 | GPT-5.4 | 说明 |
|-----------|----------|----------|---------|------|
| SWE-Bench Verified | 80.8% | **87.6%** | — | 实际软件工程能力 |
| SWE-Bench Pro | — | **64.3%** | 57.7% | 领先 GPT-5.4 6.6 分 |
| CursorBench | 58% | **70%** | — | IDE 集成编码能力 |
| MCP-Atlas | — | 领先 GPT-5.4 9.2 分 | — | 工具调用能力 |
| Rakuten-SWE-Bench | 基线 | **3x 提升** | — | 生产环境任务解决率 |

### 关键新特性

**视觉能力跃升**：最大图片分辨率从 1,568px / ~1.15MP 提升至 2,576px / ~3.75MP（3.3x 像素量提升）。这对需要分析 UI 截图、设计稿的 Agent 工作流影响重大。

**xhigh Effort Level**：新增介于 high 和 max 之间的 `xhigh` 努力等级。这个等级在后来的 [[Claude Code 2026年Q2更新|ultracode]] 模式中成为关键组件。

**Task Budgets（公测）**：支持为长时间运行的 Agent 会话设定 token 预算上限，解决了企业用户最关心的成本可控性问题。

**指令遵循精准度提升**：Opus 4.6 经常"创造性地解读"指令并跳过步骤，4.7 则严格按指令执行。这对 [[Agentic Coding]] 至关重要——Agent 的价值在于可靠地完成任务，而非"聪明地"偷懒。

### 需要注意的隐性成本

Opus 4.7 采用了新的 tokenizer，相同输入可能产生 1.0x~1.35x 的 token 数量（最多增加约 35%）。这意味着即使单价不变（$5/$25 per M tokens），实际账单可能上涨。

## Opus 4.8（2026-05-28）

### 编码 Benchmark 登顶

| Benchmark | Opus 4.7 | Opus 4.8 | GPT-5.5 | 差距 |
|-----------|----------|----------|---------|------|
| SWE-Bench Verified | 87.6% | **88.6%** | — | SWE-Bench Verified 接近饱和 |
| SWE-Bench Pro | 64.3% | **69.2%** | 58.6% | **领先 GPT-5.5 超 10 分** |
| Online-Mind2Web | — | **84%** | — | 最强浏览器 Agent |
| Computer-Use | — | **84%** | — | 桌面操作能力 |

SWE-Bench Pro 的 +4.9 分跃升是最有说服力的信号——SWE-Bench Verified 正在接近天花板（88.6%），而 Pro 版使用真实的、活跃维护的代码库，没有公开的 ground-truth 泄露，是更难、更接近现实的测试。

### Online-Mind2Web：84% 的意义

84% 的 Online-Mind2Web 分数意味着什么？这是首次有单一前沿模型跨入"让 AI 去订机票，它真的能完成全流程"的实用区间。在这个准确率下，AI 的失败率已经低于一个被 Slack 消息分心的初级员工。这使得真正的浏览器自动化产品成为可能。

### Fast Mode：高端推理成本的转折点

| 模式 | 定价（per M tokens） | 速度 | 适用场景 |
|------|----------------------|------|----------|
| Standard | $5 / $25 | 1x | 需要最高质量推理 |
| Fast | $10 / $50 | 2.5x | 编码辅助、批量处理 |

Fast mode 的定价是前代 Opus Fast mode 的 **1/3**。这不是简单的降价——它改变了高端模型的使用经济学。之前很多场景因为成本被迫使用 Sonnet，现在 Opus Fast 的性价比可能优于 Sonnet standard。

### 诚实度：4 倍改善

Opus 4.8 在自己写的代码中发现缺陷后主动指出的概率是 4.7 的 4 倍。这是 Anthropic 与 OpenAI 的哲学分野——Anthropic 押注"诚实和校准不确定性是下一个前沿"，而 OpenAI 押注"原始 Agent 吞吐量和 token 效率"。

## 定价对比

| 模型 | 输入 | 输出 | 上下文窗口 |
|------|------|------|-----------|
| Opus 4.7 Standard | $5 | $25 | 1M tokens |
| Opus 4.8 Standard | $5 | $25 | 1M tokens |
| Opus 4.8 Fast | $10 | $50 | 1M tokens |
| [[GPT-5.5 发布\|GPT-5.5]] | $5 | $30 | 1M tokens |
| GPT-5.5 Pro | $30 | $180 | 1M tokens |

Opus 4.8 Standard 在输出价格上比 GPT-5.5 便宜 $5/M tokens，且在 SWE-Bench Pro 上领先超过 10 分——性价比优势明显。

## 对 OpenClaw 的影响

### 竞争压力

1. **编码能力天花板持续抬高**：SWE-Bench Pro 69.2% 意味着纯模型驱动的编码 Agent 越来越接近"足够好"。OpenClaw 如果仅靠"用更好的模型"来差异化，空间正在收窄
2. **浏览器 Agent 实用化**：84% 的 Online-Mind2Web 意味着浏览器自动化从"demo 级"进入"生产级"，这对 OpenClaw 的 [[OpenClaw vs Google Project Mariner|浏览器 Agent 竞争]] 影响深远
3. **Fast mode 重塑经济性**：成本降至 1/3 使得更多场景可以直接用 Opus 而非 Sonnet，[[竞品成本对比]] 的格局发生变化

### 机会

1. **xhigh + Dynamic Workflows 的编排层**：模型能力的提升使得多 Agent 编排的价值更大——单个 Agent 更强，协作的产出就更高
2. **诚实度优势可以转化为信任壁垒**：在企业场景中，"AI 主动告诉你代码有问题"比"AI 默默通过有缺陷的代码"更有价值
3. **tokenizer 成本陷阱是护城河**：理解 token 计算的复杂性，为用户提供更透明的成本预估，是产品差异化的方向

## 相关节点

- [[Claude Code 2026年Q2更新]]——Opus 4.8 与 Dynamic Workflows 同日发布
- [[GPT-5.5 发布]]——直接竞争对手
- [[Anthropic Mythos 模型]]——Opus 之上的超级模型
- [[Claude Code 2026年3月更新]]——Opus 4.6 时代的 Claude Code
- [[竞品成本对比]]——模型定价的全景分析
- [[Claude 模型系列]]——Claude 模型家族完整演进
