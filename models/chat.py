# app/models/chat.py
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union

class ChatMessage(BaseModel):
    message: str
    mode: Optional[str] = None  # 'fitness', 'mindfulness', 'recipe', or 'general'
    
class ChatResponse(BaseModel):
    response: str
    mode_used: str
    confidence: float = 0.0