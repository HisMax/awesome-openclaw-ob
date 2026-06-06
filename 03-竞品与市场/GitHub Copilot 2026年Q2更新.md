---
tags:
  - GitHub-Copilot
  - 竞品动态
  - 2026年Q2
  - OpenAI
  - 计费模型
aliases:
  - Copilot Q2更新
  - GitHub Copilot 2026.Q2
  - Copilot AI Credits
  - Copilot App
---

# GitHub Copilot 2026年Q2更新


![[assets/copilot-q2.jpg]]

## 一句话理解

> 2026 年 Q2，GitHub Copilot 经历了创立以来最大的商业模式转型——从固定月费转向 usage-based billing（AI Credits），Opus 模型从 Pro 计划移除（仅 Pro+ 保留 Opus 4.7），同时 Copilot App 技术预览带来了 canvases、语音对话、cloud sessions 和 agentic browsing，标志着 Copilot 从"IDE 插件"向"Agent 原生桌面应用"的形态进化。

## 计费模式变革

### 从固定月费到 AI Credits

2026-06-01，所有 Copilot 计划正式切换为 usage-based billing。这是 Copilot 商业模式的根本性变化。

| 计划 | 月费 | 包含 AI Credits | 说明 |
|------|------|----------------|------|
| Pro | $10/月 | $10 额度 | 月费不变 |
| **Pro+** | **$39/月** | **$39 额度** | 月费不变 |
| Business | $19/用户/月 | $19/用户 额度 | 月费不变 |
| Enterprise | $39/用户/月 | $39/用户 额度 | 月费不变 |

#### AI Credits 计算方式

- **1 AI Credit = $0.01 USD**
- 用量按 token 消耗计算（输入 + 输出 + 缓存 token），使用各模型的上市 API 费率
- 代码补全和 Next Edit 建议**不消耗 Credits**——这是关键，保护了最高频的使用场景
- 代码审查同时消耗 AI Credits 和 GitHub Actions 分钟数

#### 为什么转向 usage-based

GitHub 的官方解释很直白：**Agentic 工作流根本性地改变了 Copilot 的计算需求**。

```
旧模型：用户发送短 prompt → 模型返回代码片段 → 几百 token
新模型：用户启动 Agent → Agent 并行运行数小时 → 数十万 token
```

固定月费 $10 无法覆盖 Agent 模式下的 token 消耗。一个长时间运行的 Agent 会话可能消耗等价于一个月正常使用量的 token。

#### 用户反应

转向 usage-based billing 引发了显著的社区反弹：

1. **可预测性丧失**：开发者之前知道每月最多花 $10/$39，现在需要时刻关注用量
2. **模型降级恐惧**：如果 Credits 用完，体验会降级还是停止服务？
3. **企业预算复杂化**：企业需要为每个开发者设定预算上限，增加了管理成本

GitHub 推出了用户级预算控制（budget controls）来部分缓解这些问题，但根本矛盾——Agent 消耗的不可预测性——仍然存在。

### 退款政策

如果用户对新计费模式不满意，可以在 2026-05-20 之前取消订阅并获得退款。这个日期先于 6 月 1 日正式切换，给了用户一个"用脚投票"的窗口。

## Opus 模型从 Pro 计划移除

### 变更详情

| 计划 | Opus 模型状态 | 说明 |
|------|-------------|------|
| Pro ($10/月) | **移除** | 不再提供任何 Opus 模型 |
| Pro+ ($39/月) | **保留 Opus 4.7** | Opus 4.5 和 4.6 被移除 |
| Business | 取决于管理员配置 | — |
| Enterprise | 取决于管理员配置 | — |

### 为什么移除

原因很简单：**经济不可持续**。

[[Claude Opus 4.7-4.8 发布|Opus 4.7]] 的 API 价格是 $5/$25 per M tokens。一个每月写 10 万 token prompt + 50 万 token 输出的中度用户，模型成本就接近 $13——超过了 $10 月费。在 Agent 模式下，这个数字更是轻松翻倍。

Opus 移除 + usage-based billing 的组合本质上是在说：**如果你想用最好的模型，你需要为此付出与模型成本匹配的价格**。

### 对 Copilot 竞争力的影响

| 维度 | Pro ($10) | Pro+ ($39) |
|------|-----------|------------|
| 最强模型 | GPT-5.5 | GPT-5.5 + Opus 4.7 |
| 差异化 | — | Opus 是独有优势 |
| 竞品对标 | [[Cursor 2026年Q2更新\|Cursor]] Pro ($20) | Cursor Pro+ ($40) |

$10 的 Pro 用户失去 Opus 后，与免费 ChatGPT（已有 [[GPT-5.5 发布|GPT-5.5 Instant]]）的差距缩小。这可能加速部分用户迁移到 Cursor 或 Claude Code。

## Copilot App 技术预览

### 发布时间线

| 日期 | 事件 |
|------|------|
| 2026-05-14 | Copilot App 技术预览首次发布（限量） |
| 2026-06-02 | 扩展至所有 Pro、Pro+、Business、Enterprise 用户 |

### 产品定位

Copilot App 是一个**独立桌面应用**（macOS、Windows、Linux），不是 VS Code 扩展。它的核心理念是：**Agent 需要自己的应用，而不是嵌在编辑器里**。

这与 [[Windsurf 更名 Devin Desktop|Devin Desktop]] 的 Agent Command Center 思路高度相似——行业正在形成共识：Agent 工作流需要超越传统 IDE 的交互范式。

### 核心特性

#### 1. Canvases（画布）

Canvases 是人与 Agent 之间的**双向工作面板**。Agent 在画布上更新工作状态，用户可以直接在画布上编辑、重排、审批或重定向工作。

支持的工作对象：

| 类型 | 说明 |
|------|------|
| 计划 | Agent 的执行计划 |
| Pull Request | PR 创建和审查 |
| 浏览器会话 | Agent 的网页浏览 |
| 终端 | 命令行操作 |
| 发布清单 | 发布流程管理 |
| 迁移看板 | 代码迁移追踪 |
| 事件响应 | 生产事件处理 |
| 电子表格 | 数据分析 |
| 仪表盘 | 监控和可视化 |
| 云控制台 | 云资源管理 |
| 工作流状态 | CI/CD 流程 |

这个列表揭示了 GitHub 的野心——Copilot App 不只是"写代码"，而是要覆盖软件工程的**全生命周期**。

#### 2. 语音对话（Voice Conversations）

- 使用**设备端语音转文字**（speech-to-text），音频不离开本机
- 与 Copilot CLI 中的语音功能相同的技术栈
- 隐私优先的设计——这是对 [[Cursor 2026年Q2更新|Cursor Design Mode 语音]] 的差异化竞争

#### 3. Cloud Sessions

- 从 App 中直接启动云端 Agent 会话
- 与 `copilot --cloud` CLI 命令相同的底层能力，但有图形界面
- 解决了本地算力有限时的 Agent 运行问题

#### 4. Agentic Browsing

- Agent 可以自主浏览网页、收集信息、执行操作
- 与 [[Claude Opus 4.7-4.8 发布|Opus 4.8 的 Online-Mind2Web 84%]] 结合，浏览器 Agent 正在成为标配能力
- 区别于 [[Google Project Mariner 分析|Project Mariner]] 的独立浏览器方案，Copilot 将浏览器 Agent 集成到了开发工作流中

### Copilot App vs 竞品桌面方案

| 维度 | Copilot App | Devin Desktop | Cursor |
|------|------------|---------------|--------|
| 形态 | 独立桌面应用 | 独立桌面应用 | IDE |
| 默认视图 | Canvases | Agent Command Center | 代码编辑器 |
| 代码编辑 | 通过 Canvases | 内嵌编辑器 | 原生编辑器 |
| Agent 协议 | 自有 | ACP（开源） | 多模型 |
| 语音 | 设备端 STT | — | Design Mode 覆盖 |
| 云 Agent | Cloud Sessions | Devin Cloud | 云沙箱 |

## 竞争格局影响

### Usage-based billing 的行业信号

Copilot 的转型向整个行业发出了信号：**固定月费在 Agent 时代不可持续**。

| 竞品 | 当前计费 | 可能的跟进 |
|------|---------|-----------|
| [[Cursor 2026年Q2更新\|Cursor]] | 固定月费 + 速率限制 | 可能引入 usage-based |
| [[Claude Code 2026年Q2更新\|Claude Code]] | API token 计费 / Max 固定月费 | 已经是 usage-based |
| [[Windsurf 更名 Devin Desktop\|Devin Desktop]] | 固定月费 | 可能跟进 |

Claude Code 的 API 直接计费模式实际上是最"诚实"的——你用多少付多少。Copilot 的 AI Credits 本质上是把这个模式包装了一层，但核心逻辑相同。

### 对 OpenClaw 的影响

1. **计费模式参考**：Copilot 的 AI Credits 转型提供了正反两面的参考——usage-based 更公平，但可预测性差导致用户反弹。OpenClaw 可以考虑"固定基础额度 + 超额按量"的混合模式

2. **Opus 移除是机会**：$10/月的 Copilot Pro 用户失去 Opus 后，如果 OpenClaw 能以类似价格提供 Opus 级别的能力，这是明确的获客窗口

3. **Copilot App 定义了新形态**：Canvases + 语音 + 云 Agent 的组合正在成为"Agent 原生应用"的标准配置。OpenClaw 的产品形态需要考虑是否跟进

## 相关节点

- [[GitHub Copilot 分析]]——Copilot 产品完整分析
- [[GitHub Copilot 2026年3月更新]]——Q1 的 GPT-5.4 和 Jira Agent
- [[OpenClaw vs Copilot Tasks]]——详细竞品对比
- [[GPT-5.5 发布]]——Copilot 的核心模型
- [[竞品成本对比]]——行业定价格局
- [[AI 编码助手市场数据]]——市场规模和份额
- [[Windsurf 更名 Devin Desktop]]——Devin Desktop 的类似转型
