
input = int(input("Ingresar un numero entero: "))
        
iter = 0;

while (input != 1):
    if ((input%2)==0):
        input = input/2
    else:
        input = (input*3)+1
    iter = iter+1
       
print(f"Tardaste {iter} iteraciones en llegar al 1")

