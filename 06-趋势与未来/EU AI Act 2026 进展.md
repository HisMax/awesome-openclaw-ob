---
tags:
  - 监管
  - EU-AI-Act
  - 合规
  - 趋势
  - 2026Q2
aliases:
  - EU AI Act 2026
  - 欧盟AI法案
  - 高风险AI系统
  - Digital Omnibus
---

# EU AI Act 2026 进展

> **一句话总结**：EU AI Act 的高风险 AI 系统条款原定 2026 年 8 月 2 日生效，但 78% 的企业尚未做好准备——于是欧盟在 5 月 7 日通过 Digital Omnibus 修正案将部分期限推迟至 2027/2028 年。违规罚款最高 3,500 万欧元或 7% 全球营收，超过 GDPR 的处罚力度。对 OpenClaw 而言，这意味着企业客户将更加重视 Agent 的可审计性和人工监督机制。

## 核心时间线

| 日期 | 事件 | 状态 |
|------|------|------|
| 2024.8.1 | EU AI Act 正式生效 | 已生效 |
| 2025.2.2 | 禁止不可接受风险的 AI 系统 | 已执行 |
| 2025.8.2 | 通用 AI（GPAI）模型规则生效 | 已执行 |
| **2026.8.2** | **高风险 AI 系统条款生效**（原定） | 延期中 |
| 2026.5.7 | Digital Omnibus 修正案政治协议 | 已达成 |
| 2026.12.2 | 水印义务生效（修正后） | 待正式通过 |
| 2027.12.2 | Annex III 高风险系统新期限（修正后） | 待正式通过 |
| 2028.8.2 | Annex I 高风险系统新期限（修正后） | 待正式通过 |

## 高风险系统条款要求

原定 2026 年 8 月 2 日生效的条款要求高风险 AI 系统的提供者和部署者满足以下义务：

### 技术文档

| 要求 | 详情 |
|------|------|
| 完整技术文档 | 系统架构、训练数据、测试方法、性能指标 |
| 一致性评估 | 由认证机构或自我评估完成 |
| CE 标志 | 通过评估后加贴 |
| EU 数据库注册 | 高风险系统必须注册到欧盟 AI 系统数据库 |

### 结构化人工监督

高风险 AI 系统必须设计为允许自然人进行有效监督：

- **开环架构**：人类可以在 AI 做出决策前介入
- **控制机制**：操作员可以随时中断或覆盖 AI 决策
- **可解释性**：系统必须能向人类解释其决策逻辑

### 对 AI Agent 的特殊挑战

自主 AI Agent 在这些要求下面临独特困难：

| 挑战 | 说明 |
|------|------|
| **透明性** | 接收方是否有权知道对方是 AI Agent？ |
| **高风险分类** | 控制财务、家居、医疗的 Agent 是否属于高风险？ |
| **责任归属** | Agent 造成损失，是用户、开发者还是模型提供商负责？ |
| **持续监控** | 长时运行 Agent 如何满足"实时人工监督"要求？ |

## 违规处罚

EU AI Act 的罚款力度超过 GDPR：

| 违规类型 | 最高罚款 |
|----------|----------|
| 使用禁止的 AI 实践 | 3,500 万欧元 或 7% 全球年营收（取高者） |
| 违反高风险系统义务 | 1,500 万欧元 或 3% 全球年营收 |
| 提供不正确信息 | 750 万欧元 或 1% 全球年营收 |

对比 GDPR 的最高 2,000 万欧元 / 4% 营收，EU AI Act 在处罚上更为严厉。

## Digital Omnibus 修正案（2026.5.7）

### 背景

2026 年 5 月 7 日，欧盟理事会和欧洲议会就 Digital Omnibus 修正案达成政治协议。修正案由欧盟委员会于 2025 年底提出，核心目标是"简化和精简" AI Act 规则。

### 延期方案

修正案采用两级延期结构：

| 类型 | 原期限 | 新期限 | 延期时长 |
|------|--------|--------|----------|
| **Annex III 系统**（独立高风险 AI） | 2026.8.2 | 2027.12.2 | 16 个月 |
| **Annex I 系统**（嵌入受监管产品的 AI） | 2026.8.2 | 2028.8.2 | 24 个月 |
| **水印义务**（Article 50(2)） | 2026.8.2 | 2026.12.2 | 4 个月 |

### 新增禁止事项

修正案还新增了一项禁止条款：
- 禁止使用 AI 系统生成未经同意的亲密影像（NCII）和儿童性虐待材料（CSAM），包括所谓"nudifiers"

### 法律状态

**重要**：2026 年 5 月 7 日达成的是**临时政治协议**。在共同立法者正式认可和通过之前，它不具有法律效力。鉴于原定 8 月 2 日期限的紧迫性，预计立法流程将加速进行。

但 Latham & Watkins 等律所的建议很明确：在 Omnibus 正式颁布之前，基于预期延期而暂停合规工作是重大法律风险。

## 合规现状：触目惊心

| 指标 | 数值 | 来源 |
|------|------|------|
| 未采取实质合规步骤的组织 | **78%** | 2026.4 |
| 缺乏基本 AI 资产清单的组织 | **50%+** | ai2.work, 2026.2 |
| 风险分类不明确的 AI 系统 | **40%** | appliedAI 对 106 个企业系统的研究 |

78% 的企业在距离期限不到 4 个月时仍未做好准备——这正是 Omnibus 修正案出台的直接原因。延期不是"宽容"，而是承认现实：行业需要更多时间来建立合规基础设施。

## Anthropic Mythos 与跨大西洋博弈

EU AI Act 的讨论不是在真空中发生的——[[Anthropic Series H 融资|Anthropic]] 的 Mythos 模型引发的跨大西洋安全争议为监管讨论增添了地缘政治维度：

### 事件时间线

| 日期 | 事件 |
|------|------|
| 2026.4.7-8 | Anthropic 发布 Claude Mythos Preview（可发现零日漏洞） |
| 2026.5 中旬 | EU 与 Anthropic 关于 Mythos 测试安排的谈判停滞 |
| 2026.5.29 | EU 官员呼吁"加强"与美国在前沿 AI 模型上的对话 |
| 2026.6.1 | Anthropic 同意向 ENISA 提供 Mythos 访问权（Project Glasswing） |

### 核心争议

Anthropic 告诉欧盟委员会，欧盟需要**先获得美国政府许可**才能测试 Mythos。这引发了一系列问题：
- 前沿 AI 模型是否应被视为"战略资产"？
- 非美国政府的 AI 安全测试权利如何保障？
- EU AI Act 的管辖权是否延伸到在欧洲部署的美国 AI 模型？

最终，Anthropic 通过 Project Glasswing 向 ENISA（欧盟网络安全局）提供了 Mythos 访问权，ENISA 成为首个加入该项目的欧盟机构。

## 对 OpenClaw 的影响

EU AI Act 对 OpenClaw 生态有多层影响：

### 直接影响

| 层面 | 影响 |
|------|------|
| **OpenClaw 本身** | 如果 OpenClaw 被部署于欧盟高风险场景（金融、医疗、教育），需满足 Annex III 合规要求 |
| **Skills 生态** | [[ClawHub 官方技能注册表|ClawHub]] 中的 Skills 如果处理个人数据，可能触发 GDPR + AI Act 双重合规 |
| **企业用户** | 欧盟企业使用 OpenClaw 需确保 Agent 行为可审计、可中断、可解释 |

### 间接影响

| 层面 | 影响 |
|------|------|
| **MCP 治理** | EU AI Act 推动 [[MCP 2026年Q2进展|MCP]] 加速治理标准化（Server Cards 等） |
| **NIST 联动** | EU 标准与 [[NIST AI Agent 安全标准|NIST AI Agent 标准]] 可能形成大西洋两岸的监管夹击 |
| **商业机会** | 合规需求创造了 [[企业级整合方案|企业级合规工具]] 的市场空间 |

### 78% 未合规 = OpenClaw 的机会

78% 的企业未做好 AI Act 合规准备，意味着巨大的市场空间。如果 OpenClaw 能内置合规功能（审计日志、人工监督接口、决策解释），它可以成为企业合规的"安全通道"而非"合规风险"。

## 关键洞察

### 1. 延期不等于放松

Digital Omnibus 延期 16-24 个月，但**没有降低合规标准**——所有要求原封不动，只是给了更多准备时间。企业如果把延期当作"不用管了"的信号，将在 2027-2028 年面临更大的合规压力。

### 2. AI Agent 的监管灰区

EU AI Act 的高风险分类是基于"用途"而非"技术"的。同一个 AI Agent 用于客服（低风险）和医疗诊断（高风险）会有完全不同的合规要求。这种"按用途分类"的模式对 OpenClaw 这类通用 Agent 框架构成了分类挑战。

### 3. GDPR 的教训

GDPR 在 2016 年通过、2018 年生效时，大量企业也是"赶工合规"。但 GDPR 最终成为全球隐私标准的事实表明：EU 的监管框架虽然痛苦但有效。EU AI Act 可能走同样的路——短期阵痛，长期受益。

### 4. 跨大西洋 AI 治理裂痕

Mythos 事件暴露了美国和欧盟在前沿 AI 治理上的根本分歧：美国倾向于"创新优先、安全跟进"，欧盟倾向于"安全优先、创新在框架内"。这个裂痕将持续影响全球 AI Agent 的部署和监管格局。

## 相关笔记

- [[AI Agent 安全监管趋势]] — 全球 AI Agent 监管总览
- [[NIST AI Agent 安全标准]] — 美国标准化动向
- [[AI Agent 市场趋势 2026 Q2]] — 市场与监管的交叉
- [[安全边界与风险（总览）]] — Agent 安全风险
- [[Anthropic 公司分析]] — Mythos 争议的主体

## 外部链接

- [EU AI Act 实施时间线](https://artificialintelligenceact.eu/implementation-timeline/)
- [Latham & Watkins AI Act 延期分析](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines)
- [White & Case Digital Omnibus 分析](https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules)
- [欧盟理事会 Omnibus 公告](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [CNBC Mythos 跨大西洋报道](https://www.cnbc.com/2026/05/29/mythos-ai-models-eu-talks-us.html)

> 来源：EU AI Act 官网、Latham & Watkins、White & Case、Hogan Lovells、CNBC、GLACIS，2026 年 Q2
