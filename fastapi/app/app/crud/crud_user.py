from typing import Optional

from sqlmodel import Session, select
from app.models import User, UserCreate

class CRUDUser:
    
    def create(self, db: Session, *, user_create: UserCreate) -> User:
        db_user = User(
            email=user_create.email,
            hashed_password=user_create.password,
            firstname=user_create.firstname,
            lastname=user_create.lastname,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
    
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        return db.exec(stmt).first()
    
    def get(self, db: Session, *, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        return db.exec(stmt).first()
        
       
       
user = CRUDUser() 