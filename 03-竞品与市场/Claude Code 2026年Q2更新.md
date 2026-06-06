---
tags:
  - Claude-Code
  - 竞品动态
  - 2026年Q2
  - Anthropic
  - Agent编排
aliases:
  - Claude Code Q2更新
  - Claude Code 2026.Q2
  - Dynamic Workflows
  - ultracode
---

# Claude Code 2026年Q2更新

## 一句话理解

> 2026 年 Q2，Claude Code 从"单 Agent 编码助手"进化为"千级子 Agent 编排引擎"——Dynamic Workflows 支持一次最多 1,000 个子 Agent（16 并发），ultracode 模式一键触发自动编排，Auto Mode 扩展至 Bedrock/Vertex/Foundry 三大云平台，插件生态全面简化。

## 核心更新一览

| 特性 | 发布日期 | 状态 | 影响等级 |
|------|---------|------|---------|
| Dynamic Workflows | 2026-05-28 | 研究预览 | 变革性 |
| ultracode 模式 | 2026-05-28 | 同步发布 | 高 |
| Auto Mode on Bedrock/Vertex/Foundry | 2026-05 | GA | 高 |
| 插件 .zip / URL 加载 | 2026-05 | GA | 中 |
| 插件自动加载 (.claude/skills/) | 2026-05 | GA | 中 |

## Dynamic Workflows：研究预览

### 架构革命

Dynamic Workflows 是 Claude Code Q2 最重要的更新。它的核心思路是：**用 JavaScript 脚本替代上下文窗口编排**。

传统方式：Claude Code 把所有信息塞进一个巨大的 context window，让模型自己搞清楚该做什么。随着任务复杂度上升，context window 成为瓶颈。

Dynamic Workflows 方式：Claude 在收到任务后，**先生成一个 JavaScript 编排脚本**，将任务拆解为子任务，分配给并行的子 Agent 执行，最终汇总验证结果。

```
用户请求
  ↓
Claude 生成编排脚本（JavaScript）
  ↓
拆解为 N 个子任务
  ↓
最多 16 个子 Agent 并发执行
  ↓
结果汇总 + 验证
  ↓
输出最终结果
```

### 关键参数

| 参数 | 数值 | 说明 |
|------|------|------|
| 最大子 Agent 数 | 1,000 | 单次请求可编排的上限 |
| 最大并发数 | 16 | 同时运行的子 Agent 数 |
| 编排语言 | JavaScript | Claude 动态生成的编排脚本 |
| 触发方式 | ultracode 模式 / 手动 | 两种触发路径 |

### 与 Agent Teams 的关系

[[Claude Code 2026年3月更新|3 月发布的 Agent Teams]] 是"多个 Claude Code 实例在不同 Git worktree 中协作"——人工指定分工，各自独立工作。

Dynamic Workflows 则是"一个 Claude Code 实例自动拆解任务，动态生成并行计划"——完全自动化的编排，粒度更细（子任务级而非项目级）。

两者的关系是：Agent Teams 适合"前端/后端/测试"级别的大粒度协作，Dynamic Workflows 适合"理解代码 → 修改 → 验证"级别的细粒度编排。

### 可用范围

| 计划 | 默认启用 | 说明 |
|------|---------|------|
| Pro | 手动启用 | 通过 ultracode 或 CLI flag |
| Max | **默认启用** | 开箱即用 |
| Team | **默认启用** | 开箱即用 |
| Enterprise | 管理员启用 | 需要管理员在策略中开启 |

## ultracode 模式

### 设计理念

ultracode 不是一个新模型，而是一个**组合设置**：

```
ultracode = xhigh effort + 自动 Dynamic Workflows 决策
```

当用户开启 ultracode：
1. 推理努力等级设为 `xhigh`（[[Claude Opus 4.7-4.8 发布|Opus 4.7 新增]]的最高档）
2. Claude **自动判断**当前任务是否需要 Workflow 编排
3. 如果需要，自动生成并执行 Workflow
4. 单次请求可触发多个连续 Workflow（理解 → 修改 → 验证）

### 使用场景

| 场景 | 是否触发 Workflow | 说明 |
|------|-------------------|------|
| 简单 bug 修复 | 否 | xhigh 直接处理 |
| 跨文件重构 | 是 | 拆解为多个文件的并行修改 |
| 大型代码迁移 | 是（连续多个） | 理解 → 迁移 → 测试 → 修复 |
| 代码审查 | 可能 | 取决于代码库规模 |

### 与 Auto Mode 的配合

推荐组合：**ultracode + Auto Mode**。原因是 ultracode 会生成大量子 Agent，如果每个子 Agent 的每个操作都需要用户审批，体验会极差。Auto Mode 使用后台安全分类器自动审批低风险操作，让整个流程顺畅运行。

## Auto Mode 扩展至云平台

| 云平台 | 支持模型 | 启用方式 |
|--------|---------|---------|
| Amazon Bedrock | Opus 4.7, Opus 4.8 | `CLAUDE_CODE_ENABLE_AUTO_MODE=1` |
| Google Vertex AI | Opus 4.7, Opus 4.8 | `CLAUDE_CODE_ENABLE_AUTO_MODE=1` |
| Azure Foundry | Opus 4.7, Opus 4.8 | `CLAUDE_CODE_ENABLE_AUTO_MODE=1` |

这对企业客户意义重大——很多企业因为数据合规要求，只能通过云平台的 VPC 端点访问模型。之前 Auto Mode 仅限 Anthropic API 直连，现在打通了企业最常用的三个云渠道。

## 插件生态升级

### .zip 和 URL 加载

| 方式 | 命令 | 用途 |
|------|------|------|
| 本地 .zip | `--plugin-dir path/to/plugin.zip` | 从本地 zip 包加载 |
| 远程 URL | `--plugin-url https://...` | 从 CI 构建产物等远程源加载 |
| 自动加载 | 放入 `.claude/skills/` 目录 | 下次启动自动加载 |

### 插件开发简化

- `claude plugin init` 命令可快速脚手架化新插件
- `/reload-skills` 命令无需重启即可重新扫描 skills 目录
- SessionStart hooks 可返回 `reloadSkills: true`，使新安装的插件在当前会话中即时可用

### 官方插件目录

Anthropic 在 GitHub 上发布了 [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) 官方插件仓库，提供经过审核的高质量插件集合。

## 与 OpenClaw 的竞争关系变化

### 竞争加剧的维度

1. **编排能力大幅领先**：Dynamic Workflows 的 1,000 子 Agent / 16 并发是当前行业最高规格。OpenClaw 的多 Agent 编排如果无法匹配这个规模，将面临"为什么不直接用 Claude Code"的质疑

2. **企业渗透加深**：Auto Mode 打通 Bedrock/Vertex/Foundry 意味着 Claude Code 可以在企业已有的云基础设施上无缝运行，降低了采购阻力

3. **插件生态降低门槛**：.zip/URL 加载和自动发现机制让第三方生态更容易繁荣，[[Cursor 2026年3月更新|Cursor Marketplace]] 式的生态护城河正在形成

### OpenClaw 的差异化空间

1. **模型无关性**：Claude Code 绑定 Anthropic 生态，OpenClaw 如果支持多模型编排（混合使用不同厂商的模型执行不同子任务），这是独有优势

2. **透明度**：Dynamic Workflows 的编排脚本由 Claude 自动生成，用户对中间过程的可见性有限。OpenClaw 如果提供更透明的编排过程（可视化任务拆解、进度追踪），可以吸引对黑盒不信任的用户

3. **成本优化**：ultracode + 大规模并行的 token 消耗是惊人的。OpenClaw 如果能在编排层做智能成本优化（比如识别哪些子任务可以用 Haiku 而非 Opus），有明确的价值主张

### 竞争格局总结

| 维度 | Claude Code Q2 | OpenClaw 应对方向 |
|------|---------------|------------------|
| 编排规模 | 1,000 子 Agent / 16 并发 | 多模型混合编排 |
| 云平台覆盖 | Bedrock + Vertex + Foundry | 更广泛的云适配 |
| 插件生态 | .zip / URL / 自动加载 | 开放协议、社区驱动 |
| 自动化程度 | ultracode + Auto Mode | 透明编排 + 成本优化 |

## 相关节点

- [[Claude Opus 4.7-4.8 发布]]——Opus 4.8 与 Dynamic Workflows 同日发布
- [[Claude Code 2026年3月更新]]——Q1 的 Agent Teams 和 Remote Control
- [[多Agent协作架构]]——行业多 Agent 编排趋势
- [[OpenClaw vs Claude Code]]——详细竞品对比
- [[Cursor 2026年Q2更新]]——Cursor 的 auto-review 竞争路线
- [[Agentic Coding]]——Agent 编码的大趋势
