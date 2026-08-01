from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage

from llm import llm



class Task(BaseModel):
    agent: Literal[
        "chat",
        "research",
        "code"
    ] = Field(
        description="Какой агент должен выполнить задачу"
    )

    description: str = Field(
        description="Что должен сделать агент"
    )



class Plan(BaseModel):

    goal: str = Field(
        description="Главная цель пользователя"
    )

    tasks: list[Task]



PLANNER_PROMPT = """
Ты Planner в многоагентной системе.

Ты НЕ отвечаешь пользователю.

Твоя задача:
проанализировать запрос и создать план выполнения.

Доступные агенты:

chat:
- объяснение
- перевод
- написание текста
- суммаризация
- обычные ответы

research:
- поиск информации
- интернет
- новости
- факты
- анализ источников

code:
- написание кода
- исправление ошибок
- анализ программ

Верни только JSON.

Формат:

{
 "goal": "цель пользователя",
 "tasks": [
   {
    "agent": "research",
    "description": "найти информацию"
   }
 ]
}


Правила:

1. tasks всегда список.
2. Минимум одна задача.
3. agent может быть только:
chat
research
code

Не добавляй другие поля.
"""



def planner(user_message: str) -> dict:


    structured_llm = llm.with_structured_output(
        Plan,
        method="json_mode"
    )


    result: Plan = structured_llm.invoke(
        [
            SystemMessage(
                content=PLANNER_PROMPT
            ),

            HumanMessage(
                content=user_message
            )
        ]
    )


    return result