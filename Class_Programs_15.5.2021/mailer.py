import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

def mail(current_date_time,count):
    fromaddr = "senders_email_address"
    toaddr = "recievers_email_address"
   
# instance of MIMEMultipart
    msg = MIMEMultipart()
  
# storing the senders email address  
    msg['From'] = fromaddr
  
# storing the receivers email address 
    msg['To'] = toaddr
  
# storing the subject 
    msg['Subject'] = "Hourly Logger Report"
  
# string to store the body of the mail
    body = "Attached here is the file that contains the hourly report along with hashcodes of the files and duplicates which was recorded on: "+datetime.now().strftime("%d_%m_%Y-%I_%M")+"The number of duplicate files found at time "+datetime.now().strftime("%d_%m_%Y-%I_%M")+" is "+str(count) +" and they all have been deleted"

  
# attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
# open the file to be sent 
    filename = "16_05_2021-02_29.txt"
    attachment = open(os.getcwd()+"\\"+current_date_time, 'r')
  
# instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
  
# To change the payload into encoded form
    p.set_payload((attachment).read())
  
# encode into base64
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
# attach the instance 'p' to instance 'msg'
    msg.attach(p)
  
# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
    s.starttls()
  
# Authentication
    s.login(fromaddr, "sender's [password")
  
# Converts the Multipart msg into a string
    text = msg.as_string()
  
# sending the mail
    s.sendmail(fromaddr, toaddr, text)
  
# terminating the session
    s.quit()