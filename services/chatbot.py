from openai import OpenAI
from utils.config import settings
from typing import Dict, Any

class BaseChatbot:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME
        self.temperature = settings.TEMPERATURE
        self.max_tokens = settings.MAX_TOKENS

    async def get_response(self, message: str, system_prompt: str) -> Dict[str, Any]:
        """
        Get a response from the chatbot using the OpenAI API.
        
        Args:
            message (str): The user's message
            system_prompt (str): The system prompt to guide the AI's behavior
            
        Returns:
            Dict containing the response text and confidence score
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            return {
                "response": response.choices[0].message.content,
                "confidence": 1 - (response.choices[0].finish_reason == "length")
            }
            
        except Exception as e:
            print(f"Error in getting chatbot response: {str(e)}")
            raise