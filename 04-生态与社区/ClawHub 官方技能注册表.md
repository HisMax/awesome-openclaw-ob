---
tags:
  - 生态系统
  - Skills市场
  - OpenClaw
aliases:
  - ClawHub
  - 技能注册表
  - Skills Registry
---

# ClawHub 官方技能注册表

ClawHub 是 [[OpenClaw 是什么|OpenClaw]] 的官方 [[Skills 市场]] 平台，类似于 npm 或 VS Code Extensions。

## 核心数据

| 指标 | 数值 |
|------|------|
| 总技能数（ClawHavoc前） | 5,705 |
| 清理后总技能数 | 3,286（删除 2,419 个可疑 Skills） |
| 精选技能（去重去恶意后） | 2,868 |
| 已标记恶意技能 | 341（感染率 12%，详见 [[恶意 Skills 供应链攻击]]） |
| 总下载量 | 150 万+ |
| 安装方式 | `npx clawhub@latest install <skill-slug>` |

Skills 通过 Tool Use 机制与 Agent 交互，每个 Skill 本质上是一组工具定义，遵循 MCP 协议标准。

## 安装位置

- 全局：`~/.openclaw/skills/`
- 工作空间：`<project>/skills/`

## 技能分类分布（精选 2,868 个）

| 类别 | 数量 |
|------|------|
| AI & LLMs | 287 |
| 搜索 & 研究 | 253 |
| DevOps & Cloud | 212 |
| Web & 前端 | 202 |
| 营销 & 销售 | 143 |
| 浏览器 & 自动化 | 139 |
| 生产力 & 任务 | 135 |
| 通讯 | 133 |
| 编码代理 & IDE | 133 |
| CLI 工具 | 129 |
| 笔记 & PKM | 100 |
| 媒体 & 流媒体 | 80 |
| 交通出行 | 76 |
| Git & GitHub | 66 |
| 图像 & 视频生成 | 60 |
| 智能家居 & IoT | 56 |

## 2026 年 3 月更新

截至 2026 年 3 月，ClawHub 的 GitHub 仓库已获得 **6,700+ Stars**，累计 **831 commits**。技术栈采用 OpenAI embeddings + Convex 向量搜索。此外：

- **onlycrabs.ai** — SOUL.md 人设文档注册表，为 Agent 提供标准化的人设定义方式
- 裸命令安装（bare command install）现优先选择 ClawHub 而非 npm，进一步巩固了 ClawHub 作为 Skills 首选分发渠道的地位
- **v2026.3.22**：[[ClawHub 原生安装]] 正式发布——`openclaw skills search|install|update` 命令流程、`clawhub:<package>` 安装、Claude Marketplace 注册表集成
- **v2026.3.22**：[[Marketplace 安装范围验证]] 引入——远程清单条目范围验证、外部源拒绝、owner 感知注册

## 相关事件

[[ClawHavoc 事件]] 后进行了大规模安全整改，详见 [[ClawHub 安全整改措施]]。

## 相关链接

- [[热门 Skills 排行]]
- [[ClawHavoc 事件]]
- [[ClawHub 安全整改措施]]
- [[ClawHub 原生安装]] — v2026.3.22 的原生安装机制
- [[Marketplace 安装范围验证]] — 安装安全验证

## 外部链接

- [ClawHub](https://clawhub.dev)
- [npm](https://npmjs.com)
- [OpenClaw GitHub](https://github.com/anthropics/openclawx)

> 来源：[ClawHub GitHub](https://github.com/openclaw/clawhub) | [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
