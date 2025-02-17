# app/routes/fitness.py
from fastapi import APIRouter, HTTPException
from models.fitness import FitnessRequest, FitnessResponse
from models.chat import ChatMessage, ChatResponse  
from services.fitness_chat import FitnessChatbot

router = APIRouter()
fitness_bot = FitnessChatbot()

@router.post("/workout", response_model=FitnessResponse)
async def generate_workout(request: FitnessRequest):
    """
    Generate a personalized workout plan based on user preferences and goals.
    """
    try:
        result = await fitness_bot.generate_workout_plan(
            query=request.query,
            goals=request.goals,
            fitness_level=request.fitness_level,
            age=request.age,
            weight=request.weight,
            height=request.height
        )
        return FitnessResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating workout plan: {str(e)}"
        )

@router.post("/chat", response_model=ChatResponse)
async def fitness_chat(message: ChatMessage):
    """
    Get fitness advice via chat interface.
    """
    try:
        result = await fitness_bot.get_fitness_response(message.message)
        return ChatResponse(
            response=result["response"],
            mode_used="fitness",
            confidence=result.get("confidence", 0.0)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing fitness chat: {str(e)}"
        )

