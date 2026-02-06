from db.database import get_db
from models.user import User
from core.security import verify_password
from sqlalchemy.orm import Session

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
    

def create_user(db:Session,username:str, email: str, password: str, age: int):
    new_user = User(username=username, email=email, password=password, age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        return None
    return user