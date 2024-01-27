"""
este código tenia un error y es que no actualizaba los limites superior he inferior de la variable numero
esto pasaba porque no se retornaba el valor de la variable numero, todo esto se soluciono retornando todos estos valores
por mi inexperiencia no sabia muy bien como hallar la solución y por eso pase por alto el retornar el valor de la vairble numeror
por eyo tuve que pedirle ayuda a chatgpt para ver como encontrar una solución a mi problema, asi que todo el credito a chatgpt
"""

# primero importamos los paquetes que vamos a usar
import os #"os" es para limpiar la pantalla despues de cada ronda del ciclo
import random #"random" es para generar de forma aleatoria un numero

# Función para la lógica de adivinanza de números
def adivinar_numero(secreto, inferior, superior, maquina):
    numero = random.randint(inferior, superior)
    print(f'{maquina}: {numero}')
    if numero < secreto:
        print(f'{maquina}, tu número es menor. Intenta de nuevo.\n')
        inferior = numero + 1
    elif numero > secreto:
        print(f'{maquina}, tu número es mayor. Intenta de nuevo.\n')
        superior = numero - 1
    else:
        print(f'¡{maquina} ha adivinado el número! ¡{maquina} ha ganado!\n')
        return numero
    return numero, inferior, superior

# Inicializar el diccionario de victorias
victorias = {'Maquina 1': 0, 'Maquina 2': 0}

# Ciclo de jugadas
for i in range(1, 10):
    
    inferior = 1
    superior = 1000
    secreto = random.randint(1, 1000)

    # Variable para llevar el registro de qué máquina adivinó el número
    ganador = None 

    print('<---   juego adivina el numero   --->\n')

    while ganador is None:

        # os.system('cls')

        print('Maquina 1, ¿cuál crees que es el número?')
        resultado = adivinar_numero(secreto, inferior, superior, 'Maquina 1')
        if isinstance(resultado, int):
            ganador = 'Maquina 1'
        else:
            numero, inferior, superior = resultado

        if ganador is None:
            print('Maquina 2, ¿cuál crees que es el número?')
            resultado = adivinar_numero(secreto, inferior, superior, 'Maquina 2')
            if isinstance(resultado, int):
                ganador = 'Maquina 2'
            else:
                numero, inferior, superior = resultado


    # Actualizar el diccionario de victorias
    victorias[ganador] += 1
    # Imprimir el resultado fuera del ciclo while            
    # print(f'¡{ganador} ha ganado!\n') 

# Imprimir el diccionario de victorias de cada maquina despues de finalizar todas las rondas
print(f"Maquina 1 ha ganado: {victorias['Maquina 1']} veces")
print(f"Maquina 2 ha ganado: {victorias['Maquina 2']} veces")

#input para cerrar la ventana y asi no se cierra de forma automática
input('Presione cualquier tecla para salir...')