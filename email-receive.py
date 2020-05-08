import smtplib
import RPi.GPIO as IO
from  picamera import PiCamera
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  
from smtplib import SMTPException  
from  time import sleep
camera= PiCamera()
camera.vflip



IO.setwarnings(False)
IO.setmode (IO.BCM)

IO.setup(22,IO.OUT)
IO.setup(27,IO.OUT)
IO.setup(23,IO.IN)

while 1:

 if(IO.input(23)==True):
    IO.output(27,True)
    IO.output(22,False)
    camera.start_preview()
    sleep(5)
    camera.vflip=True
    camera.capture('/home/pi/image.jpg')
    sleep(5)
    camera.stop_preview()

    fromaddr = "your email"
    toaddr = "receiver's email"
#subject=  "email a image through raspberry" 
    msg = MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "email an image through raspberry pi"
     
    body = "Door notification"
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "raspberry image"
    attachment = open("/home/pi/image.jpg", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',' attachment; filename="image.jpg"')
     
    msg.attach(part)

     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,'your password')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

  
if(IO.input(23)==False):
    IO.output(22,True)
    IO.output(27,False)





