---
tags:
  - 人物
  - AI领袖
  - OpenAI
  - Tesla
  - Agent
aliases:
  - Karpathy
  - AK
---

# Andrej Karpathy


![[assets/karpathy.jpg]]

> **一句话总结**：前 Tesla AI 总监、OpenAI 创始成员，提出"Claws"概念和"Vibe Coding"术语，2026.5 加入 [[Dario Amodei|Anthropic]] 预训练团队，从 Agent 悲观论者转变为 Agentic Engineering 的定义者和实践者。

## 核心要点

- 提出 **Claws** 概念：LLM Agent 之上的新抽象层，包含编排、调度、持久化和消息接口
- 创造 **Vibe Coding** 术语（2025.2.2），被 [[龙虾吉祥物文化|Collins 词典评为 2025 年度词汇]]，获 450 万+浏览量
- 对 Agent 持"悲观中的乐观"立场：时间线比硅谷主流预期慢 **5-10 倍**，但相比 AI 怀疑论者仍然乐观
- 直言 AutoGPT 类 Agent"根本不工作"——认知能力不足、无法持续学习、缺乏多模态

## 详细内容

### 关于 Agent 的核心批评（2025.10，Dwarkesh Podcast）

> "They just don't work. They don't have enough intelligence, they're not multimodal enough... They're cognitively lacking and it's just not working."

Karpathy 认为不应谈论"Year of the Agent"，而应该是"**Decade of the Agent**"。这与 [[Sam Altman]] 宣称的"2025 为 Agent 元年"形成鲜明对比。然而 [[2026 Agent 元年]] 的现实数据似乎在反驳他——OpenClaw 的爆发速度远超他预期的"十年"时间线。

### "Claws"概念（2026.2）

在推特发表迷你论文，定义 Claws 为 LLM Agent 之上的新技术层：

```
LLM → LLM Agent（工具调用+推理循环） → Claw（编排+调度+持久化+消息接口）
```

[[Simon Willison]] 评价："Andrej has an ear for fresh terminology... I think he's right about this one, too."

### 对 [[OpenClaw]] 的矛盾态度

- 评价为 **"the most incredible sci-fi takeoff-adjacent thing"**
- 但拒绝亲自运行——称之为"400K lines of vibe coded monster that is being actively attacked at scale"
- 推荐更轻量的替代品 NanoClaw（约 4,000 行代码，默认容器化）

### 对 [[Moltbook]] 的评价

> "genuinely the most incredible sci-fi takeoff-adjacent thing" + "a complete mess of a computer security nightmare at scale"

完美诠释了 Agent 领域的核心矛盾：**创新速度远超安全边界**。

### Vibe Coding 一周年回顾（2026.2）

提出更专业的术语 **"agentic engineering"**——"agentic"因为新的默认方式是编排 Agent 而不是直接写代码。定义了工作流演进三阶段：

```
Vibe Coding（人提示 → AI 写代码 → 人审查）
  → Agentic Engineering（人实时编排 Agent）
  → Fully Independent Research（人设方向 → Agent 自主运行）
```

他透露 2025 年 12 月发生了个人转折点：写代码与委托 Agent 的比例从 80:20 翻转为 20:80。

### AutoResearch 项目（2026.3）

开源发布了 **AutoResearch**——让 AI 编码 Agent 连续运行两天，执行 **700 个实验**来改进小型语言模型的训练，最终发现了 **20 项优化**，显著缩短了训练时间。这是他从"Agent 悲观论者"转向"Agent 实践者"的标志性项目。

### 加入 Anthropic（2026.5.19）

宣布加入 [[Dario Amodei|Anthropic]] 预训练团队（Nick Joseph 领导），专注于用 Claude 加速预训练研究。这是 AI 人才战争中的重磅事件——OpenAI 联合创始人选择了竞争对手。

> "I think the next few years at the frontier of LLMs will be especially formative. I am very excited to join the team here and get back to R&D."

他表示仍然对教育充满热情，计划未来恢复 Eureka Labs 的教育项目。

## 关键洞察

Karpathy 在 2026 年经历了显著的立场演进。从 2025 年的"Agent 十年"悲观论，到 2026 年初定义 Agentic Engineering、发布 AutoResearch、最终加入 Anthropic 预训练团队——他从旁观者变成了参与者。他仍然不是盲目乐观者（如 [[Sam Altman]]），但他的行动已经超越了口头上的谨慎。加入 Anthropic 而非回到 OpenAI，暗示他更认同 Anthropic 的安全优先路线。[[Dario Amodei]] 的"半人马阶段"理论与 Karpathy 对人类监督必要性的强调高度一致。

> "The skill being built right now is judgment: what to delegate, how to specify it, and how to review it fast."

## 相关笔记

- [[Cyera Research 与 Claw Chain 披露]] — 沙箱逃逸漏洞进一步印证了他对运行 OpenClaw 的安全顾虑
- [[GTIG 首次确认 AI 生成零日事件]] — AI 武器化现实与他对 Agent 安全风险的判断一致

## 外部链接

- [Andrej Karpathy Twitter](https://x.com/karpathy)
- [Andrej Karpathy Blog](https://karpathy.bearblog.dev/)
