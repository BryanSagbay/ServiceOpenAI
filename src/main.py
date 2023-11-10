import openai
import json
import config
import openai
import imaplib
import email
from email.header import decode_header
import json



def ReadMail ():
    username = "pruebascorreos2023@outlook.com"  # Tu correo aquí
    password = "Ucacue2023"  # Tu contraseña aquí

    # Crear conexión
    imap = imaplib.IMAP4_SSL("outlook.office365.com")
    # Iniciar sesión
    imap.login(username, password)

    status, mensajes = imap.select("INBOX")
    # Mensajes a recibir
    N = 10
    # Cantidad total de correos
    mensajes = int(mensajes[0])

    for i in range(mensajes, mensajes - N, -1):
      try:
         res, mensaje = imap.fetch(str(i), "(RFC822)")
      except:
         break
    for respuesta in mensaje:
        if isinstance(respuesta, tuple):
            # Obtener el contenido
            mensaje = email.message_from_bytes(respuesta[1])
            # Decodificar el contenido del asunto
            subject_bytes, encoding = decode_header(mensaje["Subject"])[0]
            
            if isinstance(subject_bytes, bytes):
                subject = subject_bytes.decode(encoding or "utf-8")
            else:
                subject = subject_bytes  # Si ya es una cadena, no necesita decodificación
            
            from_bytes, encoding = decode_header(mensaje["From"])[0]
            
            if isinstance(from_bytes, bytes):
                from_ = from_bytes.decode(encoding or "utf-8")
            else:
                from_ = from_bytes  # Si ya es una cadena, no necesita decodificación
            
            print("Subject:", subject)
            print("From:", from_)
            print("Mensaje obtenido con éxito")

            if mensaje.is_multipart():
                for part in mensaje.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        try:
                            encoding = part.get_content_charset() or "utf-8"
                            body = part.get_payload(decode=True).decode(encoding)
                            formatted_body = json.dumps(body)
                            return body

                            # Verificar si el tipo de problema del correo ya ha sido procesado
                        except  Exception as e:
                            print("ERROR "+e)
                            
# Variable para guardar el texto extraido del correo
texto = ReadMail()

# Autenticar con la API de OpenAI
openai.api_key = config.api_Key

# Contiene un mensaje del sistema, que indica que va a ser un asistente
messages=[{"role":"system",
          "content":"Eres un asistente diseñado para identificar problemas del sistema de una Universidad." }]

# Cargar los datos desde el archivo JSON
with open('./data/gpli.json', 'r') as f:
    data = json.load(f)

# Lista vacía
tipos = []

# Recorrer los elementos del archivo JSON y los agrega a una lista
for elemento in data:
    tipos.append(elemento['type'])

# variable donde concatena todo el prompt
datos= texto + "Clasifica el tipo de problema que esta presentando el usuario, a partir de estos tipos de problemas que existen en el sistema de la Universidad:"+", ".join(tipos)+"En caso de que no puedas identificar el problema segun los tipos de problemas que se te proporciono, solicita mas detalles al usuario."



# texto concatenado que se agrega adicionalmente al texto del prompt.
messages.append({"role":"user", "content":datos  })

# Solicita a la api que genere una respuesta a partir del mensaje creado
response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=messages
)

print(response.choices[0].message.content)
