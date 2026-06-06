---
tags:
  - 社区工具
  - 工作流
  - CLI
  - OpenClaw
aliases:
  - Lobster
  - ACPX
  - 社区工具更新
---

# Lobster 工作流 Shell

> **一句话总结**：Lobster（921 Stars）和 ACPX（1,500 Stars）是 2026 年 3 月 OpenClaw 社区涌现的两个重要工具，分别解决了工作流编排和 headless Agent 客户端的需求。

## Lobster

| 属性 | 内容 |
|------|------|
| **Stars** | 921 |
| **类型** | Typed workflow shell |
| **核心功能** | YAML 管道定义、审批门控（approval gates） |

Lobster 是一个面向 Agent 工作流编排的 typed shell。它允许用户通过 YAML 定义 Agent 执行管道，并在关键节点设置审批门控，实现**人在回路（Human-in-the-loop）**的 Agent 工作流控制。

### 设计亮点

- **YAML 管道**：声明式定义 Agent 工作流，而非命令式脚本
- **审批门控**：在关键操作前暂停等待人类确认，直接回应了 [[案例-Summer Yue 邮件删除灾难]] 等失控事件中暴露的"停止机制不可靠"问题
- **Typed Shell**：类型化的 shell 环境，减少运行时错误

## ACPX

| 属性 | 内容 |
|------|------|
| **Stars** | 1,500 |
| **类型** | Agent Client Protocol (ACP) 的 headless CLI 客户端 |

ACPX 是 Agent Client Protocol 的命令行客户端，允许开发者在无图形界面的环境中与 Agent 交互，适用于 CI/CD、服务器端自动化、批量 Agent 操作等场景。

## 社区工具生态的成熟

这两个工具的出现标志着 [[OpenClaw 社区工具|社区工具生态]] 从"展示层"（监控面板、Web UI）向"工程层"（工作流编排、协议客户端）深化：

1. **Lobster** 填补了 Agent 工作流编排的空白——此前 OpenClaw 缺乏声明式的多步骤工作流定义方式
2. **ACPX** 使 Agent 操作可以嵌入自动化管道，是 Agent 在企业 DevOps 流程中落地的关键一步
3. 两者都与 [[MCP 协议]] 的标准化方向一致，推动 Agent 工具从"演示级"走向"生产级"

## 相关笔记

- [[OpenClaw 社区工具]] — 社区工具全览
- [[社区项目速览]] — 更多社区项目
- [[MCP 协议]] — Agent 协议标准化
- [[ACP v1 生态扩展]] — Agent-编辑器协议标准化（ACPX 是 ACP 的 CLI 客户端）
- [[安全边界与风险（总览）]] — 审批门控的安全意义
- [[企业级整合方案]] — Agent 企业部署

## 外部链接

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [ClawHub](https://clawhub.dev)
