---
tags:
  - 协议
  - 标准
  - AI基础设施
  - 工具调用
aliases:
  - MCP
  - MCP（Model Context Protocol）
  - Model Context Protocol
  - 模型上下文协议
---

# MCP 协议

## 一句话理解

MCP（Model Context Protocol）是 AI 世界的 "USB 标准"。就像 USB 让你不管什么品牌的设备都能插到电脑上用一样，MCP 定义了 AI 模型和外部工具之间的标准通信协议——不管你用的是 Claude、GPT 还是 DeepSeek，也不管你要连接的是 GitHub、数据库还是智能家居，MCP 都提供统一的接口。

## MCP 是什么？

Model Context Protocol 是一个开放标准，定义了 AI Agent 如何发现、连接和调用外部工具与数据源。它由 Anthropic 发起，但设计为模型无关。

核心理念：让 AI 工具生态像 Web API 一样标准化。

## 三阶段生命周期

```
1. 初始化（Initialization）
   → Client 与 Server 握手，协商能力

2. 发现（Discovery）
   → Client 查询 Server 提供哪些工具和资源

3. 调用（Invocation）
   → Client 按标准格式请求工具执行，Server 返回结果
```

类比：你走进一家餐厅（初始化）→ 看菜单（发现）→ 点菜（调用）。

## OpenClaw 中的 MCP 集成

OpenClaw 通过 `@modelcontextprotocol/sdk` 集成 MCP：

| 配置项 | 详情 |
|--------|------|
| SDK 版本 | `@modelcontextprotocol/sdk@1.25.3` |
| 传输方式 | stdio（标准输入输出，默认） |
| 生命周期 | 标准 MCP 三阶段 |

这意味着任何实现了 MCP 标准的外部服务，都可以无缝接入 OpenClaw 的 Agent Execution Loop。Agent 在 Phase 5（Tool Execution Loop）调用 MCP 工具时，流程是（也可参见上下文管理机制）：

```
模型请求调用工具 → OpenClaw 识别为 MCP 工具 → 通过 stdio 与 MCP Server 通信 → 获取结果 → 回传给模型
```

## MCP 与 Skills 的关系

Skills 和 MCP 是两种不同但互补的扩展机制：

| 维度 | Skills | MCP |
|------|--------|-----|
| 安装方式 | `npx clawhub install` | 配置 MCP Server |
| 代码位置 | 本地 skills 目录 | 独立进程/服务 |
| 通信方式 | 直接函数调用 | 标准化 stdio/HTTP |
| 优势 | 简单直接 | 标准化、可复用、生态更广 |
| 风险 | 供应链安全 | 相对隔离，但仍有信任问题 |

MCP 提供了更好的隔离性——MCP Server 作为独立进程运行，即使出问题也不会直接影响 Agent 主进程。

## MCP 生态现状

MCP 正在成为 AI Agent 工具集成的事实标准：

- **Anthropic** 的 Claude Desktop 原生支持 MCP
- **OpenAI** 也在逐步采纳 MCP 协议
- 社区已开发大量 MCP Server：GitHub、Slack、数据库、文件系统等
- Claude Code 也使用 MCP 进行工具通信
- **MCP Registry** 官方注册服务器已达 **9,652 个**（版本记录 28,959 条），全生态服务器（含第三方目录）近 **59,000+ 个**
- 2026 年 Q2 发布了自诞生以来最大规模的协议修订 RC，协议层实现**无状态化**，详见 [[MCP 2026年Q2进展]]

## 为什么 MCP 重要？

在 MCP 之前，每个 AI Agent 框架都要自己定义工具接口——OpenClaw 有 Skills，Claude Code 有 Tools，AutoGPT 有 Plugins。这就像早期每个手机品牌都有自己的充电口。

MCP 的价值在于统一：
1. **工具开发者**只需写一次 MCP Server，所有 Agent 都能用
2. **Agent 框架**只需实现 MCP Client，就能接入所有工具
3. **用户**可以在不同 Agent 间复用同一套工具配置

MCP 标准化了工具接口，使 [[Agent 编排模式|多 Agent 编排]] 成为可能——当每个 Agent 都说同一种"工具语言"时，Agent 之间的协作和编排才有了可靠的基础。

## 技术细节

MCP 使用 JSON-RPC 2.0 作为消息格式，支持两种传输层：

| 传输方式 | 适用场景 |
|----------|----------|
| stdio | 本地工具，低延迟 |
| HTTP/SSE | 远程服务，跨网络 |

OpenClaw 默认使用 stdio——MCP Server 作为子进程启动，通过标准输入输出通信。这是最简单也最安全的方式，与沙箱机制的隔离理念一致。

## 核心洞察

MCP 对 AI Agent 生态的意义，类似于 HTTP 对 Web 的意义。它不是让 Agent 变得更聪明，而是让 Agent 的能力可以**标准化地扩展和共享**。在 Agentic AI 时代，谁的工具生态最丰富，谁就最有价值——而 MCP 是构建这个生态的基础设施。[[MCP 2026 路线图]] 进一步明确了其发展方向，[[MCP 2026年Q2进展]] 记录了 2026 年 Q2 的重大协议修订。

## 相关笔记

- [[Tool Use 机制]] - 工具调用的底层原理
- [[MCP 2026 路线图]] - 发展方向
- [[MCP 2026年Q2进展]] - Q2 无状态化 RC 与 Extensions 框架
- [[ACP v1 生态扩展]] - 与 MCP 互补的 Agent-编辑器协议
- [[Skills 市场]] - OpenClaw 的另一种扩展机制
- [[Anthropic 公司分析]] - MCP 的发起者

## 外部链接

- [MCP 官网](https://modelcontextprotocol.io)
- [npm](https://npmjs.com)
- [Linux Foundation AAIF](https://lfaidata.foundation)
