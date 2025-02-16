from .chatbot import BaseChatbot
from typing import List, Optional

class RecipeGenerator(BaseChatbot):
    def __init__(self):
        super().__init__()
        self.system_prompt = """
        You are an experienced chef and nutritionist who creates delicious, 
        healthy recipes. Your recipes should be:
        - Clear and easy to follow
        - Nutritionally balanced
        - Adaptable to different dietary requirements
        - Include preparation times, cooking times, and serving sizes
        - List complete ingredients with measurements
        - Provide step-by-step cooking instructions
        - Include nutritional information when possible
        
        Always consider food safety and proper cooking techniques.
        """

    async def generate_recipe(
        self,
        ingredients: List[str],
        meal_type: Optional[str] = None,
        dietary_restrictions: Optional[List[str]] = None,
        prep_time: Optional[int] = None
    ) -> dict:
        """
        Generate a recipe based on provided ingredients and constraints.
        
        Args:
            ingredients: List of available ingredients
            meal_type: Type of meal (breakfast, lunch, dinner, snack)
            dietary_restrictions: List of dietary restrictions
            prep_time: Maximum preparation time in minutes
            
        Returns:
            Dict containing the recipe and confidence score
        """
        recipe_prompt = f"""
        Create a recipe using these ingredients: {', '.join(ingredients)}
        
        {'Meal type: ' + meal_type if meal_type else ''}
        {'Dietary restrictions: ' + ', '.join(dietary_restrictions) if dietary_restrictions else ''}
        {'Maximum prep time: ' + str(prep_time) + ' minutes' if prep_time else ''}
        
        Please provide:
        1. Recipe name
        2. Serving size
        3. Preparation time
        4. Cooking time
        5. Ingredients list with measurements
        6. Step-by-step instructions
        7. Nutritional information (approximate)
        8. Any tips or variations
        """
        
        return await self.get_response(recipe_prompt, self.system_prompt)