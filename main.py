from llm import agent
from agents.planner import planner
from uuid import uuid4

class Assistant:

    def __init__(self):

        self.agent = agent
        self.thread_id = str(uuid4())

    def run_agent(self, user_input):

        plan = planner(user_input)

        print(f"PLAN: \n{plan}")
        
        task = plan.tasks[0]

        executor_prompt = f"""

            Ты - исполнитель. 

            Тебе назначена задача.

            Тип агента:
            {task.agent}


            Задача:
            {task.description}

            Выполни её.

        """
        
        result = self.agent.invoke(
            {
               "messages": [
                   {
                       "role": "user",
                       "content": executor_prompt
                   }, 
               ]    
            },
            
            config = {
                "configurable": {
                    "thread_id": self.thread_id
                }
            }
        )

        return result


    def chat(self):

        while True:

            user_message = input("\nTы: ")

            if user_message == "exit":
                        
                print("\nSystem: Сессия окончена!\n")
                        
                break

            if user_message == "/reset":

                self.thread_id = str(uuid4())
                        
                print("\nSystem: История очищена!\n")
                        
                continue

            answer = self.run_agent(user_message)

            print(f"AI: {answer["messages"][-1].content}")
            
if __name__ == "__main__":
    
    assistant = Assistant()
    assistant.chat()

