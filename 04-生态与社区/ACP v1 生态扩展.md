---
tags:
  - ACP
  - 协议
  - 标准
  - IDE
  - AI编码
  - 2026Q2
aliases:
  - ACP
  - Agent Client Protocol
  - ACP v1
  - ACP 协议
---

# ACP v1 生态扩展

> **一句话总结**：Agent Client Protocol（ACP）是 AI 编码 Agent 世界的"LSP"——就像 Language Server Protocol 在 2016 年终结了编辑器碎片化一样，ACP 正在终结 AI 编码 Agent 的编辑器锁定，已有 28+ Agent 和 Google/AWS/JetBrains/Neovim/Emacs 等主流客户端接入。

## ACP 是什么

ACP（Agent Client Protocol）是一个开放标准，定义了 AI 编码 Agent 与代码编辑器之间的通信接口。它由 Zed Industries 于 2025 年 8 月创建并达到 v1，JetBrains 于同年 9 月作为联合负责人加入。

### 核心类比

| 2016 | 2025-2026 |
|------|-----------|
| 每个编辑器为每种语言写一套语法支持 | 每个编辑器为每种 AI Agent 写一套集成 |
| LSP 统一了"语言 ↔ 编辑器"接口 | ACP 统一了"Agent ↔ 编辑器"接口 |
| 结果：语言工具一次开发，处处运行 | 目标：AI Agent 一次开发，任何编辑器运行 |

ACP 之前的状态：如果你开发了一个 AI 编码 Agent，你需要为 VS Code 写一套插件、为 JetBrains 写一套插件、为 Neovim 写一套插件……这是不可持续的 N x M 集成矩阵。ACP 把它压缩成 N + M。

## 技术架构

### 通信协议

| 维度 | 详情 |
|------|------|
| **消息格式** | JSON-RPC 2.0 |
| **传输层** | stdin/stdout |
| **启动方式** | 编辑器作为父进程 spawn Agent 子进程 |
| **消息交换** | 换行符分隔的 JSON-RPC 消息 |

ACP 的技术选择极为简洁——JSON-RPC over stdio，与 LSP 和 [[MCP 协议|MCP]] 完全一致。这不是巧合：三个协议共享同一传输层，降低了实现和理解门槛。

### 工作流程

```
编辑器（ACP Client）
  ↓ spawn
AI Agent（ACP Server）
  ↓ JSON-RPC over stdin/stdout
双向通信：
  - Client → Server: 用户请求、代码上下文、文件变更
  - Server → Client: 代码建议、诊断信息、编辑操作
```

## 生态现状（2026 Q2）

### Agent 端（28+ 已注册）

ACP Agent Registry 已成为 AI 编码 Agent 的"应用商店"，直接集成在 JetBrains IDE 和 Zed 中：

| Agent | 说明 |
|-------|------|
| **Devin** | Cognition 的自主编码 Agent（通过 [[Cognition Series D 融资|Devin Desktop]] 支持 ACP） |
| **Claude Code** | Anthropic 的 CLI 编码 Agent |
| **Hermes Agent** | NousResearch 的开源 Agent |
| **Cline CLI** | 终端 AI Agent 控制面板 |
| 其他 24+ | 持续增加中 |

### 客户端（编辑器/IDE）

| 客户端 | 维护方 | 状态 |
|--------|--------|------|
| **JetBrains IDEs** | JetBrains（联合负责人） | 原生集成 |
| **Zed** | Zed Industries（创始方） | 原生集成 |
| **Neovim** | 社区 | 已实现 |
| **Emacs** | 社区（emacsmirror/acp, xenodium/agent-shell） | 已实现 |
| **Google Gemini CLI** | Google | 已采纳客户端 |
| **AWS Kiro IDE** | AWS | 已采纳客户端 |

Google 和 AWS 同时采纳 ACP 客户端，说明 ACP 已获得云厂商级别的认可——这与 [[MCP 协议 2026年3月进展|MCP 被 ChatGPT/VS Code/Cursor 同时采纳]] 形成有趣的平行。

### Devin Desktop 与 ACP

[[Cognition Series D 融资|Cognition]] 收购 Windsurf 后将其更名为 Devin Desktop，并原生支持 ACP。这意味着：
- Devin 可以在任何 ACP 兼容编辑器中运行
- 用户不再被锁定在特定 IDE 中
- Cognition 的策略从"构建 IDE"转向"成为最好的 Agent"，让编辑器选择留给用户

## ACP vs MCP：互补而非竞争

ACP 和 MCP 经常被放在一起比较，但它们解决的是不同层面的问题：

| 维度 | ACP | MCP |
|------|-----|-----|
| **连接方向** | Agent ↔ 编辑器（垂直） | Agent ↔ 工具/数据源（垂直） |
| **核心问题** | "哪个 Agent 能在哪个编辑器中运行？" | "Agent 如何调用外部工具？" |
| **类比** | USB-C 连接设备到电脑 | 网络协议连接电脑到互联网 |
| **创始方** | Zed + JetBrains | Anthropic |
| **消息格式** | JSON-RPC 2.0 | JSON-RPC 2.0 |
| **传输层** | stdio | stdio / HTTP |
| **Agent 关系** | 规范 Agent 如何被编辑器调用 | 规范 Agent 如何调用工具 |

### 第三个协议：IBM ACP (Agent Communication Protocol)

值得注意的是，IBM Research 也推出了一个名为 ACP 的协议——Agent Communication Protocol（注意不是 Agent **Client** Protocol）。IBM 的 ACP 解决的是 Agent ↔ Agent 之间的水平通信，更接近 Google 的 A2A（Agent-to-Agent）协议的定位。

三者的关系：

```
             [MCP]
              ↕  Agent ↔ 工具
[ACP/A2A] ↔ [AI Agent] ↔ [ACP(Zed)]
  Agent ↔ Agent          Agent ↔ 编辑器
```

## ACP 的版本演进

| 版本 | 日期 | 说明 |
|------|------|------|
| v1 | 2025.8 | Zed Industries 发布初始版本 |
| v0.11.0 | 2026.3.4 | 持续迭代（版本号看似降低，实为 API 细化） |
| — | 2026.6 | 28+ Agent + 4 大编辑器客户端 |

GitHub Stars 2.3K+，虽然远不及 OpenClaw 或 MCP 的量级，但作为一个协议规范项目，这个数字说明开发者社区的关注度足够高。

## 对 OpenClaw 的影响

ACP 的成熟对 OpenClaw 生态有间接影响：

1. **Skills 的分发渠道扩展**：如果 OpenClaw 的 [[Skills 市场|Skills]] 通过 MCP 提供能力，而 MCP 服务器可以被 ACP Agent 调用，那么 OpenClaw 的技能生态间接触达了所有 ACP 兼容编辑器
2. **竞争格局变化**：ACP 让"选择 Agent"和"选择编辑器"解耦，用户可以在 JetBrains 中用 Devin，也可以用 Claude Code——这加剧了 Agent 层面的竞争
3. **标准化趋势**：ACP + MCP + A2A 共同构成了 Agentic AI 的"协议三件套"，[[NIST AI Agent 安全标准|NIST 标准化]] 将进一步加速这一趋势

## 关键洞察

### LSP 类比的准确性和局限性

ACP 被频繁类比为"AI 的 LSP"，这个类比在结构上是准确的（都是 N x M → N + M），但有一个关键区别：LSP 时代的语言服务器是确定性的（给定代码，分析结果是确定的），而 AI Agent 是概率性的。这意味着 ACP 需要处理 LSP 从未面对的问题：如何标准化一个"答案不唯一"的系统的输出。

### 协议碎片化的阶段

当前的 ACP/MCP/A2A 三协议格局，很像早期 Web 的 HTTP/FTP/SMTP 分层。每个协议各有其适用场景，最终会形成稳定的协议栈而非"赢家通吃"。

## 相关笔记

- [[MCP 协议]] — Agent 与工具的连接协议
- [[MCP 2026年Q2进展]] — MCP 最新进展
- [[Agent 长时运行与 ACP 演进]] — 长时运行 Agent 与协议演进
- [[Cognition Series D 融资]] — Devin Desktop 与 ACP
- [[NIST AI Agent 安全标准]] — 标准化趋势

## 外部链接

- [ACP 官网](https://agentclientprotocol.com)
- [JetBrains ACP](https://www.jetbrains.com/acp/)
- [Zed ACP](https://zed.dev/acp)
- [ACP Agent Registry](https://blog.jetbrains.com/ai/2026/01/acp-agent-registry/)
- [Emacs ACP (emacsmirror)](https://github.com/emacsmirror/acp)
- [Emacs agent-shell](https://github.com/xenodium/agent-shell)

> 来源：JetBrains ACP 文档、Zed ACP 官网、byteiota、Morph、Cognition Devin 文档，2026 年 Q2
