---
tags:
  - OpenClaw
  - 插件
  - 搜索
  - 2026年3月
aliases:
  - Exa Plugin
  - Exa Web Search
---

# Exa 网页搜索插件

## 一句话理解

> Exa 让 Agent 长了"眼睛"——能实时搜索互联网获取最新信息，而不是只依赖训练数据中的"旧记忆"。它是 v2026.3.22 新增的三个搜索类捆绑插件之一。

## 功能

- **网页搜索**：Agent 可通过 `exa_search` 工具搜索互联网
- **日期过滤**：支持按时间范围筛选搜索结果
- **搜索模式选择**：支持不同的搜索策略（关键词、语义等）

## 与其他搜索插件的对比

v2026.3.22 同时引入了三个搜索类插件，各有侧重：

| 插件 | 定位 | 核心工具 |
|------|------|----------|
| **Exa** | 网页搜索，侧重精确性 | `exa_search` |
| [[Tavily AI 搜索插件\|Tavily]] | AI 原生搜索 + 内容提取 | `tavily_search` + `tavily_extract` |
| [[Firecrawl 爬取插件\|Firecrawl]] | 网页爬取与结构化提取 | `firecrawl_search` + `firecrawl_scrape` |

三者作为 [[Plugin 扩展系统]] 的捆绑插件开箱即用，Agent 根据任务特性自动选择合适的搜索工具——这依赖于 [[Tool Use 机制]] 中的工具选择逻辑。

## 双链导航

- [[Tavily AI 搜索插件]] — 同期引入的 AI 搜索插件
- [[Firecrawl 爬取插件]] — 同期引入的爬取插件
- [[Plugin 扩展系统]] — 插件注册机制
- [[Tool Use 机制]] — Agent 如何选择使用哪个搜索工具
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
