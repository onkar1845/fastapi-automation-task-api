# FastAPI Automation Task API

A backend automation project built with FastAPI to practice the core API patterns used in AI Automation systems.

This was my first structured backend automation project and helped me build the foundation for working with external APIs, authentication, async processing, validation, and structured responses.

## What it does

The API receives an automation task, validates and authenticates the request, fetches user information from an external REST API, combines the external data with the incoming task, and returns a structured response.

## Why I Built This Project

Before integrating LLMs and AI services, I wanted to understand the backend flow that powers automation systems:

```text
Receive Request
→ Validate Data
→ Authenticate Client
→ Call External Service
→ Process Response
→ Return Structured Output
→ Run Follow-up Task
```

These same backend concepts are later used when integrating services such as Gemini, OpenAI, n8n, CRMs, databases, and other automation tools.

## Features

- FastAPI REST endpoint
- Pydantic request validation
- `Field()` validation rules
- API-key authentication
- Environment variables using `.env`
- Dependency injection using `Depends()`
- Async external API calls using HTTPX
- Structured response models
- External API error handling
- Background task logging

## Architecture

```text
Client / Postman / n8n
        ↓
POST /process_task
        ↓
API Key Authentication
        ↓
Pydantic Validation
        ↓
External REST API
        ↓
Fetch User Information
        ↓
Combine User + Task Data
        ↓
Structured JSON Response
        ↓
Background Logging
```

## Example Request

```json
{
  "user_id": 2,
  "task": "Process customer request",
  "priority": 3
}
```

## Request Header

```text
X-API-Key: created-api-key
```

## Example Response

```json
{
  "user_id": 2,
  "user_name": "Onkar Koli",
  "email": "onkar@example.tv",
  "task": "Process customer request",
  "priority": 3,
  "message": "Task processed"
}
```

## Validation Rules

- `user_id` must be greater than `0`
- `task` must contain at least `5` characters
- `priority` must be between `1` and `5`

## Tech Stack

- Python
- FastAPI
- Pydantic
- HTTPX
- REST APIs
- python-dotenv
- Uvicorn

## Key Concepts Practiced

- REST API development
- Request and response models
- Pydantic validation
- API authentication
- Dependency injection
- `async` / `await`
- External API integration
- Error handling
- Background tasks
- Environment-based secret management

## AI Automation Relevance

This project does not currently use an LLM.

Its purpose is to demonstrate the backend foundation required for AI Automation applications.

A future AI-powered version could follow:

```text
Client / n8n
→ FastAPI
→ Validation
→ Authentication
→ LLM / External AI Service
→ Structured Output
→ Business Logic
→ Automation Workflow
```

The same architecture can be extended with Gemini, OpenAI, databases, n8n workflows, or other external services.

## Environment Setup

Create a `.env` file:

```env
API_KEY=your-api-key
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd fastapi-automation-task-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
fastapi dev main.py
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Security

Secrets are stored using environment variables.

The real `.env` file is excluded from GitHub using `.gitignore`.

```text
.env
.venv/
__pycache__/
*.pyc
```

## What I Learned

This project helped me understand how a backend automation service:

- receives and validates structured input
- protects endpoints using API authentication
- communicates with external APIs asynchronously
- handles failures safely
- returns predictable structured responses
- performs follow-up work using background tasks

These concepts became the foundation for my later LLM and Generative AI projects.

## Current Status

Core backend automation functionality is complete.

## Future Improvements

- Connect with n8n workflows
- Add LLM API integration
- Add database persistence
- Add structured AI output
- Deploy the API

## Author

**Onkar Koli**
