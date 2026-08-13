from deepagents import create_deep_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver

from config import settings
from tools import search
from prompts import SYSTEM_PROMPT


llm = ChatGroq(
    model=settings.model_name,
    api_key=settings.groq_api_key,
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