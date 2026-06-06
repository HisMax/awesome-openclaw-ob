---
tags:
  - OpenClaw
  - 生态系统
  - Skills
  - 插件市场
aliases:
  - Skills Market
  - ClawHub
  - ClawHub 技能市场
  - 技能市场
  - Skills 生态
---

# Skills 市场


![[assets/skills-market.jpg]]

## 一句话理解

Skills 市场就像手机的 App Store——你的 Agent 出厂时只会基本操作，但通过安装 Skills，它可以学会控制浏览器、管理 GitHub、操作智能家居、甚至自我进化。[[ClawHub 官方技能注册表|ClawHub]] 就是 OpenClaw 的 "App Store"。

## 什么是 Skill？

Skill 是一个可安装的功能模块，赋予 Agent 新的能力。安装命令：

```bash
npx clawhub@latest install <skill-slug>
```

安装位置：
- 全局：`~/.openclaw/skills/`
- 工作空间级别：`<project>/skills/`

Skill 本质上是代码文件——这既是它强大的原因，也是它危险的原因。大多数 Skill 使用 TypeScript 编写，通过 npm 生态系统分发。

## ClawHub 核心数据

| 指标 | 数值 |
|------|------|
| 最初总技能数 | 5,705 |
| ClawHavoc 事件后清理至 | 3,286（删除 2,419 个可疑 Skills） |
| 精选技能（去重去恶意后） | 2,868 |
| 已确认恶意技能 | 341（感染率 12%） |
| 总下载量 | 150 万+ |

## 技能分类分布

| 类别 | 数量 | 说明 |
|------|------|------|
| AI & LLMs | 287 | 模型调用与 AI 工具 |
| 搜索 & 研究 | 253 | 信息检索能力 |
| DevOps & Cloud | 212 | 云基础设施管理 |
| Web & 前端 | 202 | 网页开发辅助 |
| 营销 & 销售 | 143 | 商业自动化 |
| 浏览器 & 自动化 | 139 | 网页操作 |
| 通讯 | 133 | 消息与邮件 |
| 编码代理 & IDE | 133 | 代码编写辅助 |
| 智能家居 & IoT | 56 | 物联网控制 |

## 热门 Skills 排行

| 排名 | 名称 | 下载量 | 特色 |
|------|------|--------|------|
| 1 | Capability Evolver | 35K | AI 自我进化引擎 |
| 2 | Wacli | 16K | 开发工具 |
| 3 | ByteRover | 16K | 实用工具 |
| 4 | Self-Improving Agent | 15K（132 stars，社区最高评分） | 自改进框架 |
| 5 | Gog | 14K | Google Workspace 集成 |
| 6 | Agent Browser | 11K | 浏览器自动化 |
| 7 | GitHub | 10K | PR / 代码审查 / CI |

值得注意的是，排名前两位的技能都与"自我进化"相关——社区对 Agent 自我改进的兴趣远超其他能力。

## Skills 的工作原理

Skills 通过 [[Agent-Flow-Loop 原理|Agent Execution Loop]] 的 Phase 3（Context Assembly）选择性注入：

1. 系统分析用户消息，判断需要哪些 Skills
2. **仅注入相关技能**到上下文中，避免 Token 膨胀
3. 技能定义中包含 [[Tool Use 机制|工具定义]]（TypeBox Schema）
4. 模型在 Phase 5（Tool Execution Loop）中调用这些工具

热重载机制：文件变更后 **250ms** 自动加载新版本，无需重启。

## 安全问题：ClawHub 的 "App Store 噩梦"

Skills 市场面临的最大挑战是**供应链安全**。详见 [[ClawHavoc 事件]] 和 [[恶意 Skills 供应链攻击]]。

核心数据：
- **36.82%** 的 Skills 存在漏洞（1,467/3,984）
- **13.4%** 是严重级别问题
- **341 个**已确认恶意 Skills（感染率 12%）
- 发布门槛极低：仅需 1 周以上的 GitHub 账户，**无代码审查、无签名**
- 这一问题体现了 OpenClaw 安全的核心挑战

单个攻击者 "hightower6eu" 就上传了 354 个恶意包。1Password 研究发现 ClawHub **下载量最高的 Skill** 实际分发了 Atomic Stealer 恶意软件。

### ClawHavoc 后的安全整改

- 大规模清理：5,705 → 3,286 个 Skills
- [[ClawHub 安全整改措施|VirusTotal 合作]]：所有上架 Skills 自动恶意软件扫描
- 社区审核：被举报 3 次后自动隐藏，进入人工复审

### 2026 年 Q2 安全现状

截至 Q2，Skills 生态已恢复增长至 **13,000+** 个公开技能（详见 [[OpenClaw GitHub 数据更新 2026Q2]]）。安全审计工具持续发展：

- 社区 6 步安全审计协议：元数据 & typosquat 检查 → 权限分析 → 依赖审计 → Prompt Injection 扫描 → 网络 & 数据外泄分析 → 内容红旗检测
- VirusTotal 集成持续运作，每个 Skill 页面展示扫描结果
- 已检测恶意技能维持在 **230+** 个水平（持续监控中）
- 总下载量从 150 万+ 增长至 **3,900 万+**

## 商业化

Skills 可以商业化：

| 模式 | 价格范围 |
|------|----------|
| 免费 + 付费混合 | 推荐模式 |
| 独立 Skill 定价 | $10 - $200 |
| 企业定制集成 | $500 - $2,000/次 |

早期卖家报告 $100 - $1,000/月被动收入。

## 跨界案例：游戏引擎插件

Tom Jaejoon Lee 为 Unity、Godot、Unreal 三大游戏引擎提供 AI Agent 控制插件——170+ 个工具，通过聊天界面操作游戏引擎。这展示了 Skills 生态的跨界潜力。

## 与 MCP 的关系

[[MCP 协议]] 是 Skills 的底层通信标准之一。OpenClaw 通过 `@modelcontextprotocol/sdk` 集成 MCP，使用 stdio 传输，支持标准生命周期（初始化→发现→调用）。MCP 让 Skills 可以更规范地与外部服务交互。

## 核心洞察

Skills 市场是 OpenClaw 生态飞轮的核心——更多 Skills -> 更多用例 -> 更多用户 -> 更多开发者 -> 更多 Skills。但这个飞轮的转动伴随着巨大的安全风险：**没有代码审查的开放市场，本质上就是给每台机器开了一扇后门**。

## 相关笔记

- [[Skills 商业化与定价]] - 商业化策略

## 外部链接

- [ClawHub](https://clawhub.dev)
- [npm](https://npmjs.com)
- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [MCP 官网](https://modelcontextprotocol.io)
