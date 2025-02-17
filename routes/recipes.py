# app/routes/recipes.py
from fastapi import APIRouter, HTTPException
from models.recipes import RecipeRequest, RecipeResponse
from models.chat import ChatMessage, ChatResponse
from services.recipe_gen import RecipeGenerator
import re

router = APIRouter()
recipe_bot = RecipeGenerator()

@router.post("/generate", response_model=RecipeResponse)
async def generate_recipe(request: RecipeRequest):
    """
    Generate a recipe based on ingredients, meal type, and dietary restrictions.
    """
    try:
        result = await recipe_bot.generate_recipe(
            ingredients=request.ingredients,
            meal_type=request.meal_type,
            dietary_restrictions=request.dietary_restrictions
        )
        return RecipeResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating recipe: {str(e)}"
        )

@router.post("/chat", response_model=ChatResponse)
async def recipe_chat(message: ChatMessage):
    """
    Get recipe advice via chat interface.
    """
    try:
        # Extract ingredients from message if possible
        ingredients = extract_ingredients(message.message)
        
        # Extract meal type from message if possible
        meal_type = extract_meal_type(message.message)
        
        result = await recipe_bot.generate_recipe_from_message(
            message=message.message,
            ingredients=ingredients,
            meal_type=meal_type
        )
        return ChatResponse(
            response=result["response"],
            mode_used="recipe",
            confidence=result.get("confidence", 0.0)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing recipe chat: {str(e)}"
        )

def extract_ingredients(message: str) -> list:
    # Simple extraction logic - can be enhanced with ML models
    ingredient_words = ["using", "with", "ingredients", "have"]
    for word in ingredient_words:
        if word in message.lower():
            parts = message.lower().split(word)
            if len(parts) > 1:
                # Extract potential ingredients
                ingredient_text = parts[1].strip()
                return [i.strip() for i in re.split(r',|and', ingredient_text) if i.strip()]
    return []

def extract_meal_type(message: str) -> str:
    meal_types = ["breakfast", "lunch", "dinner", "snack", "dessert"]
    for meal in meal_types:
        if meal in message.lower():
            return meal
    return None