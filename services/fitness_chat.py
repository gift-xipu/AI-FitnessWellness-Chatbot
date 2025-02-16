from .chatbot import BaseChatbot

class FitnessChatbot(BaseChatbot):
    def __init__(self):
        super().__init__()
        self.system_prompt = """
        You are an expert fitness advisor with extensive knowledge in exercise science, 
        nutrition, and personal training. Provide clear, accurate, and safe fitness advice. 
        Your responses should be:
        - Evidence-based and scientifically accurate
        - Safety-conscious and appropriate for the user's needs
        - Practical and actionable
        - Encouraging and motivational
        
        If you don't have enough information to give specific advice, ask clarifying questions.
        Always emphasize the importance of proper form and starting gradually.
        """

    async def get_fitness_response(self, message: str) -> dict:
        """
        Get a fitness-specific response from the chatbot.
        
        Args:
            message (str): The user's fitness-related question or request
            
        Returns:
            Dict containing the response and confidence score
        """
        return await self.get_response(message, self.system_prompt)