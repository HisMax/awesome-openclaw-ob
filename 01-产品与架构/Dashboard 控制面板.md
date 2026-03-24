---
tags:
  - 产品
  - UI
  - Dashboard
  - 控制面板
  - 前端
aliases:
  - Dashboard
  - 控制面板
  - OpenClaw Dashboard
  - Web UI
  - Command Palette
  - 命令面板
---

# Dashboard 控制面板

## 一句话理解

> Dashboard 是 OpenClaw 的 Web 管理界面——v2026.3.12 全面刷新为模块化视图架构，将原来的整块页面拆分为 overview、chat、config、agent、session 五大独立模块，并新增命令面板（Command Palette）实现键盘驱动操作。

## 背景

OpenClaw 的主要交互方式是通过 WhatsApp、Telegram、Discord 等 [[多频道消息架构|即时通讯平台]]。Dashboard 则是面向管理员和高级用户的 Web 控制台，用于监控 Agent 状态、管理配置、查看会话历史和调试。

v2026.3.12 之前，Dashboard 是一个功能逐步堆叠的单页面应用。随着功能增长，页面变得臃肿且难以维护。3 月的重构将其拆分为模块化视图。

## 五大模块视图

| 模块 | 职责 | 关键功能 |
|------|------|----------|
| **Overview** | 系统总览 | Agent 运行状态、资源使用、告警摘要 |
| **Chat** | 对话管理 | 实时对话查看、聊天历史浏览、消息搜索 |
| **Config** | 配置管理 | Provider 配置、模型选择、环境变量、[[Provider-Plugin 架构\|Provider Plugin]] 管理 |
| **Agent** | Agent 管理 | Agent 实例列表、Skill 配置、权限设置、[[自主执行与人机协作\|执行模式]] 切换 |
| **Session** | 会话调试 | [[会话状态管理\|会话状态]]查看、上下文窗口可视化、Token 消耗统计 |

### 命令面板（Command Palette）

灵感来自 VS Code 的 Cmd+P，提供键盘快捷搜索与导航：

- 快速切换视图模块
- 搜索 Agent、会话、配置项
- 执行常用操作（重启 Agent、清除缓存、切换模型等）

## 移动端适配

v2026.3.12 同时优化了移动端体验：

- **底部标签栏**：五大模块视图通过底部 Tab 切换，符合移动端操作习惯
- **Android 聊天设置重新设计**（v2026.3.13-1）：聊天配置界面针对 Android 重新布局
- 响应式布局确保 Dashboard 在手机、平板、桌面三种尺寸下均可用

## 性能优化

v2026.3.13-1 修复了 Dashboard 聊天历史重加载的性能问题：

- 大量历史会话场景下，避免一次性加载全部聊天记录
- 采用分页加载 + 虚拟滚动，只渲染可视区域内的消息
- 会话状态跨重置保持——重启 Gateway 后 Dashboard 不丢失当前浏览状态

## 与 Ollama 推理可见性

v2026.3.13-1 修复了 Ollama 推理可见性问题——使用本地 Ollama 模型时，推理过程（token 生成、耗时等）现在可以在 Dashboard 的 Chat 和 Session 模块中实时查看。这对调试本地模型的性能和质量至关重要。

## 关键洞察

Dashboard 模块化的意义不仅是"好看了"——它为 OpenClaw 的可观测性（Observability）奠定了基础。当 Agent 从个人玩具变成团队工具时，管理员需要的不是"一个聊天窗口"，而是"一套监控仪表盘"。五大模块分别对应了 Agent 系统的五个核心关注点：全局状态、对话内容、系统配置、Agent 行为、会话调试。这种拆分让未来每个模块都可以独立进化，也为第三方 Dashboard 插件留下了扩展空间。

## 相关笔记

- [[OpenClaw v2026.3 版本更新]] — Dashboard 刷新在 v2026.3.12 中引入，v2026.3.22/3.23 持续迭代
- [[OpenClaw 是什么]] — Dashboard 是 OpenClaw 的管理界面
- [[会话状态管理]] — Session 模块展示会话状态详情
- [[Provider-Plugin 架构]] — Config 模块管理 Provider 配置
- [[多频道消息架构]] — Chat 模块展示来自各平台的对话
- [[A2UI 与 Live Canvas]] — Dashboard 与 Live Canvas 是 OpenClaw 的两个可视化界面
- [[Heartbeat 主动监控机制]] — Overview 模块展示 Heartbeat 监控状态
- [[Expand-to-Canvas]] — v2026.3.22 新增的聊天气泡展开到画布按钮
- [[Control UI 主题系统]] — v2026.3.22 的 Roundness 滑块和 Knot 主题
- [[WCAG 无障碍标准]] — v2026.3.23 的 WCAG 2.1 AA 合规
- [[Content Security Policy]] — v2026.3.23 的 CSP SHA-256 增强
- [[每网关会话隔离]] — v2026.3.22 的多网关会话隔离
- [[Plugin 扩展系统]] — Dashboard 模块化为未来 UI 插件化做准备

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
