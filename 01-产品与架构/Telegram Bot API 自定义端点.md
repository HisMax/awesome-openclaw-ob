---
tags:
  - OpenClaw
  - Telegram
  - 集成
  - 2026年3月
aliases:
  - Custom Bot API Endpoint
  - Telegram 自定义端点
  - Telegram 代理部署
---

# Telegram Bot API 自定义端点

## 一句话理解

> 就像给每个快递员指定不同的配送站——默认走官方站点，但在网络受限的地区可以指定"本地代收点"（自定义端点），甚至自己建一个"私人配送站"（自托管 Bot API 服务器），每个 Telegram 账户独立配置，互不干扰。

## 核心功能

v2026.3.22 为 Telegram 集成新增了 **每账户自定义 Bot API 端点**支持。在此之前，所有 Telegram Bot 都必须连接到 `api.telegram.org` 官方端点。新功能允许每个 Telegram 账户独立指定 Bot API 的服务器地址，适用于以下场景：

- **代理部署**：通过中间代理服务器访问 Telegram API，绕过网络限制
- **自托管部署**：运行自己的 [Telegram Bot API Server](https://github.com/tdlib/telegram-bot-api)，获得更高的文件上传限制和更低延迟
- **合规要求**：企业环境中将 API 流量路由到指定的安全网关

此功能由 **@Cypherm** 在 PR #48842 中贡献。

## 其他 Telegram 增强（v2026.3.22）

### DM 论坛主题自动重命名

Telegram 的论坛模式（Forum Topics）中，DM 主题现在会自动使用 LLM 生成的标签进行重命名。Agent 分析对话内容后，为每个主题生成一个简洁的描述性标签——比如将 "General Topic" 重命名为"部署问题排查"或"API 密钥配置"。这极大提升了高并发 DM 场景下的主题可读性。

### topic-edit 动作

新增 `topic-edit` 动作类型，支持通过 Agent 对论坛主题进行重命名和图标更新。这是 [[ChannelMessageActionAdapter]] 统一接口的一个新动作类型，Agent 可以在执行循环中主动管理 Telegram 论坛结构。

### silentErrorReplies

新增 `channels.telegram.silentErrorReplies` 配置项（默认关闭）。开启后，当 Agent 处理消息出错时，错误回复会以静默消息（无通知声）发送，避免在深夜或安静场景中打扰用户。

### IPv4 粘性回退

针对部分网络环境中 IPv6 连接不稳定的问题，新增 IPv4 粘性回退机制——当 IPv6 连接失败时，后续请求会"粘住" IPv4 地址，直到下次重连再尝试 IPv6。这解决了某些 VPS 环境中 Telegram 轮询 `getUpdates` 请求间歇性超时的问题。

### 消息分块改进

改进了长消息的分块逻辑，现在能正确保留空格和段落分隔符。旧实现在切割长文本时可能破坏段落结构，导致代码块或列表格式错乱。

## 双链导航

- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入所有 Telegram 增强
- [[多频道消息架构]] — Telegram 作为 OpenClaw 支持的核心消息平台之一
- [[ChannelMessageActionAdapter]] — topic-edit 动作的注册接口
- [[Plugin 扩展系统]] — Telegram 插件作为 Channel Adapter 的架构基础
