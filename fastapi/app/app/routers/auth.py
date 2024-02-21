from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status

from app.dependencies import SessionDep, OAuth2FormDep
from app.core.security import create_access_token
from app.models import UserCreate, User, UserOut, Token
from app import crud

router = APIRouter()

@router.post("/login")
async def login(db: SessionDep, form_data: OAuth2FormDep):
    user = crud.user.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.email})
    
    return Token(access_token=access_token, token_type="bearer")
    