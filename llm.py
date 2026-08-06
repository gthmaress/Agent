from deepagents import create_deep_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

from tools import search

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

checkpointer = MemorySaver()

agent = create_deep_agent(

    model = llm, 

    tools = [
        search
    ],

    checkpointer = checkpointer
)   