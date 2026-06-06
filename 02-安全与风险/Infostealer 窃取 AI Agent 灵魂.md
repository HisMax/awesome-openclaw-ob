---
tags:
  - 安全
  - Infostealer
  - Vidar
  - 凭证窃取
  - AI灵魂
aliases:
  - AI灵魂窃取
  - Vidar窃取OpenClaw
  - 首例AI Agent窃取攻击
---

# Infostealer 窃取 AI Agent 灵魂

**一句话总结**：2026年2月13日，Hudson Rock 检测到 Vidar 变体首次窃取 OpenClaw 的 soul.md、MEMORY.md 和 device.json，标志着信息窃取器从浏览器凭证转向"收割 AI Agent 灵魂"的范式转变。

## 事件详情

Hudson Rock 于 **2026年2月13日** 检测到**首例**针对 [[OpenClaw 安全风险|OpenClaw]] 配置文件的 infostealer 攻击。攻击使用的是 **Vidar 变体**——与 RedLine、Lumma 并列的主流信息窃取器之一。

该恶意软件并非通过专门的"OpenClaw 模块"运作，而是利用广泛的文件抓取例程扫描 `~/.openclaw/` 目录，无意间获取了用户 AI 助手的**完整操作上下文**。

## 被窃取的关键文件

| 文件 | 内容 | 风险 |
|------|------|------|
| **`openclaw.json`** | 网关认证令牌（`gateway.auth.token`）、用户邮箱、认证配置 | 远程接管网关实例 |
| **`device.json`** | 设备公钥和**私钥**（`privateKeyPem`） | 伪装为受信设备，绕过 [[权限控制机制|安全配对检查]] |
| **`soul.md`** | Agent 行为准则、记忆文件（`AGENTS.md`、`MEMORY.md`） | 获取用户日常活动、私人消息、日程的完整蓝图 |

## 技术分析：为什么 AI Agent 配置成为目标

OpenClaw 配置文件采用**明文存储**，API 密钥、网关令牌、数据库凭证均无加密保护。RedLine、Lumma、Vidar 等窃取器已将 `~/.openclaw/` 路径加入"必窃"列表。

这种攻击的危险性在于其**信息密度**远超传统凭证窃取：

- 传统窃取：浏览器密码、Cookie → 单个服务的访问权
- AI 灵魂窃取：soul.md + 记忆文件 → 用户**完整的工作模式、思维习惯、日程安排**。Infostealer 窃取的 soul.md 和 MEMORY.md 正是[[三层记忆系统]]的核心——丢失记忆等于丢失身份
- 攻击者获得的不仅是技术访问权，更是用户的**认知模型副本**

这与 [[CEO 电脑 Root 访问出售事件]] 中 OpenClaw 作为集中式情报枢纽的风险直接呼应。

## Hudson Rock 的发现过程

Hudson Rock 的威胁情报平台在日常监控中发现 Vidar 样本的外泄数据包含 `.openclaw` 目录文件。这是该平台**首次**记录到针对 AI Agent 配置的窃取行为。

> 详见 [[Hudson Rock 威胁情报报告]] 中 CTO Alon Gal 的完整分析。

## 教训与洞察

- AI Agent 的配置文件应被视为与 SSH 私钥同等敏感的资产
- 明文存储是根本缺陷——应采用操作系统级密钥链或加密存储
- 窃取器开发者将推出专用模块解析 AI Agent 文件——"正如他们对 Chrome 和 Telegram 所做的那样"
- 这一事件揭示了 [[凭证泄露与信息窃取]] 威胁的全新维度

## 相关笔记

- [[凭证泄露与信息窃取]]
- [[Hudson Rock 威胁情报报告]]
- [[CEO 电脑 Root 访问出售事件]]
- [[安全最佳实践]]
- [[数据泄露风险]]
- [[暗网讨论分析]]
- [[Claw Chain 四漏洞链]] — 沙箱内凭证窃取的新攻击路径
- [[GTIG AI 生成零日攻击报告]] — 国家级行为者利用窃取的 Agent 凭证
- [[2026年Q2安全态势总览]] — Q2 安全态势

## 外部链接

- [Hudson Rock Threat Intelligence](https://hudsonrock.com)
- [CVE-2026-25253 - NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)
