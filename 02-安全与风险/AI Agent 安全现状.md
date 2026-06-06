---
tags:
  - 安全
  - Agent
  - 数据
aliases:
  - Agent安全
  - AI Agent 安全
---

# AI Agent 安全现状

## 2026 年行业数据

| 指标 | 数值 |
|------|------|
| 报告 AI Agent 安全事件的组织 | **88%** |
| 对整个 Agent 队伍有完整安全审批的组织 | 仅 **14.4%** |
| 无安全监督或日志运行的 Agent | **超过一半** |
| 部署活跃 AI Agent 的 Fortune 500 企业 | **超过 80%** |
| 通过安全基准的生产 Agent（AIRQ 2026 Q2） | 仅 **11%** |
| OpenClaw CVE 累计数量（截至 2026-05） | **472+** |

详细的 2026 年安全数据分析见 [[AI Agent 安全态势 2026]] 和 [[2026年Q2安全态势总览]]。

## 核心矛盾

AI Agent 的**采用速度远超安全边界的建设速度**。

[[OpenClaw 是什么|OpenClaw]] 是这个矛盾的最极端体现：
- 84 天 200K stars → 但安全团队为零
- 14,706 个技能 → 7.5% 恶意率（[[RankClaw ClawHub 审计]]全量审计）、41.7% 热门 Skill 含漏洞
- **245,000** 个暴露实例（详见 [[大规模实例暴露]]） → 但[[沙箱机制]]默认关闭

## 根本性问题

> 提示注入是否能被解决？如果不能，Agent 的能力边界在哪里？

这是 2026 年底前行业需要回答的核心问题。当前共识：**安全性和实用性之间的根本矛盾短期内无法消除**——这正是 [[致命三合一安全矛盾]] 所描述的结构性困境。权限控制机制 和 安全最佳实践 提供了缓解方案，但无法从根本上解决。

## 来源

- Dark Reading
- Gravitee - State of AI Agent Security 2026 Report

## 相关笔记

- [[安全边界与风险（总览）]]
- [[Prompt Injection 风险]]
- [[沙箱机制]]
- [[Karpathy 的 Claws 概念]]
- [[代码执行安全]]
- [[数据泄露风险]]
- [[ClawJacked 远程代码执行漏洞]]
- [[Claw Chain 四漏洞链]] — 245K 实例受影响
- [[2026年Q2安全态势总览]] — 最新安全数据

## 外部链接

- [Snyk Blog - AI Agent Security](https://snyk.io/blog/)
- [NIST AI Standards](https://www.nist.gov/artificial-intelligence)
