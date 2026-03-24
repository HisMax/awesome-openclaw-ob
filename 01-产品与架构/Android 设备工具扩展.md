---
tags:
  - OpenClaw
  - Android
  - 移动端
  - 2026年3月
aliases:
  - Android Device Tools
  - callLog.search
  - sms.search
  - Android 工具
---

# Android 设备工具扩展

## 一句话理解

> 以前 Agent 在 Android 上像个"只能看屏幕的客人"，v2026.3.22 之后它拿到了"翻通讯录和查短信"的权限——Agent 从被动的对话工具变成了真正能操作手机的数字助手。

## 新增设备工具

v2026.3.22 大幅扩展了 Android 端的 Agent 能力，新增了两个关键的设备级 [[Tool Use 机制|工具]]：

### callLog.search（PR #44073）

由 **@lixuankai** 贡献，允许 Agent 搜索设备通话记录。用户可以用自然语言查询如"上周和张三通了几次电话"、"最近的未接来电是谁"，Agent 通过 `callLog.search` 工具访问系统通话记录并返回结构化结果。

### sms.search（PR #48299）

同样由 **@lixuankai** 贡献，允许 Agent 搜索短信记录。支持按联系人、时间范围、关键词等维度检索。典型场景包括"查找某某发来的验证码"、"上个月和客户的短信往来"。

这两个工具遵循 [[TypeBox Schema 工具定义]] 的规范，参数和返回值都有严格的 Schema 定义，确保 Agent 正确理解工具能力边界。

## 系统感知深色主题（PR #46249）

**@sibbl** 贡献了系统感知的深色主题支持。Android 端的 OpenClaw 现在会跟随系统设置自动切换明暗模式，覆盖入门引导和后续所有界面。这与 [[Control UI 主题系统]] 中 Dashboard 的 Roundness 滑块和 Knot 主题精修形成呼应——桌面端和移动端的视觉体验逐步统一。

## 性能优化

### Camera/Canvas Bitmap 回收

修复了一个原生图像内存泄漏问题——当 Agent 通过相机拍照或 Canvas 截图时，Android 端的 Bitmap 对象在使用后未被正确回收，长时间运行后可能导致内存溢出。新版本在每次图像处理完成后主动调用 `bitmap.recycle()`，防止原生内存泄漏。

### Talk 语音合成迁移

语音合成（Text-to-Speech）从 Android 本地引擎迁移到 Gateway 的 `talk.speak` 接口。Android 端现在播放的是 Gateway 返回的最终响应音频，而不是本地合成。这带来了两个好处：语音质量由 Gateway 端的模型决定（可以使用更高质量的 TTS 模型），同时减轻了移动设备的计算负担。

## 关键洞察

Android 设备工具扩展的方向揭示了 AI Agent 移动端发展的核心趋势：**从"手机上的聊天机器人"到"能操作手机的智能助手"**。通话记录和短信搜索只是起点，位置信息、日历、通知管理等设备能力的逐步开放将让 Agent 越来越深入地融入用户的数字生活。但权限边界同样关键——[[OpenClaw 官方安全模型|安全模型]]中的最小权限原则和用户审批机制在这里尤为重要。

## 双链导航

- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入所有 Android 增强
- [[Tool Use 机制]] — callLog.search 和 sms.search 是 Agent 工具体系的新成员
- [[TypeBox Schema 工具定义]] — 设备工具的参数 Schema 定义规范
- [[Control UI 主题系统]] — 深色主题是整体主题系统的移动端延伸
- [[自主执行与人机协作]] — 设备级工具需要用户授权的审批流程
