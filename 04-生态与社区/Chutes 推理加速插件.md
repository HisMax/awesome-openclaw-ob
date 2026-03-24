---
tags:
  - OpenClaw
  - 插件
  - 推理
  - 2026年3月
aliases:
  - Chutes Plugin
  - Chutes Provider
---

# Chutes 推理加速插件

## 一句话理解

> Chutes 是 v2026.3.22 新增的捆绑推理加速插件——相当于给 Agent 的"大脑"装了一台涡轮增压器，通过专用推理基础设施加速模型响应，同时支持 OAuth 和 API-key 两种认证方式。

## 功能

- **模型推理加速**：通过 Chutes 基础设施转发推理请求，降低延迟
- **动态模型发现**：自动获取可用模型列表，无需手动配置
- **双认证模式**：同时支持 OAuth（用户级）和 API-key（服务级）认证

## 技术实现

Chutes 作为捆绑插件通过 [[Plugin 扩展系统]] 的 `openclaw.extensions` 机制注册。与 [[Exa 网页搜索插件]]、[[Tavily AI 搜索插件]]、[[Firecrawl 爬取插件]] 一样，它属于 v2026.3.22 新增的"开箱即用"插件阵列——安装 OpenClaw 即自动可用，无需额外 `npm install`。

贡献者 @Veightor 在 PR #41416 中提交了完整实现。

## 与提供商架构的关系

Chutes 是 [[Provider-Plugin 架构]] 的典型应用案例：它不是一个独立的 LLM，而是一个**推理代理层**，将请求转发到底层模型的同时提供加速和缓存。这种模式类似 [[OpenRouter 插件化|OpenRouter]] 的聚合角色，但专注于性能优化而非模型选择。

## 双链导航

- [[Plugin 扩展系统]] — 插件注册机制
- [[Provider-Plugin 架构]] — 提供商插件化架构
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
- [[OpenRouter 插件化]] — 类似的聚合代理模式
