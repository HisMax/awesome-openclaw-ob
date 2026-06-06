---
tags:
  - Devin
  - Windsurf
  - 竞品动态
  - 2026年Q2
  - 品牌整合
  - Agent-Command-Center
aliases:
  - Devin Desktop
  - Windsurf 更名
  - Windsurf 2.0
  - Devin Local
  - Agent Command Center
---

# Windsurf 更名 Devin Desktop

## 一句话理解

> 2026-06-02，Cognition 通过 OTA 更新将 Windsurf 更名为 Devin Desktop，用 Rust 重写的 Devin Local 取代 Cascade（30% token 效率提升），默认界面从代码编辑器切换为 Agent Command Center——这不仅是品牌整合，更是"从 IDE 到 Agent 指挥中心"的产品范式转变。

## 事件时间线

| 日期 | 事件 |
|------|------|
| 2025-02 | Cognition 以 $30 亿估值收购 Windsurf（原 Codeium） |
| 2026-03 | [[Devin 2026年3月更新\|Devin 3月更新]]：Nubank 案例、Devin Review |
| 2026-05-29 | Windsurf 2.0 发布：Agent Command Center 和 Devin 集成预告 |
| 2026-06-02 | **Windsurf 正式更名为 Devin Desktop**，OTA 推送 |
| 2026-07-01 | 旧版 Cascade Agent 停止支持（过渡截止日期） |

## 核心变化

### 1. Cascade → Devin Local

| 维度 | Cascade（旧） | Devin Local（新） |
|------|--------------|------------------|
| 语言 | — | **Rust 完全重写** |
| Token 效率 | 基线 | **+30% 提升** |
| 子 Agent | 不支持 | **支持子 Agent** |
| 过渡期 | 可用至 2026-07-01 | 默认启用 |
| 定位 | IDE 内嵌 Agent | 本地 + 云端统一 Agent |

Rust 重写带来的 30% token 效率提升不仅是性能优化，更直接影响到使用成本——在 [[竞品成本对比|Agent 按 token 计费]] 的经济模型下，30% 的效率提升等于 30% 的成本下降。

### 2. 默认界面：Agent Command Center

这是最深远的变化。打开 Devin Desktop，**首先看到的不再是代码编辑器，而是 Agent 看板**。

```
传统 IDE 视角：
  打开 → 看到代码 → 偶尔调用 AI

Devin Desktop 视角：
  打开 → 看到所有 Agent 的状态看板 → 点进具体 Agent 才看代码
```

#### Agent Command Center 的界面结构

| 区域 | 功能 |
|------|------|
| **Kanban 看板** | 所有 Agent（本地 + 云端）按状态排列：进行中 / 阻塞 / 待审查 |
| **Spaces** | 新的上下文分组概念：将会话、PR、文件、上下文关联到一起 |
| **Agent 详情** | 点击具体 Agent 查看执行过程、代码变更、日志 |

#### 为什么这很重要

Agent Command Center 的默认化标志着一个行业转折点：**Cognition 认为未来的软件开发以 Agent 为中心，而非以代码为中心**。

代码编辑器仍然在，但它从"主界面"降级为"Agent 工作的一个视图"。这与 [[Cursor 2026年Q2更新|Cursor]] 坚持以编辑器为主界面的路线形成了鲜明对比。

### 3. Agent Client Protocol (ACP)

Devin Desktop 同步发布了 ACP（Agent Client Protocol），一个开源协议，允许：

- 任何 ACP 兼容的 Agent 在任何 ACP 兼容的编辑器中运行
- 任何 ACP 兼容的编辑器承载任何 ACP 兼容的 Agent

#### 首批支持的 Agent

| Agent | 提供商 | 说明 |
|-------|--------|------|
| Devin Local | Cognition | 原生支持 |
| Codex | OpenAI | 通过 ACP 接入 |
| Claude Agent | Anthropic | 通过 ACP 接入 |
| OpenCode | 开源社区 | 通过 ACP 接入 |

ACP 的战略意图很明确：**将 Devin Desktop 定位为"Agent 运行时"而非"特定 Agent 的专属编辑器"**。如果成功，Devin Desktop 将成为所有 AI Agent 的通用平台——这比只运行自家 Agent 的 [[Claude Code 2026年Q2更新|Claude Code]] 或 [[GitHub Copilot 2026年Q2更新|GitHub Copilot]] 更开放。

但 ACP 的挑战也很明显：Anthropic 有 [[MCP 协议 2026年3月进展|MCP]]，OpenAI 有自己的工具协议——行业需要的是一个统一协议，而非又一个新协议。

## Cognition 品牌整合分析

### 收购后的品牌策略

Cognition 在 2025 年 2 月收购 Windsurf（原 Codeium）后，面临一个经典的品牌整合问题：保留两个品牌还是统一为一个？

| 方案 | 优点 | 缺点 |
|------|------|------|
| 保留两个品牌 | 不失去 Windsurf 的用户认知 | 品牌混淆、资源分散 |
| 统一为 Devin | 品牌集中度高 | 可能流失 Windsurf 忠实用户 |
| **统一为 Devin Desktop** | 保留 Windsurf 产品形态 + Devin 品牌力 | 名称较长，但概念清晰 |

最终选择"Devin Desktop"是折中方案——用 Devin 品牌统一认知，用 "Desktop" 后缀区分产品形态（对应 Devin Cloud）。

### 用户迁移策略

| 策略 | 实施 |
|------|------|
| **OTA 无感更新** | 标准版本更新，无需手动操作 |
| **设置迁移** | 所有 Windsurf 设置自动迁移至 Devin Desktop |
| **扩展兼容** | 扩展保持兼容 |
| **价格不变** | 订阅计划和定价完全继承 |
| **过渡期** | Cascade 到 2026-07-01 可用 |

这是一次教科书级的"最小中断迁移"——用户几乎不需要做任何事情。

### 品牌整合的深层逻辑

Cognition 的品牌整合传递了一个明确信号：**"自主 Agent"是核心叙事，"IDE"只是载体**。

- **Devin**（云端 Agent）= 核心产品
- **Devin Desktop**（本地 Agent + IDE）= 桌面入口
- **Devin Local**（本地执行引擎）= 技术组件

整个产品线围绕"Devin"品牌构建，IDE 功能被降格为 Agent 的一个运行环境。这与 Cursor 的"AI 增强的 IDE"定位截然不同。

## 竞争格局影响

### 与主要竞品的定位对比

| 产品 | 核心定位 | 默认视角 | 模型策略 |
|------|---------|---------|---------|
| **Devin Desktop** | Agent 指挥中心 | Agent 看板 | 多 Agent（ACP） |
| [[Cursor 2026年Q2更新\|Cursor]] | AI IDE | 代码编辑器 | 多模型路由 |
| [[Claude Code 2026年Q2更新\|Claude Code]] | CLI Agent | 终端 | 绑定 Anthropic |
| [[GitHub Copilot 2026年Q2更新\|Copilot]] | 编码助手 | IDE 内嵌 | 主要 OpenAI |

四个产品选择了四条不同的路线：
1. **Devin Desktop**：Agent-first，编辑器是配角
2. **Cursor**：Editor-first，Agent 是增强
3. **Claude Code**：Terminal-first，命令行原生
4. **Copilot**：Platform-first，嵌入现有工具

### 对 OpenClaw 的影响

**威胁**：
1. ACP 如果成为事实标准，OpenClaw 的 Agent 需要兼容这个协议才能在 Devin Desktop 中运行
2. Agent Command Center 的理念可能成为行业趋势——如果用户习惯了"看 Agent 看板"而非"看代码"，OpenClaw 需要调整产品形态

**机会**：
1. Devin Desktop 的"Agent 指挥中心"理念过于激进——大量开发者仍然偏好以代码为中心的工作流。OpenClaw 可以在两者之间找到平衡点
2. ACP 是开源的，OpenClaw 可以实现 ACP 兼容而不被 Cognition 生态锁定
3. Cascade → Devin Local 的过渡期（到 7 月 1 日）可能造成部分用户流失——这些用户是 OpenClaw 的潜在受众

## 相关节点

- [[Devin 分析]]——Devin 产品完整分析
- [[Devin 2026年3月更新]]——Q1 的 Nubank 案例和 Devin Review
- [[Windsurf 分析]]——原 Windsurf 的产品分析
- [[OpenClaw vs Devin]]——详细竞品对比
- [[多Agent协作架构]]——Agent 编排趋势
- [[Cursor 2026年Q2更新]]——Cursor 的不同路线选择
- [[2026年Q2竞品新入局]]——市场新进入者
