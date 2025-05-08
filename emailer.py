import smtplib
import email.mime.text
import email.mime.multipart
import os
from dotenv import load_dotenv

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT", 587))
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")
email_from = os.getenv("EMAIL_FROM")
email_to = os.getenv("EMAIL_TO")

# Validate required variables
if not all ([smtp_server, smtp_port, smtp_password, email_from, email_to]):
    raise ValueError("Missing required environment variables. Check your .env file.")

# Create a function to send email
def send_email(subject,body):
    # Create the email message
    msg = email.mime.multipart.MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    # Attach the body
    msg.attach(email.mime.text.MIMEText(body, 'plain'))

    # Connect to the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your username and password.")
    except smtplib.SMTPConnectError:
        print(f"Failed to connect to {smtp_server}:{smtp_port}. Check your server and port.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Test the function
if __name__ == "__main__":
    send_email("Test Email", "This is a test email from your script.")
