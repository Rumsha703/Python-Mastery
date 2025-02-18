import os
from dotenv import load_dotenv
from smtplib import SMTP,SMTP_SSL
from email.message import EmailMessage
from datetime import datetime

load_dotenv()

#1. managing senesitive data through OS
name="rumsha"
EMAIL_ADDRESS=os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.environ.get("EMAIL_PASSWORD")
email_body ="Hello, I hope this meessage meets you well, I'm reminding you of the standuo meeting scheduled for 9:00am "


msg=EmailMessage()

msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg["Subject"] = "Standup Meeting Reminder"
msg.set_content(email_body)

with SMTP_SSL("smtp.gmail.com",465) as server:
   server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
   if datetime.now().hour==8 and datetime.now().minute==30 and datetime.now().weekday == 0 :
    print("Reminder is sent")
    server.send_message(msg)
   else:
    print("Today is not monday")
    server.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS, msg="Subject : No meeting today")
   
print("email sent")




