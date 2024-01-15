def validacionint():
  try:
    x = int(input())
    return x
  except ValueError:
    print("Ese no es un numero entero.  Intenta de nuevo...")
    return validacionint()

def validacionfloat():
  try:
    x = float(input())
    return x
  except ValueError:
    print("Ese no es un numero decimal.  Intenta de nuevo...")
    return validacionfloat()

def validacionstr():
  try:
    x = str(input())
    return x
  except ValueError:
    print("Ese no es un texto.  Intenta de nuevo...")
    return validacionstr()

def validacionLlave(llave, dict):
  if llave in dict:
    print(llave,"Ya se encuentra registrada")
  else:
    return llave
