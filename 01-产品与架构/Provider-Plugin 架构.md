---
tags:
  - 架构
  - 插件系统
  - 模型提供商
  - provider
  - LLM
aliases:
  - Provider Plugin Architecture
  - 提供商插件架构
  - provider-plugin
  - LLM Provider Plugin
---

# Provider-Plugin 架构

## 一句话理解

> Provider-Plugin 架构是 [[模型无关架构]] 的工程落地——把每个 LLM 提供商（OpenAI、Anthropic、Ollama、vLLM 等）封装为独立的 npm 插件，通过 [[Plugin 扩展系统]] 的自动发现机制加载，让接入新模型从"提 PR 改核心代码"变成"npm install 一个包"。

## 背景与动机

在 v2026.3.12 之前，Ollama、vLLM、SGLang 等本地推理后端的适配代码直接写在 OpenClaw 核心仓库中。这带来三个问题：

1. **核心膨胀**：每新增一个提供商，核心代码库就多一块维护负担
2. **发布耦合**：某个提供商的适配更新必须等待核心版本发布
3. **社区门槛**：第三方开发者想接入新模型，必须 fork 核心代码并提 PR

v2026.3.12 将这些提供商迁移到 provider-plugin 架构，解耦了模型接入与核心框架。

## 架构设计

```
OpenClaw Gateway 启动
  └── Plugin Loader（src/plugins/loader.ts）
        └── 扫描 node_modules 中的 openclaw.extensions.providers
              ├── @openclaw/provider-openai      → GPT-5.4, GPT-5.4 fast mode
              ├── @openclaw/provider-anthropic    → Claude Opus, fast mode
              ├── @openclaw/provider-anthropic-vertex → Vertex AI 上的 Claude
              ├── @openclaw/provider-ollama       → 本地 Ollama 模型
              ├── @openclaw/provider-vllm         → vLLM 推理服务
              ├── @openclaw/provider-sglang       → SGLang 推理服务
              ├── @openclaw/provider-minimax      → MiniMax 模型
              ├── @openclaw/provider-xai          → xAI Grok 模型
              └── 第三方社区 Provider Plugin ...
```

### 统一接口：LLMProvider

每个 Provider Plugin 必须实现 `LLMProvider` 接口：

- `listModels()`：返回可用模型列表
- `chat(messages, options)`：发送对话请求
- `streamChat(messages, options)`：流式对话
- `embeddings(text)`：文本嵌入（可选）

这保证了 [[Agent Execution Loop]] 中的模型调用逻辑完全不感知具体使用哪个提供商。

### 插件声明

Provider Plugin 在 `package.json` 中声明：

```json
{
  "name": "@openclaw/provider-ollama",
  "openclaw": {
    "extensions": {
      "providers": "./dist/index.js"
    }
  }
}
```

Gateway 启动时，`loader.ts` 自动发现并加载所有声明了 `providers` 扩展点的包。

## v2026.3 新增的提供商支持

| 提供商 | 版本 | 说明 |
|--------|------|------|
| OpenAI GPT-5.4 fast mode | v2026.3.12 | 低延迟快速推理模式 |
| Anthropic Claude fast mode | v2026.3.12 | Anthropic 的快速推理模式 |
| [[Anthropic Vertex 提供商]] | v2026.3.22 | 通过 Google Cloud Vertex AI 调用 Claude |
| [[MiniMax M2.7 系列]] | v2026.3.22 | API/OAuth 合并 + M2.7/M2.7-highspeed |
| [[xAI Grok 集成]] | v2026.3.22 | 目录同步 + fast-mode 映射 |
| [[Z.AI GLM 4.5-4.6 系列]] | v2026.3.22 | 目录更新至 4.5/4.6 + 定价同步 |
| [[Xiaomi MiMo 提供商]] | v2026.3.22 | `/v1` 端点 + MiMo V2 Pro/Omni |
| [[Qwen DashScope 提供商]] | v2026.3.23 | DashScope 标准端点重构 |
| [[捆绑提供商插件化迁移\|OpenRouter/Copilot/Codex]] | v2026.3.22 | 从核心迁移为独立插件 |

## 与 Plugin 扩展系统的关系

Provider-Plugin 是 [[Plugin 扩展系统]] 三类扩展（工具、Channel Adapter、LLM Provider）中的第三类。区别在于：

- **工具插件**：扩展 Agent 能做什么（发邮件、查天气）
- **Channel 插件**：扩展 Agent 在哪里交互（飞书、Matrix）
- **Provider 插件**：扩展 Agent 用什么模型思考（GPT、Claude、本地模型）

三者共享同一套声明式发现和动态加载机制，但各自注册到不同的运行时组件。

## Breaking Change：SDK 路径迁移

v2026.3.22-beta.1 中，插件 SDK 从 `openclaw/extension-api` 迁移到 `openclaw/plugin-sdk/*` 子路径。所有现有 Provider Plugin 需要更新 import：

```typescript
// 旧路径（已废弃）
import { LLMProvider } from 'openclaw/extension-api';

// 新路径
import { LLMProvider } from 'openclaw/plugin-sdk/providers';
```

这个 Breaking Change 影响所有第三方 Plugin，包括 Provider、Tool 和 Channel 类型。

## 关键洞察

Provider-Plugin 架构的真正价值不只是"解耦"——它改变了 OpenClaw 生态的**创新速度**。之前，新模型发布后需要等核心团队或社区 PR 合并；现在，任何开发者都可以在新模型发布的当天发布一个 Provider Plugin 到 npm。对于 2026 年这个模型"半年一变"的时代，这种速度差异是决定性的。

同时，Provider-Plugin 架构也是 [[可插拔沙箱后端]] 设计的直接灵感来源——如果模型可以插件化，执行环境为什么不能？

## 相关笔记

- [[OpenClaw v2026.3 版本更新]] — Provider-Plugin 架构在 v2026.3.12 中引入
- [[模型无关架构]] — Provider-Plugin 是模型无关理念的工程实现
- [[Plugin 扩展系统]] — Provider-Plugin 是三类扩展之一
- [[OpenClaw 是什么]] — OpenClaw 的模型无关设计总览
- [[可插拔沙箱后端]] — 与 Provider 插件化并行的架构模块化方向
- [[Dashboard 控制面板]] — Dashboard 的 config 视图管理 Provider 配置
- [[Tool Use 机制]] — Provider 提供的模型能力驱动工具调用

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [npm 官方](https://www.npmjs.com)
