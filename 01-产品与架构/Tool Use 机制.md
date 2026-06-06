---
tags:
  - 架构
  - 工具调用
  - Agent
aliases:
  - Tool Use
  - 工具调用
  - Function Calling
---

# Tool Use 机制


![[assets/tool-use.jpg]]

Tool Use（工具调用）是 AI Agent 与外部世界交互的核心机制。Agent 在[[自主决策循环]]中通过调用工具来执行实际操作，而非仅仅生成文本。

## 在 Agent Execution Loop 中的位置

Tool Use 发生在 [[Agent Execution Loop]] 的 **Phase 5: Tool Execution Loop**：

1. 模型输出包含工具调用请求
2. 系统拦截并执行工具（可能在 Docker 沙箱中）
3. 执行结果回传给模型
4. **循环重复，直到模型产出纯文本响应**

这个循环是 Agent 实现自主决策循环的关键——模型可以连续调用多个工具来完成复杂任务。

## LLM Provider 的工具格式

[[OpenClaw 是什么|OpenClaw]] 通过统一的 Provider 插件系统支持不同格式：

- **Anthropic**：Tool Use 格式（原生流式，200K 上下文）
- **OpenAI**：Function Calling 格式（delta 流式）
- **Ollama**：本地模型适配，支持 DeepSeek 等开源模型

## TypeBox Schema 工具定义

工具参数通过 TypeBox 定义 JSON Schema 并进行运行时验证：

```typescript
const params = Type.Object({
  query: Type.String({ description: "搜索查询" }),
  limit: Type.Optional(Type.Number({ default: 10 }))
});
```

TypeBox 同时提供 TypeScript 类型推导和 JSON Schema 验证，确保工具调用的类型安全。

## 工具沙箱

- **OpenClaw**：Docker 容器隔离（可选），通过配置 `"sandbox": { "mode": "always" }` 启用
- **Claude Code**：内置沙箱

沙箱机制是安全边界与风险的重要组成部分。

## "自我修改软件"机制

OpenClaw 最具争议的设计之一——Agent 可以修改自己的源代码。这种自主性既强大又危险：

> "I made the agent very aware — it knows what its source code is." —— Steinberger

- Agent 可直接修改工作空间中的 `.ts` / `.js` 源文件
- 修改 Skill 定义以改变自身行为
- 调整[[System Prompt 设计|系统提示]]模板
- 添加新的工具实现

### Skills 热重载

文件变更后 **250ms debounce** 自动触发热重载——Agent 修改完 Skill 文件后无需重启。

### Plugin 扩展系统

`loader.ts` 启动时扫描 `package.json` 中的 `openclaw.extensions` 字段，自动发现并加载第三方插件。插件可以注册新的工具、Channel Adapter 或 LLM Provider。

## 策略执行层（v2026.5-6）

v2026.5.22 引入 **Policy Checks** 执行层——工具执行前，OpenClaw 评估动作是否符合配置的策略规则。v2026.6 的 **Auto Mode** 进一步构建了三层审批架构（策略匹配→模型审核→人工兜底），让工具调用在安全和效率之间取得平衡。详见 [[OpenClaw v2026.6 版本更新]]。

## 相关笔记

- [[Agent Execution Loop]]
- [[System Prompt 设计]]
- [[安全边界与风险（总览）]]
- [[Composio OAuth 中间件]] — 外部服务 OAuth 授权的工具集成中间件
- [[JSON Schema]] — 工具参数定义的标准格式
- [[Zapier 与 Make 自动化平台]] — 通过自动化平台扩展 Agent 的工具调用能力
- [[OpenClaw v2026.6 版本更新]] — Policy Checks 与 Auto Mode

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [MCP 规范](https://modelcontextprotocol.io)
