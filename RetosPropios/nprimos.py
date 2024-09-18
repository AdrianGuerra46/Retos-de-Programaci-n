import time

start_time = time.time()

def es_primo(numero):
    
    if numero <= 1: #Por concepto los primos son mayores a 1
        return False
    
    for i in range(2, numero):
        if ((numero % i) == 0):
            return False
        
    return True


n = int(input("Ingrese cuantos numeros primero desea imprimir: "))

primo = 0;
actualn = 0; 

while (n > primo): 
    actualn = actualn + 1;
    if (es_primo(actualn)):
        print(f"El primo numero {primo + 1} es: {actualn}")
        primo += 1;


# Termina de medir el tiempo
end_time = time.time()

# Calcula el tiempo que tomó ejecutar el código
execution_time = end_time - start_time

print(f"El código tardó {execution_time} segundos en ejecutarse.")
print(f"El código tardó {execution_time/60} minutos en ejecutarse.")