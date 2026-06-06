---
title: Docker 容器化
aliases: [Docker 部署, OpenClaw 容器化, Docker 沙箱, Docker 容器化部署]
date: 2026-03-14
tags:
  - Docker
  - 容器化
  - 沙箱
  - 部署
  - 安全
  - 隔离
  - OpenClaw
category: 技术基础
status: complete
---

# Docker 容器化


![[assets/docker.jpg]]

## 一句话理解

> 你的程序需要各种依赖——Python 3.11、某个库的特定版本、特定配置……Docker就是**给每个程序一个独立的小房间**，里面装好它需要的一切。房间之间互不干扰，搬到哪台电脑上都能直接用。

## Docker核心概念

- **镜像（Image）**：程序的"蓝图"，包含代码、依赖、配置的只读模板
- **容器（Container）**：镜像的运行实例，就是那个"小房间"
- **Dockerfile**：构建镜像的说明书
- **Docker Compose**：管理多个容器协同工作的编排工具

## 在OpenClaw中的两个角色

### 角色一：部署

Docker让[[OpenClaw 是什么|OpenClaw]]的部署变得标准化：
- 将整个OpenClaw环境打包成镜像，任何支持Docker的服务器都能运行
- 通过Docker Compose一键启动所有服务（Agent、API、数据库等）
- 环境一致性：开发、测试、生产环境完全相同，消除"在我机器上能跑"问题
- 云端部署推荐方案：DigitalOcean 1-Click、Cloudflare moltworker、Fly.io 容器

### 角色二：沙箱（Sandbox）

这是Docker在Agent安全中更关键的角色——为 [[沙箱机制]] 提供隔离环境：
- Agent生成的代码在容器内执行，**即使代码有恶意行为，也无法影响宿主机**
- 每次执行可以创建全新容器，用完即销毁
- 通过资源限制（CPU、内存、网络）防止Agent滥用系统资源
- 2026 年 Docker 推出 **Docker Sandboxes**（microVM），硬件级隔离

## OpenClaw 安全现状

Docker 本应提供隔离，但 OpenClaw 默认关闭容器隔离——把安全工具当便利工具用，这与 [[沙箱机制]] 的设计初衷形成了讽刺性的反差。沙箱是 OpenClaw 安全体系的核心防线——但**默认关闭**，需手动开启。这个设计决策引发了大量安全争议：

- **40,000+** 个 OpenClaw 实例直接暴露公网，后续扫描总计 **135,000+**
- **93.4%** 存在认证绕过条件
- CVE-2026-25253 的攻击链包含"逃出 Docker 容器"这一步骤

多 Agent 部署中 Docker 是标准实践。Jesse Genet 用多台 Mac Mini 做物理隔离，MFS Corp 用 Proxmox 容器化运行 6 个 Agent。配置示例中 `"sandbox": { "mode": "always" }` 可强制所有命令在容器内执行。

Kaspersky 建议："使用专用备用计算机或 VPS，不要在主要计算机上安装。" Docker 是实现这一建议的最低成本方案。

## 容器 vs 微虚拟机

2026年Docker推出了**Docker Sandboxes**，专门为 AI Agent 设计：

| 特性 | 传统容器 | Docker Sandboxes（microVM） |
|------|---------|---------------------------|
| 隔离级别 | 共享宿主内核 | 独立内核+虚拟机 |
| 安全性 | 内核漏洞可能逃逸 | 硬件级隔离 |
| Docker能力 | 需Docker-in-Docker | 私有Docker守护进程 |
| 适用场景 | 可信代码 | AI Agent不可预测代码 |

### 2026 年中更新

Docker Sandboxes 已正式支持 Claude Code、Gemini、Codex 等主流编码 Agent 的沙箱运行。新增能力：
- **网络隔离策略**：allow/deny 列表精细控制 Agent 网络访问
- **Docker AI Governance**：集中控制 Agent 执行方式、网络可达性、凭证使用和 MCP 工具调用权限
- **NanoClaw 集成**：Docker 与 [[NanoClaw]] 联合提供可信 Agent 安全方案

Docker 自身记录了 2024.10-2026.02 期间至少 **10 起** 因 Agent 缺乏隔离边界导致的公开安全事件（涉及 6 个主流 AI 编码工具）。

### 替代隔离技术

Docker 容器并非唯一方案，2026 年的 Agent 隔离技术栈还包括：
- **Firecracker microVMs**：AWS 开源的轻量级虚拟机
- **gVisor**：用户态内核，Google 出品
- **Kata Containers**：结合 VM 安全性与容器速度
- **Kubernetes Agent Sandbox**：为生产 AI Agent 工作负载提供编排层

## 容器化对Agent安全的意义

1. **爆炸半径控制**：Agent出错只影响容器内部，宿主系统无恙
2. **快速恢复**：容器出问题？删掉重建，几秒钟的事
3. **网络隔离**：通过白名单/黑名单控制容器能访问哪些网络资源
4. **审计追踪**：容器内的所有操作都可以被记录和审计
5. **权限最小化**：容器内只给Agent最必要的权限，遵循最小特权原则

## 与 [[代码执行安全]] 的关系

Agent执行代码时的安全防线：
- 第一层：代码审查（静态分析）
- 第二层：**容器隔离**（Docker/microVM）
- 第三层：权限控制（文件系统、网络、系统调用限制）
- 第四层：监控告警（异常行为检测）

## 关键洞察

Docker 沙箱揭示了 OpenClaw 的核心矛盾：**安全性与实用性的永恒拉锯**。Aikido.dev 的评价一针见血——"尝试保护 OpenClaw 是荒谬的。全面强化基本上把它变成了带额外编排的 ChatGPT。它只在危险时才有用。" 沙箱默认关闭的设计选择，本质上是 OpenClaw 在"有用"和"安全"之间选择了前者。Docker Sandboxes（microVM）代表了新方向——不再共享宿主内核，而是提供硬件级隔离——但这对 [[致命三合一安全矛盾]] 只是缓解而非根治。

## 外部链接

- [Docker 官方网站](https://docker.com)

## 双链导航

- [[沙箱机制]] — Docker是实现沙箱的主要技术手段
- [[代码执行安全]] — 容器化是代码安全执行的关键防线
- [[OpenClaw 是什么]] — Docker在OpenClaw部署和安全中的双重角色
- [[安全边界与风险（总览）]] — 容器化在安全体系中的位置
- [[权限控制机制]] — 容器内的权限最小化
- [[致命三合一安全矛盾]] — 沙箱无法解决的根本性安全挑战
- [[ClawJacked 远程代码执行漏洞]] — 攻击链包含容器逃逸
- [[ClawHub 安全整改措施]] — 恶意 Skills 在沙箱中的行为
- [[自主决策循环]] — 工具执行阶段的沙箱隔离
- [[CI CD 流水线]] — Docker 镜像构建与持续集成流水线的协同
- [[Operator Install Policy]] — v2026.6 引入的安装时安全策略，与运行时沙箱互补
