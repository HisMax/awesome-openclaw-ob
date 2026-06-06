---
tags:
  - 人物
  - AI领袖
  - Anthropic
  - Claude
  - Agent安全
aliases:
  - Amodei
  - Anthropic CEO
---

# Dario Amodei

> **一句话总结**：Anthropic CEO，提出"半人马阶段"理论（人+AI 组合当前最强），Claude 背后的决策者，在 AI 安全与商业化之间走钢丝。

## 核心要点

- 提出 **"半人马阶段"（centaur phase）** 理论：人 + AI Agent 的组合是当前最强大的单元
- 领导 Anthropic 达到 $380 亿估值（Series G），[[Claude Code]] 年化营收 **$25 亿**（2026.2）
- 推动 [[Constitutional AI]] 安全框架，但因商标执法引发社区争议
- 将 MCP（Model Context Protocol）捐赠给 [[AAIF 基金会]]，月 SDK 下载 9700 万+

## 详细内容

### 半人马阶段理论（2026.2.23，Axios 报道）

> "人类检查 AI 的走法可以击败独立的 AI 或人类，但机器后来完全超越了这种安排。"

Amodei 以国际象棋为类比：15-20 年前，人机组合（"半人马"）可以击败纯 AI 或纯人类。他警告这个窗口期可能"**非常短暂**"。这与 [[Andrej Karpathy]] 的"Agent 十年"论形成有趣的对比：

- Karpathy：Agent 需要十年才能独立工作
- Amodei：人机协作阶段存在，但窗口期正在关闭

### Claude 生态的商业数据

| 指标 | 数值（2026.2） | 最新数值（2026.5-6） |
|------|------|------|
| Claude Code 年化营收 | **$25 亿**（翻倍增长） | 维持高速增长，企业占比超 50% |
| Anthropic 年化总营收 | — | **$300 亿+**（2026.4，Amodei 称超自身预测 8 倍） |
| Anthropic 估值 | **$380 亿**（Series G） | **$9,650 亿**（Series H，2026.5.28） |
| SWE-bench Verified（Opus 4.6） | **80.8%**（最高） | — |
| VS Code 日安装量 | 2900 万 | — |
| 企业订阅占比 | 超过 50% | — |

[[Claude Code 营收分析]] 详述了 Claude Code 的增长，半人马理论的最佳证明就是 Claude Code 营收翻倍：人+AI 确实更强。

### Series H 融资与近万亿估值（2026.5-6）

2026.5.28，Anthropic 完成 **$650 亿 Series H** 融资，估值达 **$9,650 亿**，首次超越 OpenAI（$8,520 亿）。领投方为 Altimeter Capital、Dragoneer、Greenoaks、Sequoia Capital，联合领投方包括 Capital Group、Blackstone、Brookfield。

这可能是 IPO 前的最后一轮私募融资——Anthropic 已于 **2026.6.1 向 SEC 秘密提交 IPO 申请**，目标 2026 年 10 月上市。估值在约 3 个月内从 $380 亿翻了超过 2.5 倍，万亿美元门槛近在咫尺。

### Claude Mythos 模型与 Project Glasswing（2026.4-6）

2026.4.7，Anthropic 发布 **Claude Mythos Preview**——一个在网络安全任务上表现极为突出的新型模型。Mythos 在测试中发现了"每个主流操作系统和每个主流浏览器"中的漏洞。

Anthropic 为此启动了 **Project Glasswing**，利用 Mythos 帮助保护全球关键软件。2026.6.2，Glasswing 扩展至 **15+ 个国家的 150 个组织**，已发现超过 **10,000 个**高危或关键安全漏洞。Anthropic 确认计划在数周内向公众开放 Mythos 级别模型。

Mythos 的发布与 [[GTIG 首次确认 AI 生成零日事件]] 形成了攻防两面：AI 既是攻击工具也是防御工具。

### Andrej Karpathy 加入（2026.5.19）

[[Andrej Karpathy]] 宣布加入 Anthropic 预训练团队（Nick Joseph 领导），专注于用 Claude 加速预训练研究。这位 OpenAI 联合创始人、曾公开批评 AutoGPT 类 Agent "根本不工作"的人，选择了 Anthropic 而非回到 OpenAI——这对 Amodei 的人才战略是重大胜利。

### 与 OpenClaw 的微妙关系

Amodei 领导的 Anthropic 对 [[OpenClaw]] 的商标执法（"Clawd"与"Claude"过于相似）产生了连锁反应：

1. 发出商标通知迫使改名 → 引发 [[The Great Molt 改名事件]]
2. [[DHH 对 Anthropic 的批评|DHH 公开批评]]为"customer hostile"
3. 创始人 Steinberger 最终加入了 **OpenAI** 而非 Anthropic
4. 讽刺之处：OpenClaw 是 Claude API 最大的付费流量来源之一

### OAuth 封杀争议（2026.1-2）

Anthropic 部署服务端检测，封杀所有第三方工具使用 Claude 订阅 OAuth 令牌。部分 Max $200/月用户因误触滥用过滤器被封号。George Hotz 警告："你不会把人赶回 Claude Code，你只会把他们赶向其他模型提供商。"

### MCP 捐赠与 AAIF

Mike Krieger（Anthropic CPO）代表公司将 MCP 捐赠给 Linux Foundation 旗下的 [[AAIF 基金会]]：

> "Donating MCP to the Linux Foundation ensures it stays open, neutral, and community-driven as it becomes critical infrastructure for AI."

MCP 已有 **9700 万+月 SDK 下载**和 **10,000+ 活跃服务器**，成为 Agent 工具连接的事实标准。

## 关键洞察

Amodei 的战略困境在于：他既要推动 Claude 的商业化（年化营收从 2026.4 的 $300 亿+飙升至 Series H 时的 $470 亿+），又要维护 AI 安全的品牌形象（[[Constitutional AI]]、Project Glasswing）。商标执法事件暴露了这种张力——保护品牌的合理行为，却被社区解读为对开源生态的敌意，最终将 [[Peter Steinberger]] 和整个 OpenClaw 生态推向了竞争对手 [[Sam Altman|OpenAI]]。但 2026 年中期的格局正在逆转：[[Andrej Karpathy]] 加入 Anthropic、近万亿估值超越 OpenAI、Mythos 模型在安全领域的突破，都在重塑 Anthropic 的竞争地位。半人马阶段理论本身是深刻的，但它也隐含了一个不安的预测：人类的"必要性"窗口正在关闭。

## 外部链接

- [Anthropic 公司官网](https://anthropic.com/company)
