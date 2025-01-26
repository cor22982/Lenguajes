AVANCE =0
INICIOLEXEMA =0
LEXEMAS = []
LECTOR =0
LEXEMA = ""

# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
  global AVANCE, INICIOLEXEMA, LEXEMAS, LEXEMA
  AVANCE = 0
  INICIOLEXEMA = 0
  for i in range(len(buffer)) :
    caracter = buffer[AVANCE]
    if caracter == " " and AVANCE!=0:
      INICIOLEXEMA = i + 1
      LEXEMAS.append(LEXEMA)
      AVANCE = INICIOLEXEMA
      LEXEMA = ""
    
    else:
      AVANCE = i +1
      if caracter != " ":
        LEXEMA += caracter
        if AVANCE == len(buffer):
          LEXEMAS.append(LEXEMA)

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
  buffer = cargar_buffer(entrada,20, tamano_buffer)
  print(buffer)
  # print(AVANCE)
  while LECTOR != len(entrada):
    if AVANCE == 0:
      BUFFER1 = cargar_buffer(entrada, LECTOR, tamano_buffer)
      procesar_buffer(BUFFER1)
      LECTOR += len(BUFFER1)
    elif AVANCE== len(BUFFER1):
      BUFFER2 = cargar_buffer(entrada, LECTOR, tamano_buffer)
      procesar_buffer(BUFFER2)
      LECTOR += len(BUFFER2)
    elif AVANCE == len(BUFFER2):
      BUFFER1 = cargar_buffer(entrada, LECTOR, tamano_buffer)
      procesar_buffer(BUFFER1)
      LECTOR += len(BUFFER1)
  
  
