AVANCE =0
INICIOLEXEMA =0
LEXEMAS = []

# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
  global AVANCE, INICIOLEXEMA, LEXEMAS
  AVANCE = 0
  INICIOLEXEMA = 0
  lexema = ""
  for i in range(len(buffer)) :
    caracter = buffer[AVANCE]
    if caracter == " " and AVANCE!=0:
      INICIOLEXEMA = i + 1
      LEXEMAS.append(lexema)
      AVANCE = INICIOLEXEMA
      lexema = ""
    
    else:
      AVANCE = i +1
      if caracter != " ":
        lexema += caracter
        if AVANCE == len(buffer):
          LEXEMAS.append(lexema)

# buffer = cargar_buffer(entrada, inicio, tamano_buffer)
# print(buffer)
# procesar_buffer(buffer)

if __name__ == "__main__":

  BUFFER1 = []
  BUFFER2 = []
  tamano_buffer = 10
  entrada = list("Esto es un ejemplo de entrada con eof")

  print(len(entrada))
  # buffer = cargar_buffer(entrada, inicio, tamano_buffer)
  # print(buffer)
  # procesar_buffer(buffer)
  # print(LEXEMAS)
  # print(AVANCE)
  while AVANCE != len(entrada):
    if AVANCE == 0:
      BUFFER1 = cargar_buffer(entrada, INICIOLEXEMA, tamano_buffer)
      procesar_buffer(BUFFER1)
      INICIOLEXEMA = len(BUFFER1)
    elif AVANCE== len(BUFFER1):
      BUFFER2 = cargar_buffer(entrada, INICIOLEXEMA, tamano_buffer)
      procesar_buffer(BUFFER2)
    elif AVANCE == len(BUFFER2):
      BUFFER1 = cargar_buffer(entrada, INICIOLEXEMA, tamano_buffer)
      procesar_buffer(BUFFER1)
  
  
