import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

email=EmailMessage()

subject = "just look at this"
email.set_content(subject)

files = [r"C:\Users\ashis\OneDrive\Pictures\wp7102558-jai-shree-ram-4k-wallpapers.png",r"C:\Users\ashis\OneDrive\Pictures\Camera Roll\WIN_20250103_18_21_03_Pro.jpg"]
for file_path in files :
    with open (file_path,"rb") as f:
        file_data=f.read()
        file_name=f.name
        mime_type,_=mimetypes.guess_type(file_path)
        maintype,subtype=mime_type.split('/')
    email.add_attachment(file_data,maintype=maintype,subtype=subtype,filename=file_name)

sender_email="senders.mail@gmail.com"     # senders mail
receiver_email="receavers.mail@gmail.com"  # receivers mail
app_password="your_app_password"           # app password 

email['from']=sender_email
email['to']=receiver_email
email['subject']=subject

context= ssl.create_default_context() 
with smtplib.SMTP_SSL("smtp.gmail.com",465,context =context) as smtp :
    smtp.login(sender_email,app_password)
    smtp.send_message(email)

print ("done brooooo")


    
