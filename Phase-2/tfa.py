from email.message import EmailMessage
import random
import ssl
import smtplib

def Check(User_Email):
    Code = random.randint(100000,999999)

    App_Password = "temz annw ftkf gdyl"
    Email_Sender = "lewisclark857@gmail.com"
    Email_Reciever = User_Email
    
    Code = Code

    Subject = "Two factor Authentication Code"
    Body = f"Your two factor authentication code is {Code}"
    
    EM = EmailMessage()
    EM['From'] = Email_Sender
    EM['To'] = Email_Reciever
    EM['subject'] = Subject
    EM.set_content(Body)
    Context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=Context) as smtp:
        smtp.login(Email_Sender, App_Password)
        smtp.sendmail(Email_Sender, Email_Reciever, EM.as_string())



    return Code
   