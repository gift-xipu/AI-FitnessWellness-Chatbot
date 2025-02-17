# app/services/mindful_chat.py
from openai import OpenAI
from utils.config import settings
import json

class MindfulnessChatbot:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME
    
    async def get_mindfulness_response(self, message: str) -> dict:
        """
        Generate a mindfulness-focused response to the user's message.
        """
        system_prompt = """
        You are a compassionate mindfulness coach who provides guidance on meditation,
        stress reduction, emotional well-being, and mental health practices. Respond with
        empathy and suggest evidence-based mindfulness techniques tailored to the user's needs.
        
        When providing mindfulness advice, consider:
        1. The user's current emotional state
        2. Appropriate practices based on their situation
        3. Easy-to-implement techniques for beginners
        4. Scientific basis for recommendations when relevant
        
        Always encourage users to seek professional help for serious mental health concerns.
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
                "confidence": 0.9  # Placeholder
            }
            
        except Exception as e:
            raise Exception(f"Error in mindfulness response: {str(e)}")
    
    async def generate_mindfulness_practice(self, query: str, mood: str = None, 
                                      duration: int = None) -> dict:
        """
        Generate a structured mindfulness practice based on user parameters.
        """
        # Compile user information
        user_info = f"Query: {query}\n"
        if mood:
            user_info += f"Current Mood: {mood}\n"
        if duration:
            user_info += f"Preferred Duration: {duration} minutes\n"
        
        system_prompt = """
        You are a mindfulness instructor who specializes in creating personalized
        practices. Based on the user's information, create a detailed mindfulness
        practice that includes:
        
        1. A brief description of the practice and its benefits
        2. Step-by-step instructions
        3. Recommended duration
        
        The response should be formatted as JSON with the following structure:
        {
          "practice": "string (title of practice)",
          "description": "string (detailed guidance)",
          "duration": integer (minutes),
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
            raise Exception(f"Error generating mindfulness practice: {str(e)}")

