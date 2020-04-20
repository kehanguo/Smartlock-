import smtplib
import ssl 
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  
from smtplib import SMTPException  
camera = PiCamera()  
camera.resolution=(640,480)
 
camera.start_preview()  
sleep(5)  
camera.capture('/home/pi/image.jpg')     # image path set
sleep(5)  
camera.stop_preview()  
def send_an_email():  
    toaddr = 'email address you want to send'
    me= 'your address'     
    subject = "Senior design testing"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me
    msg['To'] =toaddr  
    msg.preamble = "test "   
   msg.attach(MIMEText(text))  
  
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open("image.jpg", "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="image.jpg"')   # File name and format name
    msg.attach(part)  
  
     try: 
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = 'email address', password = 'password')  # User id & password
       s.send_message(msg)  
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()  
    #except:  
    #   print ("Error: unable to send email")    
    except SMTPException as error:  
          print ("Error")                # Exception
  
send_an_email()
