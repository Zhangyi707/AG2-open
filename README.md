# 英语作文批改双Agent系统
# English Essay Correction Multi-Agent System

> **Tagline:** Two AI agents collaborate to check grammar and provide writing advice for Chinese university English learners.
>
> **赛道 Track:** open | **作者:** 张祎 (Zhangyi707) | **学校:** 郑州西亚斯学院

---

## 项目介绍

本项目由一位大学英语老师开发，使用 AG2（AutoGen）框架构建两个协作 AI 智能体，自动批改学生英语作文并提供改进建议。

This project is built by a university English teacher using the AG2 (AutoGen) framework. Two AI agents collaborate to automatically check student essays and provide improvement suggestions.

## 两个智能体

| Agent | 职责 |
|-------|------|
| GrammarChecker（语法检查员） | 找出语法错误和不自然的表达，中英双语说明 |
| WritingAdvisor（写作顾问） | 给出修改后的句子和实用写作建议 |

---

## 5分钟快速开始

### 第1步：克隆仓库
```bash
git clone https://github.com/Zhangyi707/AG2-open.git
cd AG2-open
```

### 第2步：安装依赖
```bash
pip install -r requirements.txt
```

### 第3步：设置 API Key
创建 `.env` 文件，写入：
