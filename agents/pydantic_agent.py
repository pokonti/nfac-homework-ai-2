import json
from pydantic_ai import Agent
from models import SummaryOutput

class PydanticAgent:
    def __init__(self):
        self.agent = Agent(
            model='google-gla:gemini-1.5-flash',
            output_model=SummaryOutput,
            system_prompt="""
You are a therapist assistant. Respond ONLY in valid JSON format.

Return exactly:
{
  "emotional_tone": "string",
  "key_points": ["point 1", "point 2", "..."],
  "therapist_style_advice": "string"
}

Do not include any text before or after the JSON.
Do not use markdown or triple backticks.
"""
        )

    def run(self, input_text: str) -> SummaryOutput:
        result = self.agent.run_sync(input_text)
        output = result.output

        if isinstance(output, SummaryOutput):
            return output

        try:
            parsed = json.loads(output)
            return SummaryOutput(**parsed)
        except Exception as e:
            raise ValueError("Failed to parse structured response:\n" + str(output)) from e


