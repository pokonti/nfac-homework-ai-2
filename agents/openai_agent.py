from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

class OpenAIAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini")

    def run(self, query: str) -> str:
        messages = [HumanMessage(content=query)]
        response = self.llm.invoke(messages)
        return response.content
