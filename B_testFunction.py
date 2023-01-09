def message_creator(text):
  # Escribe tu solución 👇
  dir = {
  "computadora": "Con mi computadora puedo programar usando Python",
  "celular": "En mi celular puedo aprender usando la app de Platzi",
  "cable": "¡Hay un cable en mi bota!"
  }
  if text in dir:
    return dir[text]

  return "Artículo no encontrado"   
  
    #return dir[text]

text = 'computadra'
response = message_creator(text)
print(response)