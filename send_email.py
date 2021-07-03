import smtplib
from cryptography.fernet import Fernet #pip3 install cryptography
from email.message import EmailMessage
import time

u = #username
sent_from = u
subject = 'Alguien se quiere poner en contácto contigo'
cipher = Fernet(b'#key') 
decoded = cipher.decrypt(b'#key')

p = str(decoded)[2:-1]

def enviar(nombre,correo,interes, comentario):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        try:
            smtp.login(u, p)
        except:
            return 0
        else:
            body = f"Datos: \n \t Nombre: {nombre}\n \t Correo: {correo}\n  \t Interés: {interes}\n \t Comentario: {comentario}  "
            message = EmailMessage()
            message['Subject'] = subject
            message['From'] = sent_from
            message['To'] = 'joules.hdz@gmail.com'
            message.set_content(body)
            smtp.send_message(message)
            return 1

