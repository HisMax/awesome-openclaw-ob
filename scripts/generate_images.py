#!/usr/bin/env python3
"""批量生成知识库配图 - 基于模板参考图 + Bltcy API"""

import json, base64, os, sys, time, re, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/Users/mozi/projects/09-OpenClaw知识库")
ASSETS = ROOT / "assets"
TEMPLATE = ASSETS / "template-base.png"
API_URL = "https://api.bltcy.ai/v1/images/generations"
API_KEY = os.environ.get("BLTCY_API_KEY", "")
MAX_WORKERS = 4

with open(TEMPLATE, "rb") as f:
    TPL_B64 = base64.b64encode(f.read()).decode()

COMMON_STYLE = """风格要求：高端年报/咨询报告风格，奶油白底（#FAF7F2），深炭灰文字（#2D2D2D），橄榄绿（#6B7B5E）和陶土色（#B8845C）作为强调色。卡片背景 #F0EDE8。绝对不要蓝色、红色、紫色、科技感、赛博风、连线图、发光效果。"""

IMAGES = [
    # === 01-产品与架构 (12张) ===
    ("01-产品与架构/OpenClaw 是什么", "openclaw-what-is",
     "标题「OpenClaw 是什么」副标题「开源 AI Agent 平台」。三个大卡片纵向排列：(1) 核心定位 — 多频道 AI Agent 操作系统，13+ 通讯平台接入 (2) 关键能力 — 模型无关、持久记忆、语音交互、浏览器控制、Skills 插件 (3) 关键数据 — 375K Stars、320万月活、1,200+ 贡献者、MIT 开源"),

    ("01-产品与架构/OpenClaw v2026.4 版本更新", "v2026-4-update",
     "标题「OpenClaw v2026.4 版本更新」副标题「从平台到运行时」。时间线纵向排列五个版本节点：v2026.4.2 TaskFlow 编排层 → v2026.4.7 Memory-Wiki → v2026.4.15 Model Auth Card → v2026.4.22 Claw Chain 修复 → v2026.4.25 Google Meet 集成。用橄榄绿圆点串联时间线"),

    ("01-产品与架构/OpenClaw v2026.5 版本更新", "v2026-5-update",
     "标题「OpenClaw v2026.5 版本更新」副标题「稳定性月」。四个卡片：(1) 渠道可靠性 — Telegram/Discord/QQ 加固 (2) 性能优化 — Gateway 懒加载、/models 4100x 提速 (3) 语音管道 — Google Meet + Twilio + Discord Voice (4) 核心瘦身 — WhatsApp/Slack/Bedrock 移出默认安装"),

    ("01-产品与架构/OpenClaw v2026.6 版本更新", "v2026-6-update",
     "标题「OpenClaw v2026.6 版本更新」副标题「治理月」。三层架构图（从上到下）：第一层「Auto Mode 三层审批」— 策略匹配 → 模型审核 → 人工兜底。第二层「Operator Install Policy」— 运营者自定义安装策略。第三层「Skill Workshop」— 降低 Skill 创建门槛"),

    ("01-产品与架构/记忆系统", "memory-system",
     "标题「OpenClaw 记忆系统」副标题「四层记忆架构」。四个水平层级从上到下：(1) Active Memory — 当前会话上下文 (2) Long-term Memory — SQLite + 向量嵌入 (3) Memory-Wiki — 结构化声明+证据+矛盾检测 (4) People-Aware Memory — 人物关系感知。层与层之间用细虚线分隔"),

    ("01-产品与架构/Plugin 扩展系统", "plugin-system",
     "标题「Plugin 扩展系统」。左右两栏：左栏「插件类型」列表 — Provider 插件、Channel 插件、Tool 插件、Skill 插件。右栏「生态数据」— ClawHub 13,000+ 技能、npm 77万周下载、Operator Install Policy 安全管控"),

    ("01-产品与架构/模型无关架构", "model-agnostic",
     "标题「模型无关架构」副标题「6 种 Provider 热切换」。一个中心节点「OpenClaw Gateway」周围环绕六个模型卡片（不要连线，用空间关系表达）：Claude / GPT / DeepSeek / Gemini / Ollama / Qwen。每个卡片标注一行特点"),

    ("01-产品与架构/自主执行与人机协作", "human-ai-collab",
     "标题「自主执行与人机协作」。三列对比：(1) YOLO 模式 — 全自主，风险高 (2) Auto Mode — 策略→模型→人工三层 (3) 审批模式 — 每步确认，效率低。中间列用橄榄绿强调为推荐方案"),

    ("01-产品与架构/多Agent协作架构", "multi-agent",
     "标题「多 Agent 协作架构」。三个卡片：(1) Durable TaskFlow — 持久化多步工作流 (2) Workboard — 编排原语 (3) Session Branching — 会话分支与恢复。每个卡片内用简洁的流程示意"),

    ("01-产品与架构/Tool Use 机制", "tool-use",
     "标题「Tool Use 机制」副标题「Agent 的手和脚」。四个图标卡片横排：(1) 代码执行 — 沙箱内运行 (2) 文件操作 — 读写本地文件 (3) 网络访问 — API 调用/浏览器 (4) 外部工具 — MCP 协议集成"),

    ("01-产品与架构/Agentic Coding", "agentic-coding",
     "标题「Agentic Coding」副标题「从辅助到自主」。进化阶梯从左到右：代码补全 → Copilot 辅助 → Agent 编码 → 数字员工。每个阶段标注代表产品和自主程度百分比"),

    ("01-产品与架构/OpenClaw 官方安全模型", "security-model",
     "标题「OpenClaw 安全模型」。三层防御架构从外到内：外层「Operator Install Policy」— 安装前拦截。中层「沙箱执行」— OpenShell 隔离。内层「权限控制」— 作用域+审批。底部标注已知挑战：Claw Chain、TOCTOU"),

    # === 02-安全与风险 (11张) ===
    ("02-安全与风险/安全边界与风险（总览）", "security-overview",
     "标题「OpenClaw 安全边界与风险」副标题「总览」。思维导图式布局（不要连线，用缩进和卡片层级表达）：核心矛盾「安全性 vs 实用性」，下分六个风险域：RCE 漏洞、Prompt Injection、凭证泄露、供应链攻击、大规模暴露、致命三合一"),

    ("02-安全与风险/Claw Chain 四漏洞链", "claw-chain",
     "标题「Claw Chain 四漏洞链」副标题「CVSS 最高 9.6」。四个卡片串联（用编号而非连线）：① CVE-44112 TOCTOU 写入 9.6 → ② CVE-44113 TOCTOU 读取 7.7 → ③ CVE-44115 Heredoc 泄露 8.8 → ④ CVE-44118 MCP 回环 8.2。底部标注「影响 245,000+ 暴露实例」"),

    ("02-安全与风险/GTIG AI 生成零日攻击报告", "gtig-zero-day",
     "标题「GTIG：AI 生成零日攻击」副标题「2026年5月 · 里程碑报告」。三个关键发现卡片：(1) 首个 AI 生成零日用于实战攻击 (2) APT45 朝鲜组织利用 AI 武器化 (3) OpenClaw/OneClaw 被用作攻击基础设施。底部标注「从理论到实践的转折点」"),

    ("02-安全与风险/RankClaw ClawHub 审计", "rankclaw-audit",
     "标题「RankClaw ClawHub 全量审计」。核心数据卡片：总技能 14,706 → 恶意 1,103 (7.5%) → VirusTotal 仅捕获已知签名。环形图展示 7.5% 恶意率。底部列出五大检测盲区"),

    ("02-安全与风险/2026年Q2安全态势总览", "security-q2-overview",
     "标题「2026 Q2 安全态势总览」。已有配图，跳过"),

    ("02-安全与风险/CVE-2026-25253 ClawJacked 漏洞详解", "clawjacked",
     "标题「ClawJacked 漏洞」副标题「CVE-2026-25253 · CVSS 8.8」。攻击链步骤卡片（编号排列）：① 访问恶意页面 → ② WebSocket 连接 localhost → ③ 暴力破解密码 → ④ 窃取 Token → ⑤ 静默注册设备 → ⑥ 关闭确认 → ⑦ 逃出沙箱 → ⑧ 宿主机 RCE"),

    ("02-安全与风险/恶意 Skills 供应链攻击", "supply-chain",
     "标题「恶意 Skills 供应链攻击」。三阶段流程：投递（仿冒热门 Skill 名称）→ 触发（安装时/运行时执行恶意代码）→ 影响（凭证窃取/数据外泄/后门植入）。底部数据：7.5% 恶意率、230+ 已检测"),

    ("02-安全与风险/Prompt Injection 风险", "prompt-injection",
     "标题「Prompt Injection 风险」副标题「最根本性安全威胁」。两列对比：直接注入（用户输入恶意指令）vs 间接注入（通过工具返回内容注入）。底部标注「无法根本修复，只能缓解」"),

    ("02-安全与风险/沙箱机制", "sandbox",
     "标题「沙箱机制」。三种沙箱模式卡片：(1) Docker 容器 — 默认隔离 (2) OpenShell — 可插拔后端 (3) Firecracker — 轻量级 VM。每个标注安全等级和性能开销"),

    ("02-安全与风险/致命三合一安全矛盾", "trinity-paradox",
     "标题「致命三合一安全矛盾」。三角形布局（三个卡片排成三角）：(1) 执行不受信任代码 (2) 处理不受信任内容 (3) 访问敏感资源。中心标注「不可能三角」"),

    ("02-安全与风险/权限控制机制", "permission-control",
     "标题「权限控制机制」。四层权限模型从上到下：(1) Operator 策略层 (2) Gateway 作用域层 (3) Agent 审批层 (4) 工具执行层"),

    # === 03-竞品与市场 (15张) ===
    ("03-竞品与市场/竞品对比总览", "competitor-overview",
     "标题「AI 编码 Agent 竞品总览」副标题「2026 Q2」。表格式卡片，6 行：Claude Code / Cursor / Devin / Copilot / OpenClaw / Kiro。列：定位、核心指标、定价模式、差异化优势。简洁表格风格"),

    ("03-竞品与市场/Claude Code 分析", "claude-code",
     "标题「Claude Code 分析」。三个指标卡片：(1) SWE-Bench Pro 69.2% (2) Anthropic ARR 470 亿美元 (3) Dynamic Workflows 1000 子 Agent。底部定位标签「专业软件开发 Agent」"),

    ("03-竞品与市场/Cursor 分析", "cursor",
     "标题「Cursor 分析」。三个指标卡片：(1) ARR 30 亿美元 (2) 5 万+ 企业团队 (3) Design Mode + Auto-review。底部定位「IDE 内嵌 AI 编码」"),

    ("03-竞品与市场/Devin 分析", "devin",
     "标题「Devin 分析」。三个指标卡片：(1) 估值 260 亿美元 (2) 89% 代码由 Devin 自写 (3) Windsurf → Devin Desktop 品牌统一。底部定位「全自主软件工程师」"),

    ("03-竞品与市场/GitHub Copilot 分析", "copilot",
     "标题「GitHub Copilot 分析」。三个指标卡片：(1) 470 万付费用户 (2) 转向 usage-based billing (3) Copilot App 技术预览。底部定位「最大装机量编码助手」"),

    ("03-竞品与市场/Claude Opus 4.7-4.8 发布", "opus-4-8",
     "标题「Claude Opus 4.7 / 4.8」。对比表：Opus 4.7 vs 4.8，指标行：SWE-Bench Verified / Pro / Online-Mind2Web / Fast Mode。4.8 列用橄榄绿强调"),

    ("03-竞品与市场/Anthropic Mythos 模型", "mythos",
     "标题「Anthropic Mythos」副标题「超越 Opus 的战略储备」。三个震撼数据卡片：(1) SWE-Bench Verified 93.9% (2) USAMO 数学奥赛 97.6% (3) AISI 黑客任务 73%。底部标注「Project Glasswing · 150+ 机构」"),

    ("03-竞品与市场/GPT-5.5 发布", "gpt-5-5",
     "标题「GPT-5.5 发布」副标题「2026年4月」。三个卡片：(1) 1M 上下文窗口 (2) SWE-Bench Verified 88.7% (3) 定价 5/30 美元每百万 token。底部对比 Opus 4.8"),

    ("03-竞品与市场/Cursor 2026年Q2更新", "cursor-q2",
     "标题「Cursor Q2 更新」。三个版本卡片：3.5 基线 → 3.6 Auto-review 模式 → 3.7 Design Mode（点击/绘制/语音）。进化箭头用编号而非连线"),

    ("03-竞品与市场/Windsurf 更名 Devin Desktop", "windsurf-devin",
     "标题「Windsurf → Devin Desktop」副标题「2026年6月 品牌终结」。变化对比：旧名 Windsurf / Cascade / 编辑器优先 → 新名 Devin Desktop / Devin Local / Agent Command Center。标注 Rust 重写、30% 效率提升"),

    ("03-竞品与市场/Claude Code 2026年Q2更新", "claude-code-q2",
     "标题「Claude Code Q2 更新」。三个重点卡片：(1) Dynamic Workflows — 1000 子 Agent、16 并发 (2) Auto Mode — Bedrock/Vertex/Foundry (3) 插件支持 .zip / URL 加载"),

    ("03-竞品与市场/GitHub Copilot 2026年Q2更新", "copilot-q2",
     "标题「GitHub Copilot Q2 更新」。两大变化卡片：(1) Usage-based Billing — AI Credits 按量计费、Opus 从 Pro 移除 (2) Copilot App — canvases、语音、cloud sessions、agentic browsing"),

    ("03-竞品与市场/2026年Q2竞品新入局", "new-competitors",
     "标题「Q2 竞品新入局」。四个新玩家卡片：(1) AWS Kiro IDE — 规范驱动 (2) Gemini CLI → Antigravity — 开源后闭源争议 (3) Gemini 3/3.5 系列 (4) OpenCode — 165K Stars、500万月活"),

    ("03-竞品与市场/竞品成本对比", "cost-comparison",
     "标题「竞品成本对比」。表格式：Claude Code Max 100-200美元 / Cursor Pro 20美元 / Devin 20美元+ACU / Copilot 10-39美元 / OpenClaw 免费+API / Kiro 免费预览。用不同色条标注价格区间"),

    ("03-竞品与市场/多 Agent 竞争格局", "multi-agent-competition",
     "标题「多 Agent 竞争格局」。四象限矩阵（用四个卡片排列）：横轴「开放 vs 封闭」纵轴「编码专用 vs 通用」。各产品放在对应象限"),

    # === 04-生态与社区 (12张) ===
    ("04-生态与社区/OpenClaw GitHub 数据更新 2026Q2", "github-q2",
     "标题「OpenClaw GitHub 数据」副标题「2026 Q2」。关键指标仪表盘：Stars 375K+ / Forks 78K+ / 贡献者 1,200+ / npm 周下载 77万 / MAU 320万 / 网站月访问 3,800万。每个数字配一个微型趋势箭头"),

    ("04-生态与社区/MCP 协议", "mcp-protocol",
     "标题「MCP 协议」副标题「AI 世界的 USB 标准」。三阶段流程：初始化（握手协商）→ 发现（查询工具列表）→ 调用（执行并返回结果）。底部数据：9,652 服务器、9,700万月 SDK 下载"),

    ("04-生态与社区/MCP 2026年Q2进展", "mcp-q2",
     "标题「MCP 2026 Q2 进展」。核心变化卡片：(1) 07-28 RC — 协议无状态化 (2) MCP Apps — HTML UI 扩展 (3) Tasks — 长时运行任务 (4) Extensions 框架 (5) Registry 9,652 服务器"),

    ("04-生态与社区/ACP v1 生态扩展", "acp-ecosystem",
     "标题「ACP v1 生态扩展」副标题「Editor-Agent 通信标准」。两列：左列「28+ Agent 支持」（Claude Code、Gemini CLI、OpenClaw 等）右列「8+ 编辑器」（JetBrains、Zed、VSCode、Neovim 等）。底部类比「ACP 之于 Agent = LSP 之于语言」"),

    ("04-生态与社区/ClawHub 官方技能注册表", "clawhub",
     "标题「ClawHub 技能注册表」。数据卡片：13,000+ 技能 / 500,000+ 运行实例 / 3,900万+ 下载。分类饼图：生产力、数据分析、Web 自动化、工具集成"),

    ("04-生态与社区/OpenClaw 社区热度总览", "community-heat",
     "标题「社区热度总览」。Q1 vs Q2 对比表：Stars 334K→375K / Discord 118K→176K / MAU 250万→320万 / 网站 725万→3,800万 / ClawHub 5K→13K / 贡献者 866→1,200"),

    ("04-生态与社区/ClawCon 2026 Q2", "clawcon-q2",
     "标题「ClawCon 2026 Q2」。三场活动卡片横排：(1) Michigan 4/16 — 密歇根大学 Crisler Center (2) Singapore 5月 — AI Engineer 前导 (3) Toronto 5/25-29 — 五天免费 290+ 注册"),

    ("04-生态与社区/AAIF 基金会", "aaif",
     "标题「AAIF Agentic AI 基金会」。关键数据：170+ 成员 / 9 场全球活动 / Gold 成员包括 Google、AWS、Microsoft。使命标注「推动 Agent 互操作标准」"),

    ("04-生态与社区/Skills 市场", "skills-market",
     "标题「Skills 市场」。市场现状三卡片：(1) 规模 — 13,000+ 公开技能 (2) 安全 — 7.5% 恶意率、6 步审计协议 (3) 商业化 — 付费 Skills、企业定制"),

    ("04-生态与社区/OpenClaw 核心生态项目", "ecosystem-projects",
     "标题「核心生态项目」。六个项目卡片网格：NanoClaw（轻量版）/ Lobster Shell（工作流）/ openclaw-ansible（部署）/ SetupClaw（白手套）/ tokenjuice（计量）/ copilot-plugin（GitHub 集成）"),

    ("04-生态与社区/社区与开源生态", "open-source-eco",
     "标题「社区与开源生态」。四个维度卡片：(1) 开发者 — 1,200+ 贡献者、MIT 开源 (2) 用户 — 320万月活 (3) 生态 — 13,000+ Skills (4) 资金 — Foundation 治理、赞助商"),

    ("04-生态与社区/中国用户与 OpenClaw", "china-users",
     "标题「中国用户与 OpenClaw」。三个卡片：(1) 中国模型 — DeepSeek、Qwen、MiniMax、GLM (2) 社区 — 飞书集成、QQBot 渠道 (3) 部署 — NanoClaw Docker 方案"),

    # === 05-商业与投资 (10张) ===
    ("05-商业与投资/Anthropic Series H 融资", "series-h",
     "标题「Anthropic Series H」。核心数据：融资 650 亿美元 / 估值 9,650 亿美元 / ARR 470 亿美元。投资方标注：Altimeter、Dragoneer、Greenoaks、Sequoia。底部标注「可能是 IPO 前最后一轮」"),

    ("05-商业与投资/Cognition Series D 融资", "cognition-d",
     "标题「Cognition Series D」。核心数据：融资 10 亿美元 / 估值 260 亿美元 / ARR 4.92 亿美元。亮点：89% 代码由 Devin 编写（从 13% 增长）。客户：Mercedes-Benz、NASA、Goldman Sachs"),

    ("05-商业与投资/AI Agent 市场规模", "market-size",
     "标题「AI Agent 市场规模」。增长曲线卡片：2026 年 109 亿美元 → 2030 年 527 亿美元 → 2035 年 2,210 亿美元。CAGR 40-50%。底部标注 Gartner/Grand View Research"),

    ("05-商业与投资/Anthropic 公司分析", "anthropic-analysis",
     "标题「Anthropic 公司分析」。关键指标：估值 9,650 亿美元 / ARR 470 亿美元 / 模型线 Claude + Mythos / 核心理念 Constitutional AI。创始人 Dario & Daniela Amodei"),

    ("05-商业与投资/Claude Code 营收分析", "claude-code-revenue",
     "标题「Claude Code 营收分析」。核心数据：25 亿美元年化营收（2026.2）。对比：Cursor 30 亿、Replit 5.25 亿、Devin 4.92 亿。市场格局正在快速变化"),

    ("05-商业与投资/OpenClaw 商业模式", "business-model",
     "标题「OpenClaw 商业模式」。四层商业化路径：(1) 开源免费 — 社区增长飞轮 (2) Skills 市场 — 开发者变现 (3) 企业版 — NemoClaw/SetupClaw (4) 大厂整合 — Microsoft Scout"),

    ("05-商业与投资/Gartner AI Agent 预测", "gartner-predictions",
     "标题「Gartner AI Agent 预测」。关键预测卡片：17% 已部署 / 60% 两年内部署 / 40% 应用将含 Agent / 多 Agent 咨询量 +1,445% / 47% AI 支出增长"),

    ("05-商业与投资/OpenClaw 投资机会因素", "investment-opportunity",
     "标题「投资机会因素」。五个利好卡片：(1) GitHub 最高 Star 项目 (2) 大厂背书 — Microsoft Scout + NVIDIA NemoClaw (3) Gartner 17% 部署率 (4) 373K+ Stars 社区 (5) MCP 标准化红利"),

    ("05-商业与投资/OpenClaw 投资风险因素", "investment-risk",
     "标题「投资风险因素」。五个风险卡片：(1) 安全债务 — CVE 472+  (2) 竞争加剧 — Claude Code + Devin (3) 大厂吞噬风险 (4) Anthropic IPO 冲击 (5) 40% 项目预计失败"),

    ("05-商业与投资/商业化路径", "commercialization",
     "标题「OpenClaw 商业化路径」。三条路径对比：(1) 社区开源 — 增长但不盈利 (2) 企业服务 — NemoClaw/Scout (3) 生态抽成 — Skills 市场。底部趋势箭头指向「企业服务」"),

    # === 06-趋势与未来 (10张) ===
    ("06-趋势与未来/2026 Agent 元年", "agent-year",
     "标题「2026 Agent 元年」。9 个 Q2 里程碑卡片网格 3x3：GPT-5.5 / Claude 自递归 / Gartner Hype Cycle / A2A v1.2 / MCP RC / Agent 365 GA / EU AI Act / ZoomMate / Bun 重写"),

    ("06-趋势与未来/AI Agent 技术成熟度", "tech-maturity",
     "标题「AI Agent 技术成熟度」副标题「Gartner Hype Cycle 2026」。简化的 Hype Cycle 曲线：标注 Agentic AI 处于「膨胀期望峰值」。数据：17% 已部署、60% 两年内、Agent Washing 警告"),

    ("06-趋势与未来/EU AI Act 2026 进展", "eu-ai-act",
     "标题「EU AI Act 2026 进展」。时间线：2026年8月2日 高风险条款生效 → 要求：技术文档 + 人工监督 + 控制机制。罚款：最高 3,500 万欧元或 7% 营收。底部标注 Omnibus 延期协议"),

    ("06-趋势与未来/AI Agent 市场趋势 2026 Q2", "market-trends-q2",
     "标题「AI Agent 市场趋势 Q2」。六个趋势卡片：(1) 长时运行工作流 (2) 多 Agent 咨询 +1,445% (3) 40% 项目预计失败 (4) Bun 11天75万行 (5) Mythos 安全争议 (6) NIST 三支柱"),

    ("06-趋势与未来/大厂 Agent 竞赛", "big-tech-race",
     "标题「大厂 Agent 竞赛」。五大厂卡片：Google（Agent Platform + A2A）/ Microsoft（Agent 365 + Scout）/ AWS（Kiro + Bedrock）/ Meta（Llama 4 + Meta AI）/ Anthropic（Claude Code + Mythos）"),

    ("06-趋势与未来/Vibe Coding 融资爆发", "vibe-coding-funding",
     "标题「Vibe Coding 融资爆发」。融资排行卡片：Cursor 500 亿估值 / Lovable ARR 4 亿（最快 SaaS）/ Replit 5.25 亿年化。Q2 AI 融资总额 426 亿美元"),

    ("06-趋势与未来/未来发展预测", "future-predictions",
     "标题「未来发展预测」。8 个预测卡片，每个标注验证状态（已验证/进行中/待验证）"),

    ("06-趋势与未来/MCP 协议 2026年3月进展", "mcp-march",
     "标题「MCP 协议进展」副标题「3月→Q2」。进化路径：3月状态 → Q2 RC 发布。新增能力：无状态化 / Extensions / MCP Apps / Tasks / OAuth 2.1"),

    ("06-趋势与未来/Agent 长时运行与 ACP 演进", "long-running-agents",
     "标题「Agent 长时运行与 ACP 演进」。三个 ACP 分化卡片：(1) ACP-IDE — Editor-Agent 通信 (2) ACP → A2A — Agent 间通信 (3) ACP-Commerce — 电商 Agent 协议"),

    ("06-趋势与未来/开发者工具市场变革", "devtools-revolution",
     "标题「开发者工具市场变革」。市场数据：108 亿美元 / Q2 融资 426 亿美元。三个变革卡片：(1) IDE 被重新定义 (2) Agent 取代工作流 (3) 按量计费成为标准"),

    # === 07-使用案例 (8张) ===
    ("07-使用案例/案例-Citi 银行 Arc 平台", "citi-arc",
     "标题「Citi 银行 Arc 平台」副标题「企业 Agent 操作系统」。三个亮点卡片：(1) 18 万员工 80% 使用 AI (2) 编排 Devin 等多 Agent (3) 治理框架对齐 EU AI Act。底部定位「Fortune 500 标杆案例」"),

    ("07-使用案例/案例-MFS Corp 零人类员工 AI 公司", "mfs-corp",
     "标题「MFS Corp 零人类员工」。实验数据：12 个 AI Agent 运行 / 模拟完整公司职能 / 行业跟进 zeroemployee.company。底部思考「Agent 取代组织？」"),

    ("07-使用案例/案例-14个Agent协作系统", "14-agents",
     "标题「14 个 Agent 协作系统」。Agent 角色网格：CEO / CTO / 设计师 / 开发者 / 测试 / 运维 / 市场 / 财务... 中心标注「多 Agent 协作范式」"),

    ("07-使用案例/案例-Reorx 从程序员到 Tech Lead", "reorx",
     "标题「从程序员到 Tech Lead」副标题「Reorx 的角色转变」。角色转变流程：写代码 → 审代码 → 指导 Agent → Tech Lead 视角。核心洞见「AI 改变的不是工具，是角色」"),

    ("07-使用案例/案例-Nat Eliason 的 AI 创业实验", "nat-eliason",
     "标题「AI 创业实验」副标题「Nat Eliason」。实验过程：想法 → OpenClaw 开发 → 上线 SaaS → 收获用户。核心数据和学到的经验教训"),

    ("07-使用案例/案例-非技术创始人用 AI 上线 SaaS", "non-tech-saas",
     "标题「非技术创始人上线 SaaS」。三步流程：(1) 自然语言描述需求 (2) Agent 生成代码 (3) 部署上线。代表了编程民主化的趋势"),

    ("07-使用案例/案例-Fast Company 记者亲测", "fast-company",
     "标题「Fast Company 记者亲测」。记者体验的三个阶段：惊艳（能力展示）→ 困惑（复杂任务失败）→ 反思（定位为辅助而非替代）"),

    ("07-使用案例/案例-汽车购买谈判省4200美元", "car-negotiation",
     "标题「汽车谈判省 4,200 美元」。谈判流程：市场调研 → 策略制定 → 话术准备 → 实际谈判 → 节省 4,200 美元。Agent 作为个人谈判教练"),

    # === 08-基础概念 (12张) ===
    ("08-基础概念/ACP 协议", "acp-protocol",
     "标题「ACP 协议」副标题「Agent Client Protocol」。核心概念：JSON-RPC 2.0 over stdio。类比：ACP 之于 Agent = LSP 之于编程语言。v1 稳定，28+ Agent 支持"),

    ("08-基础概念/Dynamic Workflows", "dynamic-workflows",
     "标题「Dynamic Workflows」副标题「Claude Code 大规模编排」。架构流程：规划 → JS 脚本生成 → 运行时调度 → 最多 1,000 子 Agent（16 并发）→ 对抗性验证 → 收敛。触发词 ultracode"),

    ("08-基础概念/Operator Install Policy", "operator-policy",
     "标题「Operator Install Policy」。Fail-Closed 设计：安装请求 → 策略命令执行 → 允许/阻止。适用范围：ClawHub / npm / git / 本地路径。与 Auto Mode 的安全三角关系"),

    ("08-基础概念/Agentic AI", "agentic-ai",
     "标题「Agentic AI」副标题「自主行动的 AI」。四级阶梯：聊天机器人 → Copilot → Agent → 数字员工。市场数据：80% Fortune 500 已部署、17% 生产环境、109 亿美元市场"),

    ("08-基础概念/Claude 模型系列", "claude-models",
     "标题「Claude 模型系列」。模型族谱：Opus 4.6 → 4.7 → 4.8 / Sonnet 4.6 / Haiku 4.5 / Mythos Preview。每个标注 SWE-Bench 分数和发布日期"),

    ("08-基础概念/GPT 模型系列", "gpt-models",
     "标题「GPT 模型系列」。模型演进：GPT-4o → GPT-5.4 → GPT-5.5 / GPT-5.5 Instant。标注 SWE-Bench 88.7%、1M 上下文、定价 5/30 美元"),

    ("08-基础概念/SWE-Bench 基准测试", "swe-bench",
     "标题「SWE-Bench 基准测试」副标题「2026 Q2 排名」。排行榜卡片：Mythos 93.9% / GPT-5.5 88.7% / Opus 4.8 88.6% / DeepSeek V4 80.6%。区分 Verified vs Pro 两个维度"),

    ("08-基础概念/Vibe Coding", "vibe-coding",
     "标题「Vibe Coding」副标题「用自然语言写代码」。演进三阶段：(1) 2025 诞生 — Karpathy 命名 (2) 2026 爆发 — Cursor 500 亿估值 (3) 安全危机 — 40-62% AI 代码含缺陷、VibeSec 清算"),

    ("08-基础概念/Docker 容器化", "docker",
     "标题「Docker 容器化」副标题「Agent 安全隔离基石」。三层容器模型：宿主机 → Docker Engine → Agent 容器（沙箱）。2026 更新：Docker Sandboxes 支持 Claude Code/Gemini/Codex"),

    ("08-基础概念/大语言模型", "llm",
     "标题「大语言模型 LLM」。2026 模型对比表：Claude Opus 4.8 / Mythos / GPT-5.5 / DeepSeek V4-Pro / Gemini 3.5 Pro。标注参数量、上下文、核心能力"),

    ("08-基础概念/Transformer 架构", "transformer",
     "标题「Transformer 架构」。简化架构图：输入 → Embedding → 多头注意力 → 前馈网络 → 输出。标注 Self-Attention 是核心创新"),

    ("08-基础概念/编程民主化", "coding-democratization",
     "标题「编程民主化」。三层金字塔：底层「非技术用户」— Vibe Coding / 自然语言 → 中层「初级开发者」— Agent 辅助 → 顶层「专业开发者」— Agent 协作。底层最宽，代表受益人群最大"),

    # === 09-人物与事件 (10张) ===
    ("09-人物与事件/Dario Amodei", "dario-amodei",
     "标题「Dario Amodei」副标题「Anthropic CEO」。人物档案卡：前 OpenAI VP Research / Constitutional AI 提出者 / 半人马阶段理论。关键成就：估值 9,650 亿、ARR 470 亿、Mythos 模型"),

    ("09-人物与事件/Sam Altman", "sam-altman",
     "标题「Sam Altman」副标题「OpenAI CEO」。人物档案卡：GPT-5.5 发布 / Codex 向所有付费用户开放 / OpenClaw 收编。与 Dario 的竞争关系"),

    ("09-人物与事件/Andrej Karpathy", "karpathy",
     "标题「Andrej Karpathy」。人物转折：Tesla AI → 独立研究 → 2026.5 加入 Anthropic。关键贡献：Vibe Coding 命名 / Agentic Engineering 定义 / AutoResearch 项目"),

    ("09-人物与事件/Toran Bruce Richards", "toran",
     "标题「Toran Bruce Richards」副标题「AutoGPT → OpenClaw 创始人」。项目演进：AutoGPT 2023 → OpenClaw 2025 → Foundation 治理 2026。GitHub Stars 记录被自己打破"),

    ("09-人物与事件/Simon Willison", "simon-willison",
     "标题「Simon Willison」副标题「AI 安全评论家」。核心观点：taint tracking + policy gating / Opus 4.7 隐性提价分析 / Agentic Engineering Patterns 项目"),

    ("09-人物与事件/v2026.3.22 发布事件", "v3-22-event",
     "标题「v2026.3.22 发布事件」。里程碑：100+ 贡献者 / 架构级重构 / Breaking Changes。后续影响：Claw Chain → GTIG 零日 → Stars 375K+ → MAU 320万"),

    ("09-人物与事件/龙虾吉祥物文化", "lobster-culture",
     "标题「龙虾吉祥物文化」。文化元素卡片：龙虾 Logo / The Great Molt 改名事件 / Moltiverse 社区概念 / 旧金山线下 Meetup。320万月活社区的文化认同"),

    ("09-人物与事件/Cyera Research 与 Claw Chain 披露", "cyera-disclosure",
     "标题「Cyera Research 与 Claw Chain 披露」。负责任披露时间线：发现 → 报告 → 修复 → 公开。团队背景：Unit 8200 老兵、Vladimir Tokarev。四漏洞链 CVSS 9.6"),

    ("09-人物与事件/GTIG 首次确认 AI 生成零日事件", "gtig-event",
     "标题「GTIG 首次确认 AI 生成零日」副标题「2026年5月 · 网络安全史里程碑」。历史定位卡片：与 Stuxnet / WannaCry / SolarWinds 并列。核心发现：AI 生成零日从理论到实战"),

    ("09-人物与事件/The Great Molt 改名事件", "great-molt",
     "标题「The Great Molt 改名事件」。改名过程：旧名（待定）→ 社区投票 → OpenClaw 诞生。龙虾蜕壳隐喻：蜕旧壳、长新甲"),
]

def generate_one(item):
    md_path_rel, img_slug, content_prompt = item
    img_name = f"{img_slug}.jpg"
    img_path = ASSETS / img_name

    if img_path.exists() and img_path.stat().st_size > 50000:
        return f"SKIP (exists): {img_slug}"

    full_prompt = f"""在这张参考图的基础上生成信息图。严格保留参考图中左下角的圆形头像、署名「histonemax / 默子要早睡」和底部居中的仓库链接，位置、大小、样式完全不变。在空白主体区域填充以下内容：

{content_prompt}

{COMMON_STYLE}"""

    payload = {
        "model": "nano-banana-2",
        "prompt": full_prompt,
        "size": "1536x1024",
        "response_format": "b64_json",
        "image": [f"data:image/png;base64,{TPL_B64}"]
    }

    try:
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            API_URL,
            data=body,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read())

        if "data" not in data or not data["data"]:
            return f"ERROR (no data): {img_slug} — {json.dumps(data, ensure_ascii=False)[:200]}"

        raw = base64.b64decode(data["data"][0]["b64_json"])
        js = raw.find(b"\xff\xd8\xff")
        ps = raw.find(b"\x89PNG")
        if ps >= 0:
            img = raw[ps:]
        elif js >= 0:
            img = raw[js:]
        else:
            img = raw

        with open(img_path, "wb") as f:
            f.write(img)

        return f"OK: {img_slug} ({len(img)} bytes)"

    except Exception as e:
        return f"ERROR (exception): {img_slug} — {e}"


def embed_images():
    """在对应的 Markdown 文件中嵌入图片引用"""
    count = 0
    for md_path_rel, img_slug, _ in IMAGES:
        md_file = ROOT / f"{md_path_rel}.md"
        img_name = f"{img_slug}.jpg"
        img_path = ASSETS / img_name

        if not md_file.exists() or not img_path.exists():
            continue

        content = md_file.read_text(encoding="utf-8")
        img_ref = f"![{md_path_rel.split('/')[-1]}](assets/{img_name})"
        # 也支持 Obsidian 内嵌格式
        obs_ref = f"![[assets/{img_name}]]"

        if img_name in content:
            continue

        # 在 frontmatter 结束后、第一个 # 标题之前插入，或在标题之后插入
        lines = content.split("\n")
        insert_idx = None
        in_frontmatter = False
        for i, line in enumerate(lines):
            if line.strip() == "---" and i == 0:
                in_frontmatter = True
                continue
            if in_frontmatter and line.strip() == "---":
                in_frontmatter = False
                continue
            if not in_frontmatter and line.startswith("# "):
                insert_idx = i + 1
                # 跳过标题后的空行
                while insert_idx < len(lines) and lines[insert_idx].strip() == "":
                    insert_idx += 1
                break

        if insert_idx is not None:
            lines.insert(insert_idx, "")
            lines.insert(insert_idx + 1, f"![[assets/{img_name}]]")
            lines.insert(insert_idx + 2, "")
            md_file.write_text("\n".join(lines), encoding="utf-8")
            count += 1

    return count


if __name__ == "__main__":
    # 跳过已有的 3 张测试图
    skip_slugs = {"openclaw-ecosystem-2026", "security-landscape-q2-2026", "competitive-landscape-2026"}
    todo = [item for item in IMAGES if item[1] not in skip_slugs]

    print(f"=== 批量生成 {len(todo)} 张图片（{MAX_WORKERS} 并发）===")
    print(f"模板: {TEMPLATE}")
    print(f"输出: {ASSETS}")
    print()

    done = 0
    errors = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(generate_one, item): item for item in todo}
        for future in as_completed(futures):
            result = future.result()
            done += 1
            if result.startswith("ERROR"):
                errors += 1
            print(f"[{done}/{len(todo)}] {result}")

    print(f"\n=== 生成完成：{done - errors} 成功 / {errors} 失败 ===")

    # 嵌入图片引用到 Markdown
    print("\n=== 嵌入图片到 Markdown ===")
    embedded = embed_images()
    print(f"嵌入了 {embedded} 个图片引用")
