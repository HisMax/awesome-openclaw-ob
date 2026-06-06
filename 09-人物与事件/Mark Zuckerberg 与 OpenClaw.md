---
tags:
  - 人物
  - 事件
  - Meta
  - AI竞争
  - Agent
aliases:
  - Zuckerberg
  - Meta CEO
  - 大厂Agent争夺
---

# Mark Zuckerberg 与 OpenClaw

> **一句话总结**：Meta CEO 亲自联系 Steinberger，与 Sam Altman 竞争争夺 OpenClaw 创始人，反映大厂对个人 AI Agent 赛道的激烈争夺，但 Meta 自身因安全漏洞已禁止内部使用 OpenClaw。

## 核心要点

- Fortune 报道 Zuckerberg **亲自向 Steinberger 伸出橄榄枝**，与 [[Sam Altman]] 竞争
- Meta 早在 2026 年 2 月中旬已因安全漏洞（CVE-2025-6514 等）**禁止内部使用 OpenClaw**
- [[案例-Summer Yue 邮件删除灾难|Summer Yue 邮件删除灾难]]进一步凸显了 Meta 对 Agent 安全的担忧
- 最终 Steinberger 选择了 OpenAI，Zuckerberg 未能如愿

## 详细内容

### 亲自出手——大厂争夺的信号

Fortune 2026.2.19 的深度报道揭示，Zuckerberg 亲自联系 [[Peter Steinberger]]。这个细节极为重要——Meta 拥有 30 亿+用户的社交平台生态（Facebook、Instagram、WhatsApp），WhatsApp 本身就是 OpenClaw 最主要的通信渠道之一。

如果 Meta 获得了 Steinberger，OpenClaw 可能直接整合进 WhatsApp 的 **20 亿用户**生态，这将是 AI Agent 历史上最大规模的分发。

### Meta 的 AI Agent 战略（2026.2 → 6 月更新）

| 维度 | 2026.2 状态 | 2026 年中最新 |
|------|------|------|
| 公开 Agent 产品 | 未发布独立 Agent 产品 | Meta AI 应用推出订阅制（$7.99/$19.99/月） |
| 内部 AI 投入 | Superintelligence Labs（前 FAIR） | Superintelligence Labs 发布首个模型 |
| AI 基础设施 | — | **Meta Compute** 计划：数十 GW 级数据中心 |
| AI 资本开支 | — | **$1,250-1,450 亿**（2026 全年，较 2025 的 $722 亿近翻倍） |
| 开源 LLM | LLaMA 系列 | **Llama 4 Scout/Maverick**（MoE 架构，1000 万 token 上下文，200+ 语言） |
| 新模型 | — | **Muse Spark**（Q2 发布） |
| OpenClaw 内部使用 | **已禁止**（2026.2 中旬） | — |
| 云服务 | — | Zuckerberg 称云计算业务"definitely on the table" |

Zuckerberg 在 2026 Q1 财报中宣称是"里程碑季度"，表示 Meta"正在按计划向数十亿用户交付个人超级智能"。

### 矛盾之处：禁而后争

Meta 在 2 月中旬因安全漏洞禁止内部使用 [[OpenClaw 是什么|OpenClaw]]，同时 Zuckerberg 又在争夺其创始人。这种矛盾反映了大厂对 Agent 赛道的复杂态度：

1. **风险认知**：安全团队清楚 Agent 的安全隐患（[[致命三合一安全矛盾]]）
2. **战略紧迫**：但又不能让竞争对手占据这一赛道
3. **人才争夺**：获取关键人才比获取代码更有价值

### Summer Yue 事件的内部冲击

[[案例-Summer Yue 邮件删除灾难|Summer Yue]]（Meta Superintelligence Labs 对齐总监）的 OpenClaw 邮件删除事件获得 **960 万次浏览**，成为 Agent 安全讨论的标志性事件。她事后自嘲：

> "Rookie mistake tbh. Turns out alignment researchers aren't immune to misalignment."

### 大厂 Agent 竞赛格局（2026.2 → 6 月更新）

| 公司 | 2026.2 动作 | 最新进展 |
|------|------|------|
| **OpenAI** | 收编 Steinberger + 赞助基金会 | GPT-5.5 发布，Codex 全面开放，200 万+周活跃用户 |
| **Meta** | Zuckerberg 亲自出手争夺，收购 Moltbook | Llama 4 发布，Meta AI 订阅制上线，$1,250 亿+ AI 资本开支 |
| **Anthropic** | Claude Cowork + 商标执法 | [[Claude Mythos]] 发布，$650 亿 Series H，近万亿估值，[[Andrej Karpathy]] 加入 |
| **Google** | Project Mariner + Gemini Code Assist | Gemini 3.5 agentic era（I/O 2026），[[GTIG 首次确认 AI 生成零日事件|GTIG AI 零日报告]] |
| **Microsoft** | Copilot Tasks + AutoGen | 持续迭代 |

### 为什么 Steinberger 选择了 OpenAI 而非 Meta？

源文件未直接说明原因，但可以推断：
- [[Sam Altman]] 的公开背书更具影响力（推文 450 万浏览）
- OpenAI 明确承诺保持 OpenClaw 开源和模型中立
- Meta 内部已禁止 OpenClaw，战略一致性存疑
- Steinberger 提前致电 Altman 确认新名称不侵权，关系更紧密

## 关键洞察

Zuckerberg 亲自出手这一细节，将个人 AI Agent 从"开源实验项目"提升到了"大厂战略级赛道"。Meta 拥有全球最大的即时通讯平台 WhatsApp（[[OpenClaw 是什么|OpenClaw]] 的核心通信渠道），如果整合成功将创造前所未有的 Agent 分发规模。但 Meta 的内部禁令与外部争夺之间的矛盾，完美体现了整个行业对 Agent 的核心困境：**它太危险了以至于不能用，但又太重要了以至于不能不争**。Gartner 最新数据显示 **17%** 的组织在生产环境部署了 Agent（较此前 8% 翻倍），但 **80%** 的 Fortune 500 已有活跃 Agent，部署与安全之间的鸿沟仍在扩大。

## 2026 年 3 月后续：收购 Moltbook

2026 年 3 月 10 日，Meta 正式收购了 [[Moltbook AI 社交网络|Moltbook]]。在未能争取到 Steinberger 之后，Meta 选择直接收购 OpenClaw 生态中最知名的衍生项目，从"争人"转向"争平台"。详见 [[Meta 收购 Moltbook]]。
