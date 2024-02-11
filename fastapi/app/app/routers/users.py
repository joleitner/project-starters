from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("")
def create_user():
    return {"message": "User created"}


@router.get("")
def get_users():
    return {"message": "List of users"}
