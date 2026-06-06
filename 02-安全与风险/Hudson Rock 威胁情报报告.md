---
tags:
  - 安全
  - 威胁情报
  - Hudson Rock
  - Infostealer
  - 行业分析
aliases:
  - Hudson Rock 报告
  - Alon Gal 安全警告
  - AI灵魂收割趋势
---

# Hudson Rock 威胁情报报告

**一句话总结**：Hudson Rock CTO Alon Gal 发出安全警告——信息窃取器已从浏览器凭证窃取进化到"收割个人 AI Agent 的灵魂和身份"，这是网络威胁格局的范式转变。

## 报告背景

Hudson Rock 是专注于 Infostealer 威胁情报的以色列安全公司。其平台在 **2026年2月** 的日常监控中，首次发现 Vidar 变体窃取了 [[OpenClaw 安全风险|OpenClaw]] 用户的完整配置文件。

这一发现经 The Hacker News、BleepingComputer、InfoStealers.com 等多家安全媒体独立确认报道。

## Alon Gal 的核心警告

> "这标志着从窃取浏览器凭证转向**收割个人 AI Agent 的'灵魂'和身份**。随着 AI Agent 深入工作流程，窃取器开发者将推出专用模块解析这些文件——正如他们对 Chrome 和 Telegram 所做的那样。"

Gal 作为 Hudson Rock CTO，其判断基于对 Infostealer 生态的长期追踪。关键论点：

1. **历史模式重复**：窃取器从浏览器 → 即时通讯 → 加密钱包 → **AI Agent**，每次新兴平台出现都会被纳入窃取目标
2. **模块化趋势**：当前的窃取是"无意间"的文件抓取副产品，但专用解析模块的出现只是时间问题
3. **信息价值升级**：AI Agent 配置包含的信息密度远超传统凭证

## 从凭证窃取到"AI 灵魂"的转变

| 阶段 | 目标 | 获取内容 | 价值 |
|------|------|---------|------|
| 第一阶段 | 浏览器 | 密码、Cookie | 单个账户访问权 |
| 第二阶段 | 即时通讯 | Telegram 会话、聊天记录 | 社交网络信息 |
| 第三阶段 | 加密钱包 | 私钥、助记词 | 直接经济价值 |
| **第四阶段** | **AI Agent** | **soul.md、记忆、设备密钥** | **用户的完整认知模型** |

详见 [[Infostealer 窃取 AI Agent 灵魂]] 中被窃取的具体文件分析。

## 技术发现细节

Hudson Rock 平台检测到的 Vidar 样本外泄数据包含：

- `openclaw.json`——网关认证令牌（`gateway.auth.token`）
- `device.json`——设备私钥（`privateKeyPem`）
- `soul.md`——Agent 行为准则和记忆文件

恶意软件利用广泛的文件抓取例程扫描 `~/.openclaw/` 目录。这意味着所有已安装窃取器的受感染机器，如果同时安装了 OpenClaw，配置文件**已经被窃取**。

## 教训与洞察

- 威胁情报平台需要扩展监控范围以覆盖 AI Agent 配置文件
- 安全行业应将 AI Agent 视为与浏览器同等重要的攻击面
- Infostealer 生态的进化速度与新兴技术的采用速度保持同步
- Hudson Rock 的发现与 [[暗网讨论分析|Flare 暗网分析]] 中"研究驱动但风险真实"的评估一致
- [[CEO 电脑 Root 访问出售事件]] 进一步验证了 AI Agent 作为高价值目标的趋势

## Q2 更新

Hudson Rock 的预测——"窃取器开发者将推出专用模块解析 AI Agent 文件"——在 Q2 得到了更多验证。2026 年 6 月报告的 160 亿凭证暴露事件中，AI Agent 配置文件正在成为窃取器的标准目标。[[GTIG AI 生成零日攻击报告]] 确认国家级行为者也在利用窃取到的凭证访问 OpenClaw 实例。

## 相关笔记

- [[Infostealer 窃取 AI Agent 灵魂]]
- [[凭证泄露与信息窃取]]
- [[暗网讨论分析]]
- [[CEO 电脑 Root 访问出售事件]]
- [[安全边界与风险（总览）]]
- [[数据泄露风险]]
- [[GTIG AI 生成零日攻击报告]] — 国家级行为者利用窃取凭证
- [[2026年Q2安全态势总览]] — Q2 安全态势

## 外部链接

- [Hudson Rock Threat Intelligence](https://hudsonrock.com)
- [Snyk Blog](https://snyk.io/blog/)
