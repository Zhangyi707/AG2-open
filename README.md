# AG2-open# 英语作文批改双Agent系统
# English Essay Correction Multi-Agent System

> **Tagline:** Two AI agents collaborate to check grammar and provide writing advice for Chinese university English learners.
> **赛道 Track:** open | **作者:** 张艺 (Zhangyi707) | **学校:** 郑州西亚斯学院

## 项目介绍

本项目由一位大学英语老师开发，使用 AG2（AutoGen）框架构建两个协作 AI 智能体，自动批改学生英语作文并提供改进建议。

## 两个智能体

| Agent | 职责 |
|-------|------|
| GrammarChecker（语法检查员） | 找出语法错误和不自然的表达 |
| WritingAdvisor（写作顾问） | 给出修改后的句子和写作建议 |

## 快速开始（5分钟）

### 1. 克隆仓库
git clone https://github.com/Zhangyi707/elite20-starter-.git

### 2. 安装依赖
pip install -r requirements.txt

### 3. 设置 API Key
创建 .env 文件，写入：
OPENAI_API_KEY=你的密钥

### 4. 运行
python main.py

## 技术栈

- 框架: AG2 / AutoGen (pyautogen)
- 模型: OpenAI GPT-4o-mini
- 语言: Python 3.9+

## 参考链接

- AG2 文档: https://docs.ag2.ai/
- AG2 GitHub: https://github.com/ag2ai/ag2
- 原始 Hackathon: https://ag2-hackathon.vercel.app/
