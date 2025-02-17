from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat, fitness, mindfulness, recipes

app = FastAPI(
    title="AI Fitness & Wellness API",
    description="""
    AI-powered fitness, mindfulness, and recipe recommendations.
    
    Example queries for each category:
    
    Fitness:
    - "What's a good workout routine for beginners?"
    - "How can I improve my running endurance?"
    - "What exercises target core muscles?"
    
    Mindfulness:
    - "I'm feeling stressed at work, what can I do?"
    - "Help me with a 5-minute meditation"
    - "Tips for better sleep?"
    
    Recipe:
    - "Healthy breakfast ideas with oats"
    - "Quick vegetarian dinner recipes"
    - "What can I cook with chicken and vegetables?"
    
    You can either:
    1. Specify the mode explicitly (fitness/mindfulness/recipe)
    2. Use general chat and let the AI determine the best category
    """,
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(fitness.router, prefix="/api/fitness", tags=["fitness"])
app.include_router(mindfulness.router, prefix="/api/mindfulness", tags=["mindfulness"])
app.include_router(recipes.router, prefix="/api/recipes", tags=["recipes"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to the AI Fitness & Wellness API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)