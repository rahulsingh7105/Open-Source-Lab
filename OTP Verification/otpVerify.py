#Simple

import random

class OTPVerificationSystem:
    def __init__(self):
        self.otp = None

    def generate_otp(self):
        self.otp = str(random.randint(1000, 9999))  # Generate a 4-digit OTP
        print("Generated OTP:", self.otp)

    def verify_otp(self, user_input):
        if self.otp == user_input:
            print("OTP verified successfully!")
        else:
            print("Invalid OTP. Please try again.")

if __name__ == "__main__":
    otp_system = OTPVerificationSystem()
    otp_system.generate_otp()

    user_input = input("Enter the OTP you received: ")
    otp_system.verify_otp(user_input)

#############################################################################################################################

# For mail
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp_email(receiver_email, otp):
    # Sender and receiver email addresses
    sender_email = "your_email@gmail.com"
    password = "your_password"

    # Email subject and body
    subject = "OTP Verification"
    body = f"Your OTP is: {otp}"

    # Configure the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach body to the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def generate_otp():
    # Generate a 6-digit OTP
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

if __name__ == "__main__":
    # Receiver's email address
    receiver_email = "receiver_email@example.com"

    # Generate and send OTP
    otp = generate_otp()
    send_otp_email(receiver_email, otp)

    print("OTP sent successfully to", receiver_email)
