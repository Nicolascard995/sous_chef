import os
from dotenv import load_dotenv
from twilio.rest import Client

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de Twilio desde las variables de entorno
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
whatsapp_from = os.getenv('TWILIO_WHATSAPP_FROM')
whatsapp_to = os.getenv('TWILIO_WHATSAPP_TO')
content_sid = os.getenv('TWILIO_CONTENT_SID')

# Inicializar el cliente de Twilio
client = Client(account_sid, auth_token)

def send_whatsapp_message():
    # Crear y enviar el mensaje de WhatsApp
    message = client.messages.create(
        from_=whatsapp_from,
        content_sid=content_sid,
        content_variables='{"1":"12/1","2":"3pm"}',
        to=whatsapp_to
    )

    print("Message SID:", message.sid)
