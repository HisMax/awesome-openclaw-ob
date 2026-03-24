---
tags:
  - 架构
  - 插件系统
  - 扩展
  - loader
  - OpenClaw-extensions
aliases:
  - Plugin System
  - 插件系统
  - openclaw.extensions
  - loader.ts
---

# Plugin 扩展系统

## 一句话总结

OpenClaw 的 Plugin 系统通过 `package.json` 中的 `openclaw.extensions` 字段声明插件入口，`src/plugins/loader.ts` 在启动时自动扫描并加载——插件可以注册新工具、新 Channel Adapter 或新 LLM Provider，无需修改核心代码。

## 核心机制：自动发现与动态加载

### 声明：openclaw.extensions 字段

插件在 `package.json` 中通过 `openclaw.extensions` 字段声明自己的入口：

```json
{
  "name": "my-openclaw-plugin",
  "openclaw": {
    "extensions": {
      "tools": "./dist/tools/index.js",
      "channels": "./dist/channels/index.js",
      "providers": "./dist/providers/index.js"
    }
  }
}
```

这是一种**约定优于配置**的设计——不需要手动注册，只要字段存在，loader 就会找到它。

### 加载流程

Gateway 启动 → `src/plugins/loader.ts` 扫描依赖 → 检查 `openclaw.extensions` 字段 → 动态 import 入口文件 → 注册到运行时。loader.ts 的职责是**桥接声明与运行时**。

### 三类扩展

| 扩展类型 | 作用 | 示例 |
|----------|------|------|
| **工具（Tools）** | 新增 Agent 可调用的工具 | 邮件发送、日历操作、智能家居控制 |
| **Channel Adapter** | 新增消息平台支持 | 飞书、Nostr、自定义 WebChat |
| **LLM Provider** | 新增模型接口 | DeepSeek、Kimi、自托管模型 |

## 与 Skills 的区别

Plugin 是**基础设施层**扩展（npm 依赖，node_modules，注册工具/Channel/Provider，启动时加载，需重启）；Skill 是**应用层**扩展（ClawHub 安装，`~/.openclaw/skills/`，定义行为模式，250ms debounce 热重载）。

[[自我修改软件机制|自我修改]]、Plugin、Skill 构成 OpenClaw 的三层扩展体系：自我修改最灵活最危险 → Plugin 系统级启动加载 → Skill 应用级热重载。ClawHub 上 3,286 个 Skills（清理后）和社区 Plugin 共同构成生态系统。

## 安全考量与关键洞察

Plugin 通过 npm 安装，继承了 npm 生态的供应链风险。相比 ClawHub 上 36.82% 存在漏洞的 Skills，Plugin 审计渠道更成熟（npm audit、Snyk 等）。但 Plugin 拥有更高的系统权限——恶意 Plugin 可注册后门工具或劫持 LLM Provider 通信。

`openclaw.extensions` 字段设计解决了一个关键生态问题：**如何让第三方开发者扩展系统能力而不需要 fork 核心代码**。VS Code 的 contributes 字段、Webpack 的 plugin 系统都采用了类似的声明式扩展点模式。loader.ts 的自动发现机制让"安装即可用"成为现实。

## 相关笔记

- [[自我修改软件机制]] -- Agent 运行时的自修改能力
- [[Tool Use 机制]] -- Plugin 注册的工具在执行循环中被调用
- [[TypeBox Schema 工具定义]] -- 插件注册工具时使用 TypeBox 定义参数
- [[多频道消息架构]] -- Plugin 可注册新的 Channel Adapter
- [[模型无关架构]] -- Plugin 可注册新的 LLM Provider
- [[Provider-Plugin 架构]] -- v2026.3 引入的模型提供商插件化，是 Plugin 系统三类扩展中 LLM Provider 的架构升级
- [[可插拔沙箱后端]] -- 沙箱后端通过插件机制注册
- [[Dashboard 控制面板]] -- Dashboard 的 Config 模块管理 Plugin 配置
- [[OpenClaw v2026.3 版本更新]] -- v2026.3.22 中插件 SDK 路径 Breaking Change
- [[v2026.3.22 Breaking Changes 迁移指南]] -- SDK 路径迁移详细指南
- [[ChannelMessageActionAdapter]] -- v2026.3.22 新增的统一消息工具发现接口
- [[可插拔记忆插件]] -- 记忆系统通过插件机制可插拔
- [[ClawHub 原生安装]] -- v2026.3.22 将 ClawHub 安装整合进核心
- [[Marketplace 安装范围验证]] -- 插件安装的安全验证
- [[OpenClaw 官方安全模型]] -- 插件的安全审计与供应链风险

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [npm 官方](https://www.npmjs.com)
