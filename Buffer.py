AVANCE =0
INICIOLEXEMA =0
LEXEMAS = []
LECTOR =0
LEXEMA = ""
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
      i = len(buffer)

    else:
      AVANCE = i +1
      if caracter != " ":
        LEXEMA += caracter

if __name__ == "__main__":
  BUFFER = []
  tamano_buffer = 10
  entrada = list("Esto es un ejemplo eof")

  while FLAG_SALIDA:
    BUFFER1 = cargar_buffer(entrada, LECTOR, tamano_buffer)
    procesar_buffer(BUFFER1)
    LECTOR += len(BUFFER1)


  for i in LEXEMAS:
    print(f"Lexema procesado: {i}")
  
  
