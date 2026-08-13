from deepagents import create_deep_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

from tools import search
from prompts import SYSTEM_PROMPT


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

checkpointer = MemorySaver()

agent = create_deep_agent(
    model=llm,
    tools=[
        search
    ],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)