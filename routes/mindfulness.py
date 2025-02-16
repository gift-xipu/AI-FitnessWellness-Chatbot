from fastapi import APIRouter, HTTPException
from models.chat import ChatMessage, ChatResponse
from services.mindful_chat import MindfulnessChatbot
from pydantic import BaseModel
from typing import Literal

router = APIRouter()
mindful_bot = MindfulnessChatbot()

class MeditationRequest(BaseModel):
    duration: int
    type: Literal["breathing", "body-scan", "loving-kindness", "mindfulness", "sleep"]

@router.post("/chat", response_model=ChatResponse)
async def mindfulness_chat(message: ChatMessage):
    """
    Endpoint for mindfulness and wellness-related chat interactions.
    """
    try:
        result = await mindful_bot.get_mindfulness_response(message.message)
        
        return ChatResponse(
            response=result["response"],
            mode_used="mindfulness",
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing mindfulness chat: {str(e)}"
        )

@router.post("/meditation", response_model=ChatResponse)
async def generate_meditation(request: MeditationRequest):
    """
    Endpoint for generating guided meditation scripts.
    """
    try:
        result = await mindful_bot.generate_meditation(
            duration=request.duration,
            type=request.type
        )
        
        return ChatResponse(
            response=result["response"],
            mode_used=f"meditation_{request.type}",
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating meditation: {str(e)}"
        )