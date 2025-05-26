from fastapi import HTTPException, Request
from passlib.context import CryptContext

SECRET_KEY="cae3def7c5c8f5c07613a742c1c5435076ccf0777c259796ad1653c0fd5dfdd7"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    # user = fake_users_db.get(username)
    # if not user or not verify_password(password, user["hashed_password"]):
    #     return None
    # return user
    pass

def get_current_user(request: Request):
    username = request.session.get("user")
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # user = fake_users_db.get(username)
    # if not user:
    #     raise HTTPException(status_code=401, detail="User not found")
    
    # return User(username=user["username"], email=user["email"])