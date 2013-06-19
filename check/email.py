
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
 
#Next, log in to the server
server.login("sawan.gupta92@gmail.com", "bhagatsingh")
 
#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("sawan.gupta92@gmail.com", "sawan.gupta92@gmail.com", msg)