---
tags:
  - OpenClaw
  - 架构
  - API
  - Breaking Changes
  - 2026年3月
aliases:
  - describeMessageTool
  - Message Tool Discovery
  - 消息工具发现
---

# ChannelMessageActionAdapter

## 一句话理解

> 旧的消息工具发现像"自我介绍"——每个适配器自己决定怎么描述自己的能力；新的 `describeMessageTool(...)` 像"统一简历模板"——所有适配器必须用同一个格式声明自己能做什么。

## 变更内容

v2026.3.22 将消息工具发现从旧的多方法模式迁移到统一接口：

| 旧方法（已移除） | 新方法 |
|-----------------|--------|
| `listActions()` | `ChannelMessageActionAdapter.describeMessageTool(...)` |
| `getCapabilities()` | 同上 |
| `getToolSchema()` | 同上 |

这是 [[v2026.3.22 Breaking Changes 迁移指南|Breaking Changes]] 的一部分，所有渠道适配器必须实现新接口。

## 设计动机

旧的三方法模式导致了工具描述的不一致——Telegram 适配器、Discord 适配器、[[飞书集成|飞书]]适配器各自用不同的格式描述相似的能力。这让 [[Agent Execution Loop|Agent]] 在选择工具时难以做出一致的比较。

统一后，Agent 看到的是标准化的工具描述，无论底层渠道是什么——这与 [[模型无关架构]] 在模型层面的统一理念一脉相承，只不过这次统一的是渠道层面。

## 影响范围

- 所有内置渠道插件已完成迁移
- 第三方渠道插件需要更新——运行 `openclaw doctor --fix` 可检测未迁移的插件
- [[ClawHub 官方技能注册表]] 中依赖旧 API 的 Skills 需要更新 import

## 双链导航

- [[Plugin 扩展系统]] — 插件如何声明能力
- [[Tool Use 机制]] — Agent 如何发现和选择工具
- [[Agent Execution Loop]] — 工具发现在执行循环中的位置
- [[v2026.3.22 Breaking Changes 迁移指南]] — 完整迁移说明
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
