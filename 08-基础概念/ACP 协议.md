---
tags:
  - ACP
  - 协议
  - Agent
  - 编辑器集成
  - JSON-RPC
  - 标准化
aliases:
  - ACP
  - Agent Client Protocol
  - 代理客户端协议
---

# ACP 协议

## 一句话理解

> ACP（Agent Client Protocol）之于 AI 编程 Agent，就像 LSP（Language Server Protocol）之于语言服务器——一个开放标准，让任何编辑器接入任何 Agent，消除 N x M 的定制集成困境。

## 概述

Agent Client Protocol（ACP）是一个标准化通信协议，定义了代码编辑器（Client）与 AI 编程代理（Agent）之间的交互方式。它基于 JSON-RPC 2.0 over stdio 实现，允许编辑器将 Agent 作为子进程启动，通过标准输入/输出交换换行分隔的 JSON-RPC 消息。

### 解决的核心问题

在 ACP 出现之前，每个编辑器要接入每个 Agent 都需要一套定制集成：

```
没有 ACP 的世界：
  VSCode ←→ Claude Code  (定制插件)
  VSCode ←→ OpenClaw     (定制插件)
  VSCode ←→ Gemini CLI   (定制插件)
  Zed    ←→ Claude Code  (定制插件)
  Zed    ←→ OpenClaw     (定制插件)
  ...
  = N 个编辑器 × M 个 Agent = N×M 个定制集成

有 ACP 的世界：
  VSCode ←→ [ACP] ←→ Claude Code
  VSCode ←→ [ACP] ←→ OpenClaw
  VSCode ←→ [ACP] ←→ Gemini CLI
  Zed    ←→ [ACP] ←→ Claude Code
  ...
  = N 个编辑器 + M 个 Agent 实现 = N+M 个实现
```

这与 LSP 解决的问题完全同构：LSP 让一个编辑器受益于任何人写的语言服务器；ACP 让一个编辑器受益于任何人写的 Agent。

## 技术架构

### 通信模型

```
┌──────────────┐     JSON-RPC 2.0     ┌──────────────┐
│              │      over stdio       │              │
│   Editor     │  ←─────────────────→  │    Agent     │
│  (Client)    │    stdin / stdout     │  (Server)    │
│              │                       │              │
└──────────────┘                       └──────────────┘
      │                                       │
      │ 管理用户环境                           │ 处理思考和工具执行
      │ 显示 Diff                              │ 代码修改
      │ MCP 服务器端点                          │ 使用 MCP 工具
      │                                       │
```

**本地 Agent 模型**：Agent 作为编辑器的子进程运行。编辑器启动 Agent 进程后，通过 stdin/stdout 进行双向通信。每条消息是一个换行分隔的 JSON-RPC 对象。

### 与 MCP 的关系

ACP 和 [[Tool Use 机制|MCP]] 解决不同的问题，但协同工作：

| 维度 | ACP | MCP |
|------|-----|-----|
| 连接方向 | Editor ←→ Agent | Agent ←→ Tool Server |
| 关注点 | UI 交互、Diff 展示、会话管理 | 工具发现、调用、上下文 |
| 数据类型 | 代码编辑相关 UX | 工具调用和结果 |
| 共存方式 | ACP 会话启动时，Editor 向 Agent 传递 MCP 端点列表 |

ACP 复用了 MCP 的 JSON 类型定义（type reuse），但为编码场景增加了自定义类型——比如在编辑器中显示 Diff 的专用类型。

### 协议版本

**当前稳定版本：v1**

ACP v1 已经达到稳定状态，意味着：
- 向后兼容性保证
- 类型定义和消息格式不会有破坏性变更
- Agent 和 Client 开发者可以安全地基于 v1 构建

## 生态系统

### 支持 ACP 的编辑器（Clients）

| 编辑器 | 集成方式 | 状态 |
|--------|----------|------|
| Zed | 原生支持 | 稳定 |
| JetBrains IDEs | 内置支持 | 稳定 |
| VS Code | ACP Client 扩展 | 稳定 |
| Neovim | 插件 | 稳定 |
| Emacs | 包 | 稳定 |
| Obsidian | Agent Client 插件 | 稳定 |
| Eclipse | 插件 | 稳定 |
| Toad | 集成 | 稳定 |

### 支持 ACP 的 Agent（Servers）

| Agent | 来源 | 说明 |
|-------|------|------|
| Claude Code | Anthropic | ACP 的发起者之一 |
| Gemini CLI | Google | Google 的命令行 AI 编程助手 |
| OpenClaw | 社区 | 前 Clawdbot / Moltbot |
| Kimi CLI | Moonshot | 支持会话管理、模型切换和 MCP |
| Kiro CLI | AWS | Amazon 的 Agent，支持 ACP |
| Devin Desktop | Cognition | 自主编程 Agent |
| OpenCode | 社区 | 开源 AI 编码工具 |

完整列表维护在 [ACP Registry](https://github.com/agentclientprotocol/registry)，截至 2026 年 6 月已有 28+ Agent 注册。

### 主要采用者

| 组织 | 参与方式 |
|------|----------|
| Google | Gemini CLI 支持 ACP |
| AWS | Kiro 采用 ACP |
| JetBrains | IDE 原生集成 |
| Anthropic | Claude Code 原生支持 |
| Cognition | Devin Desktop 支持 |

## 类比 LSP

ACP 的设计哲学直接借鉴了 LSP（Language Server Protocol）的成功经验：

| 维度 | LSP | ACP |
|------|-----|-----|
| 发布年份 | 2016 | 2026 |
| 解决的问题 | N 个编辑器 × M 种语言 | N 个编辑器 × M 个 Agent |
| 通信方式 | JSON-RPC over stdio/TCP | JSON-RPC 2.0 over stdio |
| 发起者 | Microsoft (VS Code) | 多方协作 |
| 关键能力 | 补全、诊断、重构 | Diff 展示、工具调用、会话管理 |
| 成功标志 | 几乎所有编辑器支持 | 主要编辑器和 Agent 已支持 |

LSP 花了约 3 年达到普遍采用。ACP 在 v1 稳定后的数月内就获得了 Google、AWS、JetBrains 等大厂支持，采用速度远快于 LSP——这可能是因为 AI 编程工具的市场竞争比 2016 年的语言工具更激烈，各方更有动力避免碎片化。

## ACP 会话生命周期

### 1. 初始化

```json
// Editor → Agent
{
  "jsonrpc": "2.0",
  "method": "initialize",
  "params": {
    "capabilities": {
      "diff": true,
      "streaming": true
    },
    "mcpServers": [
      {"uri": "stdio://localhost/filesystem"},
      {"uri": "stdio://localhost/git"}
    ],
    "workspaceRoot": "/home/user/project"
  }
}
```

编辑器传递自身能力声明、MCP 服务器列表和工作区路径。

### 2. 交互循环

- 用户在编辑器中输入自然语言请求
- 编辑器通过 ACP 发送给 Agent
- Agent 执行思考和工具调用
- Agent 通过 ACP 返回代码修改（Diff 格式）
- 编辑器在 UI 中展示 Diff 供用户审查

### 3. 终止

编辑器发送 `shutdown` 请求，Agent 完成清理后退出进程。

## 对 OpenClaw 的意义

OpenClaw（前 Clawdbot）是最早支持 ACP 的社区 Agent 之一。ACP 支持意味着：

- OpenClaw Agent 可以直接在 VS Code、Zed、JetBrains 等主流编辑器中使用
- 不再需要为每个编辑器开发定制集成
- 用户可以在保持编辑器偏好的同时使用 OpenClaw 的 Agent 能力

这与 OpenClaw 的 [[模型无关架构]] 理念一致——不仅模型可以替换，连前端编辑器也可以替换。

## 与其他协议的区分

注意不要混淆两个不同的"ACP"：

| 协议 | 全称 | 关注点 |
|------|------|--------|
| **Agent Client Protocol** | agentclientprotocol.com | Editor ↔ Agent 通信 |
| Agent Connect Protocol | agntcy/acp-spec | Agent ↔ Agent 通信（AGNTCY 项目） |

本节点讨论的是前者——Editor 和 Agent 之间的通信标准。

## 关键洞察

ACP 的出现标志着 AI 编程工具从"编辑器绑定"时代进入"协议驱动"时代。就像 LSP 让 Rust Analyzer 可以在任何编辑器中工作一样，ACP 让 Claude Code 可以在 Neovim 中工作、让 OpenClaw 可以在 VS Code 中工作。

但 ACP 的意义不仅是技术标准化。它反映了一个更深层的行业共识：**AI 编程 Agent 不应该是编辑器的附属品，而应该是独立的、可互操作的服务**。这个共识的形成速度之快（v1 稳定后数月内即获大厂采用），说明市场对碎片化的容忍度极低——没有人想在"Agent 锁定"的世界里重蹈"IDE 锁定"的覆辙。

## 双链导航

- [[OpenClaw 是什么]] — ACP 支持的 Agent 框架
- [[Tool Use 机制]] — ACP 与 MCP 的协同关系
- [[Agentic Coding]] — ACP 服务的核心场景
- [[Agent Execution Loop]] — Agent 在 ACP 会话中的执行模型
- [[模型无关架构]] — ACP 体现的"前端也可替换"理念
- [[Claude 模型系列]] — Claude Code 是 ACP 发起者之一
- [[Dynamic Workflows]] — Claude Code 的高级编排能力

## 参考

- [ACP 官方网站](https://agentclientprotocol.com)
- [ACP GitHub 仓库](https://github.com/agentclientprotocol/agent-client-protocol)
- [ACP Registry](https://github.com/agentclientprotocol/registry)
- [JetBrains ACP 文档](https://www.jetbrains.com/acp/)
- [Kiro ACP 文档](https://kiro.dev/docs/cli/acp/)
- [ACP 介绍 — Marc Nuri](https://blog.marcnuri.com/agent-client-protocol-acp-introduction)
- [ACP 概览 — Phil Schmid](https://www.philschmid.de/acp-overview)
