from db.database import users_collection
from core.security import hash_password, verify_password, create_access_token

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

def create_user(username:str, email: str, password: str, age: int):
    user = {
        "username": username,
        "email": email,
        "password": password,
        "age": age
    }
    users_collection.insert_one(user)
    return user

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        return None
    token = create_access_token({"sub": str(user["_id"])})
    return token