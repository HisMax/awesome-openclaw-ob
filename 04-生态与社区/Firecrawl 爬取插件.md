---
tags:
  - OpenClaw
  - 插件
  - 爬取
  - 2026年3月
aliases:
  - Firecrawl Plugin
  - firecrawl_scrape
  - 网页爬取插件
---

# Firecrawl 爬取插件

## 一句话理解

> 如果 [[Exa 网页搜索插件|Exa]] 和 [[Tavily AI 搜索插件|Tavily]] 是 Agent 的"搜索引擎"，Firecrawl 就是它的"爬虫"——不只是找到网页，而是深入网页内部**抓取和结构化**页面内容。

## 功能

- **`firecrawl_search`**：搜索网页并返回结构化结果
- **`firecrawl_scrape`**：对指定 URL 进行深度爬取，提取 Markdown 格式内容

## 使用场景

Firecrawl 在 [[Agent Execution Loop]] 中扮演"数据采集者"角色。典型场景：

1. Agent 需要分析竞品官网的定价页面 → 用 `firecrawl_scrape` 提取结构化数据
2. Agent 需要监控多个新闻源 → 用 `firecrawl_search` 批量获取最新内容
3. Agent 处理 [[案例-华尔街级股票筛选器|金融数据采集]] 类任务 → 深度爬取财报页面

## 安全考量

爬取工具天然具有网络访问能力，这与 [[SSRF 固定与代理安全]] 中的防护策略相关——v2026.3.22 加强了远程 `file://` URL 和 UNC 路径的阻断，确保爬取工具不会被利用为 SSRF 攻击向量。

## 双链导航

- [[Exa 网页搜索插件]] — 同期引入的搜索插件
- [[Tavily AI 搜索插件]] — 同期引入的 AI 搜索插件
- [[SSRF 固定与代理安全]] — 爬取工具的安全约束
- [[Agent Execution Loop]] — 爬取在执行循环中的位置
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
