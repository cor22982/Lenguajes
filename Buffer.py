AVANCE =0
INICIOLEXEMA =0
LEXEMAS = []
LECTOR =0
LEXEMA = ""
FLAG_BUFFER = 1
FLAG_SALIDA = True

# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
  global AVANCE, INICIOLEXEMA, LEXEMAS, LEXEMA, FLAG_SALIDA
  AVANCE = 0
  INICIOLEXEMA = 0
  for i in range(len(buffer)) :
    caracter = buffer[AVANCE]
    if caracter == " ":
      INICIOLEXEMA = i + 1
      LEXEMAS.append(LEXEMA)
      AVANCE = INICIOLEXEMA
      LEXEMA = ""
    
    elif caracter =="eof":
      LEXEMAS.append(LEXEMA)
      FLAG_SALIDA = False
      break

    else:
      AVANCE = i +1
      if caracter != " ":
        LEXEMA += caracter

if __name__ == "__main__":
  BUFFER1 = []
  BUFFER2 = []
  tamano_buffer = 10
  entrada = list("Esto es un ejemplo de entrada con eof")

  while FLAG_SALIDA:
    if AVANCE == 0 and FLAG_BUFFER ==1:
      BUFFER1 = cargar_buffer(entrada, LECTOR, tamano_buffer)
      procesar_buffer(BUFFER1)
      LECTOR += len(BUFFER1)
    elif AVANCE == len(BUFFER1) and FLAG_BUFFER ==1:
      BUFFER2 = cargar_buffer(entrada, LECTOR, tamano_buffer)
      procesar_buffer(BUFFER2)
      LECTOR += len(BUFFER2)
      FLAG_BUFFER = 2
    elif AVANCE == len(BUFFER2) and FLAG_BUFFER ==2:
      BUFFER1 = cargar_buffer(entrada, LECTOR, tamano_buffer)
      procesar_buffer(BUFFER1)
      LECTOR += len(BUFFER1)
      FLAG_BUFFER = 1
  
  print(LEXEMAS)
  
  
