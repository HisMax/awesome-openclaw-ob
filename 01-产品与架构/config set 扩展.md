---
tags:
  - OpenClaw
  - CLI
  - 配置
  - 2026年3月
aliases:
  - config set
  - SecretRef
  - dry-run
  - openclaw update
  - 健康监控
---

# config set 扩展

## 一句话理解

> 以前的 `config set` 像一个只会存文本的记事本——你说什么它就记什么，对不对它不管；扩展后的 `config set` 变成了带验证功能的智能表单——支持密钥引用、批量操作、JSON 语法，还能"先演练再提交"（`--dry-run`），写错了也不会搞崩系统。

## SecretRef 支持

v2026.3.22 的 `config set` 新增了 **SecretRef（密钥引用）** 类型。不再需要将 API Key 明文写入配置文件，而是引用一个安全存储的密钥标识符：

```bash
openclaw config set providers.openai.apiKey secretRef:vault/openai-key
```

SecretRef 在配置文件中存储的是引用路径而非实际值，运行时由 Gateway 的密钥解析器从安全存储（环境变量、Vault 服务等）中获取真实值。这是 [[OpenClaw 官方安全模型]] 中"零明文密钥"原则的 CLI 层面落地。

## Provider 构建器模式

新增交互式的 Provider 构建器模式，引导用户逐步配置模型提供商。运行 `openclaw config set providers --builder` 会触发一个分步引导流程：选择提供商类型 -> 输入端点 -> 配置认证 -> 验证连接。这降低了 [[Provider-Plugin 架构]] 配置的门槛，特别适合首次接入新模型提供商的用户。

## JSON/批量支持

`config set` 现在接受 JSON 格式的批量配置：

```bash
openclaw config set --json '{"providers.openai.model": "gpt-5.4", "agents.defaults.timeout": 172800}'
```

单条命令设置多个配置项，替代之前需要多次调用 `config set` 的繁琐操作。JSON 格式也让配置脚本和 CI/CD 自动化更加方便。

## --dry-run 验证

`--dry-run` 标志让用户在实际写入配置前预览变更：

```bash
openclaw config set agents.defaults.timeout 172800 --dry-run
# 输出: Would set agents.defaults.timeout = 172800 (current: 600)
# 输出: Validation: OK
```

这对生产环境的配置变更尤为重要——一个错误的配置可能导致 Gateway 无法启动。dry-run 模式执行完整的验证逻辑（类型检查、范围检查、依赖检查）但不写入，给管理员一个"后悔药"。

## openclaw update --tag main

v2026.3.22 扩展了 `openclaw update` 命令，新增 `--tag main` 选项，允许直接从 GitHub main 分支安装最新开发版本。这对需要及时获取修复或测试新功能的用户来说是一个重要的便利——不需要等待正式版本发布，也不需要手动克隆仓库。

## 健康监控扩展

新增可配置的过时事件（stale-event）阈值和每频道覆盖。[[Heartbeat 主动监控机制]] 现在支持为不同频道设置不同的健康检查灵敏度：

- 高优先级频道（如生产 WhatsApp）可以设置更短的超时阈值
- 低优先级频道（如测试 Discord）可以容忍更长的静默期
- 全局阈值作为默认值，每频道配置可覆盖

## 双链导航

- [[OpenClaw v2026.3 版本更新]] — v2026.3.22 引入所有 config set 增强
- [[OpenClaw 官方安全模型]] — SecretRef 是安全模型的 CLI 层面实践
- [[Provider-Plugin 架构]] — Provider 构建器模式简化了提供商配置流程
- [[Heartbeat 主动监控机制]] — 健康监控的可配置阈值与 Heartbeat 机制关联
- [[Dashboard 控制面板]] — Config 模块是 config set 的 Web 界面等价物
