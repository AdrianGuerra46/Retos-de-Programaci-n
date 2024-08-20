

def es_primo(numero):
    
    if numero <= 1: #Por concepto los primos son mayores a 1
        return False
    
    for i in range(2, numero):
        if ((numero % i) == 0):
            return False
        
    return True


for x in range(101):
    if (es_primo(x)):
        print(f"El numero: {x} es primo")




