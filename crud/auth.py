from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models.users import *
from passlib.context import CryptContext
from controller.auth import generate_verification_code



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, name: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = User(name=name, email=email, password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    
 
    
    return user
# def create_user(db: Session, name: str, email: str, password: str):
#     hashed_password = pwd_context.hash(password)
#     user = User(name=name, email=email, password_hash=hashed_password)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and pwd_context.verify(password, user.password_hash):
        return user
    return None



def create_verification_code(db: Session, user: User):
    """Generates and saves a verification code for a user."""
    verification_code = generate_verification_code()  # 6-digit code, e.g., "123456"
    user.verification_code = verification_code
      # 15 min validity
    db.commit()
    db.refresh(user)
    return verification_code

def verify_code(db: Session, email: str, verification_code: str):
    """Verifies the given code for a user."""
    user = db.query(User).filter(User.email == email).first()
    if not user or not user.verification_code:
        print(f"No user found or no verification code for email: {email}")
        return None

    expiration_time = datetime.now() + timedelta(minutes=10)
    current_time = datetime.now()
    print(f"Verification Code: {user.verification_code}, Expiration: {expiration_time}, Current Time: {current_time}")
    db.refresh(user)
    print(user.verification_code)
    print(verification_code)
    if str(user.verification_code).strip() == str(verification_code).strip() and current_time <= expiration_time:

        print(f"Verification successful for user: {user.email}")
        return user

    print(f"Verification failed for user: {user.email}, Code: {verification_code}, Expiration: {expiration_time}, Current: {current_time}")
    return None



