---
tags:
  - OpenClaw
  - 安全
  - 策略
  - 插件管理
  - 运营
aliases:
  - Operator Install Policy
  - 运营者安装策略
  - 安装策略
  - installPolicy
---

# Operator Install Policy


![[assets/operator-policy.jpg]]

## 一句话理解

> Operator Install Policy 是 OpenClaw 的"安检门"——运营者配置一个本地策略命令，在每次插件或 Skill 安装前运行，决定允许还是阻止，替代了之前不可定制的危险代码扫描器。

## 概述

Operator Install Policy 是 OpenClaw v2026.6 引入的安全机制，允许运营者（Operator）配置一个本地策略命令（policy command），在插件和 Skill 安装流程中充当守门人角色。当 OpenClaw 暂存好待安装的源材料后、实际安装完成前，策略命令被调用来做出允许或阻止的决策。

### 解决的问题

之前 OpenClaw 使用内置的"危险代码扫描器"（dangerous-code scanner）来检测潜在不安全的插件。这个方案有根本性缺陷：

| 问题 | 表现 |
|------|------|
| 误报率高 | 合法的文件系统操作插件被标记为危险 |
| 不可定制 | 运营者无法根据自己的安全策略调整规则 |
| 黑名单模式 | 只能阻止已知危险模式，无法适应新的攻击向量 |
| 缺乏上下文 | 扫描器不了解运营者的部署环境和信任边界 |

Operator Install Policy 将控制权交给运营者——你最了解你的环境，你来决定什么可以安装。

## 配置

### 基础配置

在 OpenClaw 配置文件中添加 `security.installPolicy` 段：

```yaml
security:
  installPolicy:
    command: "/usr/local/bin/openclaw-install-policy"
    args: ["--json"]
    timeoutMs: 10000
    env:
      POLICY_MODE: "strict"
```

### 配置字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `command` | string | 是 | 策略命令的绝对路径 |
| `args` | string[] | 否 | 传递给策略命令的参数 |
| `timeoutMs` | number | 否 | 超时时间（毫秒），默认 10000 |
| `env` | object | 否 | 传递给策略命令的环境变量 |
| `target` | string \| null | 否 | 过滤目标：`"skill"`、`"plugin"` 或 `null`（全部） |

### target 字段的重要性

`target` 省略或设为 `null` 时，策略对所有受支持目标生效。这是一个深思熟虑的默认值——确保未来新增的安装类型不会意外绕过策略：

```yaml
# 只对 Skill 安装执行策略
security:
  installPolicy:
    command: "/usr/local/bin/skill-policy"
    target: "skill"

# 对所有安装执行策略（推荐）
security:
  installPolicy:
    command: "/usr/local/bin/install-policy"
    target: null  # 或直接省略
```

## 工作流程

### 执行时序

```
用户执行安装命令
  │  openclaw plugins install <package>
  │  openclaw skills install <name>
  │
  ▼
OpenClaw 暂存源材料
  │  下载/解压/克隆到暂存目录
  │
  ▼
构建策略输入（JSON）
  │  包含包名、来源、版本、暂存路径等元数据
  │
  ▼
调用策略命令
  │  /usr/local/bin/openclaw-install-policy --json < input.json
  │
  ├── 返回 { "action": "allow" }
  │      → 继续安装流程
  │
  ├── 返回 { "action": "block", "reason": "..." }
  │      → 中止安装，向用户显示 reason
  │
  ├── 超时（超过 timeoutMs）
  │      → 中止安装（fail-closed）
  │
  └── 命令不可用 / 非零退出
         → 中止安装（fail-closed）
```

### 适用的安装来源

策略命令覆盖所有安装入口：

| 来源类型 | 说明 | 示例 |
|----------|------|------|
| ClawHub Skills | 从 ClawHub 注册表安装 | `openclaw skills install @clawhub/web-search` |
| 上传的 Skills | 手动上传的 Skill 包 | Dashboard 文件上传 |
| Git / 本地 Skills | 从 Git 仓库或本地路径安装 | `openclaw skills install ./my-skill` |
| Skill 依赖安装器 | Skill 声明的 npm/pip 依赖 | `package.json` 中的 dependencies |
| Plugin install | npm 包插件 | `openclaw plugins install some-plugin` |
| Plugin update | 更新已安装的插件 | `openclaw plugins update some-plugin` |
| Marketplace | 从 Marketplace 安装 | `openclaw plugins install marketplace:plugin` |

### 不触发策略的场景

**关键行为**：正常 Gateway 启动不触发安装策略。

策略只在以下时机运行：
- 执行 `openclaw plugins install`
- 执行 `openclaw skills install`
- 执行 `openclaw plugins update`
- Dashboard/CLI 触发的安装操作

已安装插件的加载不受影响——策略是安装时检查，不是运行时检查。

## Fail-Closed 设计

这是 Operator Install Policy 最重要的设计决策：

### 什么是 Fail-Closed

```
策略命令已配置但不可用
  │
  ├── Fail-Open（不安全）：跳过检查，允许安装
  │
  └── Fail-Closed（安全）：拒绝安装，要求修复策略命令
                          ← OpenClaw 的选择
```

### 为什么选择 Fail-Closed

- **安全优先**：宁可拒绝一个合法安装，也不放过一个恶意安装
- **运维可见性**：策略命令故障会立即暴露（安装失败），不会悄悄退化为无策略状态
- **与 [[OpenClaw 官方安全模型]] 一致**：整体安全策略偏向保守

### 实际影响

如果你配置了策略命令但忘记部署策略二进制：
- 所有安装操作会失败
- 错误信息明确指向策略命令不可用
- 运营者需要先修复策略命令，或临时移除 `installPolicy` 配置

## 编写策略命令

### 输入格式

策略命令通过 stdin 接收 JSON 输入：

```json
{
  "action": "install",
  "target": "skill",
  "package": {
    "name": "@clawhub/web-search",
    "version": "1.2.3",
    "source": "clawhub",
    "stagedPath": "/tmp/openclaw-staged/abc123"
  },
  "operator": {
    "id": "operator-uuid",
    "environment": "production"
  }
}
```

### 输出格式

策略命令通过 stdout 返回 JSON：

```json
// 允许
{ "action": "allow" }

// 阻止
{
  "action": "block",
  "reason": "Package @clawhub/web-search is not in the approved vendor list"
}
```

### 示例策略脚本

```bash
#!/bin/bash
# /usr/local/bin/openclaw-install-policy
# 简单的白名单策略

APPROVED_VENDORS=("@clawhub" "@official" "@internal")

INPUT=$(cat)
PACKAGE_NAME=$(echo "$INPUT" | jq -r '.package.name')
PACKAGE_SOURCE=$(echo "$INPUT" | jq -r '.package.source')

# 内部来源始终允许
if [ "$PACKAGE_SOURCE" = "local" ]; then
  echo '{"action": "allow"}'
  exit 0
fi

# 检查供应商白名单
for vendor in "${APPROVED_VENDORS[@]}"; do
  if [[ "$PACKAGE_NAME" == "$vendor"* ]]; then
    echo '{"action": "allow"}'
    exit 0
  fi
done

echo "{\"action\": \"block\", \"reason\": \"Package $PACKAGE_NAME is not from an approved vendor\"}"
exit 0
```

## 与其他安全机制的关系

Operator Install Policy 是 v2026.6 安全三角的一角：

```
                  ┌─────────────┐
                  │ Auto Mode   │
                  │ (执行审批)   │
                  └──────┬──────┘
                         │
            ┌────────────┼────────────┐
            │                         │
    ┌───────┴───────┐       ┌─────────┴─────────┐
    │ Install Policy │       │ Security Config   │
    │ (安装控制)      │       │ Check (配置检查)   │
    └───────────────┘       └───────────────────┘
```

| 机制 | 作用时机 | 控制对象 |
|------|----------|----------|
| [[OpenClaw v2026.6 版本更新\|Auto Mode]] | 运行时 | Agent 执行的命令 |
| **Install Policy** | 安装时 | 插件和 Skill 的来源 |
| Security Config Check | 配置时 | 系统配置的安全性 |

三者互补：Install Policy 控制"什么能进来"，Auto Mode 控制"进来的东西能做什么"，Config Check 控制"整体配置是否安全"。

## 与 Claw Chain 的关联

[[OpenClaw v2026.4 版本更新|Claw Chain 四漏洞]] 中的供应链风险（通过恶意插件注入代码）正是 Install Policy 要预防的场景。虽然 v2026.4.22 修复了具体漏洞，Install Policy 从更高层面建立了安装环节的防御纵深。

## 关键洞察

Operator Install Policy 的设计哲学是"运营者最了解运营者的环境"。一个通用的代码扫描器永远无法理解"这个公司只信任来自内部 npm registry 的插件"或"这个部署只允许通过安全审计的 ClawHub 包"。

Fail-closed 的设计选择也传递了一个明确信号：**安全是非功能性需求中不可降级的那个**。当安全检查机制本身失效时，系统应该停止而不是继续——这与航空业的安全哲学一致。

对 OpenClaw 社区生态的影响也值得关注：Install Policy 可能会让企业更愿意采用 OpenClaw，因为他们有了控制供应链安全的抓手。但它也可能增加社区插件作者的负担——如果主流部署都配置了严格的 Install Policy，新插件的推广可能会更难。

## 双链导航

- [[OpenClaw 是什么]] — 框架总览
- [[OpenClaw v2026.6 版本更新]] — Install Policy 首次引入的版本
- [[OpenClaw v2026.4 版本更新]] — Claw Chain 漏洞与供应链安全
- [[OpenClaw 官方安全模型]] — 安全体系总览
- [[Plugin 扩展系统]] — 插件安装与加载机制
- [[ClawHub 原生安装]] — ClawHub 安装流程
- [[自主执行与人机协作]] — Auto Mode 的执行审批
- [[自主决策循环]] — Agent 自主性边界

## 参考

- [OpenClaw Security — Docs](https://docs.openclaw.ai/gateway/security)
- [Plugins — OpenClaw Docs](https://docs.openclaw.ai/cli/plugins)
- [Skills Config — OpenClaw Docs](https://docs.openclaw.ai/tools/skills-config)
- [v2026.6.2-beta.1 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.6.2-beta.1)
- [OpenClaw SECURITY.md](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)
