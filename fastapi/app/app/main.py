from fastapi import FastAPI
from app.routers import users, auth
from app.core.config import settings
# from app.dependencies import TokenDep

app = FastAPI(
    title=settings.APP_NAME,
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, tags=["auth"])


@app.get("/")
async def root():
    return {"message": f"Hello World from {settings.APP_NAME}"}
