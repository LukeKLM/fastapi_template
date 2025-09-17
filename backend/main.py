from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.routers.auth_routers import router as auth_router
from core.config import settings

app = FastAPI(
    title=settings.BACKEND_APP_NAME,
    swagger_ui_parameters={"persistAuthorization": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

