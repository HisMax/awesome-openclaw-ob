---
tags:
  - OpenClaw
  - 提供商
  - MiniMax
  - 2026年3月
aliases:
  - MiniMax Provider
  - M2.7
  - M2.7-highspeed
---

# MiniMax M2.7 系列

## 一句话理解

> v2026.3.22 将 MiniMax 的 API 和 OAuth 认证合并为单一插件，同时新增 M2.7 和 M2.7-highspeed 模型——从"两个入口"简化为"一个统一入口"，体现了 [[Provider-Plugin 架构]] "一个插件一个提供商"的设计原则。

## 变更内容

- **API/OAuth 合并**：此前 MiniMax 的 API-key 认证和 OAuth 认证是两个独立的插件配置，现合并为单一插件
- **新增 M2.7**：MiniMax 最新的通用模型
- **新增 M2.7-highspeed**：高速推理变体，牺牲部分能力换取更低延迟

## 双链导航

- [[Provider-Plugin 架构]] — 提供商插件化架构
- [[模型无关架构]] — 多模型支持
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
