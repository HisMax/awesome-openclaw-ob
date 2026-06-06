---
tags:
  - OpenClaw
  - 趋势
  - Agent
  - ACP
aliases:
  - Agent Long Running
  - 48小时超时
  - ACP 演进
---

# Agent 长时运行与 ACP 演进

## 一句话理解

> Agent 从"10 分钟对话助手"变成了"48 小时自主员工"——v2026.3.22 将默认超时从 600 秒提升到 48 小时，这不只是一个数字变化，而是 Agent 使用范式从"人机对话"向"人机协作"的根本性转移。

## 驱动因素

### Vibe Coding 场景

[[Vibe Coding]] 中描述的新工作模式催生了长时运行需求：开发者启动 Agent、描述任务、然后去做其他事。Agent 自主完成代码生成、测试、修复的循环，可能需要数小时甚至更长时间。

### ACP 的成熟

Agent Controlled Process (ACP) 让 Agent 不再只是"回答问题"，而是**控制一个完整的流程**。当 Agent 在 [[飞书集成|飞书]] 中发起一个审批流程、在 Telegram 中管理一个论坛、或在 [[可插拔沙箱后端|沙箱]] 中运行一个长时部署任务时，10 分钟的超时显然是不够的。

### 复杂任务链

[[Agent Execution Loop]] 支持越来越复杂的任务链——代码生成 → 测试 → 修复 → 再测试 → 部署。每一步都可能涉及等待外部服务响应、等待人类审批、等待编译完成。

## 安全与资源挑战

48 小时超时也带来新的风险面：

- **资源消耗**：失控 Agent 在 48 小时内可消耗大量 API 调用和计算资源
- **权限范围**：长时运行意味着更长的攻击窗口，参见 [[沙箱运行时注入防护]]
- **审计追踪**：48 小时的会话历史远超此前的规模，[[会话状态管理]] 需要更强的持久化能力

## 行业趋势

这与 [[2026 Agent 元年]] 中描述的"从工具到代理"趋势一致。Devin、Claude Code、Cursor 等竞品都在走向更长时运行、更自主的 Agent 模式。OpenClaw 的 48 小时超时是对这一趋势的明确回应。

## Q2 更新：ACP 概念分化与 A2A 整合

2026 Q2，"ACP" 概念在行业中发生了重要分化：

### Agent Client Protocol（IDE 集成）
JetBrains 主导的 **Agent Client Protocol** 定义了 IDE 与 AI 编码 Agent 之间的通信标准。2026.1 GitHub Copilot CLI 以公开预览支持 ACP，当前稳定版 v1。

### Agent Communication Protocol → 并入 A2A
原来的 Agent Communication Protocol（Agent 间通信协议）已**并入 Google 的 A2A 协议**，团队停止独立开发，技术和专业知识贡献给 Linux Foundation 下的 A2A。A2A v1.2 已有 150+ 组织在生产环境使用。

### Agentic Commerce Protocol（电商）
OpenAI 和 Stripe 联合推出的 **Agentic Commerce Protocol**（2026-04-17 稳定规范），定义 AI Agent 发起结账的标准流程。

### 对 OpenClaw 的影响

- 长时运行 Agent 的需求被 Google 的 **Gemini Enterprise Agent Platform** 原生支持（含 long-running agents）
- MCP RC 引入的 **Tasks** 机制为长时任务提供了协议级支持
- OpenClaw 2026.6.x 新增 **Workboard** 编排原语和 Agent 协调工具，用于多 Agent 计划和运行追踪

## 双链导航

- [[Agent 默认超时策略]] — 具体的超时变更
- [[Vibe Coding]] — 驱动长时运行的使用模式
- [[Agent Execution Loop]] — Agent 执行流程
- [[自主执行与人机协作]] — ACP 理念
- [[2026 Agent 元年]] — 行业趋势
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
- [[AI Agent 市场趋势 2026 Q2]] — Q2 协议生态动态
