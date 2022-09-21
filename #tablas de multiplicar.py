#tablas de multiplicar 
n=int(input("ingrese numero entero positivo"))

if n>0:
    for i in range (1,11):
        print(n,"por",i,"es igual a: ",n*i)

else:
    print("el numero no es valido")