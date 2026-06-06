---
tags:
  - Claude-Code
  - 更新日志
  - 工具动态
  - 2026年3月更新
aliases:
  - Claude Code 更新
  - Claude Code v2.1
---

# Claude Code v2.1 更新日志

Claude Code 在 2026 年 3 月迎来了一波密集更新，从 v2.1.68 到 v2.1.74，几乎每隔几天就有新版本发布。这不是简单的 bug 修复——每个版本都在推动 [[Agentic Coding]] 的边界。

简单来说：Claude Code 正在从"一个聪明的终端助手"进化为"一个能自己管理工作流的编码智能体"。

## v2.1.74（2026年3月12日）

最新版本聚焦于开发者体验和稳定性：

- **/context 命令改进**：更智能的上下文加载机制，让 Agent 能更精准地理解项目结构。这意味着你不再需要手动告诉它"去看看那个文件"，它自己就知道该看什么
- **autoMemoryDirectory**：自动记忆目录功能——Agent 会自动将关键项目信息持久化到指定目录中。跟记忆系统的理念一脉相承，但更加自动化，类似于三层记忆中的项目级记忆
- **内存泄漏修复**：长时间运行的 Agent 会话终于不再越跑越慢了。这对 Agent Execution Loop 的稳定性至关重要

> 来源：https://github.com/anthropics/claude-code/releases

## v2.1.70（2026年3月6-7日）

这个版本可能是整个 v2.1 周期中最重要的更新：

- **/loop 命令**：让 Agent 进入持续执行循环，类似 Heartbeat 的理念——Agent 不再是"问一下答一下"，而是可以持续运行任务
- **cron 调度**：定时任务支持。想象一下：每天早上 9 点自动跑测试、每周五下午自动生成代码审查报告
- **ExitWorktree**：Git worktree 的退出管理，配合多分支并行开发
- **Opus 4.6 默认模型**：Claude Opus 4.6 成为默认推理模型，推理能力更强
- **启动内存减少 426KB**：看似小事，但对于频繁启动 Agent 的开发者来说，累积效果非常可观

> 来源：https://github.com/anthropics/claude-code/releases

## v2.1.68（2026年3月3日）

这个版本引入了几个"范式级"功能：

- **/simplify 命令**：一键简化复杂代码，让 AI 帮你重构冗余逻辑
- **/batch 命令**：批量处理多个任务——比如同时重命名 20 个文件、同时修复 10 个类似的 bug
- **HTTP hooks**：外部系统可以通过 HTTP 回调与 Claude Code 交互，打开了与 CI/CD、监控系统集成的大门
- **worktree 共享**：多个 Agent 实例可以共享同一个 Git worktree，这是 [[多Agent协作架构]] 在代码层面的具体实现

> 来源：https://github.com/anthropics/claude-code/releases

## 研究预览功能

除了正式发布的版本，Claude Code 还在测试几个前沿功能：

- **多智能体团队协作**：多个 Claude Code 实例协同完成一个大型任务（比如一个负责前端、一个负责后端、一个负责测试）
- **自动记忆**：Agent 自动学习你的编码习惯和项目偏好，无需手动配置
- **Cowork 桌面应用**：Claude Cowork 的桌面版本，提供更直观的多 Agent 管理界面

## 费曼总结

把 Claude Code 的进化想象成雇员的成长：v2.1.68 学会了"批量干活"和"跟外部系统对话"；v2.1.70 学会了"自己安排日程"和"持续工作"；v2.1.74 学会了"自己整理笔记"和"高效利用资源"。研究预览则在探索"团队协作"——从独立开发者变成团队领导。

## 外部链接

- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code)

## 相关笔记

- [[Claude Code 分析]]
- [[Claude Code 的技术架构]]
- [[Agentic Coding]]
- [[多Agent协作架构]]
- [[Claude Code 2026年3月更新]] — 3月后续更新：v2.1.81、Agent Teams、Agent SDK
- [[Claude Code 2026年Q2更新]] — Q2 重大更新：Dynamic Workflows、ultracode、Auto Mode
- [[Claude Opus 4.7-4.8 发布]] — Opus 4.7/4.8 模型迭代
