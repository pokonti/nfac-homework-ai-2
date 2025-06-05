from pydantic import BaseModel

class SummaryOutput(BaseModel):
    emotional_tone: str
    key_points: list[str]
    therapist_style_advice: str
