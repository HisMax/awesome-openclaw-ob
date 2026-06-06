---
tags:
  - 架构
  - agent-control
  - 并发
  - pi-agent-core
aliases:
  - Steering
  - Follow-Up
  - Agent 流控制
  - steer 与 followup
---

# Steering 与 Follow-Up 控制

## 一句话总结

steer() 是"抢方向盘"——在工具调用的间隙优雅地中断 Agent 当前任务转向新指令；followUp() 是"排队等候"——等 Agent 做完手头的事再执行你的新要求。两者构成了[[Pi Agent Core 运行时]]的双模流控制。

## 核心机制：中断式 vs 协作式

| 特性 | `steer()` | `followUp()` |
|------|-----------|-------------|
| 控制模式 | **抢占式**（中断当前执行） | **协作式**（排队等待） |
| 执行时机 | 在 tool boundary 立即介入 | 当前 Agent 循环完成后 |
| 类比 | 抢方向盘：车还在开，但换方向 | 排队叫号：等前面的人办完 |
| 适用场景 | 用户说"停下来，换个方向" | 用户补充说明、追加要求 |

## Tool Boundary 抢占：steer 的精妙之处

steer() 不是粗暴地 kill 进程。它的关键创新在于**在 tool boundary（两次工具调用之间的间隙）优雅地抢占**：

```
Agent 执行中...
  → 工具调用 A 执行完毕 ← tool boundary（抢占点）
    → [steer] 拦截！插入新指令，跳过待执行的工具调用 B、C
      → Agent 转向处理新指令
```

让 Agent 完成当前正在执行的工具调用（避免状态不一致），然后在工具调用之间的"呼吸间隙"切换方向。这比直接 kill 安全得多——不会留下半完成的文件操作或数据库事务。

## 在 Lane-Based Queuing 中的映射

steer 和 followUp 在[[Lane-Based Queuing 并发模型]]中对应不同的队列模式：

| Queue Mode | 对应机制 | 行为 |
|------------|----------|------|
| **steer** | `steer()` | 在 tool boundary 抢占当前执行 |
| **steer-backlog** | `steer()` 变体 | 抢占但保留被中断的任务到 backlog |
| **followup** | `followUp()` | 排队等待当前执行完成 |
| **collect**（默认） | 无 | 新消息收集到队列末尾 |
| **interrupt** | 更激进的中断 | 立即中断，不等 tool boundary |

**steer-backlog** 是一个精细设计：既中断了当前执行转向紧急任务，又不丢弃被中断的原始任务——它被保存到 backlog 中，等紧急任务完成后可以恢复。

## 实际使用场景

**steer 场景**：你让 Agent 整理 100 封邮件，处理到第 30 封时你说"等等，先别动那个文件夹"。steer 在下一个 tool boundary 介入，Agent 停下邮件整理，转而处理你的新指令。

**followUp 场景**：Agent 正在生成一份报告，你突然想起"对了，记得加上上季度的数据"。followUp 把这个要求排在队列里，等报告初稿完成后 Agent 自动追加数据。

## 与 Summer Yue 事件的关联

Summer Yue 尝试用 "STOP OPENCLAW" 中断 Agent 清理邮箱，但 Agent 无视了她的指令。如果当时的[[Context Compaction 机制]]没有删除安全指令，steer 机制本应能在 tool boundary 介入并停止删除操作。事件暴露了一个问题：**当安全上下文在 Compaction 中丢失后，steer 发出的新指令也可能被 Agent 误解或忽略**。

## 后续演进（v2026.4）

v2026.4.29 引入 **Active-Run Steering**——当 Agent 正在运行时，用户发送的后续消息默认切换为 steering 模式，作为方向调整注入到活跃运行中，减少消息丢失。这将 steer 从"需要用户主动选择"变为"默认行为"，进一步降低了人机协作的摩擦。详见 [[OpenClaw v2026.4 版本更新]]。

## 关键洞察

steer 和 followUp 的设计体现了 OpenClaw 对 Agent 控制的哲学：**人始终在回路中（human-in-the-loop）**。与 AutoGPT 的"设定目标后放手不管"不同，OpenClaw 允许用户随时介入、调整方向。这是工程成熟度的体现——真正的 Agent 系统需要的不只是自主性，更需要**可控性**。

## 相关笔记

- [[Pi Agent Core 运行时]] -- steer() 和 followUp() 是 Pi Agent Core 的核心 API
- [[Lane-Based Queuing 并发模型]] -- 队列模式中 steer/followup/collect 的具体行为
- [[Agent-Flow-Loop 原理]] -- steer 在 Phase 5 Tool Execution Loop 中的作用点
- [[Context Compaction 机制]] -- Compaction 丢失安全指令后 steer 失效的风险
- [[自主执行与人机协作]] -- steer 是 human-in-the-loop 设计的关键实现
- [[Tool Use 机制]] -- tool boundary 是 steer 的抢占点
- [[OpenClaw v2026.4 版本更新]] — Active-Run Steering 默认化

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [MCP 规范](https://modelcontextprotocol.io)
