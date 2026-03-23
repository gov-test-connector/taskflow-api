# taskflow-api

A lightweight Python REST API for managing tasks, projects, and deadlines.

## Features
- Create and manage tasks with priorities and due dates
- Organise tasks into projects
- Filter by status (open, in-progress, done)
- Simple REST interface via FastAPI

## Quick Start
`ash
pip install -r requirements.txt
uvicorn src.main:app --reload
`

## Endpoints
- GET /tasks — list all tasks
- GET /tasks/{id} — get a single task
- POST /tasks — create a task
- GET /projects — list all projects
- GET /health — health check
