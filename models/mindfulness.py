# app/models/mindfulness.py
from pydantic import BaseModel
from typing import Optional, List

class MindfulnessRequest(BaseModel):
    query: str
    mood: Optional[str] = None
    duration: Optional[int] = None  # in minutes
    
class MindfulnessResponse(BaseModel):
    practice: Optional[str] = None
    description: str
    duration: Optional[int] = None
    confidence: float = 0.0