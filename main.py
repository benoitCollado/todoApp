import uvicorn
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import setttings
from app.database import engine
from sqlmodel import SQLModel

app = FastAPI(
    title = setttings.PROJECT_NAME,
    version = settings.VERSION,
    description =  "API évolutive et asynchrone pour la gestiond e tâches "
)

app.includes_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return{"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)