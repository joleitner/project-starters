from fastapi import APIRouter, HTTPException

from app.dependencies import SessionDep, TokenDep, CurrentUser
from app.models import UserCreate, User, UserOut
from app import crud

router = APIRouter()


@router.post("", response_model=UserOut)
def create_user(db: SessionDep, user_create: UserCreate):
    """Create a new user."""
    
    user = crud.user.get_by_email(db, email=user_create.email)
    if user:
        return HTTPException(status_code=400, detail="Email already registered")
    
    user = crud.user.create(db, user_create=user_create)
    
    return user


@router.get("/me", response_model=UserOut)
def read_users_me(current_user: CurrentUser):
    return current_user


@router.get("/{user_id}", response_model=UserOut)
def get_users(user_id: int, db: SessionDep):
    return crud.user.get(db, user_id=user_id)

