from typing import Any
from typing_extensions import TypedDict
from typing import Annotated

from langchain_core.documents import Document
from langgraph.graph.message import add_messages

class User_profile(TypedDict):

    name: str

    language: str

    interests: list[str]

class State(TypedDict):

    messages: Annotated[list, add_messages]

    current_task: str 

    plan: list[str]

    documents: list[Document]

    user_profile: User_profile

    repository_files: list[str]

    issues: list[str]

    summary: str 

    total_cost: float

    artifacts: dict[str, Any]
