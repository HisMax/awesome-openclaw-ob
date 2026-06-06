---
tags:
  - 人物
  - 事件
  - 安全
  - Cyera
  - 漏洞披露
  - OpenClaw
aliases:
  - Cyera Research
  - Cyera 安全团队
  - Vladimir Tokarev
  - Claw Chain 披露事件
  - Cyera Claw Chain
---

# Cyera Research 与 Claw Chain 披露


![[assets/cyera-disclosure.jpg]]

## 一句话理解

> 以色列数据安全公司 Cyera 的研究团队发现了 OpenClaw 历史上最严重的漏洞组合"Claw Chain"，通过负责任披露流程给予 OpenClaw 团队充足的修复时间，最终使约 24.5 万个暴露实例免于被链式利用攻击——这是 AI Agent 安全领域迄今最具影响力的漏洞披露事件。

## Cyera 公司背景

| 属性 | 信息 |
|------|------|
| **全称** | Cyera Inc. |
| **成立** | 2021 年 |
| **总部** | 以色列 |
| **联合创始人** | Yotam Segev（CEO）、Tamar Bar-Ilan（CTO） |
| **背景** | 两位创始人均为以色列国防军 **Unit 8200**（信号情报部队）老兵 |
| **核心业务** | 数据安全态势管理（DSPM） |
| **技术特点** | 无 Agent 架构，AI/ML 混合平台，快速部署，混合环境即时数据发现 |

Cyera 不是传统意义上的漏洞挖掘公司，而是专注于企业数据安全的平台型公司。Claw Chain 的发现来自其**安全研究部门**对 AI Agent 生态的前瞻性安全审计。这种"数据安全公司发现 Agent 平台漏洞"的模式，体现了 AI Agent 安全问题的跨领域特征——数据安全与 Agent 安全正在融合。

## 研究员：Vladimir Tokarev

Claw Chain 四个漏洞的发现和报告归功于 Cyera 研究员 **Vladimir Tokarev**。他独立发现了跨越沙箱隔离、命令验证和身份认证三个不同层面的四个漏洞，并论证了它们的链式利用可能性。

这种跨层面的链式漏洞发现需要对 OpenClaw 的完整架构有深入理解——从 [[沙箱机制|OpenShell 沙箱]]的文件系统桥接层，到命令允许列表的 shell 执行层，再到 MCP 回环运行时的身份验证逻辑。

## Claw Chain 发现过程

### 研究动机

OpenClaw 作为 2025 年末以来增长最快的开源 AI Agent 平台，直接连接 LLM 与文件系统、SaaS 应用、凭证和执行环境。对于像 Cyera 这样关注数据安全的公司，这种架构天然是高风险审计目标：**一个拥有海量权限的自主 Agent，其安全边界在哪里？**

### 四个发现

Tokarev 的研究跨越了 OpenClaw 架构的三个关键层面：

```
┌─────────────────────────────────────────────┐
│               沙箱隔离层                      │
│  CVE-2026-44112 (写 TOCTOU) CVSS 9.6        │
│  CVE-2026-44113 (读 TOCTOU) CVSS 7.7        │
├─────────────────────────────────────────────┤
│             命令验证层                        │
│  CVE-2026-44115 (Heredoc 泄露) CVSS 8.8     │
├─────────────────────────────────────────────┤
│             身份认证层                        │
│  CVE-2026-44118 (MCP 回环提权) CVSS 8.2     │
└─────────────────────────────────────────────┘
```

关键洞见在于：**每个漏洞单独来看可能只是"高危"，但链式组合后实现了从沙箱内受限执行到宿主机完全控制的完整 kill chain**。这正是"Claw Chain"命名的含义。

详细技术分析见 [[Claw Chain 四漏洞链]]。

## 负责任披露流程

### 时间线

| 时间 | 事件 |
|------|------|
| 2026 年 4 月初 | Cyera 向 OpenClaw 维护团队私下报告全部四个漏洞 |
| 2026 年 4 月 | OpenClaw 团队确认漏洞，开始修复 |
| 2026-04-23 | OpenClaw 发布 **v2026.4.22**，修复全部四个 CVE |
| 补丁发布后 ~25 天 | Cyera 留出足够的时间窗口供用户更新 |
| 2026-05-18 | Cyera 公开发布技术详情博文 |

### 披露策略分析

Cyera 采用了**经典的负责任披露**（Coordinated Vulnerability Disclosure）模式：

1. **私下通知**：先向维护者报告，不公开技术细节
2. **协同修复**：给予维护者充足时间开发和测试补丁
3. **补丁优先**：确保修复版本发布后再公开
4. **缓冲期**：补丁发布后等待约 25 天，给用户更新窗口
5. **完整披露**：最终发布详细技术博文，供安全社区学习

### 与 ClawJacked 披露的对比

| 维度 | Claw Chain（Cyera） | [[ClawJacked 远程代码执行漏洞\|ClawJacked]]（Oasis Security） |
|------|---------------------|----------------------------------------------|
| 漏洞数量 | 4 个链式 | 1 个 |
| 修复周期 | ~3 周 | 24 小时协调披露 |
| 影响规模 | ~245,000 实例 | ~15,200 实例 |
| 最高 CVSS | 9.6 | 8.8 |
| 披露后缓冲 | ~25 天 | 较短 |

两次披露都体现了安全研究社区对 OpenClaw 生态的积极贡献——通过负责任披露而非公开利用来推动修复。

## 影响评估

### 直接影响

- **约 245,000 个公开暴露实例**获得了修复机会（v2026.4.22）
- **四个 GHSA** 同步发布：GHSA-5h3g-6xhh-rg6p、GHSA-wppj-c6mr-83jj、GHSA-r6xh-pqhr-v4xh、GHSA-x3h8-jrgh-p8jx
- 涉及金融、医疗、法律等敏感行业的部署被紧急通知

### 行业影响

1. **CSA（云安全联盟）** 发布了专题研究报告，将 Claw Chain 作为 AI Agent 安全的标杆案例分析
2. **Dark Reading、The Hacker News、SecurityWeek** 等主要安全媒体广泛报道
3. 推动了对 AI Agent 沙箱设计的重新审视——TOCTOU 问题在容器化 Agent 中可能是系统性的
4. 进一步强化了 [[安全厂商评估汇总|安全厂商]] 对 OpenClaw 的负面评估

### 对 OpenClaw 修复能力的验证

Claw Chain 也从侧面验证了 OpenClaw 团队的安全响应能力：从接到报告到发布修复约 3 周时间，同时处理了四个跨不同架构层的漏洞。虽然漏洞不应该存在，但响应效率是值得肯定的。

## Cyera 的更广泛 AI 安全研究

Claw Chain 不是孤立的发现。Cyera 作为数据安全公司，其安全研究部门正在系统性地审视 AI Agent 生态对企业数据安全的威胁。这种"从数据安全视角审计 Agent 平台"的方法论，可能代表了 AI Agent 安全研究的一个重要方向：

- Agent 有权访问哪些数据？
- 数据在 Agent 工作流中的边界在哪里？
- 沙箱是否真的隔离了数据访问？

Claw Chain 的答案是：**沙箱并不可靠，数据边界可以被突破**。

## 相关笔记

- [[Claw Chain 四漏洞链]]
- [[沙箱机制]]
- [[ClawJacked 远程代码执行漏洞]]
- [[大规模实例暴露]]
- [[安全厂商评估汇总]]
- [[2026年Q2安全态势总览]]
- [[安全边界与风险（总览）]]

## 外部链接

- [Cyera Blog - Claw Chain 原始披露](https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw)
- [Cyera Research 团队介绍](https://www.cyera.com/team/cyera-research)
- [Contrary Research - Cyera 公司分析](https://research.contrary.com/company/cyera)
- [Dark Reading - Claw Chain Vulnerabilities](https://www.darkreading.com/application-security/claw-chain-vulnerabilities-threaten-openclaw)
- [WebProNews - Quarter-Million Agents Exposed](https://www.webpronews.com/claw-chain-exposes-quarter-million-openclaw-agents-to-stealthy-takeovers/)
