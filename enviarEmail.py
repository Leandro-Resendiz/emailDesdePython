import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

yourEmail = 'resendizikerleandro@gmail.com'
yourPassword = 'gtpe gkxg lemm hwzm'

recipient = input('Ingresa tu correo: ')

message = MIMEMultipart()
message['From'] = yourEmail
message['To'] = recipient
message['Subject'] = 'Email de Prueba'

body = 'Este es un mensaje de Prueba de envio de mensaje desde Python'

message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(yourEmail, yourPassword)

smtp_server.sendmail(yourEmail, recipient, message.as_string())
smtp_server.quit()
print('Email enviado con exito')