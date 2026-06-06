---
tags:
  - Cursor
  - 竞品动态
  - 2026年Q2
  - IDE
  - Design-Mode
aliases:
  - Cursor Q2更新
  - Cursor 2026.Q2
  - Cursor 3.6
  - Cursor 3.7
  - Cursor Design Mode
---

# Cursor 2026年Q2更新

## 一句话理解

> 2026 年 Q2，Cursor 连发两个大版本——3.6 的 Auto-review 让 Agent 更长时间自主工作且更安全，3.7 的 Design Mode 让非工程师也能通过点击/绘制/语音来修改 UI，同时引入 GPT-5 路由将多模型竞争内化为产品优势。Cursor 正在从"程序员的 AI IDE"转型为"所有人的 AI 开发平台"。

## 版本时间线

| 版本 | 日期 | 核心特性 | 重要程度 |
|------|------|---------|---------|
| Cursor 3.6 | 2026-05-29 | Auto-review 模式 | 高 |
| Cursor 3.7 | 2026-06-05 | Design Mode 改进 | 变革性 |

## Cursor 3.6：Auto-review 模式

### 核心概念

Auto-review 是一个新的运行模式（Run Mode），位于现有的 "Ask"（只问不做）和 "Auto"（完全自动）之间：

```
Ask Mode        →  每步都需用户确认
Auto-review     →  安全分类器自动审批低风险操作，拦截高风险操作
Auto Mode       →  完全自动执行
```

### 工作原理

| 步骤 | 说明 |
|------|------|
| 1. 分类 | 每个工具调用（Shell、MCP、Fetch）经过安全分类器评估 |
| 2. 允许列表 | 已在允许列表中的调用直接执行 |
| 3. 沙箱化 | 可以被沙箱隔离的调用在沙箱中执行 |
| 4. 拦截 | 分类器认为高风险的调用暂停等待用户审批 |

### 与 Claude Code Auto Mode 的对比

| 维度 | Cursor Auto-review | Claude Code Auto Mode |
|------|-------------------|----------------------|
| 分类逻辑 | 分类器决定 | 后台安全分类器 |
| 适用工具 | Shell、MCP、Fetch | 所有操作 |
| 启用方式 | UI 切换 / `local.autoReview` | 环境变量 |
| 设计哲学 | "够安全时自动，不确定时问" | "够安全时自动，危险时阻止" |

两者的设计理念非常相似——行业正在形成共识：**完全手动审批和完全自动执行都不是最优解**，智能分级审批才是正确方向。这对 [[Claude Code 2026年Q2更新|Claude Code 的 ultracode + Auto Mode]] 组合构成了直接的产品竞争。

### 对开发者体验的影响

Auto-review 解决了 Agent 工作流的核心痛点：

- **之前**：Agent 每执行一步就暂停等待确认，开发者被迫"看着 Agent 干活"
- **之后**：Agent 可以连续运行更长时间，只在真正需要判断时暂停

这直接影响了 Agent 的实际生产力——中断越少，Agent 完成任务的速度越快，开发者的注意力切换成本越低。

## Cursor 3.7：Design Mode

### 变革性意义

Design Mode 是 Cursor 2026 年最重要的战略举措。它将 AI 编码工具的用户群从"会写代码的人"扩展到了"所有需要修改 UI 的人"。

### 三种交互方式

**1. 点击选择（Click）**

在 Cursor 内置浏览器中直接点击 UI 元素。Cursor 会识别被选中元素的代码位置、周围布局和视觉关系。

- 支持多选：同时选中两个或更多元素
- 使用场景："让这两个按钮对齐"、"删除重复内容"

**2. 绘制标注（Draw）**

在浏览器视图上绘制标注：圈出区域、框选范围、标记动画页面的某一帧。

- 标注覆盖在冻结的视口快照上，Agent 看到的是用户标注时的精确页面状态
- 使用场景："把这个区域的间距加大"、"这个部分换成卡片布局"

**3. 语音描述（Voice）**

通过 Design Mode 覆盖层的麦克风直接语音描述变更。

- **关键特性**：Agent 执行中仍可使用语音——可以在前一个任务运行时用语音排队下一个变更
- 使用场景：设计师审查页面时即时口述修改

### 用户群扩展的战略意义

```
传统 AI IDE 用户群：
  开发者 ━━━━━━━━━━━━━━━━━━━━

Cursor + Design Mode 用户群：
  开发者 ━━━━━━━━━━━━━━━━━━━━
  设计师 ━━━━━━━━━━━━━━━━
  产品经理 ━━━━━━━━━━
  创始人 ━━━━━━━
```

这与 [[Vibe Coding]] 趋势完全一致——降低编码门槛，让更多人能直接参与产品开发。但 Design Mode 比 Vibe Coding 更进一步：不仅是"用自然语言写代码"，而是"用视觉和语音修改已有的 UI"。

## GPT-5 路由

### 多模型策略

Cursor 支持来自 OpenAI、Anthropic、Google、xAI 和 Cursor 自家的所有前沿模型：

| 提供商 | 模型 | 说明 |
|--------|------|------|
| OpenAI | GPT-5, GPT-5.5 | 包括新发布的 [[GPT-5.5 发布\|GPT-5.5]] |
| Anthropic | Opus 4.7, Opus 4.8 | [[Claude Opus 4.7-4.8 发布\|最新 Opus]] |
| Google | Gemini 3.5 Flash | 高速低成本 |
| xAI | Grok | 替代选项 |
| Cursor | 自研模型 | 针对特定场景优化 |

Auto 模式允许 Cursor 根据任务自动选择最佳模型。这是 Cursor 的核心差异化：**不绑定任何单一模型供应商**，将模型竞争转化为自身优势。

### 对 OpenClaw 的启示

Cursor 的多模型路由策略验证了一个假设：**用户不关心用的是哪个模型，只关心任务是否被最好地完成**。OpenClaw 如果也实现智能模型路由，可以直接借鉴这个策略。

## 与 OpenClaw 的竞争分析

### 竞争态势

| 维度 | Cursor 3.6/3.7 | OpenClaw | 差距分析 |
|------|---------------|----------|---------|
| 自主运行 | Auto-review 分级审批 | — | Cursor 领先，行业标配 |
| 用户群 | 开发者 + 设计师 + PM | 开发者为主 | Cursor 扩展更快 |
| 模型策略 | 多模型 + 自动路由 | 待定 | Cursor 生态更成熟 |
| 融资 | [[Cursor 2026年3月更新\|$23 亿]] | — | Cursor 资金充裕 |
| ARR | [[Cursor 的 ARR 突破\|$20 亿+]] | — | 商业验证完成 |

### Cursor 的护城河

1. **$20 亿+ ARR + $23 亿融资**：Cursor 的商业规模已经证明了"AI IDE"赛道的市场容量。但同时也意味着 Cursor 必须持续增长来匹配估值，这推动了 Design Mode 等扩展用户群的举措

2. **多模型中立性**：Cursor 不绑定模型供应商，可以始终提供"当前最好的模型"。这是对 Claude Code（绑定 Anthropic）和 [[GitHub Copilot 2026年Q2更新|GitHub Copilot]]（主要绑定 OpenAI）的结构性优势

3. **Marketplace 生态**：[[Cursor 2026年3月更新|3 月的 Marketplace 爆发]] 后，Cursor 的插件生态持续增长，形成网络效应

### OpenClaw 的机会

1. **Design Mode 的开放版本**：Cursor 的 Design Mode 是封闭的——如果 OpenClaw 提供类似的视觉交互能力但基于开放协议（如 [[MCP 协议 2026年3月进展|MCP]]），可以吸引不想被 Cursor 锁定的用户

2. **Auto-review 的透明版本**：Cursor 的安全分类器是黑盒。OpenClaw 如果提供可解释的审批逻辑（用户可以看到为什么某个操作被允许或拦截），可以赢得安全敏感的企业客户

3. **成本优势**：Cursor Pro+ $39/月的价格开始让部分开发者感到不值。OpenClaw 如果能在更低价位提供核心 Agent 能力，有明确的市场空间

## 相关节点

- [[Cursor 分析]]——Cursor 产品的完整分析
- [[Cursor 2026年3月更新]]——Q1 的 Marketplace 和 Automations
- [[Cursor 的 ARR 突破]]——商业数据
- [[OpenClaw vs Cursor]]——详细竞品对比
- [[Claude Code 2026年Q2更新]]——Claude Code 的 Auto Mode 竞争
- [[GitHub Copilot 2026年Q2更新]]——Copilot 的竞争动态
- [[Vibe Coding]]——Design Mode 所在的行业趋势
