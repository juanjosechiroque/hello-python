# -*- coding: utf-8 -*-

import random


def run():

	rango_superior = int(raw_input("Ingrese hasta qué numero puede adivinar: "))

	number_found = False
	random_number = random.randint(1,rango_superior)
	intentos = 0

	while not number_found:
		intentos += 1
		number = int(raw_input("Intente nuevamente: "))

		if number == random_number:
			print("Felicitaciones! Encontraste el número en " + (str)intentos + " intento(s)")
			number_found = True
		elif number > random_number:
			print("El numero es más pequeño")			
		else:
			print("El numero es más grande")


if __name__ == "__main__":
	run()