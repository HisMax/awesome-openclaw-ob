---
tags:
  - 基础概念
  - 无障碍
  - UI
aliases:
  - WCAG
  - WCAG 2.1 AA
  - Web Content Accessibility Guidelines
  - 无障碍合规
---

# WCAG 无障碍标准

## 一句话理解

> WCAG 是 Web 内容的"无障碍规范"——规定了文字与背景的最低对比度、按钮的最小点击区域、屏幕阅读器的标签要求等，确保视力障碍、运动障碍等用户也能正常使用 Web 应用。

## 级别

| 级别 | 要求 | 典型标准 |
|------|------|----------|
| A | 最低 | 所有非文本内容有替代文本 |
| **AA** | 推荐 | 文字对比度 ≥ 4.5:1，UI 组件对比度 ≥ 3:1 |
| AAA | 最高 | 文字对比度 ≥ 7:1 |

## 在 OpenClaw 中的应用

v2026.3.23 将 [[Control UI 主题系统]] 升级为 **WCAG 2.1 AA 合规**：

- 按钮原语整合（`btn--icon`/`btn--ghost`/`btn--xs`）统一达到 AA 对比度
- **Knot 主题**精炼为黑红色调，满足 AA 对比度要求
- Diagnostics/CLI/Secrets/ACP/MCP 配置界面增加配置图标（视觉辨识）
- 使用 filter 增加 `aria-labels`（屏幕阅读器支持）

这是 OpenClaw 首次系统性地关注无障碍——@BunsDev 在 PR #53272 中完成了这项工作。

## 为什么重要

随着 OpenClaw 从开发者工具向企业级平台转型（参见 [[OpenClaw 商业模式]]），企业客户通常要求其内部工具符合无障碍标准——这是采购审批的常见门槛。WCAG AA 合规扫清了这一障碍。

## 双链导航

- [[Control UI 主题系统]] — 具体实现 WCAG 合规的 UI 组件
- [[Dashboard 控制面板]] — WCAG 保护的目标界面
- [[OpenClaw v2026.3 版本更新]] — v2026.3.23 合规
- [[OpenClaw 商业模式]] — 企业合规需求的商业背景
