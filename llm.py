from deepagents import create_deep_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

from tools import search

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

agent = create_deep_agent(

    model = llm, 

    tools = [
        search
    ],

    system_prompt = """

    Ты исполнитель.

Тебе приходит задача от Planner.

Выполни только эту задачу.

Если нужна информация -
используй инструменты.

Не создавай новый план.

"""
)   