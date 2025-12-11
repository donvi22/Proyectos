from random import *

nombre = input("Bienvenido al juego ADIVINA EL NUEMRO\n¿Cual es tu nombre?: ")
print(f"Encantado {nombre}, vamos a empezar el juego.")
secreto = randint(0, 100)
print("Las reglas son simples, vas a tener 8 intentos de adivinar un numero entre 0 a 100.\nEn cada intento fallido, te vamos a dar una pequeña pista.\n¿Estas listo? Pues empecemos.")
intento = 1

while intento > 0:
    print(f"Intento numero {intento}")
    numero = int(input("Introduce el numero: "))
    if numero == secreto:
        print(f"¡Si, lo has logrado! Has adivinado el numero secreto con {intento} intentos, enhorabuena.")
        break
    elif intento == 8:
        reintentar = input(f"Oh, que mal, se han cumplido los 8 intentos. El numero secreto era el {secreto}. ¿Quieres volver a intentarlo? (s/n)")
        if reintentar == "n":
            print("Vale, nos vemos a la proxima. Cagao.")
            break
        elif reintentar == "s":
            print("¡Perfecto! Esta vez si que lo vas a conseguir.")
            intento = 1
            secreto = randint(0, 100)
    elif numero > 100 or numero < 0:
        print("Te recuerdo que el numero secreto es entre el 0 al 100.")
        intento = intento + 1
    elif numero < secreto:
        print("El numero secreto es mas grande.")
        intento = intento + 1
    elif numero > secreto:
        print("El numero secreto es mas pequeño.")
        intento = intento + 1