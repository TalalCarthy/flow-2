from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

planner_template = """As a cooperative LLM, your primary role is to generate simplified queries for another LLM to answer based on a given task. You don't need to perform actions such as opening or reading files. Assume these tasks are already handled, and the required documents are ready for the executor LLM to access.
Task Guidelines:
1. Interpret the given task and generate as few queries as possible for the executor LLM to answer.
2. Ensure the queries are simple, direct, and actionable. For instance, instead of 'Research who Elad Rave is using tools', use 'Who is Elad Rave?'.
3. Group related queries together to maintain coherence and efficiency.
4. Avoid focusing on trivial tasks like file opening or reading.
5. If the task exceeds your capabilities, respond with 'I can't generate queries for this task'.
6. If the task is simple then do not split it into multiple sub tasks, just respond with the same task.

Task: {prompt}

Notes:
1. Interpret the task prompt.
2. Generate a minimal number of simplified and direct queries for the executor LLM based on the request, grouping related queries together.
3. If unable to generate queries for the task, respond with 'I can't generate queries for this task'.

Queries:
"""


def create_planner(template):
    llm = OpenAI(temperature=0, streaming=True)
    prompt_template = PromptTemplate(
        input_variables=['prompt'], template=template)

    chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)
    return chain


__all__ = ['create_planner', 'planner_template']
