'''
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
'''

#Para ponerme mi toque personal haré que el usuario pueda elegir hasta que numero desea imprimir en consola


try:
    number = int(input("Por favor, ingrese hasta qué número desea imprimir: "))
except ValueError:
    print("Debe ingresar un número entero.")
    exit()

# Números base de la sucesión
N0 = 0
N1 = 1

# Variables para la iteración
nActual = N0
nAnterior = None

# Imprimir los números de la sucesión de Fibonacci
for i in range(number):
    print(f"El número {i} de la sucesión de Fibonacci es: {nActual}")
    # Calcular el siguiente número de la sucesión
    if nAnterior is not None:
        nSiguiente = nActual + nAnterior
    else:
        nSiguiente = N1
    # Actualizar los números
    nAnterior = nActual
    nActual = nSiguiente


