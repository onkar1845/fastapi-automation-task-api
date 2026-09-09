from fastapi import FastAPI, Header, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import httpx

# Load environment variables
load_dotenv()

# Read API key from .env
API_KEY = os.getenv("API_KEY")

# Create FastAPI application
app = FastAPI()


# Request body model
class TaskRequest(BaseModel):
    user_id: int = Field(gt=0)
    task: str = Field(min_length=5)
    priority: int = Field(ge=1, le=5)


# Response model
class TaskResponse(BaseModel):
    user_id: int
    user_name: str
    email: str
    task: str
    priority: int
    message: str


# Background function
# Runs after API response is sent
def save_log(user_id: int, task: str):
    print("Task processed for user:", user_id)
    print("Task:", task)


# Reusable API-key authentication
def verify_api_key(
    x_api_key: str | None = Header(default=None)
):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return x_api_key


# Main automation endpoint
@app.post("/process_task", response_model=TaskResponse)
async def process_task(
    task_data: TaskRequest,
    background_tasks: BackgroundTasks,
    api_key: str = Depends(verify_api_key)
):

    # Build external API URL using user_id
    url = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{task_data.user_id}"
    )

    try:
        # Call external API asynchronously
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5)

        # Check external API response
        if response.status_code != 200:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Convert external JSON response into Python data
        user_data = response.json()

        # Schedule background task BEFORE return
        background_tasks.add_task(
            save_log,
            task_data.user_id,
            task_data.task
        )

        # Send clean response to client
        return {
            "user_id": task_data.user_id,
            "user_name": user_data["name"],
            "email": user_data["email"],
            "task": task_data.task,
            "priority": task_data.priority,
            "message": "Task processed"
        }

    # Handle network / timeout / connection errors
    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="External service unavailable"
        )