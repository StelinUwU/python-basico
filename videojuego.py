import random

def run():
    vidas = 5
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("""
Tienes 5 vidas
Elige un numero del 1 al 100: """))
    while numero_elegido != numero_aleatorio:
        vidas -= 1
        if vidas == 0:
            print("GAME OVER")
            print("Numero correcto: " + str(numero_aleatorio))
            break
        if numero_elegido > numero_aleatorio:
            print("Vidas restantes " + str(vidas))
            numero_elegido = int(input("Elige un numero mas pequeño: "))
        else:
            print("Vidas restantes " + str(vidas))
            numero_elegido = int(input("Elige un numero mas grande: "))
    if(numero_aleatorio == numero_elegido):
        print("Correcto")


if  __name__ == "__main__":
    run()    