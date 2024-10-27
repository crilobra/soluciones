import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del correo
smtp_server = "smtp.gmail.com"  # Servidor SMTP de Gmail
smtp_port = 587                 # Puerto de Gmail para TLS
sender_email = "crilobra@gmail.com"    # Correo del remitente
sender_password = "rlwd vrgm njlc bwyk"      # Contraseña del remitente

# Leer la lista de correos electrónicos desde el archivo CSV
contactos = pd.read_csv("lista.csv")

# Crear el mensaje
subject = "Saludos "
message_body = "Hola, espero que estés bien. ¡Saludos!"

# Iniciar la conexión con el servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Protocolo de encriptación
server.login(sender_email, sender_password)


# Enviar el correo a cada contacto
for index, row in contactos.iterrows():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = row['email']
    msg['Subject'] = subject

    # Cuerpo del mensaje
    msg.attach(MIMEText(message_body, 'plain'))

    # Enviar el correo
    server.sendmail(sender_email, row['email'], msg.as_string())
    print(f"Correo enviado a {row['email']}")

# Cerrar la conexión
server.quit()
print("Todos los correos han sido enviados.")
