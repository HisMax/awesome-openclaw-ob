---
tags:
  - OAuth
  - 授权
  - 安全
  - API
  - Anthropic
aliases:
  - OAuth
  - OAuth 2.0
  - 授权协议
  - 令牌套利
---

# OAuth 2.0 协议

## 一句话理解

> OAuth 2.0 是一个授权框架——让用户授权第三方应用访问自己的资源，而无需交出密码。Anthropic 正是利用 OAuth 令牌的作用域控制，在 2026 年 1 月封杀了所有第三方工具使用 Claude 订阅的行为。

## 核心概念

### OAuth 2.0 的基本流程

```
用户 → 授权服务器（"允许 App X 访问我的数据？"） → 发放 Access Token
App X → 用 Token 请求资源服务器 → 获取用户数据
```

核心思想：**Token 代替密码**。Token 有作用域限制（只能做特定操作）、有过期时间、可随时撤销。

### Anthropic 封杀第三方工具事件

2026 年 1 月 9 日，Anthropic 部署服务端检测，封杀所有第三方工具使用 Claude 订阅 OAuth 令牌：

- **背景**：用户用 Pro/Max 订阅的 OAuth 令牌接入 OpenCode（56K Stars）、OpenClaw 等第三方工具，绕过 API 按量计费——"令牌套利"
- **封杀手段**：令牌作用域绑定 + 遥测验证 + 滥用检测，非官方客户端直接报错
- **影响**：OpenCode 等工具一夜失效，部分 Max $200/月用户因误触滥用过滤器被封号
- **George Hotz 警告**："你不会把人赶回 Claude Code，你只会把他们赶向其他模型提供商"
- **后续**：Anthropic 承认误封并回滚部分封禁；OpenAI 趁机明确支持 ChatGPT 订阅登录。OAuth 封杀直接催生了 [[OpenClaw Wrapper 创业潮]]——当官方渠道被堵死，创业者嗅到了"帮用户绕过限制"的商机，117 家 wrapper 公司应运而生
- **2026 年 4 月彻底封死**：Anthropic 于 4 月 4 日切断所有第三方工具使用 Claude 订阅积分的通道，第三方工具使用现在只能通过"额外用量"计费或 API Key。OAuth 路径已完全关闭，API Key（按量付费）成为推荐方式——成本透明且无封号风险。**OpenAI OAuth 仍支持第三方工具接入**，形成差异化

### Composio 的角色

[[白手套部署服务|SetupClaw]] 等白手套部署服务使用 **Composio** 作为 OAuth 中间件，解决非技术用户的 API 授权难题。Composio 将复杂的 OAuth 流程封装为一键授权体验，让不懂技术的用户也能安全地将 Google、GitHub、Slack 等服务连接到 OpenClaw Agent。

## 应用与影响

- **平台控制权**：OAuth 令牌作用域绑定让平台方（Anthropic）可以精确控制第三方工具能做什么、不能做什么
- **开源 vs 商业的张力**：OpenClaw 的 [[模型无关架构]] 正是对这种平台锁定的回应——当一个提供商封杀你时，你可以切换到另一个
- **安全双刃剑**：OAuth 保护了授权安全，但 OpenClaw 的 `openclaw.json` 中**明文存储**的 API 密钥被 Vidar 等信息窃取器列为目标——授权机制再好，存储不安全一切白费

## 关键洞察

OAuth 封杀事件暴露了 AI 生态的权力结构：**模型提供商通过授权协议控制整个下游生态**。Anthropic 一次服务端部署就能让数万用户的工具一夜失效。这也解释了为什么 [[OpenClaw 是什么|OpenClaw]] 坚持模型无关设计——在一个提供商随时可以"关水龙头"的世界里，不被绑定就是最大的安全边际。

## 外部链接

- [OAuth 2.0 官方规范](https://oauth.net/2/)

## 双链导航

- [[OpenClaw 是什么]] — OAuth 争议的中心项目
- [[模型无关架构]] — 对 OAuth 平台锁定的架构回应
- [[安全边界与风险（总览）]] — 凭证泄露与 OAuth 令牌安全
- [[白手套部署服务]] — Composio 简化 OAuth 授权
- [[Claude 模型系列]] — OAuth 封杀事件中的模型提供方
- [[GPT 模型系列]] — OpenAI 趁机支持第三方接入
