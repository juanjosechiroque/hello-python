


def main():
	palabra = str(raw_input("Por favor, ingrese una palabra" ))

	if (palabra == palabra[::-1]) :
		print("La palabra es un pal")
	else:
		print("La palabra NO es un palindromo")


if __name__ == "__main__":
	main()