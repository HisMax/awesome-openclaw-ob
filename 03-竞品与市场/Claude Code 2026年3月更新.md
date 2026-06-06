---
tags:
  - Claude-Code
  - 竞品动态
  - 2026年3月更新
  - Anthropic
aliases:
  - Claude Code 3月更新
  - Claude Code 2026.3
---

# Claude Code 2026年3月更新

2026 年 3 月，Claude Code 迎来了从"终端编码助手"到"多Agent协作平台"的质变。v2.1.81 搭载 Opus 4.6 模型（100万 token 上下文），Agent Teams 多智能体协作、Agent SDK 自定义编排、Remote Control 跨设备会话等一系列重磅功能集中落地，标志着 Claude Code 正式进入平台化阶段。

## v2.1.81（3月20日）

3月20日发布的 v2.1.81 是本月最重要的版本更新：

- **Opus 4.6 模型**：默认搭载 [[Claude 模型系列|Opus 4.6]]，100 万 token 上下文窗口——这意味着 Agent 可以一次性理解整个中型项目的代码库，不再需要分片处理
- 延续了 [[Claude Code v2.1 更新日志]] 中 v2.1.70 以来的快速迭代节奏

## Agent Teams：多智能体协作研究预览

Claude Code 正式推出多 Agent 团队协作能力（研究预览阶段）：

- **多代理协作研究**：多个 Claude Code 实例可以协同完成一个大型任务——一个负责前端、一个负责后端、一个负责测试
- **Worktree 隔离**：每个 Agent 在独立的 Git worktree 中工作，互不干扰，最终合并成果
- **后台运行**：Agent 可以在后台持续执行任务，开发者不需要一直盯着终端

这与 [[Cursor Automations]] 的多智能体并行和 [[多Agent协作架构]] 的行业趋势完全一致——从"一个 Agent 干所有活"走向"专家 Agent 分工协作"。

## Agent SDK：构建自定义 Agent

- **完全控制编排**：开发者可以用 Agent SDK 构建自己的 Agent 工作流，定义任务分配、执行顺序、工具访问
- **工具访问控制**：精细化控制 Agent 可以调用哪些工具——文件系统、Git、网络请求等
- **权限管理**：企业级权限模型，确保 Agent 在安全边界内运行

Agent SDK 本质上是把 Claude Code 从"产品"变成了"平台"——其他开发者可以基于它构建垂直领域的编码 Agent。

## Remote Control 正式化

在 [[Claude Code Remote Control|2月研究预览]] 的基础上进一步完善：

- **`/remote-control` 命令**：在手机或浏览器中继续编码会话
- 多平台支持扩展至：Terminal、VS Code、JetBrains、Desktop App、Web、Slack
- Chrome 集成：直接在浏览器中与 Claude Code 交互

## MCP Elicitation

- [[MCP 协议 2026年3月进展|MCP]] 服务器现在可以向 Claude Code 请求结构化输入
- Agent 在执行过程中遇到需要用户决策的场景时，可以弹出结构化表单而非纯文本对话
- 这是 MCP 协议从"Agent → 工具"单向通信走向"双向交互"的重要一步

## Claude Code Review

- 专门针对 AI 生成代码的质量检查工具
- 自动检测常见的 AI 代码问题：冗余逻辑、安全漏洞、性能问题
- 回应了开发者对 AI 生成代码质量信任度下降的担忧（参见 [[2026年3月AI行业动态]]）

## 安全研究亮点

- **Claude 在 Firefox 中发现 22 个漏洞**——这不仅是安全能力的展示，也是 Agent 自主安全审计的实践案例
- 体现了 Anthropic "安全优先"的品牌定位（参见 [[Constitutional AI]]）

## 费曼总结

如果说 v2.1.68-74 是 Claude Code 学会了"批量干活"和"自己安排日程"（参见 [[Claude Code v2.1 更新日志]]），那 v2.1.81 和 3 月的一系列更新是它学会了"带团队"、"让别人基于自己的能力建造东西"、以及"在手机上远程指挥"。从独立贡献者变成了团队 Leader + 平台。

## 相关笔记

- [[Claude Code 分析]] — 基本信息与定位
- [[Claude Code v2.1 更新日志]] — v2.1 周期完整变更
- [[Claude Code Remote Control]] — 远程控制功能详解
- [[MCP 协议 2026年3月进展]] — MCP 协议最新动态
- [[多Agent协作架构]]
- [[Agentic Coding]]
- [[竞品对比总览]]
- [[Claude Code 2026年Q2更新]] — Q2 后续：Dynamic Workflows、ultracode、Auto Mode
- [[Claude Opus 4.7-4.8 发布]] — Opus 4.7/4.8 模型迭代

## 外部链接

- [Claude Code 官网](https://docs.anthropic.com/claude-code)
- [Anthropic](https://www.anthropic.com)
