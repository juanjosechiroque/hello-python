def first_not_repeating_char(char_sequence):
    
	for char in char_sequence:

		veces = 0

		for item in char_sequence:
			if char == item:
				veces += 1

		if veces == 1:
			return char

	return "_"


if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))