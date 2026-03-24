---
tags:
  - OpenClaw
  - 插件
  - 搜索
  - AI
  - 2026年3月
aliases:
  - Tavily Plugin
  - Tavily Search
  - tavily_search
---

# Tavily AI 搜索插件

## 一句话理解

> Tavily 是专为 AI Agent 设计的搜索引擎——不只是返回网页链接，而是直接返回 Agent 能理解的结构化答案。v2026.3.22 将其作为捆绑插件集成。

## 功能

- **`tavily_search`**：AI 优化搜索，返回结构化摘要而非原始网页
- **`tavily_extract`**：从指定 URL 提取结构化内容

由社区贡献者 @lakshyaag-tavily 在 PR #49200 中提交。

## 与传统搜索的区别

传统搜索引擎返回"链接列表"，Agent 需要二次访问和解析。Tavily 作为"AI 原生搜索"直接返回 Agent 可消费的内容，减少了 [[Agent Execution Loop]] 中的中间步骤，让搜索从"两步操作"变成"一步到位"。

这种 AI-first 的搜索理念与 [[2026 Agent 元年]] 中描述的"工具为 Agent 而非人类设计"趋势一致。

## 双链导航

- [[Exa 网页搜索插件]] — 同期引入的精确搜索插件
- [[Firecrawl 爬取插件]] — 同期引入的爬取插件
- [[Agent Execution Loop]] — 搜索工具在执行循环中的角色
- [[2026 Agent 元年]] — AI 原生工具的趋势
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
