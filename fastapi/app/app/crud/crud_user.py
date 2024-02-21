from typing import Optional

from sqlmodel import Session, select
from app.models import User, UserCreate
from app.core.security import verify_password, create_password_hash

class CRUDUser:
    
    def create(self, db: Session, *, user_create: UserCreate) -> User:
        db_user = User(
            email=user_create.email,
            hashed_password=create_password_hash(user_create.password),
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
    
            
    
    def authenticate(self, db: Session, *, email: str, password: str) -> User | None:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
        
       
       
user = CRUDUser() 