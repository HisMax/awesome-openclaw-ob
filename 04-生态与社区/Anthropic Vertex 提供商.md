---
tags:
  - OpenClaw
  - 提供商
  - Anthropic
  - Google Cloud
  - 2026年3月
aliases:
  - anthropic-vertex
  - Claude on Vertex AI
  - Vertex AI Claude
---

# Anthropic Vertex 提供商

## 一句话理解

> 以前用 Claude 只能走 Anthropic 官方 API 大门——现在 v2026.3.22 开了一条"Google Cloud 侧门"，企业可以通过已有的 GCP 账户和计费体系直接使用 Claude，无需额外注册 Anthropic 账号。

## 背景

Google Vertex AI 是 Google Cloud 的机器学习平台，Anthropic 将 Claude 模型部署在 Vertex AI 上供企业客户使用。对于已经深度使用 GCP 的企业，通过 Vertex AI 使用 Claude 可以复用现有的身份认证、计费、合规和网络基础设施。

## 技术实现

- 通过 [[Provider-Plugin 架构]] 作为独立插件注册
- 使用 GCP auth discovery 自动检测本地凭证（Application Default Credentials）
- 由 @sallyom 和 @yossiovadia 在 PR #43356 中贡献

## 企业价值

这对 [[OpenClaw 商业模式|企业部署]] 意义重大：

1. **合规优势**：数据不离开企业已有的 GCP 区域，满足数据驻留要求
2. **计费统一**：Claude 使用费用合并到 GCP 账单，简化财务流程
3. **IAM 复用**：GCP 的身份和权限管理直接适用，无需额外安全审计

与 [[Xiaomi MiMo 提供商]]、[[Qwen DashScope 提供商]] 等同期新增的提供商共同构成了 v2026.3.22 的模型生态大扩展。

## 双链导航

- [[Provider-Plugin 架构]] — 提供商插件化架构
- [[模型无关架构]] — OpenClaw 的多模型支持理念
- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入
- [[Xiaomi MiMo 提供商]] — 同期新增的中国模型提供商
- [[Qwen DashScope 提供商]] — 同期新增的阿里云提供商
