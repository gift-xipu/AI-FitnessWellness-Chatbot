# app/models/fitness.py
from pydantic import BaseModel
from typing import Optional, List

class FitnessRequest(BaseModel):
    query: str
    goals: Optional[str] = None
    fitness_level: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    
class WorkoutPlan(BaseModel):
    title: str
    description: str
    exercises: List[dict]
    duration: str
    intensity: str
    
class FitnessResponse(BaseModel):
    workout_plan: Optional[WorkoutPlan] = None
    advice: str
    confidence: float = 0.0