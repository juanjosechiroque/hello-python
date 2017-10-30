# -*- coding: utf-8 -*-
from lampara import Lampara

def run():
	lampara = Lampara(is_turned_on=False)

	while True:
		command = str(raw_input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

		if command == "p":
			lampara.turn_on()
		elif command == "a":
			lampara.turn_off()
		else:
			break


if __name__ == "__main__":
	run()