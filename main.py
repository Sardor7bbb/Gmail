
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

from_email = "sardorsafaraliyev69@gmail.com"


def send_mail(to_email):
    email_message = MIMEMultipart()
    email_message['From'] = from_email
    email_message['To'] = to_email
    email_message['Subject'] = "Welcome to Gmail"
    email_message.attach(MIMEText("Nima Gap", 'plain'))
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_email, "mnbb xpka dwev zlye")
    try:
        server.sendmail(from_email, to_email, email_message.as_string())
        server.quit()
        print("Mail sent successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


users = [
    "azimovoktam401@gmail.com",
    "sadullafaxriddinov03@gmail.com",
    "safaraliyevsanjar33@gmail.com",
    "sardorsafaraliyev69@gmail.com",
    "sardorsafaraliyev@icloud.com",
    "sardorsafaraliyev8@gmail.com",
    "sardorsafaraliyev47@gmail.com",
    "sadullafaxriddinov11@gmail.com",
    "azimovoktam78@gmail.com",
    "sadullafaxriddinov03@gmail.com",
    "sadullafaxriddinov03@gmail.com"
]


def send_mail_to_users():
    for user in users:
        send_mail(user)


t1 = threading.Thread(target=send_mail_to_users)
t1.start()

user_name = input("Enter your name : ")
print(f"Hello {user_name}!")

