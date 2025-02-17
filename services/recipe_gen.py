# app/services/recipe_gen.py
from openai import OpenAI
from utils.config import settings
from typing import List, Optional
import json

class RecipeGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME
    
    async def generate_recipe(self, ingredients: List[str] = None, 
                        meal_type: str = None, 
                        dietary_restrictions: List[str] = None) -> dict:
        """
        Generate a recipe based on ingredients, meal type, and dietary restrictions.
        """
        # Compile recipe constraints
        if ingredients is None:
            ingredients = []
        if dietary_restrictions is None:
            dietary_restrictions = []
            
        recipe_constraints = ""
        if ingredients:
            recipe_constraints += f"Ingredients to use: {', '.join(ingredients)}\n"
        if meal_type:
            recipe_constraints += f"Meal type: {meal_type}\n"
        if dietary_restrictions:
            recipe_constraints += f"Dietary restrictions: {', '.join(dietary_restrictions)}\n"
        
        system_prompt = """
        You are a professional chef who specializes in creating delicious, healthy recipes.
        Based on the constraints provided, create a recipe that is both nutritious and tasty.
        
        Your recipe should include:
        1. A creative title
        2. Complete list of ingredients with measurements
        3. Step-by-step cooking instructions
        4. Preparation and cooking time
        5. Number of servings
        6. Nutritional information (calories, protein, carbs, fat)
        
        The response should be formatted as JSON with the following structure:
        {
          "recipe": {
            "title": "string",
            "ingredients": ["string", "string", ...],
            "instructions": ["string", "string", ...],
            "prep_time": "string",
            "cook_time": "string",
            "servings": integer,
            "nutrition": {
              "calories": integer,
              "protein": "string",
              "carbs": "string",
              "fat": "string"
            }
          },
          "confidence": float (between 0 and 1)
        }
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": recipe_constraints or "Generate a healthy recipe"}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            return json.loads(response.choices[0].message.content)
            
        except Exception as e:
            raise Exception(f"Error generating recipe: {str(e)}")
    
    async def generate_recipe_from_message(self, message: str, 
                                    ingredients: List[str] = None,
                                    meal_type: str = None) -> dict:
        """
        Generate a recipe based on a free-form chat message.
        """
        system_prompt = """
        You are a professional chef who specializes in creating delicious, healthy recipes.
        Analyze the user's message and provide an appropriate recipe that addresses their request.
        
        If the message contains specific ingredients, meal type, or dietary preferences,
        incorporate these into your recipe suggestion.
        
        Provide your response in a conversational format, including:
        1. A brief introduction to the recipe
        2. The ingredients list
        3. Simple cooking instructions
        4. Any helpful tips
        
        Make the recipe accessible for home cooks of all skill levels.
        """
        
        additional_info = ""
        if ingredients:
            additional_info += f"\nI've identified these ingredients in your request: {', '.join(ingredients)}"
        if meal_type:
            additional_info += f"\nI see you're looking for a {meal_type} recipe."
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message + additional_info}
                ],
                temperature=0.7
            )
            
            return {
                "response": response.choices[0].message.content,
                "confidence": 0.85  # Placeholder
            }
            
        except Exception as e:
            raise Exception(f"Error in recipe chat response: {str(e)}")