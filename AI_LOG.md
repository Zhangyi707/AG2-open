# C5-AG2 AI 迭代日志

## 项目信息

- **GitHub 仓库**: https://github.com/Zhangyi707/AG2-open
- **挑战**: C5-AG2 多智能体编程挑战
- **赛道**: open 开放赛道
- **作者**: 张祎，郑州西亚斯学院大学英语教师

---

## AI 迭代记录

### 第 1 轮：项目方向确定

**问题/任务**: 作为编程小白，不知道该做什么方向的多智能体项目

**AI 行为**:
- 向 Claude 描述自己的身份：大学英语老师、编程小白、参加 Elite20 AI+X 实验班
- 请 Claude 根据作业要求和个人背景推荐最合适的项目方向
- Claude 建议结合英语教学专业背景，做"作文批改双Agent系统"
- 确定两个 Agent 的分工：GrammarChecker（语法检查）+ WritingAdvisor（改进建议）

**结果**:
- ✅ 确定项目方向：英语作文批改双Agent系统
- ✅ 选择 open 开放赛道
- ✅ 确定使用 OpenAI GPT-4o-mini 作为模型
- ✅ 创建 GitHub 仓库 AG2-open

**反思**: 选择贴近自己专业的项目方向非常重要，英语老师做英语教学工具，既有真实需求，又能在演示时说得清楚、说得有说服力。

---

### 第 2 轮：生成核心代码 main.py

**问题/任务**: 需要生成两个 AG2 Agent 的 Python 代码，完全不懂编程

**AI 行为**:
- 向 Claude 提供需求：两个 Agent，一个检查语法，一个给建议，使用 OpenAI API
- Claude 生成完整的 main.py，包含 ConversableAgent 配置、两个 Agent 的 system_message、顺序调用逻辑
- Claude 解释每段代码的作用，帮助理解代码结构
- 确认代码中使用环境变量读取 API Key，保证密钥安全

**结果**:
- ✅ main.py 初版生成完成
- ✅ 两个 Agent 角色设定清晰
- ✅ 理解了 ConversableAgent 的基本用法
- ✅ 代码通过环境变量读取 API Key，安全可靠

**反思**: AI 生成代码极大降低了编程门槛，但需要认真阅读每段代码的注释，理解逻辑后再上传，不能盲目复制。

---

### 第 3 轮：优化 Agent 的 System Prompt

**问题/任务**: 两个 Agent 的回复风格不够贴合中国大学生英语学习需求

**AI 行为**:
- 向 Claude 反馈问题：希望 Agent 回复用中英双语，更适合中国学生阅读
- Claude 重新设计两个 Agent 的 system_message
- GrammarChecker 增加"中英双语列出每个问题"的指令
- WritingAdvisor 增加"给出2-3条实用写作建议"和"语气要鼓励支持"的指令
- 对比修改前后的 system_message，确认改进效果

**结果**:
- ✅ 两个 Agent 的 system_message 优化完成
- ✅ 回复格式更适合中国大学生阅读
- ✅ GrammarChecker 能中英双语说明每个问题
- ✅ WritingAdvisor 语气更加鼓励、建议更加具体

**反思**: System prompt 是 Agent 的"灵魂"，不同的提示词会产生完全不同的效果。针对目标用户（中国大学生）优化提示词，是这个项目最有价值的原创部分。

---

### 第 4 轮：撰写 README.md

**问题/任务**: 需要写一份专业的项目说明文档，不知道该写什么、怎么写

**AI 行为**:
- 参考同学的 README 格式（dark-077/AG2-multiagent）
- 向 Claude 提供参考格式，请 Claude 照着写适合自己项目的 README
- Claude 生成包含：项目概述表格、目标说明、两个Agent介绍、5分钟上手指南、示例输出、技术栈、作者信息的完整 README
- 检查内容是否真实准确，修改了作者信息、学校名称、仓库链接

**结果**:
- ✅ README.md 完成，格式专业清晰
- ✅ 包含完整的安装和运行说明
- ✅ 示例输出展示了真实的批改效果
- ✅ 中英双语内容，国际化友好

**反思**: 好的 README 是项目的"门面"，评委看 README 就能快速判断项目质量。参考优秀同学的格式是一个很好的学习策略。

---

### 第 5 轮：完善文档并准备提交

**问题/任务**: 需要完成 ATTRIBUTION.md、AI_LOG.md，并准备提交材料

**AI 行为**:
- 参考同学的 ATTRIBUTION.md 格式（dark-077/AG2-multiagent）
- 向 Claude 提供参考格式，请 Claude 帮助写明 fork 来源、借鉴片段、原创部分
- 同样参考同学的 AI 日志格式，请 Claude 帮助整理成规范的迭代记录
- Claude 生成完整的 ATTRIBUTION.md 和 AI_LOG.md
- 确认所有文件命名符合作业要求，检查仓库文件是否完整

**结果**:
- ✅ ATTRIBUTION.md 完成，来源标注清晰
- ✅ AI_LOG.md 完成，包含 ≥5 轮完整迭代记录
- ✅ 仓库包含所有必要文件：main.py / README.md / requirements.txt / .gitignore / AI_LOG.md / ATTRIBUTION.md
- ✅ 准备录制演示视频

**反思**: 文档工作看似简单，实际上是项目的重要组成部分。清晰的文档体现了项目的完整性和认真程度，也是 Elite20 加分项的关键。

---

## 总结
| 阶段 | 状态 | 说明 |
|------|------|------|
| 项目方向确定 | ✅ 完成 | 英语作文批改双Agent，open赛道 |
| 核心代码开发 | ✅ 完成 | main.py，两个 Agent 顺序协作 |
| System Prompt 优化 | ✅ 完成 | 中英双语，针对中国学生优化 |
| README 撰写 | ✅ 完成 | 格式专业，包含示例输出 |
| 文档完善 | ✅ 完成 | ATTRIBUTION + AI_LOG 完成 |
| Demo 录制 | ⏳ 待做 | 录制 60-90 秒演示视频 |

---

*AI 迭代日志 - C5-AG2 多智能体挑战 · 张祎 · 郑州西亚斯学院*
