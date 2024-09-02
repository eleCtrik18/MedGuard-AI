from fastapi import FastAPI
from api.api import api_router

app = FastAPI()

# Include the API router
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
