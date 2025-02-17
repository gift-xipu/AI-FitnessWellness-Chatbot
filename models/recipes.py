# app/models/recipes.py
from pydantic import BaseModel
from typing import Optional, List

class RecipeRequest(BaseModel):
    ingredients: Optional[List[str]] = []
    meal_type: Optional[str] = None
    dietary_restrictions: Optional[List[str]] = []
    message: Optional[str] = None
    
class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    instructions: List[str]
    prep_time: str
    cook_time: str
    servings: int
    nutrition: Optional[dict] = None
    
class RecipeResponse(BaseModel):
    recipe: Recipe
    confidence: float = 0.0