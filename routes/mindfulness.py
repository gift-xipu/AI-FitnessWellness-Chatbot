# app/routes/mindfulness.py
from fastapi import APIRouter, HTTPException
from models.mindfulness import MindfulnessRequest, MindfulnessResponse
from models.chat import ChatMessage, ChatResponse
from services.mindful_chat import MindfulnessChatbot

router = APIRouter()
mindful_bot = MindfulnessChatbot()

@router.post("/practice", response_model=MindfulnessResponse)
async def generate_practice(request: MindfulnessRequest):
    """
    Generate a mindfulness practice based on user's needs.
    """
    try:
        result = await mindful_bot.generate_mindfulness_practice(
            query=request.query,
            mood=request.mood,
            duration=request.duration
        )
        return MindfulnessResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating mindfulness practice: {str(e)}"
        )

@router.post("/chat", response_model=ChatResponse)
async def mindfulness_chat(message: ChatMessage):
    """
    Get mindfulness advice via chat interface.
    """
    try:
        result = await mindful_bot.get_mindfulness_response(message.message)
        return ChatResponse(
            response=result["response"],
            mode_used="mindfulness",
            confidence=result.get("confidence", 0.0)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing mindfulness chat: {str(e)}"
        )

