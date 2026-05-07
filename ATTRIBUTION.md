# C5-AG2 ATTRIBUTION

## Fork 来源

本项目为**从零创建**的 AG2 多智能体项目，未直接 fork 现有仓库。

项目启发自以下资源：

| 资源 | 来源 | 用途 |
|------|------|------|
| AG2 官方文档 | https://docs.ag2.ai/ | API 参考和最佳实践 |
| AG2 build-with-ag2 示例库 | https://github.com/ag2ai/build-with-ag2 | ConversableAgent 用法参考 |
| C5-AG2 Hackathon Starter | 挑战包自带 | 挑战规则和评分标准 |
| AG2 Beta 文档 | `references/ag2_docs/20_beta_example_hello_agent.mdx` | 单 Agent 基础架构 |

---

## 借鉴片段

### 1. Agent 系统设计

**来源**: AG2 官方文档 ConversableAgent 示例

GrammarChecker + WritingAdvisor 双 Agent 顺序协作模式，参考了 AG2 官方的双 Agent 对话设计：
+--------------------------------------------------+
Agent职责模型GrammarChecker语法检查、问题列出GPT-4o-miniWritingAdvisor修改建议、写作指导GPT-4o-mini+--------------------------------------------------+
本项目将通用对话模式改造为英语教学批改场景，Agent 1 的输出作为 Agent 2 的输入，形成教学闭环。

### 2. ConversableAgent 基础配置

**来源**: https://github.com/ag2ai/build-with-ag2

基础 Agent 配置结构参考自 AG2 官方示例：

```python
llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.environ.get("OPENAI_API_KEY"),
}

agent = ConversableAgent(
    name="AgentName",
    system_message="...",
    llm_config=llm_config,
    human_input_mode="NEVER",
)
```

### 3. 顺序协作调用模式

**来源**: AG2 官方文档 `generate_reply` 方法

使用 `generate_reply` 实现 Agent 间顺序传递信息，Agent 2 读取 Agent 1 的输出作为输入：

```python
checker_result = checker.generate_reply(
    messages=[{"role": "user", "content": essay}]
)

advisor_result = advisor.generate_reply(
    messages=[{"role": "user", "content": checker_result}]
)
```

---

## 自主开发部分

以下部分为本项目原创：

| 模块 | 说明 |
|------|------|
| GrammarChecker 系统提示词 | 结合大学英语教学场景定制，要求中英双语输出 |
| WritingAdvisor 系统提示词 | 结合写作指导专家角色，针对中国学生定制建议风格 |
| 英语教学应用场景设计 | 将多智能体技术与实际课堂批改场景结合 |
| 中英双语输出格式 | 让中国大学生既能看懂英文批改，又能理解中文说明 |
| 示例作文选取与说明 | 选取中国学生典型语法错误作为演示样本 |

---

## 致谢

- **AG2 Team** — AG2 / AutoGen 框架开发与维护
- **Elite20 & AI+X 实验班** — C5-AG2 挑战策划和学习支持
- **OpenAI** — 提供 GPT-4o-mini 推理能力
- **Claude (Anthropic)** — 全程 AI 辅助开发、代码生成与文档撰写

---

*本 ATTRIBUTION.md 按照 C5-AG2 挑战要求编写，确保所有借鉴内容均有明确来源标注。*
