---
tags:
  - 安全
  - 漏洞
  - GHSA
  - RCE
  - 供应链攻击
  - OpenClaw
aliases:
  - GHSA-99qw-6mr3-36qr
  - 插件自动加载漏洞
  - Extensions Auto-Load RCE
---

# 工作区插件自动加载 RCE

**一句话总结**：OpenClaw 从 `.openclaw/extensions/` 目录自动加载插件且无需用户确认，攻击者可通过植入恶意插件实现零交互远程代码执行。

## 漏洞基本信息

| 项目 | 详情 |
|------|------|
| GHSA 编号 | GHSA-99qw-6mr3-36qr |
| 严重度 | **高危（High）** |
| 影响版本 | <=2026.3.11 |
| 修复版本 | 2026.3.12 |
| 漏洞类型 | 供应链攻击 / 远程代码执行 |

## 漏洞分析

### 根因

OpenClaw 在启动时会扫描 `.openclaw/extensions/` 目录，自动加载其中的所有插件。这个过程**完全不需要用户确认或审批**，也没有签名验证机制。任何被放入该目录的代码都会在 Agent 的权限上下文中自动执行。

### 攻击场景

#### 场景一：共享项目投毒

1. 攻击者在共享代码仓库中植入 `.openclaw/extensions/malicious-plugin`
2. 受害者克隆仓库后启动 OpenClaw
3. 恶意插件自动加载并执行，无任何提示

#### 场景二：配合其他漏洞

1. 攻击者通过 [[WebSocket 提权漏洞 GHSA-rqpp]] 或其他方式获得文件写入能力
2. 在 `.openclaw/extensions/` 下植入恶意插件
3. 下次 OpenClaw 启动时自动触发

#### 场景三：本地恶意软件

1. 已有恶意软件（如 [[凭证泄露与信息窃取|Infostealer]]）获得文件系统访问
2. 在 `.openclaw/extensions/` 下植入持久化后门
3. 随 OpenClaw 每次启动自动执行

### 与 ClawHub 供应链攻击的关系

此漏洞是 [[恶意 Skills 供应链攻击]] 在本地工作区层面的延伸：

| 维度 | ClawHub 供应链 | 本地插件自动加载 |
|------|---------------|-----------------|
| 攻击入口 | 远程 Skill 注册表 | 本地文件系统 |
| 触发方式 | 用户安装 Skill | 自动加载，无需交互 |
| 验证机制 | VirusTotal 扫描（有限） | **完全无验证** |
| 影响范围 | 单个 Skill 能力范围 | Agent 完整权限 |

本地自动加载比 ClawHub 供应链攻击更危险——**零交互、零验证、完整权限**。

## 影响评估

- 恶意插件在 Agent 上下文中执行，拥有与 Agent 相同的权限
- 可访问所有 Agent 可达的文件、凭证、网络资源
- 可利用 [[权限控制机制]] 中的 `operator.admin` 等高权限作用域
- 结合 [[代码执行安全]] 中描述的 `tools.exec.host=gateway` 可逃逸容器

## 修复措施

2026.3.12 版本修复了此漏洞，核心改进：

- 加载 `.openclaw/extensions/` 下的插件前**要求用户明确确认**
- 插件加载事件写入审计日志
- 新增插件来源校验机制

## 防御建议

1. **立即升级**至 2026.3.12 或更高版本
2. 审查现有 `.openclaw/extensions/` 目录内容
3. 在 `.gitignore` 中排除 `.openclaw/extensions/`，防止仓库投毒
4. 使用 [[沙箱机制|Docker 沙箱]] 限制插件执行范围
5. 定期扫描工作区目录，检测未知插件文件

## 后续发展

v2026.6.2 引入 [[Operator Install Policy]]，进一步强化了插件安装的安全模型——用操作者安装策略替代旧的危险代码扫描器路径，覆盖 package、archive、source、upload 和 marketplace 安装全生命周期。

## 相关笔记

- [[2026年3月安全公告汇总]] — 本月所有 GHSA 公告
- [[恶意 Skills 供应链攻击]] — ClawHub 层面的供应链风险
- [[代码执行安全]] — 代码执行风险全景
- [[Snyk ToxicSkills 研究报告]]
- [[安全最佳实践]]
- [[RankClaw ClawHub 审计]] — 全量审计揭示供应链安全现状
- [[2026年Q2安全态势总览]] — Q2 安全态势

## 外部链接

- [GHSA-99qw-6mr3-36qr](https://github.com/advisories/GHSA-99qw-6mr3-36qr)
