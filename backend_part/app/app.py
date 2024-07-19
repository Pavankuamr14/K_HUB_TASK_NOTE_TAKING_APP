from beanie import init_beanie
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.todo_model import Notes
from app.core.config import settings
from app.api.api_v1.router import router
from pydantic import BaseModel
from app.models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserLogin(BaseModel):
    email: str
    password: str


@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    db = db_client["note_taking_app"]  # Access the database named "note_taking_app"

    await init_beanie(database=db, document_models=[User, Notes])


app.include_router(router, prefix=settings.API_V1_STR)
