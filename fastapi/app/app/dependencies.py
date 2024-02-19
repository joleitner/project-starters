from typing import Annotated, Generator

from fastapi import Depends
# from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.db.engine import engine


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db() -> Generator:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
# TokenDep = Annotated[str, Depends(oauth2_scheme)]
