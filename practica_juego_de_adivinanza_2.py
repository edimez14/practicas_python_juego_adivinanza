# primero importamos los paquetes que vamos a usar
# import os  # "os" es para limpiar la pantalla despues de cada ronda del ciclo
import random  # "random" es para generar de forma aleatoria un numero

# conteo de victorias
victorias_maquina_1 = 0
victorias_maquina_2 = 0

# Ciclo de jugadas
for i in range(1, 10):

    # Definir los límites inferiores y superiores
    inferior = 1
    superior = 1000

    # Generar el número secreto
    secreto = random.randint(1, 1000)

    # Inicializar las variables de las máquinas
    maquina_1 = -1
    maquina_2 = -1

    # intentos
    max_intentos_maquina_1 = 8
    max_intentos_maquina_2 = 8

    # Mostrar el título del juego
    print('<---   juego adivina el numero   --->\n')

    # Mientras ninguna máquina haya acertado el número
    while maquina_1 != secreto and maquina_2 != secreto:

        # Limpiar la pantalla
        # os.system('cls')

        # Pedir el número de la primera máquina y mostrarlo
        print('maquina_1, cual crees que es el numero?')
        maquina_1 = random.randint(inferior, superior)
        print(f'maquina_1: {maquina_1}')
        # Verificar si el número es mayor, menor o igual al número secreto
        if maquina_1 < secreto:
            print('maquina_1 tu numero es menor, intenta de nuevo')
            inferior = maquina_1 + 1
            # disminuir los intentos
            max_intentos_maquina_1 -= 1
            print(
                f'maquina_1 has perdidos un intento te quedan: {max_intentos_maquina_1}\n')
            # si la maquina 1 fallo todos sus intentos pierde y la ronda la gana la maquina 2
            if max_intentos_maquina_1 == 0:
                print('maquina_1 has fallado todos tus intentos')
                print('como maquina_1 a fallado todos sus intentos maquina_2 gana\n')
                victorias_maquina_2 += 1
                break
        elif maquina_1 > secreto:
            print('maquina_1 tu numero es mayor, intenta de nuevo')
            superior = maquina_1 - 1
            # disminuir los intentos
            max_intentos_maquina_1 -= 1
            print(
                f'maquina_1 has perdidos un intento te quedan: {max_intentos_maquina_1}\n')
            # si la maquina 1 fallo todos sus intentos pierde y la ronda la gana la maquina 2
            if max_intentos_maquina_1 == 0:
                print('maquina_1 has fallado todos tus intentos')
                print('como maquina_1 a fallado todos sus intentos maquina_2 gana\n')
                victorias_maquina_2 += 1
                break
        else:
            print('has acertado el numero, la maquina_1 a ganado\n')
            victorias_maquina_1 += 1
            # Si la máquina acertó el número, salir del ciclo while
            break

        # Pedir el número de la segunda máquina y mostrarlo
        if maquina_1 != secreto:
            print('maquina_2, cual crees que es el numero?')
            maquina_2 = random.randint(inferior, superior)
            print(f'maquina_2: {maquina_2}')
            # Verificar si el número es mayor, menor o igual al número secreto
            if maquina_2 < secreto:
                print('maquina_2 tu numero es menor, intenta de nuevo')
                inferior = maquina_2 + 1
                if maquina_2 > inferior:
                    inferior = maquina_2 + 1
                # disminuir los intentos
                max_intentos_maquina_2 -= 1
                print(
                    f'maquina_2 has perdidos un intento te quedan: {max_intentos_maquina_2}\n')
                # si la maquina 2 fallo todos sus intentos pierde y la ronda la gana la maquina 1
                if max_intentos_maquina_2 == 0:
                    print('maquina_2 has fallado todos tus intentos')
                    print(
                        'como maquina_2 a fallado todos sus intentos maquina_1 gana\n')
                    victorias_maquina_1 += 1
                    break
                # Verificar que el número de la segunda máquina no sea igual al de la primera
            elif maquina_2 > secreto:
                print('maquina_2 tu numero es mayor, intenta de nuevo')
                superior = maquina_2 - 1
                # Verificar que el número de la segunda máquina no sea igual al de la primera
                if maquina_2 < superior:
                    superior = maquina_2 - 1
                # disminuir los intentos
                max_intentos_maquina_2 -= 1
                print(
                    f'maquina_2 has perdidos un intento te quedan: {max_intentos_maquina_2}\n')
                # si la maquina 2 fallo todos sus intentos pierde y la ronda la gana la maquina 1
                if max_intentos_maquina_2 == 0:
                    print('maquina_2 has fallado todos tus intentos')
                    print(
                        'como maquina_2 a fallado todos sus intentos maquina_1 gana\n')
                    victorias_maquina_1 += 1
                    break
            else:
                print('has acertado el numero, la maquina_2 a ganado\n')
                victorias_maquina_2 += 1
                # Si la máquina acertó el número, salir del ciclo while
                break

# Imprimir resultado final de victorias
print(f"Maquina 1 ha ganado {victorias_maquina_1} veces.")
print(f"Maquina 2 ha ganado {victorias_maquina_2} veces.\n")

# input para continuar el juego que hace que no cierre la ventana
input('presiona enter para continuar...')
