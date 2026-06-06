---
tags:
  - 架构
  - 监控
  - OpenClaw
aliases:
  - Heartbeat
  - 主动监控
  - Heartbeat 系统
---

# Heartbeat 主动监控机制

Heartbeat 是 [[OpenClaw 是什么|OpenClaw]] 的主动检查机制——Agent 不再只是被动等待用户消息，而是按计划主动巡检并在需要时发出通知。

## 4 步生命周期

1. **定时器触发**：根据配置的 `every` 间隔触发（如 30m）
2. **读取检查清单**：解析工作空间中的 HEARTBEAT.md，获取需要检查的项目列表
3. **执行 Agent 循环**：对每个检查项运行标准 [[Agent Execution Loop]]（可调用工具），这是 Agent-Flow-Loop 原理的一个实际应用场景
4. **评估响应**：HEARTBEAT_OK 则静默记录；发现异常则通过目标渠道发送告警通知（可通过 WhatsApp、Telegram 等消息渠道）

## 双层成本优化

1. **廉价预检**：先检查 HEARTBEAT.md 是否为空——如果为空，直接跳过，零 LLM 成本
2. **LLM 判断**：只有确实需要检查的项目才会触发 LLM 推理，这也是成本优化的关键

## 配置示例

```json
{
  "heartbeat": {
    "every": "30m",
    "target": "whatsapp:+1234567890",
    "active_hours": "9am-10pm EST"
  }
}
```

- `active_hours`：仅在活跃时段内触发，避免深夜打扰
- 同一检查项 **24 小时内**不会重复告警——避免"告警风暴"

## Heartbeat vs Cron

| | Cron | Heartbeat |
|---|---|---|
| 执行方式 | 机械地按时执行固定脚本 | 带判断力地检查，理解上下文后决定是否告警 |
| 灵活性 | 需要提前写好所有逻辑 | 用自然语言描述检查项，Agent 自行推理 |
| 告警质量 | 固定阈值触发 | 语义理解，能区分"正常波动"和"真正异常"（基于记忆系统中的历史上下文） |

> Cron 是机械执行，Heartbeat 是带判断力的检查。

## 后续改进

v2026.5.20 引入更安全的 cron 运行机制，v2026.5.22 的 /models 端点 4100x 性能提升（从 20 秒降至 5 毫秒）间接改善了 Heartbeat 中模型状态检查的效率。详见 [[OpenClaw v2026.5 版本更新]]。

## 相关笔记

- [[Agent Execution Loop]]
- [[自主决策循环]]
- [[OpenClaw 是什么]]
- [[上下文管理机制]]
- [[System Prompt 设计]]
- [[OpenClaw v2026.5 版本更新]] — 频道可靠性改进

## 参考

- [OpenClaw GitHub](https://github.com/anthropics/openclawx)
- [MCP 规范](https://modelcontextprotocol.io)
