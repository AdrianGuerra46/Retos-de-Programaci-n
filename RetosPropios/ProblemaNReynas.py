import numpy as np


def AttackReyna(fila,columna,tablero,tamañoTablero):
    if tablero[fila,columna] == "R":
        print("Ya hay una Reyna en esa casilla")
        return

    elif tablero[fila,columna] == "x":
        print("Hay otra Reyna atacando esa casilla")
        return
    else:
        tablero[fila,columna] = "R"
    # Recorrer todas las posiciones del Tablero
    for x in range(tamañoTablero):  # Itera sobre las filas 
        for y in range(tamañoTablero):  # Itera sobre las columnas
            if (tablero[x, y] == "R"):
                continue
            if ((x == fila) or (y == columna)):
                if(tablero[x,y] == "R"):
                    print(f"La reyna en la posicion {fila},{columna} atacaría a otra Reyna")
                    break
                else:
                    tablero[x, y] = "x"
                    
            if (((x + y)==(fila + columna)) or ((x - y)==(fila - columna))):
                if(tablero[x,y] == "R"):
                    print(f"La reyna en la posicion {fila},{columna} atacaría a otra Reyna")
                    break
                else:
                    tablero[x, y] = "x"            
            
n = int(input("Ingrese el orden del tablero: ")) #Por ejemplo si es "3" se crea un tablero 3x3
Tablero = np.zeros((n, n), dtype=object)  # Crea una matriz de ceros con tipo de dato object
print("Tu Tablero vacío es: ")
print(Tablero)
# Reynas = [];


fR1 = int(input("La fila de Ubicacion de una Reyna:")) # Las filas van desde 0 hasta n-1
cR1 = int(input("La columna de Ubicacion de una Reyna:")) # Las columnas van desde 0 hasta n-1

AttackReyna(fR1,cR1,Tablero,n)
# Reynas.append((fR1,cR1))


# Recorrer todas las posiciones del Tablero
for i in range(n):  # Itera sobre las filas 
    for j in range(n):  # Itera sobre las columnas
        if (Tablero[i,j]==0):
           AttackReyna(i,j,Tablero,n);
        
        #print(f"Posición ({i}, {j}): {Tablero[i, j]}")  

# AttackReyna(1,2,Tablero,n)
print("El tablero con las Reyna ubicadas es:")
print(Tablero)
# print("Las Reynas están ubicadas en (fila, columna): ")
# print(Reynas)

