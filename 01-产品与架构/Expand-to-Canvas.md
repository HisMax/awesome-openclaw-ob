---
tags:
  - OpenClaw
  - UI
  - Canvas
  - A2UI
  - 2026年3月
aliases:
  - Expand to Canvas
  - 展开到画布
  - Canvas Button
---

# Expand-to-Canvas

## 一句话理解

> 如果聊天气泡是一张便签纸，那么 Expand-to-Canvas 就是把便签纸贴到白板上——内容没变，但工作空间从一维文本流变成了二维自由画布，交互可能性瞬间打开。

## 功能描述

v2026.3.22 在 [[Dashboard 控制面板]] 的助手聊天气泡上新增了 **"展开到画布"（Expand-to-Canvas）按钮**。用户点击后，当前消息内容会被投射到 Canvas 工作区中，从线性对话流中"跳出来"，进入一个可自由编辑、可富交互的空间。

这个看似简单的按钮背后是 [[A2UI 与 Live Canvas|A2UI（Agent-to-UI）]] 协议的实际应用。A2UI 定义了 Agent 如何向用户呈现声明式 UI，Canvas 是这些声明式 UI 的渲染目标。Expand-to-Canvas 把触发权交给了用户——不是 Agent 主动推送 Canvas，而是用户选择哪条消息值得"升级"到 Canvas 视图。

## 交互流程

```
用户在聊天中收到 Agent 回复
  → 点击气泡上的 "展开到画布" 按钮
    → 消息内容传递到 Canvas 服务（端口 18793）
      → Canvas 渲染富交互视图（表格、图表、表单等）
        → 用户在 Canvas 中编辑/交互，结果可回传给 Agent
```

Canvas 运行在独立端口 18793，与 Gateway（18789）分离，这意味着 Canvas 渲染即使出错也不会影响核心对话服务。这种故障隔离设计在 [[A2UI 与 Live Canvas]] 中有详细说明。

## 设计意义

传统聊天界面的局限在于一维线性——所有内容按时间排列，无法并排比较或空间组织。Canvas 打破了这个限制。但如果所有消息都自动展开到 Canvas，信息过载会更严重。Expand-to-Canvas 的按钮设计是一个精妙的中间方案：**默认保持聊天的简洁性，按需获得 Canvas 的丰富性**。

这对非技术用户尤其友好——他们不需要理解 A2UI 协议，只需要知道"点这个按钮可以看到更丰富的视图"。

## 贡献者

**@BunsDev** 贡献了此功能的实现，这是他在 v2026.3.22 周期中对 UI 层面的多项改进之一（另见 [[Control UI 主题系统]]）。

## 双链导航

- [[A2UI 与 Live Canvas]] — Canvas 的技术架构和 A2UI 协议，Expand-to-Canvas 是其用户触发入口
- [[Dashboard 控制面板]] — 按钮所在的聊天模块界面
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入此功能
- [[Tool Use 机制]] — Agent 生成的工具调用结果是 Canvas 展示的典型内容
