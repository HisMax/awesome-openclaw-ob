---
tags:
  - OpenClaw
  - ClawHub
  - 安装
  - 2026年3月
aliases:
  - ClawHub Native Install
  - Skills 原生安装
  - openclaw skills install
---

# ClawHub 原生安装

## 一句话理解

> 过去安装 Skills 像逛第三方应用商店——要切换环境、手动配置；v2026.3.22 把应用商店"焊进"了操作系统，`openclaw skills install` 一条命令直达 [[ClawHub 官方技能注册表]]。

## 背景

在 v2026.3.22 之前，从 [[ClawHub 官方技能注册表]] 安装 Skills 需要额外配置步骤或通过 npm 手动下载。这增加了使用门槛，也让用户更容易绕过官方渠道从未经验证的来源安装——[[ClawHavoc 事件]] 中 12% 恶意 Skills 的传播正是部分源于此。

## 核心变更

### 新 CLI 命令

```bash
openclaw skills search <keyword>     # 搜索 Skills
openclaw skills install <name>       # 从 ClawHub 安装
openclaw skills update [name]        # 更新已安装 Skills
openclaw plugins install clawhub:<package>  # 显式指定 ClawHub 来源
```

### 安装优先级变更

这是一个 **Breaking Change**：`openclaw plugins install <package>` 对 npm 安全名称**优先查询 ClawHub**，npm 退为后备。这意味着同名包会优先从 ClawHub 解析——既提高了安全性（ClawHub 有审核机制），也可能导致意外安装了 ClawHub 版本而非 npm 版本。

### Marketplace 集成

- Claude Marketplace 注册表解析
- `plugin@marketplace` 格式安装
- 元数据跟踪：安装来源、版本、兼容性信息持久化
- Docker E2E 测试覆盖

## 安全影响

原生安装流程引入了 [[Marketplace 安装范围验证]]——远程清单条目必须通过范围扩展验证，外部 git 源、HTTP 归档和绝对路径被拒绝。这是对 [[ClawHavoc 事件]] 后安全整改的技术延续。

## 双链导航

- [[ClawHub 官方技能注册表]] — 技能注册表本身
- [[OpenClaw v2026.3 版本更新]] — 版本上下文
- [[Plugin 扩展系统]] — Skills 与 Plugins 的层级关系
- [[Marketplace 安装范围验证]] — 安装安全验证机制
- [[ClawHavoc 事件]] — 促成原生安装的安全动因
- [[v2026.3.22 Breaking Changes 迁移指南]] — 安装优先级变更的迁移说明
