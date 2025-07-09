from g4f.api import run_api
from fastapi import Request, HTTPException
import os

API_KEY = "ghioipuygfhvbjyut78976r5tdfghvcxders45r6t7y8"

# Create the g4f FastAPI app
app = run_api()

# Add API key authentication middleware
@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)
