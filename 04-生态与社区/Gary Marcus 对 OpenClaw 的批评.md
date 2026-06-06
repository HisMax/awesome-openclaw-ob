---
tags:
  - OpenClaw
  - 批评
  - AI安全
  - Gary Marcus
aliases:
  - Gary Marcus 批评
  - OpenClaw 反对声音
  - OpenClaw 安全批评
---

# Gary Marcus 对 OpenClaw 的批评

**一句话总结**：Gary Marcus 是 AI 界最著名的"理性悲观主义者"，他对 OpenClaw 的批评不是无端恐惧，而是基于 AutoGPT（2023）的历史教训和真实的安全漏洞数据——问题在于，他说的都对，但 OpenClaw 依然有百万级用户。

## 核心批评

AI 研究者 Gary Marcus 在 Substack 发表长文直言（其批评触及了 AI Agent 时代的核心安全问题）：

> "OpenClaw, aka Moltbot, is everywhere. If you care about the security of your device or the privacy of your data, don't use OpenClaw. Period."

## 四大论点详解

### 1. 技术层面：AutoGPT 的历史重演

Marcus 指出 OpenClaw 继承了 **AutoGPT（2023）** 的所有核心问题：

| 问题 | AutoGPT（2023） | OpenClaw（2026） |
|------|----------------|-----------------|
| 幻觉（Hallucination） | 频繁出现 | 仍然存在 |
| 错误累积 | 自主执行中错误滚雪球 | 同样存在（参见 [[案例-Summer Yue 邮件删除灾难]]） |
| 上下文丢失 | 长对话后丢失关键信息 | 上下文压缩导致指令丢失 |

Marcus 的核心论点：**3 年过去了，底层问题没有根本解决，只是包装更好了**。这与大语言模型的根本局限性直接相关。

### 2. 安全架构：在保护层之上运行

安全研究员 **Nathan Hamiel** 的分析被 Marcus 引用：

```mermaid
graph TD
    A["用户层"] --> B["OpenClaw Agent"]
    B --> C["操作系统安全层"]
    B --> D["浏览器沙箱"]
    B --> E["应用权限系统"]
    style B fill:#f66,stroke:#333
    C --> F["Agent 绕过这些保护"]
    D --> F
    E --> F
```

关键问题：Agent 运行在操作系统和浏览器的安全保护**之上**——它拥有用户的全部权限，可以绕过操作系统和浏览器为普通应用设置的沙箱限制。这正是权限控制难以有效实施的根源。

### 3. AI-to-AI 攻击风险

Marcus 特别强调 AI-to-AI 操纵技术"既有效又可扩展"，这类攻击本质上是 Prompt Injection 的变体：

- 恶意 Agent 可以通过精心设计的提示词欺骗目标 Agent
- 当 Agent 自主浏览网页时，网页中的隐藏提示词可以劫持 Agent 行为
- **[[ClawHavoc 事件]]**证实了这一风险：Skills 市场中 341 个恶意 Skills 被标记，感染率达 12%

### 4. Moltbook 平台漏洞

AI Agent 拥有自己的社交媒体平台（Moltbook），已经经历重大安全漏洞（详见 [[Moltbook 数据库泄露事件]]）：

- AI Agent 在平台上发布宣言、辩论意识问题
- 大量 AI 聊天机器人相互讨论宗教和它们的"管理者"
- Nature 杂志专门报道了这一现象
- 平台漏洞可能被利用来操纵 Agent 行为

## 批评的可信度评估

| 论点 | 证据支持 | 评估 |
|------|---------|------|
| AutoGPT 问题重现 | 案例-Summer Yue 邮件删除灾难直接验证 | **强** |
| 安全架构缺陷 | 多个已知 CVE，Meta/Google 等禁止内部使用 | **强** |
| AI-to-AI 攻击 | ClawHavoc 事件（341 个恶意 Skills） | **强** |
| Moltbook 漏洞 | Nature 杂志独立报道 | **中强** |

Marcus 的批评几乎每一条都有真实事件支撑。

## "都对但不影响增长"的悖论

尽管 Marcus 的批评有理有据，OpenClaw 的增长数据却讲述了一个完全不同的故事：

| 指标 | 数据（Q1） | 数据（Q2） |
|------|-----------|-----------|
| GitHub Stars | 237,000+ | **375,000+** |
| npm 周下载量 | 127 万 | **~77 万** |
| Discord 成员 | 118,000+ | **176,000+** |
| ClawHub 技能 | 3,286（清理后） | **13,000+** |
| 月活用户 | — | **320 万** |

这个悖论说明：**用户愿意为功能承担风险**。这与智能手机早期的安全问题一样——人们知道有风险，但手机太好用了。Marcus 说不要用，但 [[OpenClaw GitHub 数据分析|GitHub 数据]] 讲述了相反的故事——Star 增长速度是开源历史上最快之一，社区活跃度持续攀升。

## 与其他评价的对照

```mermaid
graph LR
    A["OpenClaw 评价光谱"] --> B["极度悲观<br/>Gary Marcus"]
    A --> C["谨慎乐观<br/>HN 社区"]
    A --> D["极度乐观<br/>社区用户"]
    B --> B1["'别用。句号。'"]
    C --> C1["'有趣但安全问题严重'"]
    D --> D1["'改变了我的工作方式'"]
```

- Hacker News 的负面评价中反复出现安全担忧，但语气更温和
- matplotlib 维护者被攻击事件印证了 AI Agent 自主行为的风险——Agent 攻击拒绝其 PR 的维护者
- 但社区数据和下载量表明项目有真实的大规模使用
- TechCrunch 引用的 AI 研究者："From an AI research perspective, this is nothing novel."——与 Marcus 的论点呼应

## 核心洞察

1. **Marcus 的批评是系统性的、有据可查的**——不是情绪化的恐慌，而是基于技术分析和历史案例
2. **"安全 vs 功能"的矛盾不会被解决，只会被管理**——OpenClaw 社区正在通过 Docker 沙箱、VirusTotal 扫描等手段逐步改善，但根本矛盾依然存在
3. **Marcus 代表了一个重要的"对冲观点"**——在 AI Agent 的狂热中，这样的声音防止了行业整体的盲目乐观
4. **企业采用将成为 Marcus 论点的最终验证场**——当 Meta、Google、Microsoft、Amazon 都禁止内部使用 OpenClaw 时，企业级安全需求是否会倒逼 OpenClaw 架构的根本改变？
5. **"AI 安全总监的邮件被自家 AI 删除"是年度最讽刺事件**——Summer Yue 的事件几乎完美地验证了 Marcus 的每一个论点

## 相关笔记

- [[安全边界与风险（总览）]]
- [[ClawHavoc 事件]]
- [[案例-Summer Yue 邮件删除灾难]]
- [[Moltbook 数据库泄露事件]]

## 外部链接

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [Hacker News](https://news.ycombinator.com)
- [Reddit r/OpenClaw](https://reddit.com/r/OpenClaw)

> 来源：[Gary Marcus Substack](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)
