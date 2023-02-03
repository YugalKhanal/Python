from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Yugal Khanal"
message["to"] = "hellguy247@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("hellguy247@gmail.com", "zjwhohjxzbyfhutj")
    smtp.send_message(message)
    print("Sent...")