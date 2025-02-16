from fastapi import APIRouter, HTTPException
from models.chat import ChatResponse
from services.recipe_gen import RecipeGenerator
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
recipe_bot = RecipeGenerator()

class RecipeRequest(BaseModel):
    ingredients: List[str]
    meal_type: Optional[str] = None
    dietary_restrictions: Optional[List[str]] = None
    prep_time: Optional[int] = None

@router.post("/generate", response_model=ChatResponse)
async def generate_recipe(request: RecipeRequest):
    """
    Endpoint for generating recipes based on available ingredients and preferences.
    """
    try:
        result = await recipe_bot.generate_recipe(
            ingredients=request.ingredients,
            meal_type=request.meal_type,
            dietary_restrictions=request.dietary_restrictions,
            prep_time=request.prep_time
        )
        
        return ChatResponse(
            response=result["response"],
            mode_used="recipe_generation",
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating recipe: {str(e)}"
        )

@router.post("/meal-plan", response_model=ChatResponse)
async def generate_meal_plan(request: RecipeRequest):
    """
    Endpoint for generating a weekly meal plan based on preferences.
    """
    try:
        meal_plan_prompt = f"""
        Create a 7-day meal plan using these ingredients: {', '.join(request.ingredients)}
        
        {'Considering dietary restrictions: ' + ', '.join(request.dietary_restrictions) if request.dietary_restrictions else ''}
        {'Maximum prep time per meal: ' + str(request.prep_time) + ' minutes' if request.prep_time else ''}
        
        Please provide:
        1. Daily breakfast, lunch, and dinner suggestions
        2. Snack ideas
        3. Shopping list
        4. Meal prep tips
        5. Estimated daily caloric intake
        """
        
        result = await recipe_bot.get_response(meal_plan_prompt, recipe_bot.system_prompt)
        
        return ChatResponse(
            response=result["response"],
            mode_used="meal_plan_generation",
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating meal plan: {str(e)}"
        )