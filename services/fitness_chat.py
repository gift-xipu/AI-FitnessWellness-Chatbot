# app/services/fitness_chat.py
from openai import OpenAI
from utils.config import settings
import json

class FitnessChatbot:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME
        
    async def get_fitness_response(self, message: str) -> dict:
        """
        Generate a fitness-focused response to the user's message.
        """
        system_prompt = """
        You are a knowledgeable fitness trainer who provides personalized advice
        on workouts, exercise techniques, and fitness goals. Respond with accurate
        information tailored to the user's needs. Keep responses focused on fitness.
        
        When providing workout advice, consider:
        1. Safety first - recommend proper form and suitable exercises
        2. Progressive overload principles
        3. Rest and recovery importance
        4. Nutrition basics as they relate to fitness goals
        
        Always encourage users to consult medical professionals before starting new programs.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                temperature=0.7
            )
            
            return {
                "response": response.choices[0].message.content,
                "confidence": 0.9  # Placeholder - implement proper confidence scoring
            }
            
        except Exception as e:
            raise Exception(f"Error in fitness response: {str(e)}")
    
    async def generate_workout_plan(self, query: str, goals: str = None, 
                               fitness_level: str = None, age: int = None,
                               weight: float = None, height: float = None) -> dict:
        """
        Generate a structured workout plan based on user parameters.
        """
        # Compile user information into a comprehensive prompt
        user_info = f"Query: {query}\n"
        if goals:
            user_info += f"Goals: {goals}\n"
        if fitness_level:
            user_info += f"Fitness Level: {fitness_level}\n"
        if age:
            user_info += f"Age: {age}\n"
        if weight:
            user_info += f"Weight: {weight}\n"
        if height:
            user_info += f"Height: {height}\n"
        
        system_prompt = """
        You are a certified personal trainer who specializes in creating personalized
        workout plans. Based on the user's information, create a detailed workout plan
        that includes:
        
        1. A title for the workout plan
        2. A brief description explaining the focus and benefits
        3. A list of exercises with sets, reps, and rest periods
        4. Total duration for the workout
        5. Intensity level (beginner, intermediate, advanced)
        
        The response should be formatted as JSON with the following structure:
        {
          "workout_plan": {
            "title": "string",
            "description": "string",
            "exercises": [
              {
                "name": "string",
                "sets": integer,
                "reps": integer or "string" (for time-based exercises),
                "rest": "string",
                "notes": "string (optional)"
              }
            ],
            "duration": "string",
            "intensity": "string"
          },
          "advice": "string (additional personalized advice)",
          "confidence": float (between 0 and 1)
        }
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_info}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            return json.loads(response.choices[0].message.content)
            
        except Exception as e:
            raise Exception(f"Error generating workout plan: {str(e)}")
    
    async def get_response(self, message: str, custom_prompt: str) -> dict:
        """
        Generate a response with a custom system prompt.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": custom_prompt},
                    {"role": "user", "content": message}
                ],
                temperature=0.7
            )
            
            return {
                "response": response.choices[0].message.content,
                "confidence": 0.8  # Placeholder
            }
            
        except Exception as e:
            raise Exception(f"Error in custom response: {str(e)}")

