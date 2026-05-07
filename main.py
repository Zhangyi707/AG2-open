"""
English Teaching Multi-Agent System
英语教学双智能体系统

Agent 1 - GrammarChecker: 找语法错误和表达问题
Agent 2 - WritingAdvisor: 给出改进建议和示范句子

作者: 张祎 | 学校: 郑州西亚斯学院 | 赛道: open
"""

import os
from autogen import ConversableAgent

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.environ.get("OPENAI_API_KEY"),
}

# Agent 1：语法检查老师
checker = ConversableAgent(
    name="GrammarChecker",
    system_message="""You are an experienced English grammar checker for Chinese university students.
Your job:
1. Identify grammar mistakes in the student's essay
2. Point out awkward expressions or unclear sentences
3. List each issue with the original sentence and the error type
4. Be encouraging and supportive in your tone
Always respond in both English and Chinese so students can understand easily.""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# Agent 2：改进建议老师
advisor = ConversableAgent(
    name="WritingAdvisor",
    system_message="""You are a supportive English writing coach for Chinese university students.
Your job:
1. Read the grammar issues identified by GrammarChecker
2. Provide corrected versions of each problematic sentence
3. Suggest better vocabulary or expressions
4. Give 2-3 practical writing improvement tips
Always respond in both English and Chinese so students can understand easily.""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# 示例学生作文
student_essay = """
My summer holiday was very good. I go to Beijing with my family.
We visited the Great Wall and it was very big and long.
The weather is hot but we are happy.
I think Beijing is a beautiful city and I want to visit again in future.
"""

print("=" * 60)
print("英语作文批改双Agent系统")
print("=" * 60)
print(f"\n学生作文：\n{student_essay}")

print("\n" + "=" * 60)
print("Agent 1 (GrammarChecker) 正在检查语法错误...")
print("=" * 60)

checker_result = checker.generate_reply(
    messages=[{
        "role": "user",
        "content": f"Please check this student essay for grammar and expression issues:\n\n{student_essay}"
    }]
)
print(f"\n{checker_result}")

print("\n" + "=" * 60)
print("Agent 2 (WritingAdvisor) 正在生成改进建议...")
print("=" * 60)

advisor_result = advisor.generate_reply(
    messages=[{
        "role": "user",
        "content": f"Based on these grammar issues:\n\n{checker_result}\n\nPlease provide corrected sentences and writing improvement tips."
    }]
)
print(f"\n{advisor_result}")

print("\n" + "=" * 60)
print("批改完成！感谢使用英语教学双Agent系统")
print("=" * 60)
