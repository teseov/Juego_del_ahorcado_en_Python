import random

palabras = ['madrid', 'barcelona', 'malaga', 'sevilla', 'bilbao', 'pamplona']

palabra = random.choice(palabras)

adivina = list("_" * len(palabra))

max_intentos = 6
intentos = 0

while intentos < max_intentos and "_" in adivina:
    print("".join(adivina))

    letra = input("juego del ahorcado. Adivina la ciudad de España. Escribe una letra: ")

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                adivina[i] = letra
    else:
        intentos += 1
        print("Has fallado. Te quedan {} intentos.".format(max_intentos - intentos))

    if "_" not in adivina:
        print("¡Felicidades! La palabra adivinada es: {}".format(palabra))
        break

if intentos == max_intentos:
    print("Perdiste. Esta era la palabra: {}".format(palabra))

