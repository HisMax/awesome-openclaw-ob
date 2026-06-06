---
tags:
  - 竞品分析
  - Google
  - 浏览器自动化
aliases:
  - Project Mariner
  - Google Mariner
---

# Google Project Mariner 分析

**一句话总结**：Google 的浏览器自动化 AI 代理，基于 Gemini 2.0 模型，在 WebVoyager 基准上达到 83.5% 成功率，但刻意限制了购买等高风险操作——代表了大厂"安全优先"的 Agent 设计哲学。

## 基本信息

- **类别**：浏览器自动化 AI 代理
- **架构**：云端 VM + Chrome 扩展
- **模型**：Gemini 2.0
- **并发**：最多 **10 个**并发任务
- **发布方**：Google DeepMind
- **状态**：研究预览阶段

## 架构设计

Project Mariner 采用了一个精心设计的云-端混合架构：

- **云端 VM**：Agent 的推理和决策发生在 Google 云端的虚拟机中——这意味着用户本地设备不承担计算负担
- **Chrome 扩展**：作为浏览器端的"手"和"眼"，负责页面操作和视觉信息采集
- **通信桥**：云端 VM 和本地扩展之间通过安全连接实时同步

这个架构的核心权衡是：**安全性和可控性 > 自由度和灵活性**。对比 OpenClaw 的本地守护进程 + 消息桥接架构，Mariner 的云端方式让 Google 能够在服务端实施更严格的安全策略和行为审计。

## 基准性能

- WebVoyager 基准 **83.5% 成功率**（发布时为单代理 SOTA）
- 但竞品已经超越：**Browserable 90.4%**、**Magnitude 94%**

WebVoyager 是一个标准化的网页导航基准测试，模拟真实网页操作任务（搜索、填表、导航等）。83.5% 意味着每 6 个任务中大约有 1 个会失败——对于低风险的信息检索任务可以接受，但对于涉及金钱的操作（购物、付款）来说风险过高。

这也解释了 Mariner 为什么选择**不支持**购买操作。

## 关键限制

Mariner 明确不能完成以下操作：
- **完成购买**（不能下单、付款）
- **接受 Cookie**
- **同意服务条款**

这些限制不是技术能力不足，而是**刻意的产品决策**。Google 作为全球最大的广告公司，深知让 AI 代替用户同意服务条款和完成购买的法律风险。这与 [[案例-Tesco 超市自动购物]] 形成鲜明对比——OpenClaw 的社区用户已经在让 Agent 完成完整的购物流程，而 Google 选择了更保守的路线。

## 并发能力

支持最多 **10 个并发任务**是 Mariner 的一大亮点。对比：
- **OpenClaw**：单实例单任务（虽然可以部署多个实例）
- **Mariner**：原生支持 10 个并发，可以同时在多个标签页执行不同任务

这对效率有巨大影响——想象同时让 Agent 在 10 个不同的网站上搜集信息，而不是一个一个来。

## 核心洞察

Project Mariner 代表了大厂做 AI Agent 的典型思路：

1. **专注垂直场景**：只做浏览器自动化，不试图做通用 AI 助手。对比 OpenClaw 的"什么都能做"策略，Mariner 选择了"做好一件事"
2. **安全红线不可逾越**：宁可功能受限也不冒法律和安全风险
3. **标准化基准先行**：用 WebVoyager 83.5% 的数据说话，而非靠社区口碑。OpenClaw 至今没有标准化基准测试
4. **云端控制权**：云端 VM 架构让 Google 保留了对 Agent 行为的最终控制权，而 OpenClaw 的本地运行意味着用户拥有全部控制权——这是自主执行与人机协作模型的两个极端

## 与 OpenClaw 浏览器控制的对比

| 维度 | Mariner | OpenClaw 浏览器控制 |
|------|---------|-------------------|
| **架构** | 云端 VM + Chrome 扩展 | 本地 Playwright/Puppeteer |
| **基准** | 83.5% WebVoyager | 无标准化基准 |
| **购买操作** | 禁止 | 可以（如 Tesco 案例） |
| **并发** | 10 个任务 | 单任务 |
| **隐私** | 数据经 Google 服务器 | 数据留在本地 |
| **成本** | Google 订阅（待定） | 免费 + API 费用 |

两者定位截然不同：Mariner 是**安全可控的浏览器自动化工具**，OpenClaw 是**自由但自负风险的通用 AI 助手**。这也是 API 定价与成本分析中两种商业模式的缩影。

## 2026年Q2更新——项目关停

> **Google 于 2026.5.4 正式关停 Project Mariner**，结束了长达 17 个月的实验。

- 2026 年 3 月已有内部人员被调离 Mariner 团队的迹象
- 关停原因：截图→识别→操作的工作流速度慢、成本高、容易出错
- **技术去向**：Mariner 的核心技术被整合到 **Gemini Agent** 和 Chrome 的 **auto-browse** 功能中
- 独立工具已停止运行，但其浏览器自动化理念延续在 Google 主产品线中

## 相关对比

- [[OpenClaw vs Google Project Mariner]]——详细对比表（注：Mariner 已关停，对比仅作为历史参考）
- [[竞品对比总览]]——全景视图
- [[案例-Tesco 超市自动购物]]——OpenClaw 浏览器控制的实际案例
- [[2026年Q2竞品新入局]] — Q2 市场全景

## 外部链接

- [Google Project Mariner](https://deepmind.google/technologies/project-mariner/)（已关停）

## 来源

- [Programming Helper - Google Project Mariner](https://www.programming-helper.com/tech/google-project-mariner-ai-browser-agent-2026-autonomous-web-navigation)
- [AllAboutAI - Project Mariner](https://www.allaboutai.com/ai-agents/project-mariner/)
- [Google Blog - Gemini AI Update](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)
