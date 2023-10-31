import openai
import json



# Autenticar con la API de OpenAI
openai.api_key = "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"

username="pruebascorreos2023@outlook.com"
password="Ucacue2023"


# Cargar los datos desde el archivo JSON
with open('./data/gpli.json', 'r') as f:
    data = json.load(f)
 

# Obtener el texto del usuario
texto = input("Ingrese el texto: ")

# Prompt para la clasificación del problema
opciones = "\n".join([f"{i+1}. {item['type']}" for i, item in enumerate(data)])
prompt = f"Este usuario informa que: {texto}\n\nClasifica el tipo de problema relacionado:\n{opciones}\n\n:"

# Interración con el modelo GPT-3
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Obtener la respuesta del modelo
clasificacion = response.choices[0].text.strip()

# Buscar el tipo en los datos y, si se encuentra una coincidencia, imprimir el ingeniero y el correo correspondientes
for item in data:
    if item['type'].lower() in clasificacion.lower():
        print("Caso:", item['caso'])
        print("Ingeniero:", item['engineer'])
        print("Correo:", item['email'])
        print("Tipo de Caso:", item['type'])
        break
else:
    print("No se encontró ninguna coincidencia para el texto ingresado.Puedes especificar con mas detalles el problema")