from agents.openai_agent import OpenAIAgent
from agents.pydantic_agent import PydanticAgent
from dotenv import load_dotenv
load_dotenv()

def main():
    query = "How does journaling help reduce anxiety and improve emotional health?"

    agent1 = OpenAIAgent()
    raw_output = agent1.run(query)
    print("\n📘 OpenAIAgent Response:\n", raw_output)

    agent2 = PydanticAgent()
    structured_output = agent2.run(raw_output)
    print("\n📊 PydanticAgent Structured Summary:")
    print("Tone:", structured_output.emotional_tone)
    print("Key Points:", structured_output.key_points)
    print("Advice:", structured_output.therapist_style_advice)

if __name__ == "__main__":
    main()
