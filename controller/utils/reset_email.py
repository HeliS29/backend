# import smtplib
# from email.mime.text import MIMEText

# def send_verification_code(email: str, code: str):
#     subject = "Verification Code"
#     message = f"Your verification code is: {code}"
#     sender_email = "helishah2116@gmail.com"
#     sender_password = "kubl tpuf yhbc wvxy"

#     msg = MIMEText(message)
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = email

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.send_message(msg)

# import secrets

# def generate_verification_code(length: int = 6) -> str:
#     """Generates a secure random verification code of given length."""
#     return ''.join(secrets.choice('0123456789') for _ in range(length))

# # Example usage:
# verification_code = generate_verification_code()
# print(verification_code)
