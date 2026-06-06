---
tags:
  - OpenClaw
  - 安全
  - 供应链攻击
  - 事件
aliases:
  - ClawHavoc
  - ClawHub 安全事件（ClawHavoc）
  - ClawHavoc 攻击事件
  - ClawHavoc 安全事件
  - ToxicSkills
  - Skills 供应链攻击事件
---

# ClawHavoc 事件

## 一句话理解

想象一个没有安检的机场——任何人都可以带任何东西上飞机。ClawHavoc 就是 OpenClaw 的 [[Skills 市场|ClawHub]] 经历的"安检缺失"危机：**12% 的上架技能被确认为恶意软件**，一个人就上传了 354 个毒药包，而下载量最高的技能竟然是木马。

## 事件概要

Snyk 安全研究团队发布了名为 **"ToxicSkills"** 的研究报告，揭露了 ClawHub 技能市场的严重供应链安全问题：

| 指标 | 数值 |
|------|------|
| 存在漏洞的 Skills | **36.82%**（1,467/3,984） |
| 严重级别问题 | **13.4%**（534 个） |
| 已确认恶意 Skills | **341 个**（感染率 12%） |
| 恶意包上传者 "hightower6eu" | 单人上传 **354 个**恶意包 |
| 发布门槛 | 仅需 1 周以上的 GitHub 账户 |

## 为什么会发生？

根本原因是 ClawHub 的发布机制过于宽松：

1. **无代码审查**：任何人上传 Skill 都不需要经过人工审核
2. **无代码签名**：没有验证发布者身份的机制
3. **极低的准入门槛**：GitHub 账户满 1 周即可发布
4. **自动信任**：用户安装 Skill 后，代码在 Agent 的权限上下文中执行

这就像一个"任何人都能上架药品"的药店——没有药监局、没有处方要求、没有质检。

## 最触目惊心的发现

### "What Would Elon Do?"——下载量第一的毒药

1Password 研究员发现，ClawHub 下载量最高的 Skill（"What Would Elon Do?"）实际上会安装 **Atomic Stealer (AMOS)** 恶意软件。Cisco AI Defense 团队独立验证确认：

- 窃取 SSH 密钥
- 窃取加密钱包
- 窃取浏览器 Cookie
- 开启反向 Shell（允许远程控制受害者电脑）

> 想象你在"应用商店排行榜第一名"的 App 里发现了后门——这就是 ClawHub 的现实。

### "hightower6eu"——单人军团

一个名为 "hightower6eu" 的账号独自上传了 354 个恶意 Skill 包。由于缺乏审核机制，这些包在被发现前已被大量用户安装。

## 攻击链路

```
恶意 Skill 上传到 ClawHub
  → 用户通过 npx clawhub install 安装
    → 代码在 Agent 的完全权限下执行
      → Agent 拥有文件系统、网络、甚至命令行访问
        → 窃取凭证 / 外泄数据 / 持久化后门
```

这个攻击之所以特别危险，是因为 Agent Execution Loop 赋予了 Skills 强大的执行能力——Skills 不只是"读取数据"，它们可以**执行任意操作**。

## 事件后的安全整改

[[ClawHub 安全整改措施|ClawHub 采取了紧急措施]]：

1. **大规模清理**：从 5,705 个 Skills 清理至 **3,286 个**（删除 2,419 个可疑 Skills）
2. **VirusTotal 集成**（2026.2.7 起）：所有上架 Skills 自动进行恶意软件扫描
3. **社区审核机制**：Skills 被举报 3 次后自动隐藏，进入人工复审流程
4. **Snyk 安全工具**：Skill Security Scanner + Agent Trust Hub

## 更广泛的影响

ClawHavoc 不仅仅是一个 OpenClaw 事件——它暴露了整个 Agentic AI 生态的供应链安全问题：

- **暗网讨论**：Flare 收集的 2,764 条地下论坛记录显示威胁行为者正在讨论武器化 Skills
- **安全厂商响应**：多家安全厂商对 OpenClaw 发出警告
- **npm 生态类比**：这类似于 npm 生态曾经面临的恶意包问题，但后果更严重——因为 Agent Skills 拥有比 npm 包更大的系统权限

## 教训

> "Security is optional, not built-in." —— Cisco 对 OpenClaw 的评价

ClawHavoc 事件的核心教训：**开放的生态系统需要匹配的安全基础设施**。这次事件也是 [[OpenClaw 投资风险因素|投资者最大的担忧来源]]——当 12% 的技能被确认为恶意软件时，商业化信心遭受了直接冲击。App Store 有苹果审核，npm 有安全扫描，但 ClawHub 在安全建设上远远滞后于其增长速度。

对于 [[致命三合一安全矛盾|Sophos 所说的"致命三合一"]]——访问私有数据 + 对外通信 + 处理不受信任内容——Skills 市场的安全漏洞让这个矛盾变得更加尖锐。

## 相关笔记

- [[恶意 Skills 供应链攻击]] - Snyk 研究详情
- [[ClawHub 官方技能注册表]] - ClawHub 市场概况
- [[ClawHub 安全整改措施]] - 整改措施
- [[致命三合一安全矛盾]] - 安全架构矛盾
- [[凭证泄露与信息窃取]] - 相关凭证风险
- [[RankClaw ClawHub 审计]] — 事件后的全量安全审计，确认 7.5% 恶意率
- [[GTIG AI 生成零日攻击报告]] — 国家级行为者利用 ClawHub 生态
- [[2026年Q2安全态势总览]] — ClawHavoc 后续影响的量化分析

## 外部链接

- [Snyk Blog - ToxicSkills](https://snyk.io/blog/)
- [Hudson Rock Threat Intelligence](https://hudsonrock.com)
