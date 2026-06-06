---
tags:
  - OpenClaw
  - 版本更新
  - 2026年4月
  - changelog
  - TaskFlow
  - Memory-Wiki
  - 安全
aliases:
  - v2026.4
  - OpenClaw v2026.4
  - 4月版本更新
  - v2026.4.2
  - v2026.4.7
  - v2026.4.15
  - v2026.4.22
  - v2026.4.25
  - v2026.4.29
---

# OpenClaw v2026.4 版本更新

## 一句话理解

> 2026 年 4 月是 OpenClaw 从"可组装平台"迈向"持久化运行时"的转折月——Durable TaskFlow 让工作流具备状态持久化能力，Memory-Wiki 赋予 Agent 结构化长期记忆，Claw Chain 四漏洞修复暴露了沙箱安全的深层挑战，Google Meet 集成与 DeepSeek V4 默认化则标志着语音场景和模型生态的双重扩张。

## 版本总览

| 版本 | 发布日期 | 性质 | 核心主题 |
|------|----------|------|----------|
| v2026.4.2 | 4月3日 | 正式版 | Durable TaskFlow 编排层 |
| v2026.4.7 | 4月8日 | 正式版 | Memory-Wiki + Session Branching + Webhook TaskFlow |
| v2026.4.15 | 4月17日 | 正式版 | Model Auth Card + 插件安全加固 |
| v2026.4.22 | 4月23日 | **安全补丁** | Claw Chain 四漏洞修复 + /models add |
| v2026.4.24/25 | 4月26日 | 正式版 | Google Meet 集成 + DeepSeek V4 Flash/Pro |
| v2026.4.29 | 4月30日 | 正式版 | People-Aware Memory + Steering 改进 + NVIDIA 提供商 |

---

## v2026.4.2（4月3日）— Durable TaskFlow 编排层

### 核心概念

Durable TaskFlow 是 OpenClaw 引入的持久化多步工作流编排机制。它解决的核心问题是：当一个 Job 需要跨越多个 prompt 甚至多次 Gateway 重启时，如何保持状态一致性和可恢复性。

与传统的"发一条消息触发一次响应"模式不同，TaskFlow 维护独立的 owner session、return context 和 revision tracking，使编排逻辑可以脱离单次对话存活。

### 关键特性

**持久化状态管理**

- 托管 vs 镜像两种同步模式（managed / mirrored）
- 每个 Flow 拥有独立的状态和修订追踪（state/revision tracking）
- `openclaw flows` CLI 命令支持 list、show、cancel 操作

**子任务编排**

- 托管子任务生成（managed child task spawning）
- 粘性取消意图（sticky cancel intent）：外部编排器可立即停止调度，让父 TaskFlow 在活跃子任务完成后优雅终止
- 绑定 `api.runtime.taskFlow` 接口：插件和可信编排层可直接创建和驱动 TaskFlow，无需逐次传递 owner 标识

**安全与隔离**

- 提供商传输和路由安全加固
- 更严格的插件激活边界

### 对架构的影响

TaskFlow 的引入让 OpenClaw 从"对话式 Agent"升级为"工作流运行时"。这意味着：

1. 复杂任务（如 CI/CD 流水线触发、多步数据处理）不再需要外部编排器
2. 模型热切换变得实际可行——Flow 有自己的身份标识，不依赖于底层使用哪个模型
3. 插件开发者可以构建跨会话的长运行 Skill

详见 [[Agent-Flow-Loop 原理]] 和 [[Agent 编排模式]]。

---

## v2026.4.7（4月8日）— Memory-Wiki、Session Branching 与 Webhook TaskFlow

这是 4 月最能力密集的版本，三大特性同时落地。

### Memory-Wiki 结构化记忆系统

Memory-Wiki 是 OpenClaw 在 [[三层记忆系统]] 基础上引入的第四层——持久化结构化知识存储。

**与已有记忆层的区别**

| 记忆层 | 生命周期 | 数据形态 | 典型用途 |
|--------|----------|----------|----------|
| 上下文窗口 | 单次对话 | 原始消息 | 当前任务 |
| Session Memory | 跨轮次 | 键值对 | 会话偏好 |
| Active Memory | 跨重启 | 向量嵌入 | 事实检索 |
| **Memory-Wiki** | **永久** | **声明+证据+元数据** | **知识积累** |

**五个 Wiki 工具**

| 工具 | 功能 |
|------|------|
| `wiki_status` | 查看 Wiki 概览和统计 |
| `wiki_search` | 搜索 Wiki 条目 |
| `wiki_get` | 获取特定条目的完整内容 |
| `wiki_apply` | 创建或更新条目（含声明和证据） |
| `wiki_lint` | 检查条目的一致性和新鲜度 |

**声明-证据-矛盾检测模型**

每条 Wiki 条目不是简单的文本笔记，而是包含：
- **声明（Claims）**：结构化的事实陈述
- **证据（Evidence）**：支持声明的来源引用
- **时间戳和新鲜度追踪**：标记信息的时效性
- **矛盾检测**：当新证据与已有声明冲突时自动标记

这种设计让 Agent 的知识不再是"记住了什么"，而是"以什么置信度相信什么，基于什么证据"。

### Providence-Rich Memory（来源标注）

Memory-Wiki 的一个关键设计决策是记忆来源标注。每条记忆条目追踪四种来源：

| 来源类型 | 含义 | 可信度 |
|----------|------|--------|
| Observed from source | Agent 从文件、消息、日志中直接观察到 | 高 |
| Confirmed by user | 人类明确验证 | 最高 |
| Inferred by model | 模型推断，无人验证 | 中 |
| Imported from transcript | 从对话历史中提取 | 中低 |

来源标注在长期运行场景中至关重要——当你的 Agent 积累了三个月的代码库习惯记忆，你需要知道某条记忆是用户确认的规范还是模型自己推断的猜测。

详见 [[记忆系统]] 和 [[可插拔记忆插件]]。

### Session Branching 会话分支与恢复

Session Branching 允许在对话中途"分叉"，尝试一个风险操作，然后在分支失败时恢复到之前的状态。

**工作流程**

```
主会话线 ──→ 分支点 ──→ 分支 A（尝试重构）
                │               ↓
                │         失败 → 丢弃
                │
                └──→ 恢复到分支点 → 继续主线
```

这个特性对 [[Agentic Coding]] 场景特别有价值：Agent 可以在隔离的分支中尝试激进的代码修改，失败了回退，成功了合并。

### Webhook 触发 TaskFlow

在 v2026.4.2 的 Durable TaskFlow 基础上，v2026.4.7 加入了 Webhook 触发机制：

- HTTP 端点接收外部 payload（CI、数据管道、CRM 事件等）
- 请求经过认证后交给预定义的 TaskFlow 图执行
- 支持端到端自动化场景：媒体本地化、内容审核、多 Agent 检索

这实质上把 OpenClaw 从"需要人类发起的对话系统"变成了"可以被事件驱动的自动化平台"。

详见 [[Webhook 技术]]。

### 新模型支持

- Arcee 模型集成
- Google Gemma 4 支持
- Ollama Vision 多模态推理

---

## v2026.4.15（4月17日）— Model Auth Card 与插件安全

### Model Auth Card

在 Control UI / Overview 中新增模型认证状态卡，一目了然地显示：
- OAuth Token 健康状态
- 提供商速率限制压力
- Token 即将过期或已过期的注意提醒

这解决了一个长期的运维痛点：当 Agent 突然不响应时，运营者需要快速判断是模型问题还是认证问题。

### Manifest 插件安全模型

v2026.4.15 强化了插件运行时隔离：

- 捆绑频道惰性缓存按活跃 bundled root 分区，防止 `OPENCLAW_BUNDLED_PLUGINS_DIR` 切换时复用过期状态
- 从捆绑插件运行时依赖中剔除测试代码，npm 发布验证会在测试代码重新出现时失败
- 默认缩减启动和 Skills 提示词预算，长会话中 `memory_get` 输出默认截断并附带续读元数据

### 飞书安全加固

- Webhook 传输和卡片动作重放守卫强化为 fail-closed 模式
- 缺少 `encryptKey` 时拒绝启动 Webhook 传输
- 无密钥时拒绝未签名请求

### 稳定性修复

- 修复 Linux/systemd 上因插件自动启用导致的 SIGUSR1 重启循环
- 新增配置 hash 守卫防止不必要的重启

---

## v2026.4.22（4月23日）— 安全补丁：Claw Chain 四漏洞修复

这是 4 月最紧急的版本——由 Cyera Research 披露的四个可链式利用的 CVE，被命名为 "Claw Chain"。

### 漏洞概览

| CVE | CVSS | 类型 | 影响 |
|-----|------|------|------|
| CVE-2026-44112 | 9.6 (Critical) | TOCTOU 写入 | 沙箱逃逸，在宿主写入后门和配置篡改 |
| CVE-2026-44113 | 7.7 (High) | TOCTOU 读取 | 沙箱外敏感文件读取 |
| CVE-2026-44115 | 8.8 (High) | Shell 白名单绕过 | 通过 heredoc 内嵌 shell 扩展令牌执行未授权命令 |
| CVE-2026-44118 | 7.8 (High) | MCP Loopback 提权 | 非 owner 客户端冒充 owner 控制 Gateway 配置 |

### 攻击链分析

Claw Chain 的危险在于四个漏洞可以串联：

```
CVE-2026-44113 (读取凭证)
    ↓
CVE-2026-44115 (绕过白名单执行命令)
    ↓
CVE-2026-44118 (提权到 owner 级别)
    ↓
CVE-2026-44112 (在宿主植入后门实现持久化)
```

**CVE-2026-44112 详解**：利用 TOCTOU（time-of-check/time-of-use）竞态条件，在路径验证通过后将文件路径替换为符号链接，将文件系统写入重定向到沙箱 mount root 之外。

**CVE-2026-44118 详解**：MCP Loopback 运行时信任客户端控制的 `senderIsOwner` 标志，任何非 owner 的 Loopback 客户端都可以冒充 owner，获得 Gateway 配置、cron 调度和执行环境的控制权。

### 修复措施

- TOCTOU 漏洞：加固沙箱边界验证，消除路径验证和使用之间的竞态窗口
- Shell 白名单：修复不完整的禁止输入列表
- MCP Loopback：为 owner 和 non-owner 发放不同的 bearer token，`senderIsOwner` 不再信任客户端 header

### /models add 命令

同版本新增 `/models add` 命令，简化自定义模型注册流程。Pi SDK 更新到 0.68.1，模型目录从 Pi 加载而非插件维护的别名。

### 安全启示

Claw Chain 暴露了 AI Agent 框架的独特安全挑战——当你给予 Agent 执行代码的能力时，传统 Web 应用的沙箱模型不够用。TOCTOU 竞态在文件系统操作中是经典问题，但在 AI Agent 上下文中被重新激活，因为 Agent 的文件操作频率和路径复杂度远超传统应用。

详见 [[OpenClaw 官方安全模型]]。

---

## v2026.4.24/25（4月26日）— Google Meet 集成与 DeepSeek V4

### Google Meet 集成

OpenClaw Agent 现在可以作为参与者加入 Google Meet 会议：

**核心能力**

- 通过个人 Google 认证加入会议
- Chrome/Twilio 实时会话支持
- 配对节点 Chrome 支持
- 实时音频转写（基于 Gemini Live）
- 考勤记录导出和 Artifact 导出

**语音架构升级**

Talk、Voice Call 和 Google Meet 三种语音场景统一为实时语音循环（realtime voice loop），在需要更深层工具支持时自动咨询完整的 OpenClaw Agent。

**恢复机制**

- 已打开的 Meet 标签页自动检测和恢复
- 浏览器自动化恢复改进

这标志着 OpenClaw 正式进入"会议 AI 助手"领域，与 [[OpenClaw 语音交互]] 系统深度集成。

### DeepSeek V4 Flash / V4 Pro

| 模型 | 参数量 | 激活参数量 | 定位 |
|------|--------|------------|------|
| DeepSeek V4 Flash | 2840 亿 | 130 亿 | **新默认模型**，极致性价比 |
| DeepSeek V4 Pro | 1.6 万亿 | — | 前沿推理能力 |

V4 Flash 以仅 130 亿激活参数实现了接近 1.6 万亿参数 V4 Pro 的 Max mode 推理性能，成为 OpenClaw 新的默认模型。这是一个大胆的决策——将默认模型从 GPT 系列切换到 DeepSeek，反映了 [[模型无关架构]] 的成熟和中国 AI 模型的竞争力提升。

### Codex OOTH 路由

新增通过 ChatGPT 订阅访问 OpenAI Codex 的路由：

- 如果你已有 ChatGPT Plus/Pro 订阅，可以通过 OAuth 路由使用 GPT-5.5，无需额外 API 账单
- Sam Altman 在 5 月 1 日确认 Codex 对所有付费 ChatGPT 用户开放
- 这使 GPT-5.5 via Codex 成为 OpenClaw 工作流中获取前沿模型性能最具性价比的路径之一

### 运行时 6 种模型提供商热切换

4 月的 Provider Manifest 架构使得以下 6 类提供商可以在运行时无需重建即可切换：

1. GPT-5.5 via Codex（OOTH 路由）
2. Claude API（Anthropic 直连）
3. Gemini（Google AI）
4. DeepSeek（V4 Flash/Pro）
5. OpenRouter（聚合路由）
6. Ollama / LM Studio / Gemma 4（本地模型）

关键洞察：TaskFlow 使热切换真正可行——因为工作流有独立的持久化身份，模型切换不会中断进行中的 Flow。

详见 [[Provider-Plugin 架构]] 和 [[模型无关架构]]。

---

## v2026.4.29（4月30日）— People-Aware Memory 与 Steering 改进

### People-Aware Memory

Memory-Wiki 从"知识存储"进化为"人脉感知"：

- **人物别名（Aliases）**：同一个人的不同称呼自动关联
- **人物卡片（Person Cards）**：为频繁交互的人物建立结构化档案
- **关系图谱（Relationship Graphs）**：追踪人与人之间的关系
- **来源视图（Provenance Views）**：可视化每条人物信息的来源
- **人物搜索**：按"谁是某某"搜索，而不仅仅是匹配原始文本片段

### Active-Run Steering

当 Agent 正在运行时，用户发送的后续消息不再像之前那样"一条一条排队"，而是默认切换为 steering 模式——后续消息作为方向调整注入到活跃运行中，减少消息丢失。

### 安全加固

- 配置了 `tools.exec` 或 `tools.fs` 的限制性工具配置不再意外扩大访问权限
- 更安全的 exec/pairing/owner 控制

### 新增提供商

- **NVIDIA** 提供商和模型目录加入
- 更快的启动速度和插件/频道修复

---

## 4 月跨版本主题总结

### 运行时持久化

从 TaskFlow 的状态追踪到 Memory-Wiki 的知识持久化，再到 Session Branching 的会话状态管理，4 月的主线是让 OpenClaw 的所有层面都具备"跨重启生存"的能力。

### 安全攻防

Claw Chain 是 OpenClaw 历史上最严重的安全事件之一。四个漏洞被命名、被媒体广泛报道（The Hacker News、Dark Reading 等），影响了约 25 万 OpenClaw 部署。但修复速度也很快——4 月 22 日披露，次日发布补丁。

### 模型生态多极化

DeepSeek V4 成为默认模型、Codex OOTH 路由通过 ChatGPT 订阅免费接入、NVIDIA 提供商加入——4 月的模型策略是"不绑定任何一家，但让每一家都尽可能方便"。

### 创始人动向

值得注意的是，OpenClaw 创始人 [[Peter Steinberger]] 已加入 OpenAI，这与 Codex OOTH 路由的深度集成时间线高度吻合。

## 关键洞察

v2026.4 系列完成了 OpenClaw 的"运行时化"转型。如果说 v2026.3 是"让平台可组装"（Provider 插件化、沙箱可插拔），那么 v2026.4 就是"让运行时可持久"（TaskFlow 状态追踪、Memory-Wiki 知识积累、Session Branching 状态管理）。

这两个阶段合在一起，OpenClaw 已经不再是一个"聊天机器人框架"，而是一个"持久化 Agent 运行时"——具备状态管理、知识积累、工作流编排和事件驱动能力的完整平台。

但 Claw Chain 事件也提醒我们，能力越大风险越大。当你的 Agent 可以持久化运行、拥有长期记忆、响应外部事件时，攻击面也相应扩大。沙箱的 TOCTOU 问题、MCP Loopback 的信任模型缺陷，都是"给 Agent 更多能力"的副作用。

## 双链导航

- [[OpenClaw 是什么]] — 框架总览
- [[OpenClaw v2026.3 版本更新]] — 上一个版本系列
- [[OpenClaw v2026.5 版本更新]] — 下一个版本系列
- [[Agent-Flow-Loop 原理]] — TaskFlow 的设计基础
- [[Agent 编排模式]] — 多步工作流编排范式
- [[三层记忆系统]] — Memory-Wiki 之前的记忆架构
- [[记忆系统]] — 记忆系统全貌
- [[可插拔记忆插件]] — 记忆插件扩展机制
- [[Webhook 技术]] — Webhook 触发 TaskFlow 的底层技术
- [[Provider-Plugin 架构]] — 模型提供商热切换的架构基础
- [[模型无关架构]] — 6 种提供商热切换的理论基础
- [[OpenClaw 官方安全模型]] — Claw Chain 修复与安全体系
- [[OpenClaw 语音交互]] — Google Meet 集成的语音架构
- [[Agentic Coding]] — Session Branching 的应用场景
- [[Peter Steinberger]] — 创始人加入 OpenAI
- [[会话状态管理]] — Session Branching 与状态管理
- [[自主执行与人机协作]] — exec approval 与安全执行

## 参考

- [OpenClaw GitHub Releases](https://github.com/openclaw/openclaw/releases)
- [v2026.4.2 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.4.2)
- [v2026.4.7 Release Notes — Blink Blog](https://blink.new/blog/openclaw-2026-4-7-whats-new-update-guide)
- [Claw Chain: Cyera Research](https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw)
- [Claw Chain: The Hacker News](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)
- [DeepSeek V4 Default — TechNode](https://technode.com/2026/04/27/deepseek-v4-becomes-default-model-for-openclaw/)
- [OpenClaw April 2026: 6 Model Providers — MindStudio](https://www.mindstudio.ai/blog/openclaw-april-2026-model-agnostic-provider-manifest)
- [OpenClaw April 2026 Update — MindStudio](https://www.mindstudio.ai/blog/openclaw-april-2026-update-new-features-agentic-runtime)
