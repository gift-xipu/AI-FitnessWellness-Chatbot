from .chatbot import BaseChatbot

class MindfulnessChatbot(BaseChatbot):
    def __init__(self):
        super().__init__()
        self.system_prompt = """
        You are a compassionate mindfulness and wellness advisor with expertise in:
        - Meditation and breathing techniques
        - Stress management
        - Sleep hygiene
        - Emotional well-being
        - Work-life balance
        - Mental health awareness
        
        Provide gentle, supportive guidance while:
        - Respecting the user's emotional state
        - Offering practical, accessible techniques
        - Encouraging sustainable wellness habits
        - Being mindful of cultural sensitivity
        
        If someone appears to be in crisis, kindly remind them that you're not a substitute 
        for professional mental health support and encourage them to seek appropriate help.
        """

    async def get_mindfulness_response(self, message: str) -> dict:
        """
        Get a mindfulness-specific response from the chatbot.
        
        Args:
            message (str): The user's wellness-related question or concern
            
        Returns:
            Dict containing the response and confidence score
        """
        return await self.get_response(message, self.system_prompt)

    async def generate_meditation(self, duration: int, type: str) -> dict:
        """
        Generate a guided meditation script.
        
        Args:
            duration (int): Desired length of meditation in minutes
            type (str): Type of meditation (e.g., breathing, body scan, loving-kindness)
            
        Returns:
            Dict containing the meditation script and confidence score
        """
        meditation_prompt = f"""
        Create a {duration}-minute guided {type} meditation script.
        The script should be:
        - Clear and easy to follow
        - Calming and supportive in tone
        - Appropriate for the specified duration
        - Include appropriate pauses and timing cues
        """
        return await self.get_response(meditation_prompt, self.system_prompt)