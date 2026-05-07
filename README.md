# 🎓 英语作文批改双Agent系统
# English Essay Correction Multi-Agent System

> **C5-AG2 多智能体挑战 · open 赛道**
> 基于 AG2 (formerly AutoGen) 构建的 GrammarChecker + WritingAdvisor 双智能体协作系统，专为中国大学英语教学场景设计。

---

## 📋 项目概述

| 项目 | 内容 |
|------|------|
| 挑战 | C5-AG2 多智能体编程挑战 |
| 赛道 | open 开放赛道 |
| 框架 | AG2 (formerly AutoGen) |
| GitHub | https://github.com/Zhangyi707/AG2-open |
| 运行模式 | 顺序协作（Checker → Advisor） |
| 作者 | 张祎，郑州西亚斯学院大学英语教师 |

---

## 🎯 项目目标

我是一名大学英语老师，每学期需要批改大量学生作文，工作量大、反馈慢。

本项目基于 AG2 框架，构建两个协作 AI 智能体，模拟"两位老师分工批改"的场景：

1. **Agent 1：GrammarChecker（语法检查员）** — 找出语法错误、时态问题、中式英语表达，中英双语列出每一个问题
2. **Agent 2：WritingAdvisor（写作顾问）** — 读取检查结果，给出修改后的句子和实用写作建议

---

## 🤖 技术栈

- **AG2 (pyautogen)**: 开源多智能体框架
- **Python 3.9+**: 编程语言
- **LLM**: OpenAI GPT-4o-mini

---

## 📁 项目结构
---

## 🚀 5分钟上手指南

### 1. 克隆仓库

```bash
git clone https://github.com/Zhangyi707/AG2-open.git
cd AG2-open
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API 密钥

在项目目录下新建 `.env` 文件，填入你的 OpenAI API Key：
> ⚠️ `.env` 文件已加入 `.gitignore`，不会被上传到 GitHub，密钥安全。

### 4. 运行程序

```bash
python main.py
```

### 5. 更换批改内容

打开 `main.py`，找到以下位置，把引号内换成你要批改的作文：

```python
student_essay = """
在这里粘贴学生作文
"""
```

---

## 📊 示例输出

**输入作文：**
My summer holiday was very good. I go to Beijing with my family.
The weather is hot but we are happy.
I want to visit again in future.
**Agent 1 输出（GrammarChecker）：**
问题1：时态错误
原句：I go to Beijing with my family.
应改为：I went to Beijing with my family.
中文说明：描述过去的事情需要用动词过去式。
问题2：冠词缺失
原句：I want to visit again in future.
应改为：I want to visit again in the future.
中文说明："in the future" 是固定搭配，不可省略 "the"。
**Agent 2 输出（WritingAdvisor）：**
修改建议：

"I went to Beijing with my family." ✓
"I want to visit again in the future." ✓

写作提升建议：

全篇保持时态一致，描述过去经历统一用过去时
用更具体的形容词代替 "very good"，如 "memorable" 或 "wonderful"
使用连接词让句子更流畅，如 "Although the weather was hot, we thoroughly enjoyed ourselves."
---

## 📚 参考资源

- [AG2 官方文档](https://docs.ag2.ai/latest/)
- [AG2 GitHub](https://github.com/ag2ai/ag2)
- [AG2 Hackathon](https://ag2-hackathon.vercel.app)
- [参考项目](https://github.com/ag2ai/build-with-ag2)

---

## 📝 提交物

- [x] `张祎_C5-AG2_repo.md` — 仓库链接 + tagline
- [x] `AI_LOG.md` — AI 迭代记录（≥5轮）
- [x] `ATTRIBUTION.md` — Fork 来源说明
- [ ] `张祎_C5-AG2_demo.mp4` — 演示视频（录制中）

---

## 👤 作者

- GitHub: [@Zhangyi707](https://github.com/Zhangyi707)
- 身份: 郑州西亚斯学院大学英语教师
- 赛道: open 开放赛道

---

*Built with ❤️ using AG2 · 让AI成为英语教学的好帮手*
