#contador de negativos y postivos
n=int(input("ingrese el numero de datos por porcesar: "))

if n>0:
    postivos=0
    negativos=0
    nulos=0

    for i in range (n):
        dato=int(input("ingrese un numero natural: "))

        if dato > 0:
            positivos+=1

        elif dato < 0:
            negativos+=1

        else:
             nulos += 1

    print ("la cantidad de numero postivos fue: ",positivos,
    "la cantida de numeros negativos fue:",negativos,
    "la cantida ae numeros nulos fue:",nulos)
else:
    print("el numero ingresado no es validod")