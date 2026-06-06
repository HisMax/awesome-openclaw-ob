---
tags:
  - Vibe-Coding
  - 编程范式
  - AI
aliases:
  - 氛围编程
  - 自然语言编程
---

# Vibe Coding


![[assets/vibe-coding.jpg]]

## 定义

Andrej Karpathy 提出的概念：不再逐行写代码，而是通过自然语言描述意图，让 AI 生成代码。这一理念与 [[编程民主化]] 运动密切相关。

## 起源

2025 年 2 月 2 日，Karpathy 在 X 上发布：

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."

这条推文获得 **450 万+浏览量**，迅速传播到纽约时报、Ars Technica、The Guardian 等主流媒体。

2025 年 11 月，**柯林斯词典将"vibe coding"评为 2025 年度词汇**。

## 一周年回顾（2026.2）

Karpathy 写道：
> "This was a shower of thoughts throwaway tweet that I just fired off without thinking, but somehow it minted a fitting name at the right moment."

他还提出了更专业的术语 **"agentic engineering"**——"agentic"因为新的默认方式是编排 Agent 而不是直接写代码，"engineering"强调其中涉及的专业知识。详见 [[Agentic Coding]]。

## OpenClaw 如何促进 Vibe Coding

[[OpenClaw 是什么|OpenClaw]] 天然适合 Vibe Coding 实践：

1. **消息界面降低心理门槛**：通过多频道发消息比打开 IDE 轻松得多
2. **Agent 自主编写技能**：当现有技能不够用时，Agent 可以自己写代码
3. **错误处理透明化**：执行循环中 AI 遇到错误会自己尝试修复，用户只看到最终结果

## Vibe Coding 的局限

HN 社区的清醒声音：
> "Falls apart when faced with the types of things that are actually difficult in software development."

**结论**：Vibe Coding 适合原型和简单应用，复杂工程仍需专业开发者。值得警惕的是，Vibe Coding 让编程更容易的同时，也让安全漏洞更容易产生——当开发者"forget that the code even exists"时，[[AI 代码生成安全问题|AI 生成代码中的安全隐患]]也被一并忽略了。

[[Peter Steinberger|Steinberger]] 的自嘲：
> "I do agentic engineering... maybe after 3am I switch to vibe coding, then have regrets."

## 2026年3月：融资爆发

Vibe Coding 从概念变成了资本市场的热门赛道。Lovable 融资 3.3 亿美元（估值 66 亿）、Cursor 融资 23 亿美元、Replit 估值飙升至 90 亿美元。Salesforce 推出 Agentforce Vibes，LinkedIn 推出 Vibe Coding 技能认证。详见 [[Vibe Coding 融资爆发]]。

## 2026年中：安全危机与"VibeSec 清算"

Vibe Coding 的高速扩张开始暴露严重后果：

**安全数据恶化**：
- **40-62%** 的 AI 生成代码包含安全缺陷
- AI 未能防御跨站脚本攻击（XSS）的概率高达 **86%**
- 2026 年 3 月单月新增 **35 个 CVE** 直接归因于 AI 生成代码（1 月仅 6 个）
- 一款纯 vibe coding 开发的应用发生重大数据泄露，暴露 **150 万 API 密钥 + 3.5 万用户邮箱**

**行业反思**：
- Martin Fowler 发表《VibeSec Reckoning》，系统批判 vibe coding 的安全隐患
- Apple 从 App Store 下架无法保证安全的 vibe coding 应用
- 开源社区报告大量 AI 生成的低质量 PR 和代码涌入，影响维护负担
- 2026 年美国开发者中 **92%** 日常使用 AI 编码工具，全球 **41%** 代码由 AI 生成——规模放大了安全风险

**从 Vibe Coding 到 Agentic Engineering**：Karpathy 本人已将注意力转向 "agentic engineering"，承认 vibe coding 适合原型但不足以支撑生产工程。行业正从"忘记代码存在"转向"编排 Agent 做专业工程"。详见 [[Agentic Coding]]。

## 相关笔记

- [[OpenClaw 是什么]]
- [[Vibe Coding 融资爆发]] — 2026年3月融资数据
- [[Agentic Coding]] — Vibe Coding 的进化方向
- [[ACP 协议]] — Agent 编排的标准化协议
