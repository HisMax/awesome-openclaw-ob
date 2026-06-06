---
tags:
  - 安全
  - 风险
  - OpenClaw
aliases:
  - 安全债务
  - OpenClaw CVE
---

# OpenClaw 安全风险

> 风险类别总览和分类框架见 [[安全边界与风险（总览）]]

本笔记聚焦 OpenClaw 项目层面的**安全债务**现状。这是 [[OpenClaw 投资风险因素]] 的核心问题之一。

## 安全债务现状

- **无专职安全团队**
- **无 Bug 赏金计划**
- CVE 累计突破 **472 个**（截至 2026 年 5 月），平均每天 2.7 个新漏洞
- 存在多个严重 CVE：[[ClawJacked 远程代码执行漏洞]]（CVSS 8.8）、[[Claw Chain 四漏洞链]]（CVSS 最高 9.6）、CVE-2026-32922（CVSS 9.9）
- **245,000+ 个 OpenClaw 实例暴露在互联网上**（2026 年 5 月 Shodan + ZoomEye 数据）
- [[Prompt Injection 风险]] 无法从架构层面解决
- 恶意 Skills 供应链攻击风险持续存在——[[RankClaw ClawHub 审计|全量审计]] 确认 7.5% 恶意率

## 已知安全漏洞修复进度

OpenClaw Foundation 治理 目前缺少安全响应团队，与 Linux Foundation 等成熟项目形成鲜明对比。安全修复主要依赖社区贡献者，缺乏系统性的漏洞跟踪和响应流程。[[OpenClaw 官方安全模型]] 承认"没有完美安全的设置"，这与 [[致命三合一安全矛盾]] 的分析一致。

## 生态安全服务

围绕 OpenClaw 安全问题，已出现专门的第三方安全服务：

| 公司 | 产品 |
|------|------|
| Snyk | Skill Security Scanner + Agent Trust Hub |
| Daytona | 安全沙箱运行 |
| VirusTotal | 原生 Skills 扫描集成 |

## AI 代码生成安全

详见 [[AI 代码生成安全问题]]——45% AI 生成代码样本未通过安全测试。这与代码执行安全问题密切相关，也是沙箱机制必要性的有力佐证。

## 相关笔记

- [[安全边界与风险（总览）]]
- [[OpenClaw 投资风险因素]]
- [[OpenClaw 官方安全模型]]
- [[ClawHavoc 事件]]
- [[2026年3月安全公告汇总]] — 最新 GHSA 安全公告
- [[WebSocket 提权漏洞 GHSA-rqpp]] — CVSS 10.0 满分漏洞
- [[Claw Chain 四漏洞链]] — 2026 年 5 月最严重链式漏洞
- [[GTIG AI 生成零日攻击报告]] — AI 武器化实战确认
- [[RankClaw ClawHub 审计]] — ClawHub 全量安全审计
- [[2026年Q2安全态势总览]] — Q2 安全态势总览

## 外部链接

- [CVE-2026-25253 - NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)
- [Snyk Blog](https://snyk.io/blog/)
