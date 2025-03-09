from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

# Variable para almacenar el número secreto y los intentos
numero_secreto = randint(1, 100)
intentos_dict = {}

# Establecer el límite de intentos
limite_intentos = 8

def obtener_intento(intento_str):
    try:
        intento = int(intento_str)
        if 1 <= intento <= 100:
            return intento
        else:
            return None
    except ValueError:
        return None

def dar_pista_avanzada(numero_secreto, intento):
    diferencia = abs(numero_secreto - intento)
    
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
    
    if numero_secreto % 2 == 0:
        pistas.append("El número secreto es par")
    else:
        pistas.append("El número secreto es impar")
    
    if numero_secreto % 5 == 0:
        pistas.append("Es múltiplo de 5")
    elif numero_secreto % 3 == 0:
        pistas.append("Es múltiplo de 3")
    
    if numero_secreto > 50:
        pistas.append("Es mayor que 50")
    else:
        pistas.append("Es menor o igual que 50")
    
    return pistas[intento % len(pistas)]  # Rotamos las pistas

def calcular_puntos(intentos_realizados):
    if intentos_realizados <= 3:
        return 100
    elif intentos_realizados <= 5:
        return 70
    elif intentos_realizados <= 7:
        return 40
    else:
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global numero_secreto
    puntos = None  # Inicializamos los puntos como None
    if request.method == 'POST':
        intento_str = request.form.get('intento')
        intento = obtener_intento(intento_str)
        
        if intento is None:
            return render_template('index.html', mensaje="Entrada no válida. Por favor, ingresa un número entre 1 y 100.", intentos=intentos_dict, numero_secreto=numero_secreto, puntos=puntos)
        
        # Validación de números repetidos
        if intento in intentos_dict.values():
            return render_template('index.html', mensaje="Ya intentaste ese número. Por favor, ingresa un número diferente.", intentos=intentos_dict, numero_secreto=numero_secreto, puntos=puntos)
        
        # Si se ha alcanzado el límite de intentos, no permitir más intentos
        if len(intentos_dict) >= limite_intentos:
            mensaje = f"Has alcanzado el límite de {limite_intentos} intentos. El número secreto era {numero_secreto}."
            puntos = calcular_puntos(len(intentos_dict))  # Calculamos los puntos basados en intentos realizados
            return render_template('index.html', mensaje=mensaje, intentos=intentos_dict, numero_secreto=numero_secreto, puntos=puntos, juego_terminado=True)
        
        # Agregar intento al historial
        intentos_dict[f"intento{len(intentos_dict)+1}"] = intento
        
        if intento == numero_secreto:
            mensaje = f"¡Felicidades! Adivinaste el número secreto {numero_secreto}."
            puntos = calcular_puntos(len(intentos_dict))  # Calculamos los puntos en base a los intentos realizados
            return render_template('index.html', mensaje=mensaje, intentos=intentos_dict, numero_secreto=numero_secreto, puntos=puntos, juego_terminado=True)
        else:
            pistas_avanzada = dar_pista_avanzada(numero_secreto, intento)
            pistas_matematica = dar_pista_matematica(numero_secreto, len(intentos_dict))
            return render_template('index.html', mensaje="Intenta de nuevo.", pistas_avanzada=pistas_avanzada, pistas_matematica=pistas_matematica, intentos=intentos_dict, numero_secreto=numero_secreto, puntos=puntos)
    
    return render_template('index.html', mensaje="Bienvenido al juego 'Adivina el Número'!", intentos=intentos_dict, numero_secreto=numero_secreto, puntos=puntos)

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global numero_secreto, intentos_dict
    numero_secreto = randint(1, 100)
    intentos_dict = {}
    return render_template('index.html', mensaje="Bienvenido al juego 'Adivina el Número'!", intentos=intentos_dict, numero_secreto=numero_secreto, puntos=None)

if __name__ == '__main__':
    app.run(debug=True)
