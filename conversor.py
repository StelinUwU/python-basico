def conversor(tipo_pesos, valor_dolar):
  monedas = input("Ingrese la cantidad de " +  tipo_pesos + ": ")
  monedas = float(monedas)
  dolares = monedas / valor_dolar
  dolares = round(dolares, 3)
  dolares = str(dolares)
  print("Tienes $" + dolares + " dólares")


opcion = input("""
  Bienvenido al conversor de monedas❤
  1 -Lempiras
  2 -Pesos colombianos
  3- Pesos mexicanos

  Elige una opción: """)



if opcion == "1":
  conversor("Lempiras", 24.274)
elif opcion == "2":
  conversor("Pesos colombianos", 3560.01)
elif opcion == "3":
  conversor("Pesos mexicanos", 20.28)
else:
  print("Ingresa una opcion correcta")

