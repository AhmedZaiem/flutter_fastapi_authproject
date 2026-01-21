from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserLogin
from services.user_service import get_user_by_email, create_user
from core.security import hash_password, verify_password


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    create_user(user.email, hashed_password)

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"message": "Login successful"}
