from typing import Annotated, Generator
from pydantic import ValidationError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from sqlmodel import Session

from app.db.engine import engine
from app.models import User, TokenPayload
from app.core.config import settings
from app.core import security
from app import crud


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db() -> Generator:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(oauth2_scheme)]
OAuth2FormDep = Annotated[OAuth2PasswordRequestForm, Depends()]


async def get_current_user(db: SessionDep, token: TokenDep) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Could not validate credentials"
            )
    user = crud.user.get_by_email(db, email=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
            )
    return user
    
    
CurrentUser = Annotated[User, Depends(get_current_user)]