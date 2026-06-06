---
tags:
  - 安全
  - 恶意软件
  - AMOS
  - ClawHub
  - macOS
  - 供应链攻击
aliases:
  - Atomic Stealer
  - AMOS ClawHub
  - What Would Elon Do
---

# Atomic Stealer 通过 ClawHub 分发

**一句话总结**：ClawHub 下载量第一的热门 Skill "What Would Elon Do?" 实际上是 Atomic Stealer (AMOS) 恶意软件的分发载体，能窃取 SSH 密钥、加密钱包、浏览器 Cookie 并开启反向 Shell。

## 事件详情

**1Password 研究员**发现 [[恶意 Skills 供应链攻击|ClawHub]] 下载量最高的 Skill——**"What Would Elon Do?"**——实际上会导致安装 **Atomic Stealer (AMOS)**，一种针对 macOS 的高级信息窃取恶意软件。

**Cisco AI Defense 团队**独立验证确认该 #1 Skill 的恶意行为。Trend Micro 随后发布了详细技术分析报告。

## 技术分析

### AMOS 的窃取能力

该恶意 Skill 在 [[OpenClaw 安全风险|OpenClaw]] 的受信自动化上下文中执行后，AMOS 能够：

| 窃取目标 | 具体内容 |
|----------|---------|
| **SSH 密钥** | `~/.ssh/` 下的所有密钥对 |
| **加密钱包** | MetaMask、Phantom、多种硬件钱包的凭证 |
| **浏览器 Cookie** | Chrome、Safari、Firefox 的会话数据 |
| **反向 Shell** | 建立持久化远程控制通道 |

### 为什么特别危险

1. **受信环境执行**：用户安装 Skill 时信任 ClawHub 平台，不会像下载可执行文件那样警惕
2. **AI Agent 权限**：Skill 继承了 Agent 的所有系统权限——文件访问、网络通信、命令执行
3. **社会工程效果**：伪装为热门/有趣的 Skill，利用下载排名制造虚假信任
4. **平台零审核**：[[Snyk ToxicSkills 研究报告|Snyk 研究]] 证实 ClawHub 发布仅需 1 周 GitHub 账户，无代码审查

### 攻击链

```
用户浏览 ClawHub → 看到 #1 热门 Skill
  → 安装 "What Would Elon Do?"
    → Skill 在 Agent 上下文中执行
      → 静默安装 AMOS
        → 窃取 SSH 密钥、加密钱包、浏览器数据
          → 开启反向 Shell → 持久化远程控制
```

## 与供应链攻击生态的关联

> Flare 评估："当前已确认的风险模式——恶意 Skill 分发 → 受信自动化上下文中执行 → 凭证/会话/数据外泄——**已经足够危险**。"

该事件完美印证了 [[Snyk ToxicSkills 研究报告]] 中 36.82% Skills 有漏洞、341 个恶意 Skill 的统计发现。它也是 [[暗网讨论分析]] 中 Flare 收集到的 193 条 Skills 安全讨论的核心案例。

## 教训与洞察

- **排名 ≠ 安全**：下载量第一不代表经过安全审核，可能正相反——恶意攻击者刻意刷排名
- **macOS 用户同样面临严重威胁**：AMOS 专门针对 macOS 生态，打破了"Mac 更安全"的错觉
- **AI Agent Skills 是新的攻击载体**：类似浏览器扩展和 npm 包的信任模型缺陷
- 企业安全团队应将 ClawHub Skills 纳入[[安全最佳实践|软件供应链审计]]范围

## 相关笔记

- [[恶意 Skills 供应链攻击]]
- [[Snyk ToxicSkills 研究报告]]
- [[ClawHub 安全整改措施]]
- [[暗网讨论分析]]
- [[凭证泄露与信息窃取]]
- [[代码执行安全]]
- [[RankClaw ClawHub 审计]] — 全量审计进一步量化恶意 Skill 规模
- [[GTIG AI 生成零日攻击报告]] — 国家级行为者利用 Skill 生态
- [[2026年Q2安全态势总览]] — Q2 供应链安全态势

## 外部链接

- [Snyk Blog - ToxicSkills Research](https://snyk.io/blog/)
- [Hudson Rock Threat Intelligence](https://hudsonrock.com)
