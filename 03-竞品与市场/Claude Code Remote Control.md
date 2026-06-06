---
tags:
  - 竞品分析
  - Claude-Code
  - Anthropic
  - 远程控制
  - AI编码工具
aliases:
  - Remote Control
  - Claude Code 远程控制
  - CC Remote
---

# Claude Code Remote Control

## 一句话总结

Anthropic 于 2026.2.25 发布的研究预览功能，让开发者通过手机或浏览器远程操控本地终端中的 Claude Code 会话，采用纯出站 HTTPS 架构确保安全。

## 核心数据

| 维度 | 数据 |
|------|------|
| 发布日期 | 2026 年 2 月 25 日（研究预览） |
| 可用计划 | 仅限 Max 计划用户 |
| 网络架构 | 纯出站 HTTPS |
| 凭证机制 | 短期凭证 + TLS 加密桥 |
| 超时策略 | 网络断开约 10 分钟超时 |
| 持久性 | 关闭终端即结束 |
| 模型限制 | 仅 [[Anthropic 公司分析|Anthropic]] 模型 |

## 分析

Remote Control 解决的核心问题是"离开电脑后继续操控编码会话"。它将本地终端会话投射到手机上，开发者可以在通勤、会议间隙查看 Agent 进度并下达新指令。

安全设计上，Remote Control 选择了与 [[OpenClaw 商业模式|OpenClaw]] 截然不同的路径：纯出站 HTTPS 意味着不需要在防火墙上打开任何入站端口，短期凭证降低了令牌泄露后的风险窗口。相比 OpenClaw 的明文密钥存储和多个已知 CVE，这是企业级安全思维的体现。

但 Remote Control 的能力边界也很明确——它是会话制的，关闭终端即结束，不具备 OpenClaw 那样的 24/7 持续运行能力。它本质上是开发者工具的移动端延伸，而非通用 AI Agent。

## 关键洞察

Remote Control 和 [[OpenClaw vs Claude Code Remote Control|OpenClaw]] 的本质区别在于：一个是**把终端投射到手机**，另一个是**把 AI 内嵌到聊天 App**。前者服务开发者的编码工作流，后者服务所有人的日常自动化。二者目标场景完全不同，与其说竞争，不如说分别占据了 AI Agent 光谱的两端——[[Claude Code 分析|Claude Code]] 的专业深度 vs [[OpenClaw vs Claude Code|OpenClaw]] 的通用广度。Anthropic 用安全换取了能力的边界约束，这在 [[Fortune 500 企业 AI Agent 部署|企业部署场景]]中反而是优势。

## 外部链接

- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code)

## 2026年Q2关联

- Claude Cowork 的 **Dispatch 功能** 提供了类似的"手机操控电脑端 Agent"能力，但面向非开发者
- Claude Code 的 **Dynamic Workflows**（详见 [[Claude Code 2026年Q2更新]]）进一步扩展了远程操控的价值——手机端可以监控千级子 Agent 的执行状态

## 来源

- [VentureBeat - Claude Code Remote Control](https://venturebeat.com/orchestration/anthropic-just-released-a-mobile-version-of-claude-code-called-remote)
- [DevOps.com - Remote Control](https://devops.com/claude-code-remote-control-keeps-your-agent-local-and-puts-it-in-your-pocket/)
- [Help Net Security - Remote Control](https://www.helpnetsecurity.com/2026/02/25/anthropic-remote-control-claude-code-feature/)
