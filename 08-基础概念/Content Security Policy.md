---
tags:
  - 基础概念
  - 安全
  - Web
aliases:
  - CSP
  - 内容安全策略
---

# Content Security Policy

## 一句话理解

> CSP 是浏览器的"白名单安检"——告诉浏览器"只有这些来源的脚本可以执行、只有这些来源的样式可以加载"，所有未列入白名单的内容一律拦截，从根本上防止 XSS 攻击。

## 基本原理

CSP 通过 HTTP 响应头 `Content-Security-Policy` 或 `<meta>` 标签声明，指定哪些内容来源是可信的：

- `script-src`：允许执行的脚本来源
- `style-src`：允许加载的样式来源
- `img-src`：允许加载的图片来源
- `connect-src`：允许建立的网络连接

## 在 OpenClaw 中的应用

v2026.3.23 增强了 [[Dashboard 控制面板]] 的 CSP 策略：

- 为 `index.html` 中的内联 `<script>` 计算 **SHA-256 哈希**
- 将哈希值加入 `script-src` CSP 指令
- 默认阻止所有未列入白名单的内联脚本

这意味着即使攻击者成功注入了恶意脚本到 Dashboard 页面中（比如通过 [[Prompt Injection 风险|Prompt Injection]] 让 Agent 生成包含 `<script>` 的 HTML），浏览器也会因为哈希不匹配而拒绝执行——CSP 成为了最后一道防线。

## 与 XSS 防护的关系

传统 XSS 防护依赖输入转义（"不让恶意内容进来"），CSP 提供了额外的纵深防御（"即使进来了也不让执行"）。对于 Agent 可能自动生成 HTML 内容的 OpenClaw 场景，CSP 尤其重要。

## 双链导航

- [[Dashboard 控制面板]] — CSP 保护的目标
- [[安全边界与风险（总览）]] — 整体安全架构
- [[OpenClaw v2026.3 版本更新]] — v2026.3.23 增强
