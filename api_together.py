import os
from together import Together

def preguntarIA (petCliente, mensaje):
    # Enviamos la pregunta a la IA y usamos el modelo Llama
    respuesta = petCliente.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": mensaje}],
        stream=True,
    )

    # Componemos la respuesta completa de la IA
    respuestaCompleta = ""
    for trozoActual in respuesta:
        respuestaCompleta = f"{respuestaCompleta}{trozoActual.choices[0].delta.content}"    
    
    return respuestaCompleta

# Cargamos la API de Together pasando el API Key
petCliente = Together(api_key="dcb7a0ccb...84...6")

# Definimos una lista de preguntas y respuestas, para poder hacer varias
preguntas = []
respuestas = []

# Iniciamos el prompt para preguntas/peticiones
textoConsola = "Pregúntame o pídeme cualquier cosa (pulsa INTRO sin pregunta para salir): "
pregunta = input(textoConsola)
if pregunta != "":
    # Almacenamos la primera pregunta en la lista
    preguntas.append(pregunta)
    # Iniciamos un bucle para preguntar hasta que se pulse INTRO sin pregunta
    while True:
        if pregunta != "":
            # Establecemos el mensaje o pregunta que queramos realizar a la IA
            # Y lo almacenamos en la lista de respuestas     
            respuesta = preguntarIA(petCliente, pregunta)
            respuestas.append(respuesta)
            # Mostramos la respuesta actual dada por la IA
            print(respuesta)
            # Volvemos a solicitar al usuario si quiere hacer más preguntas a la IA
            pregunta = input(textoConsola)
            preguntas.append(pregunta)
        else:
            break

# Al finalizar mostramos todas las preguntas y las respuestas
i = 0
for pregunta in preguntas:
    if pregunta != "":
        i += 1
        print(f"[Pregunta {i}]: \n{pregunta}")
        print(f"[Respuesta {i}]: \n{respuestas[i -1]}\n")
