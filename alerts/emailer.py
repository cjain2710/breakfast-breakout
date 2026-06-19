import smtplib
import os
from email.message import EmailMessage

def send_email(file_path):

    msg = EmailMessage()
    msg["Subject"] = "Breakfast Breakout Report"
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = os.getenv("EMAIL_ADDRESS")

    msg.set_content("Daily breakout report attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="octet-stream",
                           filename="report.csv")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_ADDRESS"),
                   os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)