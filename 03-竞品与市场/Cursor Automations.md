---
tags:
  - Cursor
  - 自主编码
  - 竞品动态
  - 2026年3月更新
aliases:
  - Cursor Automations
  - Cursor 自动化
---

# Cursor Automations

2026 年 3 月 5 日，Cursor 推出了 **Automations** 功能，将自己从"AI 辅助 IDE"升级为"始终在线的自主编程系统"。这是 Cursor 对 [[Agentic Coding]] 趋势的正面回应。

## 费曼式理解

传统的 AI 编码助手像一个"随叫随到的顾问"：你问它问题，它给你答案。Cursor Automations 则把这个顾问变成了"全职员工"——它不需要你发起对话，它自己会在后台监控代码库，发现问题就自动修复，收到通知就自动响应。

你可以把它想象成一个"永不下班的初级开发者"，它坐在你的代码仓库旁边，7×24 小时盯着所有动静。

## 核心特性

### "始终在线"自主编程系统

- Agent 不再需要手动触发，而是持续运行在后台
- 可以自主发现代码问题、自动提交修复 PR
- 类似 [[Heartbeat 主动监控机制]] 的理念，但聚焦在代码层面

### 事件驱动架构

Automations 的核心创新在于**事件驱动**——Agent 可以被外部事件自动触发：

| 事件源 | 触发场景 |
|--------|----------|
| **代码提交** | 新 commit 推送时自动跑代码审查 |
| **Slack 消息** | 团队成员在 Slack 提出 bug 报告，Agent 自动开始修复 |
| **PagerDuty 告警** | 生产环境告警触发时，Agent 自动分析日志并提出修复方案 |
| **定时任务** | 每天凌晨自动运行代码质量扫描 |

这跟 Claude Code v2.1.70 引入的 cron 调度异曲同工——行业在同一时期都在向"自主运行"的方向演进。

### 多智能体并行

- 多个 Agent 实例可以同时处理不同的任务
- 一个 Agent 负责修 bug，另一个同时在写新功能，第三个在跑测试
- 这与 [[多Agent协作架构]] 的行业趋势完全吻合

## 与竞品对比

| 特性 | Cursor Automations | Claude Code /loop | OpenClaw Heartbeat |
|------|-------------------|-------------------|-------------------|
| 运行模式 | 始终在线 | 循环执行 | 定时检查 |
| 触发方式 | 事件驱动 | 手动/cron | 定时 |
| 应用场景 | 编码 | 编码 | 全领域 |
| 多 Agent | 支持 | 研究预览 | 支持 |

## 市场影响

Automations 的推出进一步巩固了 Cursor 在 AI IDE 市场的领先地位：
- Cursor 的 ARR 预估已达 $20-30 亿
- 这个功能直接对标 [[Devin 分析|Devin]] 的自主编码能力，但价格只有 $20/月 vs Devin 的 $500/月（现已降至 $20/月）
- 也对 GitHub Copilot 的 Copilot Tasks 功能构成压力

## 隐忧

"始终在线"意味着 Agent 有更多自主权，这也带来了更大的安全风险。如果 Agent 在无人监督的情况下推送了有问题的代码到生产环境，后果可能很严重。

> 来源：https://cursor.com/blog/automations
> 来源：https://techcrunch.com/2026/03/05/cursor-automations

## 外部链接

- [Cursor 官网](https://cursor.com)

## 相关笔记

- [[Cursor 分析]]
- [[竞品对比总览]]
- [[Cursor 2026年3月更新]] — 3月 Automations 的进一步扩展（常驻 Agent、更多事件源）
- [[Cursor 2026年Q2更新]] — Q2 后续：3.6 Auto-review、3.7 Design Mode
