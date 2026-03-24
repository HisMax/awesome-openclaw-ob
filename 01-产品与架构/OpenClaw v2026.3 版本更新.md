---
tags:
  - OpenClaw
  - 版本更新
  - 2026年3月
  - changelog
aliases:
  - v2026.3
  - OpenClaw v2026.3
  - 3月版本更新
  - v2026.3.12
  - v2026.3.13
  - v2026.3.22
  - v2026.3.23
---

# OpenClaw v2026.3 版本更新

## 一句话理解

> 2026 年 3 月是 OpenClaw 架构大变革月——Dashboard 全面模块化、模型提供商迁移到 [[Provider-Plugin 架构]]、[[可插拔沙箱后端]] 引入 OpenShell、插件 SDK 路径 Breaking Change，标志着框架从"功能堆叠"进入"系统级模块化"阶段。

## 版本总览

| 版本 | 发布日期 | 性质 | 核心主题 |
|------|----------|------|----------|
| v2026.3.12 | 3月13日 | 正式版 | Dashboard 刷新 + Provider-Plugin 架构 |
| v2026.3.13-1 | 3月14日 | 热修复 | 性能优化 + 平台适配修复 |
| v2026.3.22-beta.1 | 3月23日 | Beta | ClawHub 原生安装 + 可插拔沙箱 + Breaking Changes |
| v2026.3.22 | 3月23日 | **正式版** | 架构级重构正式发布 + 100+ 贡献者 + 安全大幅加固 |
| v2026.3.23 | 3月23日 | 热修复 | 插件运行时修复 + 认证加固 + Qwen 重构 |

---

## v2026.3.12（3月13日）— Dashboard 刷新与插件化架构

### Dashboard UI 全面刷新

- 模块化视图拆分为五大独立模块：overview、chat、config、agent、session
- 新增**命令面板（Command Palette）**，支持键盘快捷搜索与导航
- 移动端优化底部标签栏，改善小屏体验

详见 [[Dashboard 控制面板]]。

### 模型提供商插件化

- **OpenAI GPT-5.4 fast mode** 支持
- **Anthropic Claude fast mode** 集成
- Ollama、vLLM、SGLang 迁移到 [[Provider-Plugin 架构]]（模块化提供商插件）
- MiniMax 和 xAI 模型目录对齐

这是 [[模型无关架构]] 的重大工程落地——从"配置驱动切换"升级为"插件驱动扩展"。

### 部署

- 新增 **Kubernetes 部署文档**，覆盖 Helm Chart 和高可用配置

---

## v2026.3.13-1（3月14日）— 热修复与性能优化

此版本修复损坏的 v2026.3.13 标签，并带来多项稳定性改进：

### 性能

- **Dashboard 聊天历史重加载性能优化**：大量历史会话场景下加载速度显著提升
- **会话状态跨重置保持**：重启 Gateway 后会话状态不再丢失，与 [[会话状态管理]] 的 JSONL 持久化机制配合

### 平台修复

- **Discord 网关元数据处理改进**：修复特定消息类型的元数据解析问题
- **Ollama 推理可见性修复**：本地模型推理过程现在可在 Dashboard 实时查看
- **Android 聊天设置重新设计**：移动端配置界面优化
- **macOS exec approval 集成**：macOS 平台执行审批流程原生集成，增强 [[自主执行与人机协作|人机协作]] 安全性

---

## v2026.3.22-beta.1（3月23日）— Beta 预览

> 此版本已被 v2026.3.22 正式版取代，以下保留 Beta 发布时的记录。

这是 3 月最重要的版本，引入多项架构级变更和 Breaking Changes。

### ClawHub 原生安装

- ClawHub 安装流程整合进核心，无需额外配置即可从 [[ClawHub 官方技能注册表]] 安装 Skills

### 可插拔沙箱后端

- **OpenShell 后端**：支持 mirror 和 remote 两种工作区模式
- **核心 SSH 后端**：用于远程执行场景

详见 [[可插拔沙箱后端]]。

### 浏览器自动化增强

- 批量操作支持
- 选择器定位优化
- **Chrome DevTools MCP** 集成，通过 [[Chrome DevTools Protocol]] 实现更精细的浏览器控制

### 新增提供商与平台

- **Anthropic Vertex AI 提供商**支持，通过 [[Provider-Plugin 架构]] 接入 Google Cloud 上的 Claude
- **Matrix 插件完全重写**：基于 `matrix-js-sdk`，替代旧的自定义实现

### Breaking Changes

> **插件 SDK 路径迁移**：从 `openclaw/extension-api` 迁移到 `openclaw/plugin-sdk/*` 子路径。所有第三方插件需要更新 import 路径。

> **环境变量统一**：移除所有旧版 `CLAWDBOT_*` 和 `MOLTBOT_*` 环境变量，统一为 `OPENCLAW_*`。这是 [[OpenClaw 的起源与发展历程|改名事件]] 的最终技术清理。

> **移除旧版 Chrome 扩展中继路径**。

> **Discord 原生命令部署**：从旧方案切换为 Carbon reconcile。

---

## v2026.3.22（3月23日）— 正式版：架构级重构全面落地

由 [[Peter Steinberger]] 发布，100+ 贡献者参与，这是 v2026.3 系列的里程碑版本。Beta 阶段的所有特性正式稳定，并新增大量功能和安全修复。

### Breaking Changes（正式版完整清单）

**插件 SDK 与扩展架构**

- 公共插件接口从 `openclaw/extension-api` 迁移到 `openclaw/plugin-sdk/*` 子路径
- 捆绑插件不再直接 import 宿主模块，改为通过注入的运行时操作
- 消息工具发现必须使用 `ChannelMessageActionAdapter.describeMessageTool(...)` ，旧适配器方法移除
- 旧版 `.moltbot` 状态目录和 `CLAWDBOT_*`/`MOLTBOT_*` 环境变量彻底清除

**浏览器与 MCP**

- Chrome MCP 扩展中继路径移除，捆绑扩展资源删除
- `driver: "extension"` 和 `browser.relayBindHost` 配置项弃用
- 用户需运行 `openclaw doctor --fix` 将本地浏览器配置迁移到 `existing-session`/`user` 模式

**模型与技能配置**

- 图像生成统一为核心 `image_generate` 工具，移除 `nano-banana-pro` Skill 包装
- 默认 OpenAI 模型切换为 `openai/gpt-5.4`
- 捆绑图像生成使用 `agents.defaults.imageGenerationModel` 配置

**安全与运行时加固**

- 沙箱环境阻止 JVM 注入（`MAVEN_OPTS`、`SBT_OPTS`、`GRADLE_OPTS`、`ANT_OPTS`）
- 阻止 Glibc 可调参数利用（`GLIBC_TUNABLES`）和 .NET 依赖劫持（`DOTNET_ADDITIONAL_DEPS`）
- 语音通话 Webhook 预认证请求体限制降至 64 KB，超时 5 秒
- Discord 原生命令部署默认切换为 Carbon reconcile

**Matrix 插件**

- 全新 Matrix 插件基于官方 `matrix-js-sdk`，现有用户需按迁移指南操作

**安装优先级**

- `openclaw plugins install <package>` 对 npm 安全名称优先查询 ClawHub

### ClawHub 与市场集成

- 原生 `openclaw skills search|install|update` 命令流程
- `openclaw plugins install clawhub:<package>` 支持元数据跟踪
- Claude marketplace 注册表解析与 `plugin@marketplace` 安装
- Marketplace 列表与更新支持，含 Docker E2E 覆盖

详见 [[ClawHub 官方技能注册表]]。

### 插件与提供商架构

- 新增 owner-gated `/plugins` 和 `/plugin` 聊天命令（列表/显示/启用/禁用）
- 捆绑提供商逻辑迁入插件：OpenRouter、GitHub Copilot、OpenAI Codex
- Codex、Claude、Cursor 捆绑发现与 Skill 映射兼容
- 新增捆绑插件：**Chutes**（含 OAuth/API-key 认证）、**Exa**（网页搜索）、**Tavily**（搜索提供商）、**Firecrawl**（搜索/爬取）

详见 [[Provider-Plugin 架构]] 和 [[Plugin 扩展系统]]。

### 模型提供商大扩展

- **Anthropic Vertex**：通过 GCP auth 发现接入 Google Vertex AI 上的 Claude
- **MiniMax**：合并 API/OAuth 接口为单一插件，新增 M2.7 和 M2.7-highspeed
- **xAI Grok**：目录与 Pi SDK 同步，fast-mode 映射支持新变体
- **Z.AI GLM**：目录更新至 4.5/4.6 系列，含当前定价
- **Mistral**：元数据同步至当前定价
- **Xiaomi（小米）**：切换至 `/v1` OpenAI 兼容端点，支持 MiMo V2 Pro/Omni
- **OpenAI**：前向兼容 `gpt-5.4-mini` 和 `gpt-5.4-nano`

### 可插拔沙箱后端

- 引入可插拔沙箱架构
- **OpenShell 后端**：`mirror` 和 `remote` 两种工作区模式
- **核心 SSH 后端**：支持 secret-backed 密钥/证书/known_hosts
- 共享远程执行/文件系统工具迁移到核心

详见 [[可插拔沙箱后端]]。

### 浏览器增强

- Chrome DevTools MCP 支持 `browser.profiles.<name>.userDataDir`
- Brave、Edge 及 Chromium 系浏览器通过 user data 目录附加
- 捆绑插件 MCP 服务器在嵌入式 Pi 中暴露可运行工具
- 相对路径捆绑 MCP 启动默认使用 bundle root

### Android 与移动端

- 系统感知深色主题覆盖入门和后续界面
- 语音合成迁移到 Gateway `talk.speak`，Android 播放使用最终响应音频
- 新增 `callLog.search` 和 `sms.search` 工具（通话记录和短信查询）
- 位置请求超时处理，防止 "Already resumed" 崩溃

### Telegram 增强

- 支持每账户自定义 Bot API 端点（代理/自托管部署）
- 自动重命名 DM 论坛主题（LLM 生成标签）
- `topic-edit` 动作支持论坛主题重命名和图标更新
- 静默错误回复（`channels.telegram.silentErrorReplies`，默认关闭）
- 改进消息分块，保留空格和段落分隔符

### 飞书集成

v2026.3.22 引入深度飞书（Feishu/Lark）集成：

- 结构化交互式审批卡片与快捷操作启动器
- 回调用户和会话上下文保持
- 当前会话 ACP 与子代理会话绑定
- `onReasoningStream` 和 `onReasoningEnd` 支持思考 Token Markdown 展示
- 身份感知结构化卡片头部和注释页脚
- 扩展动作面：消息已读/编辑、显式线程回复、置顶、成员检查

### Agent 与上下文引擎改进

- 每 Agent 的 thinking/reasoning/fast 默认值，含不允许覆盖时的自动回退
- `/btw` 旁问命令：无工具回答，不改变会话上下文
- 可插拔记忆插件系统提示词注册
- 上下文引擎 `assemble()` 接收嵌入运行器 `modelId`，实现每模型适配
- 转录维护重写：活跃分支元数据保持
- 紧凑目录回退：超出提示词预算前保留所有已注册 Skills

### Dashboard 与控制 UI

- 助手聊天气泡新增"展开到画布"按钮
- 统一主题边框圆角，新增 Roundness 滑块调节圆角半径
- 改进用量概览样式和响应式展示
- 移除单列布局中的空会话详情占位卡
- 系统感知深色主题集成
- 每网关会话选择和历史范围限定

### 配置与 CLI

- `config set` 扩展：SecretRef、提供商构建器模式、JSON/批量支持、`--dry-run` 验证
- `openclaw update --tag main` 支持从 GitHub main 分支安装
- 插件自有认证 + 分发基础设施（Marketplace 和捆绑提供商）
- 健康监控：可配置过时事件阈值和每频道覆盖

### 安全修复与加固

**网络与传输安全**

- 阻止远程主机 `file://` 媒体 URL 和 UNC/网络路径在本地文件系统解析前
- 显式代理 SSRF 固定 + HTTPS 代理隧道翻译
- Bonjour 和 DNS-SD 服务端点失败在发现/入门阶段闭合处理
- Windows SMB 凭证握手防护

**认证与配对**

- iOS 设置码绑定到预期节点配置文件
- 首次使用引导兑换拒绝更广角色/范围请求
- 设备审批对照调用者会话范围检查
- 无设备身份的控制 UI 会话阻止特权配对审批 RPC

**Webhook 与消息安全**

- 飞书签名 Webhook 验证使用常量时间比较
- Nostr DM 解密前强制执行入站 DM 策略
- Nostr DM 加密前的速率和大小守卫
- Synology Chat 回复绑定稳定数字 `user_id`
- 邮件 Webhook 元数据外部内容包装前消毒
- Tlon DM 授权在引用展开前强制执行

**执行与工具访问**

- `jq` 从默认安全 bin 白名单移除（`jq -n env` 失败关闭）
- 透明分发包装器处理在审批解析中统一
- `time` 在白名单评估中视为透明包装器
- macOS 白名单解析加固，防止 wrapper 和 `env` 欺骗
- 韩文空白填充码点在审批提示中转义
- 宿主环境变量覆盖处理在 Gateway 和 Node 间加固

**插件与 Marketplace 安全**

- 远程 Marketplace 清单条目验证安装范围扩展
- 外部 git/GitHub 源、HTTP 归档和绝对路径被拒绝
- 插件拥有的上下文引擎注册强制 owner 感知
- 核心 `legacy` 引擎 ID 欺骗防护

### 性能与稳定性

- 捆绑频道插件从编译的 `dist/extensions` 加载
- WhatsApp Gateway 冷启动时间大幅缩短
- CLI 启动优化：频道添加和根帮助路径懒加载
- Discord 提供商/会话懒加载，消除无关提供商导入
- 模型目录按配置和 auth 文件状态缓存
- Gateway WS 握手超时提升到 10 秒（`OPENCLAW_HANDSHAKE_TIMEOUT_MS` 可覆盖）
- 每账户频道启动序列化，防止重叠启动/提供商重复
- Android 相机位图回收防止原生图像内存泄漏

### 关键 Bug 修复

- Agent 默认超时从 600 秒提升到 48 小时（长运行 ACP/Agent 会话）
- `memory_search` 和 `memory_get` 独立注册，防止互相抑制
- OpenAI 兼容提供商重复 tool call ID 去重，防止 HTTP 400 拒绝
- 上下文压缩后转录修复 + 溢出恢复触发
- WhatsApp 重连后粘性入站时间戳保持
- Telegram 轮询卡住 `getUpdates` 请求硬超时
- Gateway Bonjour IPv4 丢失断言在接口变化时抑制
- CLI 配置：严格 JSON 执行 + JSON5 回退
- 控制 UI 子代理完成的外部投递路由保持
- macOS `openclaw node start/stop --json` 恢复（Mac app 集成）
- 浏览器启动时移除多余空白标签页

---

## v2026.3.23（3月23日）— 热修复：运行时修复与认证加固

紧随 v2026.3.22 发布的热修复版本，解决正式版中发现的关键问题。

### Breaking Changes

- **Qwen 提供商重构**：重命名为"Qwen (Alibaba Cloud Model Studio)"，切换到新 DashScope 端点
- **UI 按钮原语整合**：统一按钮组件并应用 WCAG 2.1 AA 对比度标准
- **CSP 安全增强**：为内联脚本计算 SHA-256 哈希

### 关键修复

- **捆绑插件运行时 sidecar 恢复**：修复 npm 包中 WhatsApp 和 Matrix 等捆绑插件无法加载的问题
- **单频道设置认证修复**：解决单频道配置时的认证问题
- **OpenAI Token 凭证处理**：防止凭证回退
- **设备认证绕过路径中的操作员范围保持**
- **ClawHub 插件兼容性检查增强**

### 集成改进

- **Browser/CDP**：慢速系统上的会话复用改进
- **Telegram**：DM 主题线程上下文正确填充
- **Discord**：命令返回明确的未授权回复替代通用错误
- **Mistral**：Token 限制默认值降低，含自动修复能力

### 统计

- 40+ 项修复，覆盖认证、插件系统、消息平台和基础设施稳定性
- 16 位社区成员贡献

## 应用与影响

- **模块化转型完成**：Dashboard 模块化 + Provider 插件化 + 沙箱可插拔，三条线同时推进，OpenClaw 正在从"单体框架"变为"可组装平台"
- **历史包袱清理**：`CLAWDBOT_*`/`MOLTBOT_*` 环境变量和旧 Chrome 中继路径的移除，说明项目有决心切断向后兼容包袱
- **安全改进持续**：macOS exec approval 和可插拔沙箱后端表明安全仍是优先事项
- **生态大爆发**：v2026.3.22 的 100+ 贡献者和 ClawHub 原生集成标志着社区参与达到新高度
- **企业级集成深化**：飞书深度集成、Anthropic Vertex 接入、Qwen DashScope 端点切换表明 OpenClaw 在企业市场的渗透正在加速
- **安全加固全面化**：从 JVM 注入防护到 Glibc 可调参数阻断，从 SSRF 固定到 SMB 凭证握手防护，v2026.3.22 的安全修复覆盖了前所未有的攻击面

## 关键洞察

v2026.3 系列标志着 OpenClaw 的"第二次架构跃迁"——第一次（v2.1）是安全补课，这一次是工程成熟度提升。Provider-Plugin 架构让模型接入从"PR 合并"变成"npm install"，可插拔沙箱让执行环境从"硬编码"变成"可替换"，Dashboard 模块化让前端从"整块页面"变成"视图组件"。这些变化的共同方向是：**让 OpenClaw 的每一层都可以被独立替换和扩展**。

v2026.3.22 正式版的发布标志着这一愿景的全面落地。Beta 中的 Breaking Changes 经过社区验证后进入稳定通道，同时新增的飞书集成、7 家新模型提供商、以及 Agent 超时从 600 秒到 48 小时的跃升，显示项目正在从"开发者工具"向"企业级平台"转型。

但风险同样显著——v2026.3.23 热修复在正式版发布当天即出，修复了捆绑插件 sidecar 无法加载等关键问题，说明如此大规模的架构重构仍有稳定性债务需要偿还。对于 ClawHub 上的 Skills 和社区 Plugin 生态来说，SDK 路径迁移和环境变量清理意味着不小的迁移成本。

## 双链导航

- [[OpenClaw 是什么]] — 框架总览
- [[OpenClaw v2.1 版本更新]] — 上一个重大版本
- [[Dashboard 控制面板]] — v2026.3.12 引入的 Dashboard 模块化
- [[Provider-Plugin 架构]] — 模型提供商插件化架构
- [[可插拔沙箱后端]] — OpenShell 沙箱后端
- [[Plugin 扩展系统]] — 插件加载与扩展机制
- [[模型无关架构]] — Provider-Plugin 是模型无关的工程落地
- [[会话状态管理]] — 会话状态跨重置保持的改进
- [[自主执行与人机协作]] — macOS exec approval 的安全理念
- [[OpenClaw 的起源与发展历程]] — 环境变量清理与改名事件的关联
- [[Chrome DevTools Protocol]] — 浏览器自动化的底层协议
- [[ClawHub 官方技能注册表]] — v2026.3.22 的 ClawHub 原生集成
- [[Peter Steinberger]] — v2026.3.22 发布者
- [[2026年3月安全公告汇总]] — 同期安全公告

## 参考

- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [OpenClaw Releases](https://github.com/openclaw/openclaw/releases)
- [v2026.3.22 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.3.22)
- [v2026.3.23 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.3.23)
