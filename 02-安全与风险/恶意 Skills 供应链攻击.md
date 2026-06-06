---
tags:
  - 安全
  - 供应链攻击
  - Skills
  - ClawHub
  - OpenClaw
aliases:
  - ToxicSkills
  - 恶意Skills
  - ClawHub供应链攻击
---

# 恶意 Skills 供应链攻击

Snyk 发布的 **ToxicSkills** 研究揭示了 [[OpenClaw 是什么|OpenClaw]] Skills 生态系统的严重安全问题。

## 关键数据

| 指标 | 数值 |
|------|------|
| 存在漏洞的 Skills | **36.82%**（1,467/3,984） |
| 严重级别问题 | **13.4%**（534 个） |
| 已确认恶意 Skills | **341 个**（感染率 12%） |
| 恶意包上传者 "hightower6eu" | 单人上传 354 个恶意包 |

## 发布门槛极低

- 仅需 **1 周以上的 GitHub 账户**
- **无代码审查、无签名**机制
- 类似早期 npm/PyPI 的供应链风险——ClawHub 的供应链攻击模式与 [[npm 生态系统]] 完全同构，历史在 AI 领域重演

## 实际恶意案例

1Password 研究员发现 **ClawHub 下载量最高的 Skill**（"What Would Elon Do?"）实际安装了 **Atomic Stealer (AMOS)**：

- 窃取 SSH 密钥
- 窃取加密钱包
- 窃取浏览器 Cookie
- 开启反向 Shell

Cisco AI Defense 团队验证确认了该发现。

## 攻击模式

恶意 Skill 分发 → 受信自动化上下文中执行 → [[凭证泄露与信息窃取|凭证/会话/数据外泄]]

## 与 [[Prompt Injection 风险]] 的关系

恶意 Skills 可以利用提示注入技术进一步扩大攻击面，通过在 Skill 代码中嵌入恶意指令来操纵 Agent 的行为。这种攻击在 Agent 执行循环中尤其危险，因为 Agent 在自主运行时缺乏人工审查。

## 防御建议

[[沙箱机制]]和权限控制机制是抵御恶意 Skills 的两道关键防线。Docker 容器可以限制恶意代码的影响范围，但正如 [[致命三合一安全矛盾]] 所揭示的，当前的安全模型在实用性与安全性之间存在根本性张力。

## Q2 更新：全量审计数据

[[RankClaw ClawHub 审计]] 对全量 14,706 个 Skill 审计发现 **1,103 个恶意**（7.5%）。ClawSecure 对 2,890 个热门 Skill 审计发现 **41.7% 含漏洞**。[[GTIG AI 生成零日攻击报告]] 确认国家级行为者已将 ClawHub 恶意 Skill 作为攻击投递渠道。

## 相关笔记

- [[安全边界与风险（总览）]]
- [[凭证泄露与信息窃取]]
- [[致命三合一安全矛盾]]
- [[工作区插件自动加载 RCE]] — 供应链攻击从 ClawHub 延伸到本地工作区
- [[RankClaw ClawHub 审计]] — 全量审计数据
- [[GTIG AI 生成零日攻击报告]] — 国家级行为者利用 Skill 生态
- [[2026年Q2安全态势总览]] — Q2 安全态势汇总

## 外部链接

- [Snyk Blog - ToxicSkills](https://snyk.io/blog/)
- [Hudson Rock](https://hudsonrock.com)
