# Setup Guide

## Prerequisites
- Python 3.10+
- pip

## Installation
`ash
git clone https://github.com/gov-test-connector/taskflow-api
cd taskflow-api
pip install -r requirements.txt
`

## Running the API
`ash
uvicorn src.main:app --reload
`

Visit http://localhost:8000/docs for the auto-generated Swagger UI.

## Running Tests
`ash
pytest tests/
`
