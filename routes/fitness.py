from fastapi import APIRouter, HTTPException
from models.chat import ChatMessage, ChatResponse
from services.fitness_chat import FitnessChatbot

router = APIRouter()
fitness_bot = FitnessChatbot()

@router.post("/chat", response_model=ChatResponse)
async def fitness_chat(message: ChatMessage):
    """
    Endpoint for fitness-related chat interactions.
    """
    try:
        # Get response from fitness chatbot
        result = await fitness_bot.get_fitness_response(message.message)
        
        return ChatResponse(
            response=result["response"],
            mode_used="fitness",
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing fitness chat: {str(e)}"
        )

@router.post("/analyze_routine")
async def analyze_workout_routine(message: ChatMessage):
    """
    Endpoint for analyzing workout routines and providing feedback.
    """
    try:
        analysis_prompt = f"""
        Please analyze this workout routine and provide feedback:
        {message.message}
        
        Consider:
        - Exercise selection and balance
        - Volume and intensity
        - Rest and recovery
        - Potential improvements
        """
        
        result = await fitness_bot.get_fitness_response(analysis_prompt)
        
        return ChatResponse(
            response=result["response"],
            mode_used="fitness_analysis",
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing workout routine: {str(e)}"
        )