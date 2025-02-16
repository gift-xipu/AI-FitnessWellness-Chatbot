from pydantic import BaseModel, Field
from typing import Optional, Literal

class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1, description="The user's message")
    mode: Optional[Literal["fitness", "mindfulness", "recipe", "general"]] = Field(
        default="general",
        description="The chat mode to use"
    )

class ChatResponse(BaseModel):
    response: str = Field(..., description="The chatbot's response")
    mode_used: str = Field(..., description="The mode that was used to generate the response")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score of the response")