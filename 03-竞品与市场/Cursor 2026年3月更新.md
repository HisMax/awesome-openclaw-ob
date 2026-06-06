---
tags:
  - Cursor
  - 竞品动态
  - 2026年3月更新
  - IDE
aliases:
  - Cursor 3月更新
  - Cursor 2026.3
---

# Cursor 2026年3月更新

2026 年 3 月是 Cursor 有史以来最密集的发布月——从 MCP Apps 交互式 UI 到 JetBrains 支持、从 Automations 常驻 Agent 到 Marketplace 生态爆发，再到 Composer 2 引发的 Kimi 争议。Cursor 正在从"AI IDE"加速进化为"AI 开发平台"，同时也因模型溯源问题首次卷入地缘政治漩涡。

## v2.6（3月3日）：MCP Apps 与团队 Marketplace

- **MCP Apps 交互式 UI**：MCP 服务器可以直接在 Cursor 中渲染富交互界面——不再只是文本输入输出，Agent 可以展示图表、表单、可视化组件
- **团队 Marketplace**：企业团队可以在私有 Marketplace 中共享和管理 MCP 插件、Prompt 模板和自动化规则
- 这与 [[MCP 2026 路线图]] 中 MCP Apps（UI 扩展）的方向完全吻合

## JetBrains IDE 支持（3月4日）

- 通过 **Agent Client Protocol** 实现 Cursor 的 Agent 能力在 JetBrains 全家桶中运行
- 覆盖 IntelliJ IDEA、PyCharm、WebStorm 等主流 JetBrains IDE
- 这打破了 Cursor 只能在自有 IDE 中使用的限制，正面挑战 [[GitHub Copilot 分析|GitHub Copilot]] 的多 IDE 覆盖策略

## Automations 持续进化（3月5日）

在 [[Cursor Automations]] 的基础上进一步扩展：

- **常驻 Agent**：真正的 7x24 后台运行，不再依赖用户保持窗口打开
- **事件触发源扩展**：
  - Slack：团队消息触发自动修复
  - Linear：项目管理 Issue 自动分配给 Agent
  - GitHub：PR/Issue 事件驱动
  - PagerDuty：生产告警自动响应
- 与 Claude Code 的 Agent Teams 形成差异化——Cursor 走事件驱动路线，Claude Code 走协作编排路线

## Marketplace 生态爆发（3月11日）

- **新增 30+ 官方插件**：Atlassian（Jira/Confluence）、Datadog、GitLab、Sentry、Notion 等
- 这些插件将 Cursor 的 Agent 能力从"写代码"扩展到了"管理整个开发生命周期"
- Marketplace 的繁荣程度直接影响 Cursor 的平台护城河深度

## Composer 2（3月19日）与 Kimi 争议

Composer 2 是 Cursor 本月最具争议的更新：

- **功能层面**：Composer 2 大幅提升了多文件重构和跨项目理解能力
- **争议核心**：被爆出 Composer 2 基于月之暗面（Moonshot AI）的 **Kimi 2.5 模型**加 RL 训练
- 详见 [[Cursor Composer 2 与 Kimi 争议]] 的完整分析

## 融资：23 亿美元

- Cursor 完成 **23 亿美元**新一轮融资
- 这使其成为 AI 编码工具赛道融资额最高的公司之一
- 结合 [[Cursor 的 ARR 突破|$10亿+ ARR]]，Cursor 的商业规模已进入独角兽头部梯队
- 详见 [[Vibe Coding 融资爆发]]

## 相关笔记

- [[Cursor 分析]] — 基本信息与定位
- [[Cursor Automations]] — Automations 功能详解
- [[Cursor 的 ARR 突破]] — 商业数据
- [[Cursor Composer 2 与 Kimi 争议]] — Kimi 模型争议完整分析
- [[Vibe Coding 融资爆发]] — 行业融资总览
- [[MCP 协议 2026年3月进展]] — MCP 协议动态
- [[竞品对比总览]]
- [[Cursor 2026年Q2更新]] — Q2 后续：3.6 Auto-review、3.7 Design Mode

## 外部链接

- [Cursor 官网](https://cursor.com)
- [Cursor Changelog](https://changelog.cursor.com)
