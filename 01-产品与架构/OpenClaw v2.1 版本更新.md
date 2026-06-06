---
tags:
  - OpenClaw
  - 版本更新
  - 安全
  - 性能
aliases:
  - v2.1
  - OpenClaw v2.1
  - 版本更新
  - 2026.2.25 更新
---

# OpenClaw v2.1 版本更新

## 一句话理解

> OpenClaw v2.1（v2026.2.25+）是安全事件驱动的重大更新——CVE-2026-25253 一键 RCE 漏洞在 24 小时内被修复，TOFU 信任策略和 Origin 头验证成为新的安全基线，同时 Skills API 优化和性能提升让框架更加稳固。

## 核心概念

### 安全改进（最关键变化）

**CVE-2026-25253 修复**（CVSS 8.8）：

v2.1 之前的攻击链：受害者访问恶意页面 → 跨站 WebSocket 劫持 → 暴力破解 Gateway 密码 → 窃取 Token → 完全控制 Gateway → 任意命令执行。约 15,200 个实例面临 RCE 风险。

v2.1 引入的防御：
- **TOFU（Trust On First Use）策略**：首次连接时建立信任锚点，后续连接必须匹配，阻止未知设备静默注册
- **Origin 头验证**：WebSocket 连接必须包含合法 Origin，阻断跨站劫持攻击路径
- **速率限制修复**：localhost 连接不再豁免暴力破解防护

### ClawHub 安全整改

- **VirusTotal 集成**（2026.2.7 起）：所有新上架 Skills 自动恶意软件扫描
- **大规模清理**：从 5,705 个 Skills 清理至 3,286 个，删除 2,419 个可疑 Skills
- **社区举报机制**：被举报 3 次自动隐藏，进入人工复审

### 性能与功能

- **版本 2026.3.7**：2026 年 3 月 7 日发布的后续版本带来了性能优化和新的 Skills API
- **GitHub Stars 突破 28 万**：截至 3 月中旬约 280,000，较 2 月底的 237,000 增长 18%
- **npm 周下载量**：从 2 月初的 ~720,000 增长至 2 月底的 ~1,270,000

### 相关时间线

| 日期 | 事件 |
|------|------|
| 2026.1.30 | OpenClaw 正式定名 |
| 2026.2.5 | Claude Opus 4.6 发布，SWE-Bench 80.8% |
| 2026.2.7 | ClawHub VirusTotal 集成上线 |
| 2026.2.14 | Steinberger 宣布加入 OpenAI |
| 2026.2.25 | v2.1 安全修复发布；Claude Code Remote Control 研究预览 |
| 2026.3.7 | v2026.3.7 性能优化版本 |

## 应用与影响

- **安全态势转变**：v2.1 标志着 OpenClaw 从"安全是可选的"向"安全是内建的"迈出了第一步——但 Cisco 的评价仍然是"安全是可选的，不是内建的"，说明差距仍大
- **社区信心恢复**：24 小时修复响应时间和 ClawHub 清理行动展示了社区的快速响应能力
- **基金会治理测试**：这是 Steinberger 加入 OpenAI 后、项目转交基金会前的最后一次由核心团队主导的重大更新

## 关键洞察

v2.1 是一个"被迫的安全补课"——不是因为规划好的安全路线图，而是因为 CVE-2026-25253 的紧急披露。OpenClaw 在 24 小时内完成修复体现了开源社区的响应速度，但也暴露了一个根本问题：**一个 237K Stars 的项目，安全团队为零，Bug 赏金计划为零**。v2.1 解决了已知漏洞，但未解决安全债务的根源。

## 双链导航

- [[OpenClaw 是什么]] — v2.1 是其最新重大版本
- [[OpenClaw v2026.3 版本更新]] — v2.1 之后的下一个重大版本系列
- [[OpenClaw v2026.4 版本更新]] — Claw Chain 事件暴露更深层安全挑战
- [[安全边界与风险（总览）]] — CVE-2026-25253 的完整分析
- [[VirusTotal 安全扫描]] — v2.1 配套的 ClawHub 安全措施
- [[OpenClaw 官方安全模型]] — TOFU 策略的设计理念
- [[ClawHub 官方技能注册表]] — Skills 清理行动的直接影响
- [[OpenClaw 的起源与发展历程]] — 版本演进的完整时间线
- [[Skill 热重载机制]] — v2.1 中 Skills API 优化涉及的热重载改进

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
