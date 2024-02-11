from fastapi import FastAPI
from app.routers import users
from app.dependencies import TokenDep

app = FastAPI()

app.include_router(users.router)


@app.get("/")
async def root(token: str = TokenDep):
    return {"message": "Hello World"}
