# Smartlock-This is a smartlock program. 
The emailreceive.py program works with a pi camera and infrared sensor. The picamera is directly connected with the camera port in raspberry pi. As for our project, we used raspberry pi model B+. For the raspberry pi GPIOs, Pin1 is connected to IR power port, Pin23 is the sensing port and ground should be connected to pin6.
This program allows the raspberry pi to take picture when obstacles is detected by IR sensor. And the taken image will be sent from the user email to other's mailbox.

The testemail.py program are able to read emails inbox and extract key words from it.
