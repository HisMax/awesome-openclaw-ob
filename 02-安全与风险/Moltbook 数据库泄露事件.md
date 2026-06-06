---
tags:
  - 安全
  - 数据泄露
  - Moltbook
  - Supabase
aliases:
  - Moltbook泄露
  - Moltbook安全事件
---

# Moltbook 数据库泄露事件

2026年1月31日，Wiz 研究团队发现 AI 社交网络 Moltbook（Nature 杂志曾报道的 AI Agent 社交平台）存在严重的 **Supabase 配置错误**，导致生产数据库完全暴露。

## 暴露数据

| 数据类型 | 数量 |
|----------|------|
| API 认证令牌 | **~150 万个**（允许完全冒充任何 Agent） |
| 用户邮箱 | **~35,000 个** |
| 早期访问注册邮箱 | **29,631 个** |
| 私人对话 | **~4,060 条**（部分含明文 OpenAI API 密钥） |

## 根本原因

- 客户端 JavaScript 中**硬编码 Supabase 凭证**
- 数据库未启用 **Row Level Security（RLS）**

## "Vibe Coding" 的代价

创始人 Matt Schlicht 公开表示"没有亲手写过一行代码"，完全由 AI 生成。这是 AI 辅助开发忽视代码执行安全的典型案例，也是 Karpathy 称之为"400K lines of vibe coded monster"的真实写照。

## 虚假繁荣

- 声称 150 万 "AI agents"，实际仅约 **17,000 个人类账户**（88:1 比例）
- 研究员 Gal Nagli 测试发现数分钟内可注册百万 Agent
- 这与 GitHub Stars 争议中的增长异常有类似的"数据注水"疑虑

## 响应速度

Wiz 于 2026-01-31 21:48 UTC 联系维护者，约 **3 小时 12 分钟**内完成修复（2026-02-01 01:00 UTC）。无证据表明数据在修复前被恶意利用。

## 相关笔记

- [[安全边界与风险（总览）]]
- [[数据泄露风险]]
- [[凭证泄露与信息窃取]]
- [[Karpathy 的 Claws 概念]]
- [[2026年Q2安全态势总览]] — AI Agent 生态安全全景

## 外部链接

- [Snyk Blog - AI Security](https://snyk.io/blog/)
- [NIST AI](https://www.nist.gov/artificial-intelligence)
