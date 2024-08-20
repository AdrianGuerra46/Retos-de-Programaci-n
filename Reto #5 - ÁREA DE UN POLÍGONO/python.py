
import math

def poligono(lados,longitud):
    if lados <= 2:
        return "Error los poligonos tienen 3 lados o más"

    Rad = math.radians((math.pi)/lados)
    #La formula para calcular el área de un poígono regular es: A = (#lados * longitud^2)/(4*tan(pi/lados))
    A = (lados*(longitud**2))/(4*math.tan(Rad))
    return A

try: 
    Y = int(input("Por favor ingrese el número de lados que tiene tu polígono"))
except:
    print("Deber ingresar un número entero")

try: 
    X = int(input("Por favor ingrese la longitud de cada lado"))
except:
    print("Deber ingresar un número entero")

print(poligono(Y,X))