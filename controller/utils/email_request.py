import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email_via_smtp(recipient_email, subject, body, attachment_path):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    EMAIL_USERNAME = "helishah2116@gmail.com"  # Your Gmail address
    EMAIL_PASSWORD = "lkyr uoby fjql ygka"  # Your app password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file if provided
    if attachment_path:
        try:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {attachment_path.split('/')[-1]}")
            msg.attach(part)
        except Exception as e:
            print(f"Error attaching file: {e}")

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Correct username and password
            server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


# def send_email_via_smtp(recipient_email, subject, body):
#     SMTP_SERVER = "smtp.gmail.com"
#     SMTP_PORT = 587
#     EMAIL_USERNAME = "helishah2116@gmail.com"
#     EMAIL_PASSWORD = "kubl tpuf yhbc wvxy"


#     try:
#         # Create the email message
#         message = MIMEMultipart()
#         message["From"] = EMAIL_USERNAME
#         message["To"] = recipient_email
#         message["Subject"] = subject
#         message.attach(MIMEText(body, "plain"))

#         # Connect to the server and send the email
#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()  # Secure the connection
#         server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
#         server.send_message(message)
#         server.quit()

#         return True
#     except Exception as e:
#         print(f"Error sending email: {e}")
#         return False