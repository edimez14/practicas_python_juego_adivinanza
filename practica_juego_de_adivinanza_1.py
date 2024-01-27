import os
import random

# vitorias_m1 = 0
# vitorias_m2 = 0

#ciclo de jugadas
for i in range(1, 10):
	inferior = 1
	superior = 1000000
	secreto = random.randint(1, 1000000)
	maquina_1 = -1
	maquina_2 = -1
	print('<---   juego adivina el numero   --->')
	while maquina_1 != secreto and maquina_2 != secreto:
		
		os.system('cls')
		print('maquina_1, cual crees que es el numero?')
		#jugador maquina_1
		maquina_1 = random.randint(inferior, superior)
		print(f'maquina_1: {maquina_1}')
		if maquina_1 < secreto:
			print('maquina tu numero es menor, intenta de nuevo')
			inferior = maquina_1 + 1
		elif maquina_1 > secreto:
			print('maquina tu numero es mayor, intenta de nuevo')
			superior = maquina_1 - 1
		else:
			print('has acertado el numero, la maquina_1 a ganado')
		#jugador maquina_2
		if maquina_1 != secreto:
			maquina_2 = random.randint(inferior, superior)
			print(f'maquina_2: {maquina_2}')
			if maquina_2 < secreto:
				print('maquina_2 tu numero es menor, intenta de nuevo')
				inferior = maquina_2 + 1
				if maquina_2 > inferior:
						inferior = maquina_2 + 1
			elif maquina_2 > secreto:
				print('maquina_2 tu numero es mayor, intenta de nuevo')
				superior = maquina_2 - 1
				if maquina_2 < superior:
					superior = maquina_2 - 1
			else:
				print('has acertado el numero, la maquina_2 a ganado')
		# if maquina_1 == secreto:
		# 	vitorias_m1+=1
		# 	print(f'la maquina_1 a gano {vitorias_m1} veces')
		# elif maquina_2 == secreto:
		# 	vitorias_m2+=1
		# 	print(f'la maquina_2 a gano {vitorias_m2} veces')



	# input('presiona enter para continuar...')