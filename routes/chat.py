# app/routes/chat.py
from fastapi import APIRouter, HTTPException
from models.chat import ChatMessage, ChatResponse
from services.fitness_chat import FitnessChatbot
from services.mindful_chat import MindfulnessChatbot
from services.recipe_gen import RecipeGenerator
from utils.config import settings
from openai import OpenAI
import json

router = APIRouter()

# Initialize chatbots
fitness_bot = FitnessChatbot()
mindful_bot = MindfulnessChatbot()
recipe_bot = RecipeGenerator()

class ChatRouter:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
    async def classify_message(self, message: str) -> str:
        """
        Classify the message to determine which chatbot should handle it.
        """
        classification_prompt = """
        Analyze the following message and determine which category it best fits into:
        - fitness: Exercise, workouts, physical activity, sports, body building, weight loss
        - mindfulness: Mental health, meditation, stress, anxiety, sleep, emotional well-being
        - recipe: Cooking, food, nutrition, meal planning, ingredients, dietary advice
        
        Respond with only one word: 'fitness', 'mindfulness', or 'recipe'.
        
        Message: """
        
        try:
            response = self.client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    {"role": "system", "content": classification_prompt},
                    {"role": "user", "content": message}
                ],
                temperature=0.3,
                max_tokens=10
            )
            
            category = response.choices[0].message.content.strip().lower()
            return category if category in ['fitness', 'mindfulness', 'recipe'] else 'general'
            
        except Exception as e:
            print(f"Error in message classification: {str(e)}")
            return 'general'

chat_router = ChatRouter()

@router.post("/", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """
    Main chat endpoint that routes messages to appropriate specialized chatbots.
    """
    try:
        # If mode is specified, use that directly
        mode = message.mode
        
        # If mode is 'general' or not specified, classify the message
        if mode == "general" or mode is None:
            mode = await chat_router.classify_message(message.message)
        
        # Route to appropriate chatbot
        if mode == "fitness":
            result = await fitness_bot.get_fitness_response(message.message)
        elif mode == "mindfulness":
            result = await mindful_bot.get_mindfulness_response(message.message)
        elif mode == "recipe":
            result = await recipe_bot.generate_recipe(
                ingredients=[],  # Extract ingredients from message if possible
                meal_type=None  # Extract meal type from message if possible
            )
        else:
            # Default to a general response combining all domains
            general_prompt = """
            You are a wellness assistant with expertise in fitness, mindfulness, and nutrition.
            Provide helpful advice drawing from any or all of these domains as appropriate.
            """
            result = await fitness_bot.get_response(message.message, general_prompt)
        
        return ChatResponse(
            response=result["response"],
            mode_used=mode,
            confidence=result.get("confidence", 0.0)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing chat message: {str(e)}"
        )

@router.post("/analyze")
async def analyze_message(message: ChatMessage):
    """
    Analyze a message to determine its category without generating a response.
    """
    try:
        category = await chat_router.classify_message(message.message)
        return {"category": category}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing message: {str(e)}"
        )

