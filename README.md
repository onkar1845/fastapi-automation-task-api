# FastAPI Automation Task API

A beginner-friendly FastAPI project built to practice backend concepts useful for AI Automation.

## Features

- FastAPI REST API
- Pydantic request validation
- `Field()` validation rules
- API-key authentication
- Environment variables using `.env`
- Dependency injection using `Depends()`
- Async external API calls using `httpx`
- Error handling using `HTTPException`
- Response models
- Background task logging

## Project Flow

Client / n8n / Postman  
↓  
POST `/process_task`  
↓  
API Key Authentication  
↓  
Pydantic Validation  
↓  
External API Call  
↓  
Fetch User Data  
↓  
Combine Task + User Data  
↓  
Structured JSON Response  
↓  
Background Logging

## Request Example

```json
{
  "user_id": 2,
  "task": "Process customer request",
  "priority": 3
}




Header:

X-API-Key: created-api-key

Response Example
{
  "user_id": 2,
  "user_name": "Onkar Koli",
  "email": "onkar@example.tv",
  "task": "Process customer request",
  "priority": 3,
  "message": "Task processed"
}

Validation Rules
user_id must be greater than 0
task must contain at least 5 characters
priority must be between 1 and 5

Environment Setup

Create a .env file:

API_KEY=created-secret-api-key


Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL
cd fastapi-automation-task-api

Install dependencies:

pip install -r requirements.txt

Run the FastAPI application:

fastapi dev main.py

Open Swagger documentation:

http://127.0.0.1:8000/docs

Technologies Used
Python
FastAPI
Pydantic
HTTPX
python-dotenv
Uvicorn

Concepts Practiced
REST API creation
GET / POST endpoints
Request and response models
Path and query parameters
API authentication
Dependency injection
Async / await
Calling external APIs
Error handling
Background tasks

AI Automation Relevance

This project demonstrates the backend pattern commonly used in AI Automation:

Client / n8n
    ↓
FastAPI
    ↓
Validation + Authentication
    ↓
External API / AI Service
    ↓
Structured Response
    ↓
Automation Workflow

The external API used in this project can later be replaced with an LLM API such as OpenAI or Gemini.

Author

Onkar Koli


