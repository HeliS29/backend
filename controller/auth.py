from datetime import datetime, timedelta

from fastapi import Depends
import jwt
from config import settings
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]

def create_jwt_token(data: dict):
    expiration = datetime.now() + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES)
    data.update({"exp": expiration})
    # print(settings.JWT_SECRET)
    # print(data)
    # print(settings.JWT_ALGORITHM)
    token = jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        print(payload)
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None



# def generate_reset_token(user_id: int):
#     payload = {
#         "user_id": user_id,
#         "exp": datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
#     }
#     return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

# def verify_reset_token(token: str):
#     try:
#         payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
#         return payload.get("user_id")
#     except jwt.ExpiredSignatureError:
#         return None
#     except jwt.InvalidTokenError:
#         return None




import smtplib
from email.mime.text import MIMEText

def send_verification_code(email: str, code: str):
    subject = "Verification Code"
    message = f"Your verification code is: {code}"
    sender_email = "helishah2116@gmail.com"
    sender_password = "kubl tpuf yhbc wvxy"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

import secrets

def generate_verification_code(length: int = 6) -> str:
    """Generates a secure random verification code of given length."""
    return ''.join(secrets.choice('0123456789') for _ in range(length))

# Example usage:
# verification_code = generate_verification_code()
# print(verification_code)