---
tags:
  - 基础概念
  - Discord
  - 部署
aliases:
  - Carbon Reconcile
  - Discord Command Deployment
---

# Carbon Reconcile

## 一句话理解

> Carbon Reconcile 是 Discord 的应用命令部署策略——像一个"声明式同步器"，对比本地定义和远端已注册的命令，只更新有差异的部分，而非每次全量重新注册。

## 在 OpenClaw 中的应用

v2026.3.22 将 Discord 原生命令部署从旧方案切换为 Carbon Reconcile（这是一个 **Breaking Change**）。此前 OpenClaw 使用自定义的命令注册流程，现在统一采用 reconcile 模式：

1. 启动时读取本地命令定义
2. 与 Discord API 已注册的命令对比
3. 只推送差异部分（新增/修改/删除）
4. 减少 API 调用次数，避免 rate limit

## 为什么重要

Discord 对应用命令注册有严格的 [[权限控制机制|rate limit]]。旧方案每次启动全量注册，在命令数量多时容易触发限制。Reconcile 模式让 OpenClaw 的 Discord 集成更稳定、更高效。

## 双链导航

- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
- [[v2026.3.22 Breaking Changes 迁移指南]] — 迁移说明
