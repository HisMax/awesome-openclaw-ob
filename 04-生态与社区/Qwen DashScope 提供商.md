---
tags:
  - OpenClaw
  - 提供商
  - 阿里巴巴
  - 中国
  - 2026年3月
aliases:
  - Qwen Provider
  - DashScope
  - Alibaba Cloud Model Studio
  - 通义千问
---

# Qwen DashScope 提供商

## 一句话理解

> v2026.3.23 将阿里的 Qwen 提供商重构为"Qwen (Alibaba Cloud Model Studio)"，切换到标准的 DashScope 端点——这不是简单的重命名，而是从"社区适配"升级为"官方对接"。

## 核心变更

这是 v2026.3.23 的 **Breaking Change**：

| 属性 | 旧 | 新 |
|------|---|---|
| 名称 | Qwen | Qwen (Alibaba Cloud Model Studio) |
| 端点 | 自定义 | DashScope 标准端点（中国+全球） |
| 计费 | 自管理 | 按量付费（DashScope 计费体系） |

新端点同时支持中国区域和全球区域，解决了此前国际用户访问不稳定的问题。

## 阿里云模型工作台

阿里云模型工作台（Alibaba Cloud Model Studio）是阿里巴巴的 AI 模型服务平台，提供 Qwen 系列模型的 API 访问。与 Anthropic 的 API 直接服务模式类似，但包含阿里云的企业级功能（身份管理、计费、合规）。

通过 [[Provider-Plugin 架构]] 注册后，用户只需在 OpenClaw 配置中填入 DashScope API Key 即可使用全系列 Qwen 模型。

## 中国模型生态位置

Qwen 与 [[Xiaomi MiMo 提供商|MiMo]]、[[Z.AI GLM 4.5-4.6 系列|GLM]] 共同构成 OpenClaw 的中国模型层。结合 [[中国用户与 OpenClaw]] 的市场数据，中国模型在 OpenClaw 生态中的分量正在快速上升。

## 双链导航

- [[Provider-Plugin 架构]] — 提供商插件化架构
- [[Xiaomi MiMo 提供商]] — 同期新增的小米提供商
- [[Z.AI GLM 4.5-4.6 系列]] — 同期新增的智谱提供商
- [[中国用户与 OpenClaw]] — 中国市场热潮
- [[OpenClaw v2026.3 版本更新]] — v2026.3.23 重构
