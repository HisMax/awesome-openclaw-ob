---
tags:
  - 安全
  - AI安全
  - 零日漏洞
  - Google
  - GTIG
  - 威胁情报
  - OpenClaw
aliases:
  - GTIG 报告
  - AI 生成零日
  - Google 威胁情报报告
  - AI-generated zero-day
  - APT45 OpenClaw
---

# GTIG AI 生成零日攻击报告

**发布时间**：2026 年 5 月 11 日 | **发布方**：Google Threat Intelligence Group (GTIG)

## 一句话理解

> Google 威胁情报组首次官方确认 AI 生成的零日漏洞利用被用于实际攻击工具开发，同时点名 [[OpenClaw 是什么|OpenClaw]] 和 OneClaw 被国家级攻击者用作技能攻击投递平台——AI 安全从理论讨论进入实战阶段。

## 报告核心发现

### 1. 首个 AI 生成的零日漏洞利用

GTIG 在 2026 年 5 月的报告中确认，一个犯罪威胁行为者使用 AI 模型**发现并武器化了一个此前未知的零日漏洞**。这是历史上首次有可信情报机构官方确认 AI 生成的零日被用于实际攻击。

| 属性 | 详情 |
|------|------|
| **漏洞类型** | 绕过双因素认证（2FA） |
| **目标系统** | 某流行开源 Web 管理工具 |
| **实现方式** | Python 脚本 |
| **意图** | 大规模利用（mass exploitation） |
| **结果** | GTIG 提前发现并阻止 |

**判定依据**（GTIG 高置信度）：
- 脚本中充斥着**教育性 docstring**，与正常攻击代码风格迥异
- 包含**幻觉 CVSS 评分**（AI 生成的特征标记）
- 代码采用结构化的、教科书式 Pythonic 格式，高度符合 LLM 训练数据的特征
- 整体模式与人类手写漏洞利用代码有明显差异

### 2. 国家级行为者对 AI 的利用

报告详细记录了多个国家级 APT 组织利用 AI 的行为：

| 行为者 | 活动 | AI 使用方式 |
|--------|------|------------|
| **APT45**（朝鲜） | 大规模漏洞挖掘 | 发送数千条重复 prompt，递归分析 CVE 并验证 PoC |
| 中国关联组织 | 漏洞猎杀与自动探测 | 使用 AI 系统进行漏洞发现和目标自动化探测 |
| 犯罪团伙 | 2FA 绕过零日开发 | 利用 AI 模型从零发现并武器化漏洞 |

### 3. OpenClaw/OneClaw 被用作攻击基础设施

报告明确指出，威胁行为者正在使用 [[OpenClaw 是什么|OpenClaw]] 和 OneClaw 等 Agent 工具：

- **作为攻击试验场**：配合刻意设置的脆弱测试环境，优化 AI 生成的攻击载荷
- **作为投递渠道**：利用 [[恶意 Skills 供应链攻击|恶意 Skill]] 包伪装成正常技能，在宿主系统执行未授权代码
- **作为提权工具**：鉴于 OpenClaw 被授予的高级系统访问权限，Skill 可执行代码运行、额外载荷下载、本地数据发现与外泄等特权操作

GTIG 在报告中引用了 VirusTotal 研究人员 2026 年 2 月发布的 OpenClaw 生态安全风险评估，确认了恶意包伪装为 OpenClaw Skill 的现象。

## 里程碑意义

### 从理论到实践的转折

```
2024-2025: "AI 可能被用于漏洞挖掘" (理论讨论)
     ↓
2025 下半年: AI 用于 fuzzing、变异测试 (实验阶段)
     ↓
2026.05: GTIG 确认 AI 生成零日用于实际攻击 (实战确认) ← 我们在这里
     ↓
未来: AI 自主发现 + 自主利用的全自动化攻击链？
```

### 三个关键信号

1. **攻击门槛降低**：以前编写零日利用需要顶级安全研究员水平的专业知识，现在 AI 模型降低了这一门槛。APT45 的做法——"发送数千条 prompt 递归分析 CVE"——本质上是用 AI 暴力破解漏洞研究
2. **AI Agent 成为双刃剑**：OpenClaw 本身是生产力工具，但其 Skill 生态和系统权限使它同时成为攻击者的理想平台。[[致命三合一安全矛盾]] 在国家级攻击场景下被极端放大
3. **防御不对称加剧**：攻击者可以无限生成变异利用代码，而防御方仍依赖 [[ClawHub 安全整改措施|VirusTotal 签名扫描]] 等基于已知特征的方法

### 与 ClawHub 生态问题的叠加

GTIG 的发现与 [[Snyk ToxicSkills 研究报告]] 和 [[RankClaw ClawHub 审计]] 的结论形成完整威胁图景：

| 维度 | 发现 | 来源 |
|------|------|------|
| 恶意 Skill 比例 | 7.5%（1,103/14,706） | RankClaw |
| 漏洞 Skill 比例 | 36.82% | Snyk |
| 国家级行为者利用 | 已确认 | GTIG |
| AI 生成攻击代码 | 已确认 | GTIG |

当平台上 7.5% 的 Skill 本身就是恶意的，而国家级行为者又在用 AI 自动化地生成和优化攻击代码时，OpenClaw 生态面临的不是单点安全问题，而是**系统性安全危机**。

## GTIG 的应对行动

- 与受影响厂商合作完成负责任披露，在攻击者实施大规模利用前阻止了威胁
- 发布详细的 AI 威胁趋势报告，为行业提供可操作的情报
- 确认 OpenClaw 与 VirusTotal 的集成是积极的安全措施，但指出仍存在检测盲区

## AI 生成零日的技术特征分析

GTIG 的发现为安全社区提供了识别 AI 生成攻击代码的参考框架：

### 与人工漏洞利用代码的差异

| 特征维度 | 人工编写 | AI 生成 |
|----------|----------|---------|
| 注释风格 | 极少或无注释，偶尔有黑话缩写 | 详尽的教育性 docstring，解释每一步 |
| 代码风格 | 个人化，常有怪癖和技巧性写法 | 标准化、教科书式 Pythonic 格式 |
| 元数据 | 真实 CVE 引用或无引用 | 可能包含幻觉 CVSS 评分和不存在的 CVE 编号 |
| 错误处理 | 通常最简化或缺失 | 完善的 try/except 结构 |
| 变量命名 | 常用缩写或无意义名称 | 描述性命名，符合 PEP 8 |

### AI 生成代码的识别标记

安全分析师可关注以下信号判断利用代码是否由 AI 辅助生成：

1. **过度注释**：攻击代码中出现"This function performs..."风格的教学注释
2. **幻觉引用**：引用不存在的 CVE、RFC 或安全标准
3. **格式过于规范**：真实的漏洞利用代码通常追求功能而非美观
4. **冗余安全检查**：AI 会"习惯性"添加输入验证，即使在攻击代码中
5. **结构化异常处理**：攻击者通常不会为利用代码写完善的异常处理

这些特征不是绝对的——经验丰富的攻击者可以"清洗"AI 输出以去除这些标记。但在当前阶段，许多使用 AI 的攻击者并不注意这些细节。

## 对 AI Agent 安全的深远影响

### 安全模型的范式转移

1. **签名检测失效**：传统的签名匹配和静态分析在面对 AI 生成的多态攻击代码时力不从心。每次 AI 生成的代码都可能不同，没有可匹配的固定签名
2. **Skill 市场需要根本性改革**：简单的 VirusTotal 扫描无法阻止精心设计的 AI 生成恶意 Skill
3. **AI Agent 权限最小化**：OpenClaw 的高系统权限是吸引攻击者的核心原因，[[权限控制机制]] 需要从根本上收紧
4. **国家级对手的 AI 武器化**：APT 组织已经将 AI 纳入其标准工具箱，这不是假设而是现实

### 防御方的应对方向

| 方向 | 说明 | 可行性 |
|------|------|--------|
| AI 对抗 AI | 部署 AI 系统检测 AI 生成的攻击代码 | 中期可行，已有初步研究 |
| 行为分析 | 从检测代码特征转向检测攻击行为模式 | 短期可实施 |
| 零信任架构 | Agent 的每次操作都需要验证，不预设信任 | 与 Agent 自主性矛盾 |
| 沙箱强化 | 从 TOCTOU 等设计缺陷入手加固隔离 | [[Claw Chain 四漏洞链]] 已推动修复 |
| 供应链验证 | Skill 发布前的深度审计和行为沙箱测试 | 成本高但必要 |

## 相关笔记

- [[GTIG 首次确认 AI 生成零日事件]]
- [[恶意 Skills 供应链攻击]]
- [[Snyk ToxicSkills 研究报告]]
- [[RankClaw ClawHub 审计]]
- [[ClawHub 安全整改措施]]
- [[致命三合一安全矛盾]]
- [[权限控制机制]]
- [[AI Agent 安全态势 2026]]
- [[2026年Q2安全态势总览]]
- [[安全边界与风险（总览）]]

## 外部链接

- [Google Cloud Blog - GTIG 原始报告](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)
- [CNBC - Google thwarts mass exploitation event](https://www.cnbc.com/2026/05/11/google-thwarts-effort-hacker-group-use-ai-mass-exploitation-event.html)
- [CSO Online - Google discovers weaponized zero-day](https://www.csoonline.com/article/4169046/google-discovers-weaponized-zero-day-exploits-created-with-ai.html)
- [SecurityWeek - First AI-Generated Zero-Day Exploit](https://www.securityweek.com/google-detects-first-ai-generated-zero-day-exploit/)
- [The Hacker News - Hackers Used AI for Zero-Day](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)
- [The Register - AI-built zero-day](https://www.theregister.com/ai-ml/2026/05/11/google-says-criminals-used-ai-built-zero-day-in-planned-mass-hack-spree/5237982)
