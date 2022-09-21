#numero primos 
numero=int(input("ingrese numero"))
valor=range(2,numero)
contador=0
for n in valor:
    if numero % n==0:
        contador+=1
if contador>0:
    print("el numero no es primo")
else:
    print("el numero es primo")