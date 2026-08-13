from llm import agent
from uuid import uuid4

class Assistant:

    def __init__(self):
        self.agent = agent
        self.thread_id = str(uuid4())

    def run_agent(self, user_input: str) -> str:

        result = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": self.thread_id
                }
            }
        )

        return result["messages"][-1].content

    def chat(self):

        while True:

            user_message = input("\nТы: ").strip()

            if user_message.lower() == "exit":
                print("\nSystem: Сессия окончена!\n")
                break

            if user_message.lower() == "reset":
                self.thread_id = str(uuid4())
                print("\nSystem: История очищена!\n")
                continue

            try:
                answer = self.run_agent(user_message)
                print(f"\nAI: {answer}")

            except Exception as e:
                print(f"\nERROR: {e}")


if __name__ == "__main__":
    assistant = Assistant()
    assistant.chat()