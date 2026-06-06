---
tags:
  - 案例
  - 零人类公司
  - 多Agent
  - 自动化商业
  - OpenClaw
aliases:
  - MFS Corp
  - 零人类员工公司
  - AI公司
---

# 案例：MFS Corp 零人类员工 AI 公司


![[assets/mfs-corp.jpg]]

**项目**：MFS Corp，6 个自主 Agent 运行在 Proxmox 上，零人类员工，真实产生收入

## Agent 架构

| Agent | 角色 | 职责 |
|-------|------|------|
| **Morgan** | 参谋长（Chief of Staff） | 编排和协调所有 Agent |
| **Atlas** | IT 部门 | 24/7 监控，自动重启失败服务 |
| 运营 Agent | 运营部门 | 日常业务运营 |
| 工程 Agent | 工程部门 | 产品构建和开发 |
| 战略 Agent | 战略部门 | 内容发布、商业策略 |
| 加密 Agent | 加密部门 | 加密货币市场情报分析 |

## 关键数据

- 成本仅约 **$50/月**（大部分推理在 Ollama 本地运行）
- 基础设施：Proxmox PVE 9.1，48 核，503GB RAM，ZFS
- 可从 1 个编排者扩展到 15+ 专业化 Agent
- 甚至由 AI Agent "Ramsix" 自己撰写 DEV Community 文章

## 技术要点

这是 多Agent协作架构 的商业化极致案例，也是 自主执行与人机协作 频谱中"完全自主"一端的代表。与 [[案例-14个Agent协作系统]] 的技术探索不同，MFS Corp 已经在真实产生收入。Morgan 作为编排者的角色体现了 Agent-Flow-Loop 原理中"主 Agent 分配子任务"的模式。

成本控制方面，通过 Ollama 本地推理将月费控制在 $50（对比 API 定价与成本分析 中的云端方案），这与 [[案例-三个 AI 人格深度评测]] 的 €5-7/月 VPS 方案都说明了 OpenClaw 部署成本可以非常低。这种模型无关架构允许在本地和云端模型之间灵活切换，是商业化路径中降低运营成本的关键策略。该案例也从侧面验证了 Agentic AI 在商业运营中的可行性，以及 Tool Use 机制 对企业自动化的支撑能力。

## 来源

- [DEV Community - How I Automated My Entire Business with OpenClaw](https://dev.to/mfs_corp/how-i-automated-my-entire-business-with-openclaw-multi-agent-architecture-383c)
- [Hacker News Discussion](https://news.ycombinator.com)
- [Ars Technica - AI-Only Companies](https://arstechnica.com)

## 相关笔记

- [[案例-MFS Corp 零人类员工后续]] — 后续发展与行业跟进
- [[案例-14个Agent协作系统]]
- [[案例-三个 AI 人格深度评测]]
- [[案例-Nat Eliason 的 AI 创业实验]]
- [[案例-Citi 银行 Arc 平台]] — 企业级 AI Agent 平台的另一种路径
