import smtplib
from cryptography.fernet import Fernet #pip3 install cryptography
from email.message import EmailMessage
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("formularioesfm-firebase-adminsdk-f9csg-da5faa24f2.json")
firebase_admin.initialize_app(cred)#,{'projectId': 'formularioesfm'})
db = firestore.client()

u = 'club.de.programacion.esfm@gmail.com'
sent_from = u
subject = 'Bienvenido al Club de Programación ESFM'
p = 'xewguejeyjslnszh'

subject_test = 'Test enviado correctamente'

def load_key():
    return open("secret.key", "rb").read()

def encrypt(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    return str(f.encrypt(encoded_message)).replace("'",'%27')

def test(data):
    def confirmar_id(data):
        ide_correo = data['id']
        respuestas = db.collection(u'Id-correo')
        query_ref = respuestas.where(u'Id',u'==',ide_correo)
        registros = query_ref.stream()
        #print( registros)
        
        for registro in registros:
            if registro:
                return registro.to_dict()['Correo'],registro.to_dict()['Curso']
        
        #    print('except')
         #   return [None,None]
        #else:
         #   print('else registros')
        #    
    try:  
        correo_registro,curso = confirmar_id(data)
    except TypeError:   
        correo_registro = None  
    if correo_registro:
        correo_enviado = send_email_test(correo_registro,data['id'],curso)
    else:
        doc_ref = db.collection('Test-noemail-errors').document(data['id'])
        doc_ref.set({u'Id':data['id']})
        
def send_email_test(to,ide, curso):
    if curso == 'Python-zh':
        link = 'https://discord.gg/mxBQnEV'
        curso = 'Python from zero to hero'
    elif curso == 'Ingenieria-datos':
        link = 'https://www.discord.gg/jy6cJVt'
        curso = 'Ingeniería de datos'
    elif curso == 'Pandas-ciencia':
        link = 'https://discord.gg/NnpsUEy'
        curso = 'Pandas para ciencia de datos'
    elif curso == 'Matlab':
        link = 'https://www.google.com'
        curso = 'Matlab'
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        try:
            smtp.login(u, p)
        except:
            return 0
        else:
            body = "Tu test con ID {} ha sido enviado con éxito. Muy pronto sabrás tus resultados.\n\n Te recordamos que puedes ingresar a Discord para que puedas compartir tus experiencias o dudas y te enteres de las últimas noticias del Club.\n {}\n\n ".format(ide,link)
            msg = f'Subject: {subject_test}\n\n{body}'
            message = EmailMessage()
            message['Subject'] = subject
            message['From'] = sent_from
            message['To'] = to
            message.set_content(body)
            message.add_alternative(f"""
                        <!DOCYPE html>
                        <html>
                            <body style = "text-align: center;background-color: #061d47; color: #ffffff; font-family: Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif;">
                                <div style = "padding-top: 20px;padding-bottom:200px;margin-top:20px">
                                    <img src = "https://fotos.subefotos.com/1ea5493402c85218b1af851e3e8deaa5o.png" style="width: 70%;margin-top:10px;margin-left:auto;margin-right:auto;display:block"/>
                                    <h4>¡Tu test con ID {ide} ha sido enviado con éxito!</h4>
                                    <br></br>
                                    <h4 style ="color:#f9a836;">Muy pronto sabrás tus resultados. </h4>
                                    <br></br>
                                    <p>Te recordamos que puedes ingresar a <a href = "{link}" style="color: #f9a836;">Discord</a> para que puedas compartir tus experiencias o dudas y te enteres de las últimas noticias del Club. </p>
                                </div>
                            </body>
                        </html>
            
            """, subtype= 'html')
            smtp.send_message(message)
            time.sleep(3)
            return 1

def send_email(to,name,ide,curso):
    name = ''.join(word.capitalize() + ' ' for word in name.lower().split(' '))
    discord_tutorial = 'https://drive.google.com/file/d/1EGl8DYvPgQIhrjishLiqkbG0iG0KDCWF/view'
    if curso == 'Python-zh':
        link = 'https://discord.gg/mxBQnEV'
        curso = 'Python from zero to hero'
    elif curso == 'Ingenieria-datos':
        link = 'https://www.discord.gg/jy6cJVt'
        curso = 'Ingeniería de datos'
    elif curso == 'Pandas-ciencia':
        link = 'https://discord.gg/NnpsUEy'
        curso = 'Pandas para ciencia de datos'
    elif curso == 'Matlab':
        link = 'https://www.google.com'
        curso = 'Matlab'
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        try:
            smtp.login(u, p)
        except:
            return 0
        else:
            if curso == 'Matlab':
                body = "Hola {}, bienvenido(a) al Club de Programación ESFM. \n\n Tu ID de registro es: {} \n\n ¡Nos alegra que te intereses en nuestro curso {}! Muy pronto nos pondremos en contacto contigo para invitarte a Microsoft Teams.".format(name,ide,curso)
                test = ''
                discord = f"""   
                                    <p>Nos alegra que te intereses en nuestro curso {curso}. Muy pronto te enviaremos el enlace para que te unas a Microsoft Teams.  </p>
                            """
            elif curso == 'Ingeniería de datos' or curso == 'Pandas para ciencia de datos':
                body = "Hola {}, bienvenido(a) al Club de Programación ESFM. \n\n Tu ID de registro es: {} \n\n ¡Nos alegra que te intereses en nuestro curso {}! Te enviamos el link de la plataforma que ocuparemos para las sesiones: \n {} .\n Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos:\n {}\n\n Si no has hecho el Test, no pierdas tu lugar y accede al siguiente enlace para realizarlo (sólo lo tienes que hacer una vez): \n https://cdpesfm.college/test?id={}&name={}".format(name,ide,curso,link,discord_tutorial,encrypt(ide),encrypt(name))
                test = f"""<p> Si no has hecho el Test, no pierdas tu lugar y accede al siguiente enlace para realizarlo (sólo lo tienes que hacer una vez):<p>
                            <a href = "https://cdpesfm.college/test?id={encrypt(ide)}&name={encrypt(name)}" style="color: #f9a836;">Hacer Test</a>"""
                discord = f"""       <p>Nos alegra que te intereses en nuestro curso {curso}. Te enviamos el link de la plataforma que ocuparemos para las sesiones: <a href = "{link}" style="color: #f9a836;">Discord</a>.  </p>
                                    <p> Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos: <a href = "{discord_tutorial}" style="color: #f9a836;">Tutorial Discord</a>.  </p>
                                    <br></br>"""
            else:
                body = "Hola {}, bienvenido(a) al Club de Programación ESFM. \n\n Tu ID de registro es: {} \n\n ¡Nos alegra que te intereses en nuestro curso {}! Te enviamos el link de la plataforma que ocuparemos para las sesiones: \n {} . \nSi no estás familiarizado con Discord, te adjuntamos una guía que preparamos: \n{}\n\n ".format(name,ide,curso,link,discord_tutorial)
                test = ''
                discord = f"""       <p>Nos alegra que te intereses en nuestro curso {curso}. Te enviamos el link de la plataforma que ocuparemos para las sesiones: <a href = "{link}" style="color: #f9a836;">Discord</a>.  </p>
                                    <p> Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos: <a href = "{discord_tutorial}" style="color: #f9a836;">Tutorial Discord</a>.  </p>
                                    <br></br>"""
            msg = f'Subject: {subject}\n\n{body}'

            message = EmailMessage()
            message['Subject'] = subject
            message['From'] = sent_from
            message['To'] = to
            message.set_content(body)
            message.add_alternative(f"""
                        <!DOCYPE html>
                        <html>
                            <body style = "text-align: center;background-color: #061d47; color: #ffffff; font-family: Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif;">
                                <div style = "padding-top: 20px;padding-bottom:200px;margin-top:20px">
                                    <img src = "https://fotos.subefotos.com/1ea5493402c85218b1af851e3e8deaa5o.png" style="width: 70%;margin-top:10px;margin-left:auto;margin-right:auto;display:block"/>
                                    <br></br>
                                    <h4>¡Hola {name}, bienvenido(a) al Club de Programación ESFM!</h4>
                                    <h4 style ="color:#f9a836;">Tu ID de registro es: {ide} </h4>
                                    <br></br>
                                    {discord}
                                    {test}
                                </div>
                            </body>
                        </html>
            
            """, subtype= 'html')
            
            smtp.send_message(message)
            time.sleep(3)
            #smtp.sendmail(sent_from, to, msg.encode("utf8"))
            return 1