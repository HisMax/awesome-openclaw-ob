---
tags:
  - 概念
  - Agentic-Coding
  - AI开发
aliases:
  - Agentic Coding
  - 智能体编程
  - Agent 编程
---

# Agentic Coding

Agentic Coding 是一种以 AI Agent 为核心驱动力的软件开发范式。开发者不再逐行编写代码，而是通过自然语言指令引导 AI Agent 自主完成代码的编写、测试和迭代。这种范式由大语言模型的推理能力驱动，正在催生 [[编程民主化]] 的新浪潮。

## 核心特征

1. **自然语言驱动**：开发者用 prompt 描述需求，Agent 自主生成代码
2. **自主决策循环**：Agent 自行规划步骤、调用工具、修正错误
3. **人在回路**：开发者审查和引导，而非手动编码
4. **迭代式交互**：通过持续对话逐步完善代码

## 典型实践

Peter Steinberger 的编码哲学是 Agentic Coding 的极端案例，也是 Vibe Coding 的先驱实践者：

- **多 Agent 并行**：同时运行 3-4 个不同的 AI Agent 在不同终端窗口
- **语音提示**：使用 WisprFlow 语音输入进行 prompt 编写
- **惊人产出**：2025 年 1 月一个人提交超过 6,600 次 commits
- **"ship beats perfect"**：先发布，再完善
- **Prompt Requests 替代 Pull Requests**：不再做传统代码审查，而是用自然语言请求替代

> "I ship code I don't read" —— Steinberger

## 代表工具

- **[[Claude Code 的技术架构|Claude Code]]**：Anthropic 的终端/IDE 代码 Agent，SWE-bench 80.8%
- **OpenClaw**：通用 AI Agent 框架，具备源代码自修改能力
- **Cursor**：AI 增强的 IDE

这些工具的共同基础是大语言模型的代码理解与生成能力，以及 [[Tool Use 机制]] 赋予的自主操作能力。

## 与传统开发的区别

| 传统开发 | Agentic Coding |
|---------|---------------|
| 开发者写代码 | Agent 写代码，开发者审查 |
| Pull Request 代码审查 | Prompt Request，信任 Agent 输出 |
| 手动调试 | Agent 自动诊断和修复 |
| 逐步实现 | 描述目标，Agent 自主规划 |

## 后续发展

v2026.4.7 引入的 **Session Branching** 对 Agentic Coding 场景特别有价值——Agent 可以在隔离的分支中尝试激进的代码修改，失败了回退，成功了合并。v2026.6.1 的 **Skill Workshop** 则让 Agent 可以在执行任务过程中将操作步骤直接封装为可复用 Skill，经人工审核后注册。详见 [[OpenClaw v2026.4 版本更新]] 和 [[OpenClaw v2026.6 版本更新]]。

## 相关笔记

- [[Claude Code 的技术架构]]
- [[Tool Use 机制]]
- [[编程民主化]]
- [[OpenClaw v2026.4 版本更新]] — Session Branching
- [[OpenClaw v2026.6 版本更新]] — Skill Workshop

## 参考

- [Anthropic 官网](https://anthropic.com)
- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
