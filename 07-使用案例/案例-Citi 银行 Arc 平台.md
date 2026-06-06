---
tags:
  - 案例
  - 企业
  - 金融
  - Citi
  - Agentic-AI
  - 2026Q2
aliases:
  - Citi Arc
  - 花旗银行 AI
  - Citi Agentic AI
  - Arc 平台
---

# 案例：Citi 银行 Arc 平台


![[assets/citi-arc.jpg]]

> **一句话总结**：2026 年 4 月，花旗银行推出 Arc——一个中央化的 Agentic AI 平台，被内部称为"Agent 操作系统"。18 万名员工中 80% 已在使用 AI 工具，Arc 的目标是将分散的 AI 用例统一到一个可治理、可审计、可扩展的平台上，并首先面向 40,000 名开发者引入 Cognition 的 Devin 编码 Agent。

**企业**：Citigroup（花旗集团）
**产品**：Arc Agentic AI 平台
**公告时间**：2026 年 4 月 30 日
**关键人物**：David Griffiths（Citi CTO）

## Arc 平台概述

### 定位

Arc 不是一个 AI 聊天机器人，而是一个**Agent 编排平台**——CTO David Griffiths 将其描述为"AI Agent 的操作系统"。它的核心功能是：

| 功能 | 说明 |
|------|------|
| **集中管理** | 将分散的 AI Agent 和用例统一到一个中央平台 |
| **编排** | 协调多个自主 Agent 协作完成复杂任务 |
| **治理** | 每个 Agent 的行为都被监控、审计和管控 |
| **可扩展** | 从开发者团队扩展到全行覆盖 |

### 与传统 AI 工具的区别

| 维度 | 传统 AI 工具（Citi AI） | Arc 平台 |
|------|------------------------|----------|
| 模式 | 人类提问 → AI 回答 | 人类布置任务 → Agent 自主执行 |
| 范围 | 单一工具、单一用例 | 多 Agent 编排、跨用例 |
| 治理 | 分散管理 | 中央化监控和审计 |
| 扩展性 | 按工具添加 | 按平台扩展 |

## 部署规模

| 指标 | 数值 |
|------|------|
| **企业 AI 工具用户** | 180,000 名员工 |
| **活跃使用率** | 80%+ 定期使用 |
| **Arc 首批用户** | 开发者（40,000 人规模） |
| **完成提示工程培训的员工** | 大多数有 AI 访问权的员工 |

80% 的使用率在企业级 AI 部署中极为突出。大多数企业的 AI 工具使用率在 20-40% 之间——Citi 的 80% 说明 AI 已深度嵌入日常工作流，而非"可选项"。

## Devin 集成

### 编码 Agent 部署

Citi 选择了 [[Cognition Series D 融资|Cognition 的 Devin]] 作为编码 Agent，面向内部开发者团队：

| 维度 | 详情 |
|------|------|
| **Agent** | Devin（Cognition AI） |
| **目标用户** | Citi 内部开发者 |
| **使用场景** | 自动化简单编程任务 |
| **安全控制** | 人类监控 + 随时中断能力 |

### 为什么选择 Devin

从 Citi 的视角，Devin 的优势在于：
1. **企业级客户验证**：[[Cognition Series D 融资|Goldman Sachs、Mercedes-Benz、NASA]] 等已在使用
2. **人类控制机制**：员工和管理者可以监控 Agent 行为并随时停止任务
3. **ACP 兼容**：[[ACP v1 生态扩展|Agent Client Protocol]] 支持意味着 Devin 可以集成到 Citi 已有的开发工具链中
4. **审计能力**：每个 Agent 动作都可追溯

## 业务用例

### 财富管理场景

Arc 最具代表性的用例之一是财富管理领域的客户会议准备：

**传统流程**：
```
银行家手动收集客户信息
  ↓ 数小时
整理市场数据和投资组合分析
  ↓ 数小时
准备会议材料
  ↓ 数小时
参加客户会议
```

**Arc 流程**：
```
Agent 团队自动收集客户信息
  ↓ 并行
Agent 分析市场数据和投资组合
  ↓ 并行
Agent 生成会议材料
  ↓ 分钟级
银行家审核 → 参加客户会议
```

官方表述："一个 AI Agent 团队将能够主动完成这些工作，并在需要时精确交付信息。"这改变了银行家的角色——从"协调者"（coordinator）变成"架构师和顾问"（architect and advisor）。

### 其他潜在用例

| 领域 | 可能的 Agent 应用 |
|------|------------------|
| **风险合规** | 自动化合规检查、监管报告生成 |
| **交易运营** | 交易确认、结算异常检测 |
| **客户服务** | 多语言客户查询处理 |
| **代码开发** | Devin 自动化编码任务 |
| **研究** | 市场研究报告自动生成 |

## 治理框架

Arc 的治理设计是其最重要的差异化特征——在金融业，没有治理的 AI 等于没有 AI。

### 核心原则

| 原则 | 详情 |
|------|------|
| **可监控** | 每个 Agent 的行为实时可见 |
| **可审计** | 所有 Agent 动作有完整日志 |
| **可治理** | 统一的策略引擎控制 Agent 权限 |
| **可中断** | 人类随时可以停止 Agent 任务 |
| **可度量** | 追踪每个 Agent 的价值交付 |

### 与 EU AI Act 的对齐

Arc 的治理设计天然符合 [[EU AI Act 2026 进展|EU AI Act]] 对高风险 AI 系统的要求：

| EU AI Act 要求 | Arc 实现 |
|---------------|----------|
| 技术文档 | Agent 行为日志和系统架构文档 |
| 人工监督 | 员工和管理者监控 + 中断能力 |
| 可追溯性 | 完整审计轨迹 |
| 控制机制 | "stop tasks if needed" |

这使 Citi 在欧洲市场的 Agent 部署具有合规优势。

## 部署策略

### 分阶段推出

| 阶段 | 对象 | 目的 |
|------|------|------|
| **Phase 1** | 开发者 | 在可控环境中验证 Agent 行为 |
| **Phase 2** | 特定业务线 | 验证业务价值和治理有效性 |
| **Phase 3**（规划中） | 全行推广 | 将成功用例扩展到所有业务线 |

"先开发者、后全行"的策略是典型的企业级 AI 部署路径——开发者既是 AI 工具的使用者，也是 AI 工具的建设者，他们最适合在早期发现和修复问题。

## 行业背景

### 金融业 Agentic AI 竞赛

| 银行 | AI Agent 策略 |
|------|---------------|
| **Citi** | Arc 平台 + Devin 集成 |
| **Goldman Sachs** | Devin 用户 + 内部 Agent 开发 |
| **JP Morgan** | LLM Suite 内部平台 |
| **Morgan Stanley** | AI 助手 + GPT-4 深度集成 |

Citi 的差异化在于"平台化思路"——不是只买一个 AI 工具，而是建一个 Agent 操作系统。这与 [[Fortune 500 企业 AI Agent 部署|Fortune 500 企业 AI Agent 部署]] 的趋势一致。

### 与 OpenClaw 的关系

虽然 Citi Arc 是企业自建平台，但其架构理念与 OpenClaw 有多处相似：

| 维度 | Citi Arc | OpenClaw |
|------|----------|----------|
| 核心理念 | Agent 操作系统 | 个人 AI Agent 框架 |
| Agent 编排 | 多 Agent 协作 | 多 Agent 工作流 |
| 工具调用 | 企业内部 API | [[MCP 协议|MCP]] + [[Skills 市场|Skills]] |
| 安全模型 | 企业级审计和治理 | 沙箱 + 权限控制 |
| 差异 | 封闭企业环境 | 开源开放生态 |

Citi Arc 可以被理解为"企业级闭源的 OpenClaw"——解决的是相同的问题（如何编排和治理 AI Agent），但在不同的安全和合规约束下。

## 关键洞察

### 1. "Agent 操作系统"是企业 AI 的终态

从"买工具"到"建平台"，Citi 的选择代表了企业 AI 部署的成熟方向。就像企业最终需要 Kubernetes 来管理容器一样，企业也将需要"Agent OS"来管理 AI Agent。Arc 可能是最早实现这一愿景的大型企业案例之一。

### 2. 80% 使用率是 Agent 部署的前提

Citi 能推出 Arc 是因为 80% 员工已经在用 AI——如果员工连基本的 AI 交互都不熟悉，直接上 Agent 只会造成混乱。这暗示了一个采纳路径：**AI 助手（Copilot）→ AI Agent → Agent 平台**。

### 3. "银行家从协调者到架构师"

这种角色转变与 [[案例-Reorx 从程序员到 Tech Lead|Reorx 的"程序员到 Tech Lead"转变]] 异曲同工——AI Agent 不是替代人类，而是改变人类的工作性质。在 Citi 的语境下，银行家不再花时间在数据收集和报告准备上，而是专注于客户关系和战略建议。

### 4. 治理即竞争力

在金融业，最好的 AI 不是最聪明的，而是最可控的。Citi 强调"every agent will be monitored, auditable and governed"——这不是限制，而是竞争力。无法被审计的 Agent 在受监管行业没有市场。

### 5. Devin 的企业化验证

Citi 选择 Devin 而非自建编码 Agent，说明 [[Cognition Series D 融资|Cognition]] 的企业销售能力已经成熟。当全球最大的银行之一信任你的 Agent 处理其内部代码，这是最强的产品验证。

## 与其他案例的关系

- 与 [[案例-14个Agent协作系统]] 在"多 Agent 编排"主题上共鸣——Citi Arc 是企业级实践
- 与 [[Fortune 500 企业 AI Agent 部署]] 数据互为印证——Citi 是 Fortune 500 中 Agent 部署最激进的案例之一
- 与 [[Deloitte 企业 AI Agent 采用报告]] 的行业预测吻合——金融业是 Agent 采纳最快的行业

## 相关笔记

- [[Cognition Series D 融资]] — Devin 的创造者
- [[ACP v1 生态扩展]] — Agent 与编辑器的协议
- [[Fortune 500 企业 AI Agent 部署]] — 企业 Agent 部署趋势
- [[EU AI Act 2026 进展]] — 金融业 Agent 合规
- [[AI Agent 市场趋势 2026 Q2]] — 市场趋势
- [[案例-Reorx 从程序员到 Tech Lead]] — 角色转变主题

## 外部链接

- [Citigroup 官方公告](https://www.citigroup.com/global/news/perspectives/2026/introducing-ai-agents-next-phase-citi-artificial-intelligence-journey)
- [Axios 独家报道](https://www.axios.com/2026/04/30/exclusive-citi-moves-into-agentic-ai)
- [CIO Dive](https://www.ciodive.com/news/citi-launches-arc-scale-ai-agents/819113/)
- [American Banker](https://www.americanbanker.com/news/citi-is-rolling-out-agentic-ai-to-its-40-000-developers)
- [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/citi-debuts-platform-to-bring-ai-agents-to-banking-work/)

> 来源：Citigroup 官方博客、Axios、CIO Dive、American Banker、PYMNTS，2026 年 4 月 30 日
