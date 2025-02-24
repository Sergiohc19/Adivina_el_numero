from random import randint

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

def dar_pista_avanzada(numero_secreto, intento):
 diferencia = abs(numero_secreto - intento)
 
 # Pista sobre la distancia
 if diferencia > 50:
     return "¡Estás muy lejos!"
 elif diferencia > 30:
     return "Estás bastante lejos"
 elif diferencia > 20:
     return "Te estás acercando..."
 elif diferencia > 10:
     return "¡Cada vez más cerca!"
 elif diferencia > 5:
     return "¡Casi casi!"
 else:
     return "¡Estás muy muy cerca!"

def dar_pista_matematica(numero_secreto, intento):
 pistas = []
 
 # Pista sobre par/impar
 if numero_secreto % 2 == 0:
     pistas.append("El número secreto es par")
 else:
     pistas.append("El número secreto es impar")
 
 # Pista sobre múltiplos
 if numero_secreto % 5 == 0:
     pistas.append("Es múltiplo de 5")
 elif numero_secreto % 3 == 0:
     pistas.append("Es múltiplo de 3")
 
 # Pista sobre dígitos
 if numero_secreto > 50:
     pistas.append("Es mayor que 50")
 else:
     pistas.append("Es menor o igual que 50")
 
 return pistas[intento % len(pistas)]  # Rotamos las pistas

def jugar():
 numero_secreto = randint(1, 100)
 intentos_dict = {}
 nombre = input("¿Cuál es tu nombre? ")

 print(f"\nHola, {nombre}. He pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinarlo.")

 for i in range(1, 9):
     intento = obtener_intento()
     intentos_dict[f"intento{i}"] = intento

     if intento == numero_secreto:
         print(f"¡Felicidades, {nombre}! ¡Adivinaste el número secreto {numero_secreto} en el intento {i}!")
         break
     else:
         # Damos múltiples pistas
         print(f"\nIntento {i}:")
         if intento < numero_secreto:
             print("El número secreto es mayor que tu intento.")
         else:
             print("El número secreto es menor que tu intento.")
         
         print(dar_pista_avanzada(numero_secreto, intento))
         print(dar_pista_matematica(numero_secreto, i))
         print(f"Intentos restantes: {8-i}")
         print("-" * 40)
 else:
     print(f"\n¡Lo siento! No lograste adivinar el número secreto. Era {numero_secreto}.")

 # Imprimimos el historial de intentos
 print("\nTu historial de intentos:")
 for clave, valor in intentos_dict.items():
     print(f"{clave}: {valor}")

 # Preguntar si quiere jugar otra vez
 jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
 if jugar_otra_vez == "s":
     print("\n" + "="*50 + "\n")  # Separador visual entre juegos
     jugar()
 else:
     print("\n¡Gracias por jugar!")

# Iniciar el juego
if __name__ == "__main__":
 jugar()