from random import randint

# Función para manejar la validación de la entrada
def obtener_intento():
    while True:
        try:
            intento = int(input("¿Cuál crees que es el número? "))
            if 1 <= intento <= 100:
                return intento
            else:
                print("Por favor, ingresa un número entre 1 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

# Función principal para jugar
def jugar():
    numero_secreto = randint(1, 100)
    intentos_dict = {}
    nombre = input("¿Cuál es tu nombre? ")

    print(f"\nHola, {nombre}. He pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinarlo.")

    for i in range(1, 9):  # Va del 1 al 8
        intento = obtener_intento()
        intentos_dict[f"intento{i}"] = intento  # Guardamos el intento en el diccionario

        # Lógica de juego
        if intento < numero_secreto:
            print(f"Intento {i}: El número secreto es mayor al número.")
        elif intento > numero_secreto:
            print(f"Intento {i}: El número secreto es menor al número.")
        else:
            print(f"¡Felicidades, {nombre}! Adivinaste el número secreto {numero_secreto} en el intento {i}!")
            break
    else:
        print(f"\nNo lograste adivinar el número secreto. Era {numero_secreto}.")

    # Imprimimos el diccionario con los intentos
    print("\nTus intentos fueron:")
    for clave, valor in intentos_dict.items():
        print(f"{clave}: {valor}")

    # Preguntar si quiere jugar otra vez
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if jugar_otra_vez == "s":
        jugar()
    else:
        print("¡Gracias por jugar!")

# Iniciar el juego
jugar()
