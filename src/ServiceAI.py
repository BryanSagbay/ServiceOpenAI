import openai
import json
import config

# Autenticar con la API de OpenAI
openai.api_key = config.api_Key

# Contiene un mensaje del sistema, que indica que va a ser un asistente
messages=[{"role":"system",
          "content":"Eres un asistente diseñado para identificar problemas del sistema de una Universidad." }]

# Obtener el texto del usuario
texto = input("Ingrese el texto: ") 

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