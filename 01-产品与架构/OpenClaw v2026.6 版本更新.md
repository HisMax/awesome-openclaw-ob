---
tags:
  - OpenClaw
  - 版本更新
  - 2026年6月
  - changelog
  - Auto Mode
  - 安全
  - 策略执行
aliases:
  - v2026.6
  - OpenClaw v2026.6
  - 6月版本更新
  - v2026.6.1
  - v2026.6.2
---

# OpenClaw v2026.6 版本更新

## 一句话理解

> 2026 年 6 月是 OpenClaw 的"治理月"——Auto Mode 用"策略优先→模型审核→人工兜底"的三层架构替代了粗暴的 YOLO 模式，Operator Install Policy 让运营者可以用自定义策略命令控制插件安装，v2026.6.2 则在频道可靠性、运行时恢复和发布验证上全面收紧。

## 版本总览

| 版本 | 发布日期 | 性质 | 核心主题 |
|------|----------|------|----------|
| v2026.6.1 | 6月初 | 正式版 | Skill Workshop + Workboard 编排 + Code Mode 命名空间 |
| v2026.6.2-beta.1 | 6月初 | Beta | Auto Mode + Operator Install Policy + 安全配置检查 |
| v2026.6.2 | 6月上旬 | 正式版 | 更安全的插件安装 + Gateway/Agent/Provider 恢复 + 频道可靠性 |

---

## v2026.6.1 — Skill Workshop 与 Workboard 编排

### Skill Workshop

新增 review-first 的方式将 Agent 工作成果转化为可复用 Skill：

- Agent 在执行任务过程中总结的操作步骤可以直接封装为 Skill
- 需要人工审核确认后才能注册到 Skill 库
- 降低了 Skill 创建的门槛——从"手写 YAML 定义"变为"让 Agent 帮你写，你审一遍"

### Workboard 编排原语

Workboard 新增多 Agent 编排工具：

- 多 Agent 计划和运行追踪
- 任务支持的 Board Run 与任务评论集成
- 编辑模态中的任务评论面板

这是 [[Agent 编排模式]] 在 UI 层的落地——让非开发者也能可视化地编排多 Agent 工作流。

### Code Mode 改进

- 内部命名空间支持作用域 Agent/全局会话
- 精确命名空间工具分发
- MCP API 文件和文档支持 Code Mode 集成

### iOS 改进

- 托管推送中继默认值
- 实时 Talk 播放
- 受保护的 WebSocket ping 路径，提升移动端会话可靠性

---

## Auto Mode：企业级 Exec 审批模式

### 为什么需要 Auto Mode

OpenClaw 之前的 exec 审批有两个极端：

| 模式 | 行为 | 问题 |
|------|------|------|
| **Ask（严格模式）** | 每条命令都需要人工审批 | 对话流不断被打断，效率低 |
| **YOLO 模式** | 跳过所有审批，直接执行 | 对企业环境太危险，无法审计 |

Auto Mode 是第三条路——"比 YOLO 安全，比 Ask 高效"。

### 三层审批架构

```
命令提交
    │
    ▼
┌─────────────────┐
│ 第一层：策略匹配   │ ← 白名单 / safe-bin 规则
│ 匹配 → 直接执行    │
└────────┬────────┘
         │ 未匹配
         ▼
┌─────────────────┐
│ 第二层：模型审核   │ ← 独立审核模型（非 Agent 模型）
│ 低风险 → 允许执行   │
└────────┬────────┘
         │ 不确定
         ▼
┌─────────────────┐
│ 第三层：人工兜底   │ ← 人类审批
│ 最终决策          │
└────────┴────────┘
```

### 模型审核器设计

**关键设计决策**：审核模型与 Agent 模型分离。

- Agent 可以使用本地模型执行日常工作
- exec 审核指向前沿模型（如 `openai/gpt-5.5`）以获得更强的安全判断力
- 审核模型被提示将所有输入数据（命令文本、argv、cwd、env 键名、heredoc、字符串、文件名）视为不可信数据
- 如果不可信数据试图指示审核器或请求决策，自动降级到人工审批

**审核包（Review Packet）**

当命令未命中策略时，OpenClaw 构建一个有限范围的审核包：

```json
{
  "command": "rm -rf ./build",
  "argv": ["rm", "-rf", "./build"],
  "cwd": "/home/user/project",
  "env_keys": ["PATH", "HOME", "NODE_ENV"],
  "host": "prod-server-01",
  "parser_analysis": {
    "destructive": true,
    "recursive": true,
    "target": "relative_path"
  }
}
```

审核模型只能允许单次低风险执行——不能给出"以后这种命令都允许"的永久授权。

### 配置示例

Auto Mode 是 opt-in 的企业级功能：

```yaml
tools:
  exec:
    approval: auto
    autoReviewer:
      model: openai/gpt-5.5
      maxRiskLevel: low
    policy:
      allowlist:
        - "git *"
        - "npm test"
        - "ls *"
      safeBins:
        - cat
        - echo
        - pwd
```

### 与 YOLO 模式的对比

| 维度 | YOLO | Auto Mode |
|------|------|-----------|
| 审批提示 | 无 | 仅不确定项 |
| 安全性 | 最低 | 高 |
| 适用场景 | 受信任的本地自动化 | 企业生产环境 |
| 审计能力 | 无 | 完整审批记录 |
| 模型审核 | 无 | 独立审核模型 |
| 人工兜底 | 无 | 有 |

Auto Mode 实质上是 [[自主执行与人机协作]] 理念的工程落地——Agent 拥有高度自主权，但关键决策仍有人类把关。

---

## Operator Install Policy：运营者可配置安装策略

### 背景

之前 OpenClaw 使用一个"危险代码扫描器"（dangerous-code scanner）来检查插件安装的安全性。这个方案存在两个根本问题：

1. **误报率高**：合法插件可能触发扫描器的规则
2. **不可定制**：运营者无法根据自己的安全策略调整行为

### 新模型

Operator Install Policy 用运营者可配置的本地策略命令替代了旧的代码扫描器：

```yaml
security:
  installPolicy:
    command: "/usr/local/bin/openclaw-install-policy"
    args: ["--json"]
    timeoutMs: 10000
    env:
      POLICY_MODE: "strict"
    target: null  # null = 所有目标（skill + plugin）
```

### 工作流程

```
用户执行 openclaw plugins install <package>
    │
    ▼
OpenClaw 暂存源材料（staged source material）
    │
    ▼
调用配置的策略命令
    │
    ├── 返回 allow → 继续安装
    ├── 返回 block → 安装中止，显示原因
    └── 超时/不可用 → 安装中止（fail-closed）
```

### 适用范围

策略命令对以下所有安装来源生效：

- ClawHub Skills
- 上传的 Skills
- Git / 本地 Skills
- Skill 依赖安装器
- Plugin install/update 来源
- Marketplace 安装

### Fail-Closed 设计

**关键行为**：当策略命令配置了但不可用时，安装会失败（fail-closed），而不是跳过检查（fail-open）。正常 Gateway 启动不触发安装策略——只在实际安装/更新时运行。

### 可选 target 过滤

`target` 字段可设为 `"skill"` 或 `"plugin"`——省略时策略对所有受支持目标生效，避免新增安装类型意外绕过策略。

详见 [[Operator Install Policy]]。

---

## v2026.6.2 — 更安全的插件安装、运行时恢复与频道可靠性

### 插件安装安全

- Operator Install Policy 正式替代旧的 dangerous-code scanner 路径
- 覆盖 doctor 检查、CLI 流程、ClawHub 元数据、问题排查界面
- 适用于 package、archive、source、upload 和 marketplace 安装路径

### 频道与消息可靠性

v2026.6.2 对主要频道进行了广泛的可靠性修复：

| 频道 | 修复内容 |
|------|----------|
| Telegram | 重复转录镜像、管理员回写、流式预览 |
| 飞书 | 审批白名单、设置运行时状态 |
| Discord | 语音错误处理、内部进度追踪 |
| WhatsApp | 出站交付路径安全 |
| 通用 | 投票修饰符、streamed-final 预览 |

### Gateway / Agent / Provider 恢复改进

- Agent 和 CLI 运行时从中断的工具调用中更干净地恢复
- 过期会话绑定的处理改进
- 压缩交接（compaction handoff）的恢复
- 媒体交付重试机制改善

### Anthropic Extended-Thinking 恢复

Anthropic extended-thinking 会话在 prompt-cache 过期或 Gateway 重启后可恢复——流启动事件等待 `message_start`，让预生成签名错误触发已有的恢复重试机制。

这解决了一个生产环境中的痛点：使用 Anthropic 模型的 extended-thinking 功能时，如果 prompt cache 过期或 Gateway 意外重启，整个会话不再崩溃。

### QQBot Thinking 标签过滤

QQBot 在原生交付前剥离模型推理/思考脚手架，防止原始 `<thinking>` 内容泄露到频道回复中。

这是一个容易被忽略但用户体验影响大的修复——用户在 QQ 中看到的应该是最终回答，而不是模型的内部推理过程。

### MCP 工具结果类型强制转换

MCP 工具结果在 materialize 边界强制转换以下类型：

- `resource_link`
- `resource`
- `audio`
- 畸形 `image`
- 未来的非 text/image 块

**修复目的**：防止当 MCP 工具返回更丰富的内容类型时，Anthropic API 返回 400 错误和会话历史被污染。

### CI 与发布验证

- 更严格的 CI 流水线
- 包装和发布验证加固
- 确保发布的稳定性

---

## 安全配置检查

v2026.6.2 新增安全配置检查功能，帮助运营者发现不安全的配置：

- 检查 exec 审批模式是否过于宽松
- 验证 Webhook 端点的签名配置
- 检查插件安装策略是否启用
- 提示敏感环境变量的暴露风险

这与 Auto Mode 和 Operator Install Policy 形成安全三角——从执行审批、安装控制到配置检查，覆盖了 OpenClaw 安全面的三个关键维度。

---

## 6 月跨版本主题总结

### 从"信任"到"验证"

4 月的主题是"给 Agent 更多能力"（TaskFlow、Memory-Wiki），5 月是"让这些能力更可靠"（稳定性修复），6 月则是"确保这些能力被安全地使用"（Auto Mode、Install Policy、配置检查）。

这是一个自然的成熟路径：
1. **先能做** → v2026.4 能力建设
2. **再做好** → v2026.5 稳定化
3. **最后做安全** → v2026.6 治理与策略

### 企业级定位

Auto Mode 和 Operator Install Policy 都明确标记为"企业特性"。OpenClaw 正在从开发者工具向企业平台转型——个人开发者可以继续用 YOLO 模式，但企业部署需要审批记录、策略控制和配置审计。

### Claw Chain 的余波

v2026.6 的安全加固可以看作是 [[OpenClaw v2026.4 版本更新|Claw Chain 事件]] 的长期响应。v2026.4.22 修复了具体漏洞，而 v2026.6 则在系统层面引入了防御机制——安装策略、执行审批、配置检查——减少未来类似漏洞造成的影响。

## 关键洞察

v2026.6 系列回答了一个关键问题：**当你的 AI Agent 能做越来越多的事情时，谁来决定它应该做什么？**

答案是三层治理架构：

1. **执行层**：Auto Mode 的"策略→模型→人工"三级审批
2. **安装层**：Operator Install Policy 的 fail-closed 策略命令
3. **配置层**：安全配置检查的预防性验证

这不是在限制 Agent 的能力，而是在建设使用这些能力的信任基础设施。一个企业 CISO 需要的不是"Agent 不能执行命令"，而是"Agent 执行的每条命令都有审批记录、策略依据和人工兜底"。

从这个角度看，v2026.6 可能是 OpenClaw 历史上对企业采用影响最大的版本——不是因为它加了什么新功能，而是因为它让已有功能变得可治理。

## 双链导航

- [[OpenClaw 是什么]] — 框架总览
- [[OpenClaw v2026.5 版本更新]] — 上一个版本系列
- [[OpenClaw v2026.4 版本更新]] — Claw Chain 事件背景
- [[自主执行与人机协作]] — Auto Mode 的理论基础
- [[Operator Install Policy]] — 安装策略的完整概念
- [[OpenClaw 官方安全模型]] — 安全体系总览
- [[Plugin 扩展系统]] — 插件安装流程
- [[Agent 编排模式]] — Workboard 编排的基础
- [[多频道消息架构]] — 频道可靠性改进
- [[Tool Use 机制]] — Policy Checks 的作用点
- [[自主决策循环]] — Auto Mode 中的 Agent 自主性边界

## 参考

- [OpenClaw GitHub Releases](https://github.com/openclaw/openclaw/releases)
- [Safer Than YOLO: Auto Mode for Exec Approvals — OpenClaw Blog](https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals)
- [Exec Approvals — OpenClaw Docs](https://docs.openclaw.ai/tools/exec-approvals)
- [v2026.6.1 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.6.1)
- [v2026.6.2-beta.1 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.6.2-beta.1)
- [Security — OpenClaw Docs](https://docs.openclaw.ai/gateway/security)
