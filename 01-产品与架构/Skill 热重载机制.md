---
tags:
  - Skills
  - 热重载
  - 架构
  - 自修改软件
aliases:
  - 热重载
  - 热更新
  - Skill Hot Reload
  - 250ms debounce
---

# Skill 热重载机制

## 一句话理解

> OpenClaw 的 Skill 文件被修改后，系统在 250ms 内自动加载新版本——无需重启、无需重新部署。这意味着 Agent 可以在运行中修改自己的行为，实现"自我进化"。

## 核心概念

### 热重载的工作原理

```
Skill 文件变更 → 文件监视器检测 → 250ms debounce → 自动加载新版本 → Agent 立即使用新行为
```

**250ms debounce** 是关键设计：当文件快速连续变更时（如 Agent 正在逐行编写代码），系统等待最后一次变更后 250ms 才触发重载，避免加载中间不完整状态。

### 文件监视器

OpenClaw 的 `src/plugins/loader.ts` 负责：
1. 启动时扫描 `package.json` 中的 `openclaw.extensions` 字段
2. 自动发现并加载第三方插件
3. **持续监控** Skills 目录（`~/.openclaw/skills/` 和 `<workspace>/skills/`）的文件变更
4. 变更触发后，重新解析 Skill 定义并注入 Agent 运行时

### "自我修改软件"——最具争议的设计

[[Peter Steinberger|Steinberger]] 的原话：
> "I made the agent very aware — it knows what its source code is."

Agent 可以直接修改工作空间中的 `.ts` / `.js` 源文件：
- 修改 Skill 定义以改变自身行为
- 调整系统提示模板
- 添加新的工具实现

修改完成后，热重载机制**立即**生效——Agent 不需要等人来重启它，250ms 后就能使用自己刚写的新能力。

### ClawHub 最热门的自进化 Skills

| Skill | 下载量 | 功能 |
|-------|--------|------|
| **Capability Evolver** | 35K | AI 自我进化引擎 |
| **Self-Improving Agent** | 15K（132 stars，社区评分最高） | 自改进框架 |

这两个 Skill 都依赖热重载机制：Agent 分析自身不足 → 编写新 Skill 代码 → 热重载生效 → 能力自动增强。

## 应用与影响

- **开发者体验**：Skill 开发的迭代周期从"修改→重启→测试"缩短为"修改→250ms→立即生效"
- **Agent 自主性**：热重载是"自我修改软件"的技术基础——没有它，Agent 每次修改代码后都需要人工重启
- **安全风险**：[[提示注入]]攻击可以诱骗 Agent 修改自己的 Skill 文件，热重载让恶意修改 250ms 后即刻生效，攻击者甚至可以通过修改 SOUL.md 植入持久化后门
- **对比 Claude Code**：Claude Code 是会话制工具，没有热重载需求；OpenClaw 作为 24/7 运行的守护进程，热重载是保证持续运行的关键机制

## 关键洞察

250ms debounce 热重载体现了 OpenClaw 的核心设计哲学：**"ship beats perfect"**。传统软件的插件系统需要精心设计的加载/卸载生命周期；OpenClaw 选择了最简单粗暴的方式——文件变了就重新加载，250ms 足够过滤掉抖动。这种设计在快速迭代中非常高效，但也是 [[安全边界与风险（总览）|Aikido.dev 评价"尝试保护 OpenClaw 是荒谬的"]] 的原因之一——当 Agent 可以 250ms 内修改自己的源代码时，任何静态安全措施都可能被动态绕过。

## 后续演进：Skill Workshop（v2026.6）

v2026.6.1 引入 **Skill Workshop**——Agent 在执行任务过程中总结的操作步骤可以直接封装为 Skill，需要人工审核确认后才能注册到 Skill 库。这将 Skill 创建的门槛从"手写 YAML 定义"变为"让 Agent 帮你写，你审一遍"。Workshop 创建的 Skill 同样受益于 250ms debounce 热重载机制——审核通过后立即生效。详见 [[OpenClaw v2026.6 版本更新]]。

## 双链导航

- [[OpenClaw 是什么]] — 热重载依附的核心框架
- [[OpenClaw v2026.6 版本更新]] — Skill Workshop
- [[Agent Execution Loop]] — 热重载后 Agent 立即使用新 Skill 的执行流程
- [[Tool Use 机制]] — Skills 通过 Tool Use 被 Agent 调用
- [[安全边界与风险（总览）]] — 自修改能力带来的安全隐患
- [[ClawHub 技能市场]] — Skills 的分发与安装
- [[TypeScript]] — Skills 的主要编写语言

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [MCP 规范](https://modelcontextprotocol.io)
