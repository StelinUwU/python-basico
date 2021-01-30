def es_Palindromo(palabra):
  if palabra == palabra[::-1]:
    return True
  else:
    return False


def run():
  palabra = input(""" 
  ¿Es un palíndromo?
  Ingresa la palabra: """)
  palabra = palabra.lower().replace(" ", "");
  if es_Palindromo(palabra):
    print("Es Palindromoooooooooooo")
  else:
    print("No es palindromo, chale")

if __name__ == "__main__":
  run()