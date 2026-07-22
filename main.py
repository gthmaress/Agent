from uuid import uuid4

from dotenv import load_dotenv
from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

from langgraph.checkpoint.memory import MemorySaver

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / "others" / ".env")

from tools import search
from state import User_profile, State

# LLM

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Добавляем инструменты модели
llm = llm.bind_tools([search])

# ChatBot Node

def chatbot(state: State):

    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }

# Tool Node

tool_node = ToolNode([search])

# Graph

graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chatbot")

graph.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph.add_edge("tools", "chatbot")

# Memory

memory = MemorySaver()

app = graph.compile(
    checkpointer=memory
)

class Assistant:

    def __init__(self):

        # Идентификатор текущего диалога.
        # По нему LangGraph хранит историю.
        self.thread_id = str(uuid4())

    def ask(self, question: str):

        system_prompt = """
        Отвечай только на русском.
        Используй интструменты только тогда, когда ты не знаешь овтета.
        Не придумывый овтеты.
        """


        result = app.invoke(
            {
                "messages": [
                    SystemMessage(content=system_prompt), HumanMessage(content=question)
                ]
            },
            config={
                "configurable": {
                    "thread_id": self.thread_id
                }
            }
        )

        return result["messages"][-1].content

    def reset(self):

        # Новый thread_id = новый разговор
        self.thread_id = str(uuid4())

    def chat(self):

        print("\nВведите 'exit' для выхода.")
        print("Введите '/reset' для новой истории.\n")

        while True:

            question = input("Ты: ")

            if question.lower() == "exit":
                print("\nСессия завершена.")
                break

            if question.lower() == "/reset":
                self.reset()
                print("\nИстория очищена.\n")
                continue

            answer = self.ask(question)

            print(f"AI: {answer}\n")

if __name__ == "__main__":

    assistant = Assistant()
    assistant.chat()