---
tags:
  - 安全
  - Marketplace
  - 供应链
  - OpenClaw
  - 2026年3月
aliases:
  - Marketplace Installation Scope Validation
  - 安装范围验证
  - 插件安装范围检查
---

# Marketplace 安装范围验证

## 一句话理解

> Marketplace 安装范围验证就像海关检查——进口商（插件）申报的货物清单（manifest）必须与实际装箱内容一致。如果申报"文本处理工具"但箱子里装着"系统管理权限"，海关直接扣押。v2026.3.22 让这个海关从抽检变成了逐件扫描。

## 问题根源：清单与实际安装的脱节

[[ClawHub 官方技能注册表|ClawHub]] 作为 OpenClaw 的官方 Skill/插件分发平台，每个插件都有一个 manifest（清单文件）声明其安装范围——需要哪些权限、会修改哪些目录、注册哪些上下文引擎。但在 v2026.3.22 之前，远程 Marketplace 的 manifest 条目在安装时**缺乏严格的范围验证**，攻击者可以在 manifest 中声明较小的权限范围，而实际安装时通过以下手段扩大权限：

1. **安装范围扩展**：manifest 声明只修改 `~/.openclaw/skills/`，但安装脚本实际写入系统目录
2. **外部源注入**：manifest 引用外部 git 仓库、GitHub 源或 HTTP 归档作为依赖，绕过 ClawHub 的审查
3. **绝对路径逃逸**：manifest 中使用绝对路径（如 `/etc/cron.d/`）突破安装目录沙箱

这与 [[恶意 Skills 供应链攻击]] 描述的 ToxicSkills 研究结论高度吻合——36.82% 的 Skills 存在漏洞，而安装范围验证缺失是漏洞利用的关键前提。

## v2026.3.22 的验证机制

### Manifest 条目范围校验

每个远程 Marketplace manifest 条目在安装前都会经过严格的范围验证：

- **路径白名单**：安装路径必须在用户级 OpenClaw 目录内，绝对路径被直接拒绝
- **源地址限制**：外部 git/GitHub 源、HTTP 归档地址被拒绝，所有资源必须来自 ClawHub 官方 CDN
- **权限声明一致性**：manifest 声明的权限范围与实际安装行为进行运行时比对

### 上下文引擎注册的 Owner 感知

OpenClaw 的上下文引擎（Context Engine）允许插件注册自定义的上下文处理器。v2026.3.22 引入了 **owner-aware registration**：

- 每个插件只能注册属于自己命名空间的上下文引擎 ID
- 跨插件的引擎 ID 注册被拒绝，防止恶意插件劫持合法插件的上下文处理

### Core Legacy 引擎 ID 欺骗防护

OpenClaw 内置了一些核心上下文引擎（标记为 `legacy`）。攻击者可能尝试注册与核心引擎同名的 ID 来劫持系统行为。v2026.3.22 对核心 `legacy` 引擎 ID 进行了保护性锁定，第三方插件无法注册或覆盖这些 ID。

## 与 ClawHavoc 事件的关联

[[ClawHavoc 事件]] 是 OpenClaw 生态最严重的安全事件之一，其中恶意 Skill 通过 ClawHub 分发后执行了远超声明范围的操作。如果当时存在安装范围验证机制，攻击的影响面将大幅缩小——恶意 Skill 无法在安装时偷偷扩大权限范围。

[[ClawHub 原生安装]] 机制在 v2026.3 中得到增强，安装范围验证是其安全保障的核心组件。从 [[ClawHub 官方技能注册表]] 下载的每个 Skill 现在都必须通过这一验证关卡。

## 双链导航

- [[ClawHub 官方技能注册表]] — Marketplace 安装范围验证是 ClawHub 分发体系的安全基石
- [[ClawHavoc 事件]] — 安装范围验证缺失是该事件中恶意 Skill 得逞的关键原因之一
- [[ClawHub 原生安装]] — 原生安装流程集成了范围验证作为必要步骤
- [[恶意 Skills 供应链攻击]] — 安装范围验证是抵御供应链攻击的关键防线
- [[2026年3月安全公告汇总]] — 本条目属于 v2026.3.22 的"插件与 Marketplace 安全"加固范畴
- [[Plugin 扩展系统]] — 上下文引擎注册是插件扩展系统的核心能力，owner 感知保护其完整性
- [[工作区插件自动加载 RCE]] — 供应链攻击从远程 Marketplace 到本地工作区的完整链路
