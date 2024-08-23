import smtplib
import ssl
from getpass import getpass
from email.message import EmailMessage
from constants import *
from mail_data import *
from pass_enc_dec import *

port = 465

def mail(receiver:str, subject:str, msge:str):
    password = decoder('Password in encoding form')
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(msge)
    msg["Subject"] = subject#"Important Mail"
    msg["From"] = 'Sender Email ID'
    msg["To"] = receiver

    #"This is a test mail message."
    #server2 = smtplib.SMTP_SSL("smtp.gmail.com",587,context = context)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login("Email ID",password)
        server.send_message(msg)

