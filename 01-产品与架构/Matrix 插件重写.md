---
tags:
  - OpenClaw
  - Matrix
  - 插件
  - Breaking Changes
  - 2026年3月
aliases:
  - Matrix Plugin Rewrite
  - matrix-js-sdk
  - Matrix 集成
---

# Matrix 插件重写

## 一句话理解

> 旧的 Matrix 插件像一辆手工改装车——能跑但零件都是非标的，坏了只有原作者能修；重写后的插件换上了"原厂发动机"（matrix-js-sdk），任何熟悉 Matrix 生态的开发者都能维护。

## 重写背景

v2026.3.22 对 Matrix 插件进行了**完全重写**，用官方 `matrix-js-sdk` 替代了之前的自定义实现。这是一个 Breaking Change，现有 Matrix 用户必须按迁移指南操作。

旧的自定义实现存在三个核心问题：事件处理逻辑与 Matrix 协议规范存在偏差，导致某些房间类型的消息无法正确接收；缺乏对加密房间的完整支持；以及维护者只有原始作者一人，社区无法有效贡献修复。迁移到官方 SDK 一次性解决了这三个问题。

## 核心特性

### 持久化事件去重

新插件实现了持久化的事件去重机制。Matrix 协议中，由于联邦（federation）特性，同一事件可能通过多个路径到达——旧实现使用内存去重，Gateway 重启后会重复处理历史事件。新实现将已处理的事件 ID 持久化到磁盘，即使重启也不会重复响应。

### Mention-Gated Messaging

新增 mention-gated 消息模式——在群聊房间中，Agent 只响应 @mention 的消息，忽略普通对话。这与 [[多频道消息架构]] 中其他平台（Discord、Telegram 群组）的行为保持一致，避免 Agent 在活跃群聊中过度响应。

### allowBots 策略

`allowBots` 配置项控制是否处理来自其他 Bot 的消息。默认关闭——这防止了两个 Agent 在同一房间中互相触发形成无限对话循环。这是 [[OpenClaw 官方安全模型]] 中"最小权限"原则在消息层面的体现。

## 迁移影响

此重写是 [[v2026.3.22 Breaking Changes 迁移指南]] 中的重要条目。迁移需要：

1. 更新插件依赖到新版本
2. 重新配置 Matrix homeserver 连接参数（格式变更）
3. 如果使用了自定义事件处理钩子，需要适配 matrix-js-sdk 的事件模型
4. 首次启动时会自动建立事件去重数据库，初始化可能需要额外时间

运行 `openclaw doctor --fix` 可以检测 Matrix 配置是否需要迁移。

## 与插件系统的关系

Matrix 插件是 [[Plugin 扩展系统]] 三类扩展中 Channel Adapter 类型的一个实例。它通过 `openclaw.extensions.channels` 声明入口，由 Gateway 的 `loader.ts` 在启动时自动发现和加载。重写后的插件遵循新的 `openclaw/plugin-sdk/*` 路径规范。

## 双链导航

- [[Plugin 扩展系统]] — Matrix 插件作为 Channel Adapter 的加载与注册机制
- [[v2026.3.22 Breaking Changes 迁移指南]] — 完整迁移步骤和影响清单
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入完全重写
- [[多频道消息架构]] — Matrix 是 OpenClaw 支持的消息平台之一
- [[OpenClaw 官方安全模型]] — allowBots 策略的安全理念来源
