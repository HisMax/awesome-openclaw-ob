# awesome-openclaw-ob

**OpenClaw 深度研究知识库** | An Obsidian-based knowledge base for OpenClaw deep research

[![Obsidian](https://img.shields.io/badge/Obsidian-Knowledge%20Base-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
[![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Notes](https://img.shields.io/badge/Notes-282-blue)](#知识库结构)
[![Wikilinks](https://img.shields.io/badge/Wikilinks-2397+-green)](#知识库结构)

---
> 佬友发帖专属：感谢LinuxDO社区～ https://linux.do/

## 中文

### 这是什么

最近两个月，OpenClaw 小龙虾的火爆确实让人 FOMO。从 1 月下旬的初露头角到 3 月的各种流派并起，信息量已经大到了让人疲惫的程度。

当热潮开始进入冷静期，反而是一次"补票上车"的最好时机。与其在焦虑中盲目跟风，不如在看清全貌后再精准入局。**没有调研，就没有发言权。**

为了帮大家建立这个"全貌"，默子花了一周时间，深度调研并梳理了所有的 OpenClaw 核心资料，制作成了这份庞大的 **Obsidian 原子化知识库**——包含 **282 篇笔记**、**2397+ 条双向链接**，覆盖 9 大主题。

> **OpenClaw** 是一个免费、开源的自主 AI Agent 框架，运行在用户本地设备上，通过 WhatsApp、Telegram、Discord 等即时通讯应用连接大语言模型来自主执行任务。

### 为什么用 Obsidian

[Obsidian](https://obsidian.md) 是一款知识管理工具，支持原子化、卡片式笔记。它的核心特性是**双链机制**——你可以在任意两个概念之间建立连接：

- 从一个点跳到另一个点，从一个概念立马查看到另一个概念
- 在 Graph View 中查看所有概念之间的关联，比如和 OpenClaw 安全相关的话题有哪些，节点图中一目了然
- 像大脑一样搭建知识网络，而不是在碎片的海洋里游泳

### 知识库结构

```
├── 01-产品与架构/     (38 篇)  核心架构、执行循环、Tool Use、沙箱等
├── 02-安全与风险/     (36 篇)  漏洞分析、CVE、安全事件、威胁模型
├── 03-竞品与市场/     (31 篇)  Claude Code、Cursor、Copilot 等竞品对比
├── 04-生态与社区/     (44 篇)  MCP 协议、插件生态、社区动态
├── 05-商业与投资/     (27 篇)  融资、市场规模、商业化路径
├── 06-趋势与未来/     (18 篇)  Agent 范式转变、2026 预测
├── 07-使用案例/       (17 篇)  真实案例复盘与分析
├── 08-基础概念/       (54 篇)  AI Agent、LLM、MCP 等基础知识
└── 09-人物与事件/     (15 篇)  关键人物与标志性事件
```

### 如何使用

1. 克隆仓库

```bash
git clone https://github.com/HisMax/awesome-openclaw-ob.git
```

2. 用 [Obsidian](https://obsidian.md) 打开文件夹作为 Vault
3. 从 `OpenClaw 知识库.md` 开始，沿双链自由探索
4. 打开 Graph View 查看全局知识图谱

### 推荐入口

- **架构**：`Agent-Flow-Loop 原理` → `Agent Execution Loop` → `Tool Use 机制`
- **安全**：`安全边界与风险（总览）` → `致命三合一安全矛盾` → `ClawHavoc 事件`
- **竞品**：`竞品对比总览` → `Claude Code 分析` → `Cursor 分析`
- **趋势**：`2026 Agent 元年` → `Agent 范式转变` → `半人马阶段理论`

---

## English

### What is this

An **Obsidian-based atomic knowledge base** for deep research on **OpenClaw** — an open-source autonomous AI Agent framework. Contains **282 notes** with **2397+ bidirectional links** across 9 topics: architecture, security, competitors, ecosystem, business, trends, use cases, concepts, and key figures.

> **OpenClaw** is a free, open-source autonomous AI Agent framework that runs locally on user devices, connecting to LLMs via messaging apps (WhatsApp, Telegram, Discord) to autonomously execute tasks.

### How to use

1. Clone the repo

```bash
git clone https://github.com/HisMax/awesome-openclaw-ob.git
```

2. Open the folder as a Vault in [Obsidian](https://obsidian.md)
3. Start from `OpenClaw 知识库.md` and follow the wikilinks
4. Use Graph View to explore the knowledge graph

### Repository structure

| Directory | Count | Topic |
|-----------|-------|-------|
| `01-产品与架构` | 38 | Core architecture, execution loop, sandboxing |
| `02-安全与风险` | 36 | Vulnerabilities, CVEs, security incidents |
| `03-竞品与市场` | 31 | Claude Code, Cursor, Copilot comparisons |
| `04-生态与社区` | 44 | MCP protocol, plugins, community |
| `05-商业与投资` | 27 | Funding, market size, monetization |
| `06-趋势与未来` | 18 | Agent paradigm shift, 2026 predictions |
| `07-使用案例` | 17 | Real-world case studies |
| `08-基础概念` | 54 | AI Agent, LLM, MCP fundamentals |
| `09-人物与事件` | 15 | Key figures and landmark events |

---

## Contributing

欢迎贡献！提交 Issue 或 Pull Request 即可。请保持中文写作风格一致，使用 `[[双链]]` 语法引用其他笔记。

Contributions welcome! Submit an Issue or Pull Request. Please maintain consistent Chinese writing style and use `[[wikilink]]` syntax for cross-references.

## License

本知识库采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可证。

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Star History

如果这个知识库对你有帮助，请给一个 ⭐ Star！

If you find this knowledge base helpful, please give it a ⭐ Star!
