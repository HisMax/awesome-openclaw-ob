---
tags:
  - OpenClaw
  - 版本更新
  - 2026年5月
  - changelog
  - 稳定性
  - 语音
  - 安全
aliases:
  - v2026.5
  - OpenClaw v2026.5
  - 5月版本更新
  - v2026.5.3
  - v2026.5.4
  - v2026.5.5
  - v2026.5.6
  - v2026.5.12
  - v2026.5.20
  - v2026.5.22
---

# OpenClaw v2026.5 版本更新


![[assets/v2026-5-update.jpg]]

## 一句话理解

> 2026 年 5 月是 OpenClaw 的"稳定性月"——在 4 月的能力大爆发之后，5 月密集迭代十余个版本，重心转向渠道可靠性、启动性能瘦身、语音管道打磨和策略执行层建设，同时修复了 Codex OAuth 路由回退等高影响 Bug。

## 版本总览

| 版本 | 发布日期 | 性质 | 核心主题 |
|------|----------|------|----------|
| v2026.5.3 | 5月4日 | 正式版 | File Transfer 插件 + 统一流式进度 |
| v2026.5.4 | 5月5日 | 正式版 | Twilio Meet 语音 + 启动懒加载 |
| v2026.5.5 | 5月6日 | 正式版 | 50+ Bug 修复，Grok 推理修复 |
| v2026.5.6 | 5月6日 | 热修复 | Codex OAuth 路由回退 |
| v2026.5.12 | 5月中旬 | 正式版 | 核心安装瘦身 + Telegram 可靠性 |
| v2026.5.20 | 5月21日 | 正式版 | Discord Voice Follow + Policy 插件 + 语音上下文修复 |
| v2026.5.22 | 5月23日 | 正式版 | /models 性能 4100x + Meeting Notes 插件 + Policy Checks |

---

## v2026.5.3（5月4日）— File Transfer 插件与统一流式进度

### File Transfer 插件

新增四个 Agent 工具用于配对节点之间的二进制文件操作：

| 工具 | 功能 |
|------|------|
| `file_fetch` | 从配对节点获取文件 |
| `file_write` | 向配对节点写入文件 |
| `dir_list` | 列出远程目录 |
| `dir_fetch` | 批量获取目录内容 |

**安全限制**：
- 单次往返上限 16 MB
- 运营者可控路径策略（operator-controlled path policies）
- 符号链接遍历默认禁止

### 统一流式进度配置

告别各频道独立的流式配置——单一 `streaming.mode: "progress"` 值现在在 Discord、Telegram、Slack、Matrix 和 Microsoft Teams 上行为完全一致。

这看似是小改动，但对多频道部署的运维负担影响显著。之前每个频道的流式行为需要独立配置和测试，现在一个值搞定全部。

---

## v2026.5.4（5月5日）— Twilio Meet 语音桥与启动性能

### Twilio Dial-in for Google Meet

在 [[OpenClaw v2026.4 版本更新|v2026.4.25]] 的 Google Meet 集成基础上，v2026.5.4 加入了 Twilio 电话拨入能力：

- 通过 Twilio 拨入 Google Meet 会话
- 与 Gemini 实时语音桥集成
- 带节奏的音频流（paced audio streaming）和背压感知缓冲（backpressure-aware buffering）
- 更好地处理多人同时说话的场景

### Gateway 启动性能大幅改善

- 插件和运行时发现改为懒加载
- cron、schema、session、模型元数据按需加载
- 对大型安装（多插件场景）的启动时间和峰值内存显著降低

### OpenRouter 缓存

- OpenRouter 用户可通过 `X-OpenRouter-Cache` 头部选择性启用响应缓存
- 对高频调用的成本优化效果显著

---

## v2026.5.5（5月6日）— 50+ Bug 修复

这是 5 月修复量最大的版本，GitHub Release Notes 列出超过 50 项修复。

### 关键修复

**Grok 推理修复**：OpenClaw 错误地向原生 Grok Responses 模型发送了 OpenAI 风格的 reasoning effort 控制参数，导致 `xai/grok-4.3` 报 "Invalid reasoning effort" 错误。修复后正确适配 xAI 的原生参数格式。

**安全加固**：
- 群组提示文本从系统提示中隔离
- 重复点号主机名规范化处理
- 阻止有副作用的命令包装器

### doctor --fix 引入的问题

v2026.5.5 引入了一个 `doctor --fix` 修复，自动将 `openai-codex/*` 路由重写为 `openai/*`。这对大多数用户是正确的，但破坏了通过 Codex OAuth 插件路径运行 GPT-5.5 的配置。

---

## v2026.5.6（5月6日）— 热修复：Codex OAuth 路由回退

**同日发布**——v2026.5.6 在数小时内回退了 v2026.5.5 中导致 GPT-5.5 Codex OAuth 路径中断的特定路由迁移。

这个"快速发布→发现问题→快速修复"的循环展示了 OpenClaw 的发布节奏：ship fast, detect fast, fix fast。对于依赖 [[OpenClaw v2026.4 版本更新|Codex OOTH 路由]] 的用户来说，v2026.5.5 是一个需要跳过的版本。

### 其他同版本改进

- QQBot 现在会在原生交付前剥离模型推理/思考脚手架，防止原始 `<thinking>` 内容泄露到频道回复中
- MCP 工具结果现在在 materialize 边界强制转换 `resource_link`、`resource`、`audio`、畸形 `image` 和未来的非 text/image 块，防止 Anthropic 返回 400 错误和污染会话历史
- Anthropic extended-thinking 会话在 prompt-cache 过期或 Gateway 重启后可恢复——流启动事件等待 `message_start`，让预生成签名错误触发已有的恢复重试机制

---

## v2026.5.12（5月中旬）— 核心安装瘦身与 Telegram 可靠性

### 依赖瘦身

大量集成从核心安装中移出，改为按需安装：

| 移出的集成 | 说明 |
|-----------|------|
| WhatsApp | 频道插件 |
| Slack | 频道插件 |
| Amazon Bedrock | 模型提供商 |
| Anthropic Vertex | 模型提供商 |
| OpenShell 沙箱 | 沙箱后端 |

**效果**：新安装更小、更新路径更不容易中断。

### Telegram 可靠性全面加固

- 轮询改为独立 worker 运行，配备持久化本地 spool
- 惰性 cron 通知保留渲染格式
- 未提及的群组媒体可在下载前跳过
- 支持的 HTML 标签在可见回复和持久镜像中保留

这些改进针对的是 Telegram 频道在生产环境中的长期运行稳定性——轮询卡住、消息格式丢失、不必要的媒体下载等问题。

---

## v2026.5.20（5月21日）— Voice Follow 与 Policy 插件

### Discord Voice Follow

Agent 可以跟随你加入 Discord 语音通话——当你在语音频道时，Agent 自动加入并提供实时语音交互。

### 捆绑 Policy 插件

首次引入策略插件的捆绑版本，为后续 [[OpenClaw v2026.6 版本更新|v2026.6 的 Auto Mode]] 和 [[Operator Install Policy]] 铺路。

### 语音上下文修复

Agent 处理转写后的语音输入时不再丢失上下文帧，解决了 Agent 误解口语指令的问题。这个修复看似小，但对语音交互的准确性影响重大。

### 其他

- 更安全的 cron 运行
- Codex 更新到 0.132.0
- 十余项关键修复

---

## v2026.5.22（5月23日）— /models 4100x 提速、Meeting Notes 与 Policy Checks

### /models 端点 4100x 性能提升

| 指标 | 改进前 | 改进后 | 提升倍数 |
|------|--------|--------|----------|
| 响应时间 | 20 秒 | 5 毫秒 | **4,100x** |

实现方式：启动时预热提供商认证状态（provider auth-state pre-warming），而不是每次请求时去检查。

这是一个典型的"把一次性成本从热路径移到冷启动"的优化——对 Dashboard 和 CLI 中频繁查看模型列表的用户体验提升极为显著。

### Meeting Notes 插件

新增源码级外部 Meeting Notes 插件：

- 自动启动会议捕获配置
- 手动转录导入
- 只读 `openclaw meeting-notes` CLI 访问
- Discord 语音作为首个实时来源

这与 [[OpenClaw v2026.4 版本更新|v2026.4.25]] 的 Google Meet 集成形成互补——Meet 负责"加入会议"，Meeting Notes 负责"记录会议"。

### Policy Checks 执行层

新增 Agent 工具使用的策略执行层：

- 工具执行前，OpenClaw 评估动作是否符合配置的策略规则
- 有治理需求的团队可以阻止特定工具类别，而无需禁用整个 Agent
- 为 v2026.6 的 [[Operator Install Policy]] 和 Auto Mode 奠定基础

---

## 5 月跨版本主题总结

### 从能力到稳定

4 月引入了 TaskFlow、Memory-Wiki、Session Branching 等重大特性，5 月则专注于让这些特性在生产环境中可靠运行。Telegram 轮询稳定性、Gateway 启动性能、流式进度统一——这些都是"让已有功能更好用"而非"加新功能"。

### 语音管道成熟

从 v2026.4.25 的 Google Meet 集成，到 v2026.5.4 的 Twilio 拨入，到 v2026.5.20 的 Discord Voice Follow 和语音上下文修复，再到 v2026.5.22 的 Meeting Notes 插件——OpenClaw 的语音能力在 5 月从"能用"变成"好用"。

### 安装瘦身

v2026.5.12 将大量集成移出核心安装，这是一个工程成熟度标志：团队意识到"所有功能默认安装"的模式不可持续，开始向"按需安装"转型。

### 策略层建设

从 v2026.5.20 的 Policy 插件到 v2026.5.22 的 Policy Checks，5 月悄悄搭建了 6 月 Auto Mode 和 Operator Install Policy 的基础设施。

### 快速发布节奏

v2026.5.5 引入的 Codex OAuth 路由问题在 v2026.5.6 中数小时内修复，展示了 OpenClaw 社区的快速响应能力。但这也暗示 4 月密集的特性开发留下了稳定性债务。

## 关键洞察

v2026.5 系列是 OpenClaw 项目成熟度的重要标志。一个快速增长的开源项目需要定期的"稳定化窗口"来消化之前积累的技术债务。5 月的密集迭代——十余个版本、50+ 单版本修复、核心安装瘦身、频道可靠性加固——正是这种消化过程。

同时，5 月也展现了 OpenClaw 的两个战略方向：

1. **语音优先**：Google Meet → Twilio 拨入 → Discord Voice Follow → Meeting Notes，语音不再是附加功能，而是核心交互模式
2. **策略执行**：Policy 插件 → Policy Checks → 为 Auto Mode 铺路，从"信任 Agent"向"验证 Agent"转型

## 双链导航

- [[OpenClaw 是什么]] — 框架总览
- [[OpenClaw v2026.4 版本更新]] — 上一个版本系列
- [[OpenClaw v2026.6 版本更新]] — 下一个版本系列
- [[OpenClaw 语音交互]] — 语音管道的演进
- [[Provider-Plugin 架构]] — 依赖瘦身的架构基础
- [[模型无关架构]] — Codex OAuth 路由修复的背景
- [[Operator Install Policy]] — Policy Checks 的后续发展
- [[Plugin 扩展系统]] — File Transfer 插件与 Meeting Notes 插件
- [[Heartbeat 主动监控机制]] — 频道可靠性改进
- [[多频道消息架构]] — 统一流式进度的架构基础
- [[Telegram Bot API 自定义端点]] — Telegram 可靠性改进
- [[Discord Bot 集成]] — Voice Follow 特性

## 参考

- [OpenClaw GitHub Releases](https://github.com/openclaw/openclaw/releases)
- [What's New in OpenClaw May 2026 — Blink Blog](https://blink.new/blog/openclaw-whats-new-may-2026)
- [v2026.5.22 Release Notes — Blink Blog](https://blink.new/blog/openclaw-v2026-5-22-release)
- [v2026.5.22 Release — OpenClaw Hub](https://openclaw-hub.com/blog/release-v2026.5.22)
- [OpenClaw Latest Version May 2026 — Fastio](https://fast.io/resources/openclaw-latest-version/)
