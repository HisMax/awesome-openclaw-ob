---
tags:
  - Claude Code
  - Agent编排
  - Dynamic Workflows
  - 多Agent
  - Anthropic
  - ultracode
aliases:
  - Dynamic Workflows
  - 动态工作流
  - Claude Code Dynamic Workflows
  - ultracode
  - 动态编排
---

# Dynamic Workflows


![[assets/dynamic-workflows.jpg]]

## 一句话理解

> Dynamic Workflows 是 Claude Code 的大规模 Agent 编排范式——Claude 动态生成 JavaScript 编排脚本，运行时调度最多 1,000 个子 Agent（16 并发），用对抗性验证确保结果收敛，将编排逻辑从上下文窗口搬到脚本变量中，突破了传统逐轮 Agent 模式的扩展瓶颈。

## 概述

Dynamic Workflows 于 2026 年 5 月 28 日发布，是 Anthropic 为 Claude Code 设计的多 Agent 编排架构。核心思想是：当任务复杂到需要数十甚至数百个 Agent 并行工作时，不再让主模型在上下文窗口中一步步协调，而是让 Claude 生成一段 JavaScript 编排脚本，由后台运行时负责调度和执行。

### 为什么需要 Dynamic Workflows

传统的 Agent 编排有一个根本性瓶颈——上下文窗口：

```
传统模式（逐轮协调）：
  用户请求 → 主模型规划 → 调用子 Agent 1 → 等待结果 → 
  调用子 Agent 2 → 等待结果 → ... → 综合回答
  
  问题：所有中间结果都要放在主模型的上下文窗口中
  结果：超过 5-10 个子任务后上下文窗口就溢出

Dynamic Workflows（脚本编排）：
  用户请求 → Claude 生成 JS 脚本 → 运行时执行脚本 →
  并行调度 N 个子 Agent → 对抗验证 → 收敛后返回结果
  
  优势：编排逻辑在脚本变量中，不占用模型上下文
  结果：可扩展到 1,000 个子 Agent
```

## 架构

### 执行流程

```
┌──────────────────────────────────────────────────┐
│                  用户 Prompt                       │
│   "对整个代码库做安全审计"                           │
└────────────────────┬─────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────┐
│              Claude 规划阶段                       │
│   分析任务 → 分解子任务 → 生成 JS 编排脚本          │
└────────────────────┬─────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────┐
│            JavaScript 编排脚本                     │
│   const tasks = [                                │
│     { name: "scan-auth", files: [...] },         │
│     { name: "scan-sql", files: [...] },          │
│     { name: "scan-xss", files: [...] },          │
│     ...                                          │
│   ];                                             │
│   // 并行调度 + 对抗验证 + 收敛检查               │
└────────────────────┬─────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────┐
│              后台运行时                            │
│                                                  │
│   ┌─────┐ ┌─────┐ ┌─────┐ ... ┌─────┐          │
│   │Agent│ │Agent│ │Agent│     │Agent│  ← 最多16并发│
│   │  1  │ │  2  │ │  3  │     │ 16  │           │
│   └──┬──┘ └──┬──┘ └──┬──┘     └──┬──┘          │
│      │       │       │           │               │
│      ▼       ▼       ▼           ▼               │
│   ┌──────────────────────────────────┐           │
│   │       对抗性验证层                 │           │
│   │  Skeptic Agents 尝试反驳每个发现   │           │
│   └──────────────────┬───────────────┘           │
│                      │                           │
│                      ▼                           │
│   ┌──────────────────────────────────┐           │
│   │       收敛检查                    │           │
│   │  迭代直到结果收敛                  │           │
│   └──────────────────────────────────┘           │
└────────────────────┬─────────────────────────────┘
                     │
                     ▼
              最终综合报告
```

### 关键设计决策

**编排逻辑外置化**

传统多 Agent 系统将编排逻辑放在主模型的上下文窗口中。Dynamic Workflows 将其放入 JavaScript 脚本——脚本变量保存状态，而不是占用 token。这是一个根本性架构转变：

| 维度 | 传统模式 | Dynamic Workflows |
|------|----------|-------------------|
| 编排状态存储 | 上下文窗口（token） | JS 脚本变量（内存） |
| 并发上限 | 受上下文窗口限制 | 1,000 总量 / 16 并发 |
| 中间结果处理 | 全部加载到上下文 | 按需传递 |
| 可检查性 | 黑箱（在模型脑中） | 可读的 JS 代码 |

**每个子 Agent 独立上下文**

每个子 Agent 获得自己的全新上下文窗口和狭窄的任务切片。子 Agent 之间不共享上下文——这不是缺陷，而是特性：

- 避免了信息泄露和交叉污染
- 使对抗验证成为可能（验证者不受被验证者的偏见影响）
- 每个 Agent 可以 100% 专注于自己的子任务

## 触发方式

### 方式一：关键词触发

在 prompt 中包含 "workflow" 一词，Claude Code 会高亮它并规划一个 fan-out 工作流：

```
"对这个代码库运行一个 workflow，找出所有潜在的性能瓶颈"
```

### 方式二：Ultracode 设置

通过 `/effort ultracode` 命令或 effort 菜单激活：

```
/effort ultracode
```

**Ultracode 的含义**：

| 设置 | 效果 |
|------|------|
| 推理级别 | xhigh（最高） |
| 自主决策 | Claude 自行判断每个请求是否值得启动 Workflow |
| Token 消耗 | 显著增加 |
| 时间消耗 | 显著增加 |

激活 ultracode 后，一个请求可能触发多个连续 workflow：先理解代码库，再做出修改，最后验证修改——每个阶段都是独立的 workflow。

### 版本要求

Dynamic Workflows 需要 Claude Code v2.1.154 或更高版本。

## 对抗性验证

Dynamic Workflows 最具创新性的设计是内置的对抗性验证（adversarial verification）架构：

### 工作原理

```
Producer Agent          Skeptic Agent
  │                         │
  ├── 生成发现 ──────────→ │
  │                         ├── 尝试反驳
  │                         │   （基于评分标准）
  │                         │
  │   ← 反驳结果 ──────── │
  │                         │
  ├── 发现存活 → 进入报告    │
  └── 发现被驳 → 丢弃       │
```

**关键约束**：Producer 和 Skeptic 永远不共享上下文窗口。这消除了自我偏好偏差（self-preferential bias）——审核者不会因为看到了生产者的推理过程而倾向于认同它。

### 收敛机制

对抗验证不是一次性的。系统会迭代：

1. 第一轮：所有 Producer Agent 并行工作
2. 第一轮验证：Skeptic Agents 反驳发现
3. 存活的发现进入下一轮（可能需要更深入的分析）
4. 迭代直到结果收敛——没有新的发现被推翻

### 实际应用：/deep-research

内置的 `/deep-research` 命令直接展示了这个模式：

1. Fan-out：并行执行多个 Web 搜索
2. 交叉检查：每个来源与其他来源交叉验证
3. 存活投票：对每条声明进行存活投票
4. 输出：带引用的综合报告

## 可恢复性

### 中断与恢复

Dynamic Workflows 支持运行中断后恢复：

- 运行时追踪每个子 Agent 的状态
- 已完成的 Agent 返回缓存结果（不会重跑）
- 只有未完成的 Agent 需要重新执行
- 恢复在同一个会话内进行

### 进度保存

进度随运行实时保存。这意味着即使一个 500 Agent 的大型 workflow 在 Agent #300 时中断，恢复后只需要运行剩余的 200 个。

## 规模参数

| 参数 | 值 | 说明 |
|------|-----|------|
| 最大子 Agent 总数 | 1,000 | 单次 workflow run |
| 最大并发 Agent | 16 | 运行时并行限制 |
| 触发关键词 | "workflow" | 在 prompt 中出现即触发 |
| 触发设置 | ultracode | /effort ultracode |
| 推理级别 | xhigh | ultracode 自动设置 |
| 最低版本 | v2.1.154 | Claude Code 版本要求 |

## 典型使用场景

### 代码库级安全审计

```
"运行一个 workflow 对整个代码库做安全审计：
 检查 SQL 注入、XSS、认证绕过、路径遍历和信息泄露"
```

Claude 会为每种漏洞类型 × 每个模块生成独立的 Agent，再用 Skeptic Agent 验证每个发现。

### 性能优化审计

```
"基于 profiler 输出，用 workflow 分析这个项目的所有性能瓶颈"
```

每个 Agent 负责一个模块或热路径的分析，最终合并为优先级排序的优化建议。

### 大规模重构

```
"workflow：将所有 Class 组件迁移到 React Hooks"
```

每个文件或组件由独立 Agent 处理，另一组 Agent 负责验证迁移后的类型安全和行为一致性。

### 跨文件 Bug 定位

```
"用 workflow 找到导致这个集成测试失败的根因"
```

多个 Agent 从不同角度调查——代码变更历史、依赖关系、运行时行为——最终收敛到最可能的根因。

## 与其他编排模式的对比

| 维度 | Dynamic Workflows | [[Agent 编排模式\|静态编排]] | [[OpenClaw v2026.4 版本更新\|Durable TaskFlow]] |
|------|-------------------|--------------|-----------------|
| 编排脚本 | 动态生成 JS | 预定义 YAML/JSON | 预定义 Flow 图 |
| 运行时 | Claude Code 内置 | 框架调度 | OpenClaw Gateway |
| 规模 | 1,000 Agent | 通常 < 10 | 取决于部署 |
| 对抗验证 | 内置 | 无 | 无 |
| 持久化 | 会话级 | 取决于框架 | 跨重启持久 |
| 触发方式 | 自然语言/设置 | API/配置 | Webhook/CLI |
| 所属产品 | Claude Code | 通用 | OpenClaw |

Dynamic Workflows 和 Durable TaskFlow 解决不同层面的问题：Dynamic Workflows 是"一次性大规模探索"，TaskFlow 是"可持久化的生产工作流"。前者适合研究和审计，后者适合自动化管线。

## 与 OpenClaw 的关系

OpenClaw 通过 [[ACP 协议]] 支持 Claude Code 作为 Agent 后端，这意味着 Dynamic Workflows 可以在 OpenClaw 生态中被间接使用。但 Dynamic Workflows 本身是 Claude Code 的原生能力，不需要 OpenClaw。

两者可以互补：
- Dynamic Workflows 用于大规模探索和分析（一次性任务）
- OpenClaw 的 TaskFlow 用于持久化生产工作流（长期运行）

## 关键洞察

Dynamic Workflows 的核心创新不是"让更多 Agent 并行工作"——这是工程问题。真正的洞察是**将编排逻辑从模型上下文中解放出来**。

传统的 multi-agent 系统都有一个隐含假设：需要一个"主脑"在上下文窗口中理解所有子任务的进展。Dynamic Workflows 打破了这个假设——Claude 写出编排脚本后，运行时接管调度，Claude 的上下文窗口被释放。这就像从"CEO 亲自盯每个人的工作"变成"CEO 写好工作流程手册后交给 COO 执行"。

对抗性验证则解决了 AI 系统最顽固的问题之一：自我确认偏差。让 Producer 和 Skeptic 不共享上下文，确保了审核的独立性。这个思路来自 [[Constitutional AI]] 的理念，但在工程实现上更加激进——不是在同一个模型内部做自我批评，而是在完全隔离的 Agent 之间做对抗。

然而，1,000 Agent 的上限和 16 并发的约束也暗示了当前的边界：token 成本和计算资源仍然是实际限制。一个 1,000 Agent 的 workflow 在 ultracode 模式下的 token 消耗可能相当可观。

## 双链导航

- [[Agentic Coding]] — Dynamic Workflows 服务的核心场景
- [[ACP 协议]] — Claude Code 与编辑器的通信标准
- [[Agent 编排模式]] — 其他编排范式的对比
- [[Agent-Flow-Loop 原理]] — Agent 执行的基本循环
- [[Agent Execution Loop]] — 单个 Agent 的执行模型
- [[Constitutional AI]] — 对抗性验证的理论基础
- [[Claude 模型系列]] — Dynamic Workflows 的模型依赖
- [[多Agent协作架构]] — 多 Agent 系统设计的通用问题
- [[OpenClaw v2026.4 版本更新]] — Durable TaskFlow 编排层的对比

## 参考

- [Introducing Dynamic Workflows in Claude Code — Anthropic Blog](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [A Harness for Every Task — Claude Blog](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)
- [Orchestrate Subagents at Scale — Claude Code Docs](https://code.claude.com/docs/en/workflows)
- [Dynamic Workflows — InfoQ](https://www.infoq.com/news/2026/06/dynamic-workflows-claude-code/)
- [Claude Code Dynamic Workflows — TechTimes](https://www.techtimes.com/articles/317363/20260529/claude-code-dynamic-workflows-scripts-replace-context-windows-ultracode-automates-orchestration.htm)
- [Ultracode in Claude Code: Effort Setting Explained](https://claudefa.st/blog/guide/development/ultracode)
- [Dynamic Workflows — MarkTechPost](https://www.marktechpost.com/2026/05/28/anthropic-ships-claude-opus-4-8-alongside-dynamic-workflows-and-cheaper-fast-mode-with-workflows-capped-at-1000-subagents/)
