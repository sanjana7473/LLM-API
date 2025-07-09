from g4f.api import run_api
from fastapi import Request, HTTPException

API_KEY = "ghioipuygfhvbjyut78976r5tdfghvcxders45r6t7y8"

# Create FastAPI app from g4f
app = run_api()

# API key middleware
@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)
