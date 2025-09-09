#Este ejercicio es para subior una decima en el corte

while True:

    numero = input("Introduce un número para saber si es par o impar: ")

    while not numero.isdigit():  
        print("Por favor, ingresa un número entero.")
        numero = input("Introduce un número para saber si es par o impar: ")

    numero = int(numero)  # Convierte la entrada a un número entero

    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
