#parcial1

n=int(input("ingrese el numero de personas al procesar: "))
inicio=0

def calculo(a,b):

    imc=(a/b*b)
    print(f"el imc calculado es: {imc}")
    if imc < 18.5:
            print("bajo peso")
            print(f"el imc calculado es: {imc}")
    elif 18.5>= imc and  IMC < 24.9:
            print("normal")
            print(f"el imc calculado es: {imc}")
    elif 25 >= imc and imc <26.9:
            print("sobre peso grado I")
            print(f"el imc calculado es: {imc}")
    elif 27 >= imc and imc <29.9:
         print("sobre peso grado II")
         print(f"el imc calculado es: {imc}")
    elif  30>= imc and imc <34.9:
            print("obesidad tipo I")
            print(f"el imc calculado es: {imc}")
    elif  35>= imc and imc <39.9:
            print("obesidad de tipo II")
            print(f"el imc calculado es: {imc}")
    elif 40 >= imc and imc <49.1:
            print("obesidad de tipo III")
            print(f"el imc calculado es: {imc}")
    elif  50>= imc:
            print("obesidad tipo IV")
            print(f"el imc calculado es: {imc}")

while inicio < n:
    nombre=str(input("ingrese tu nombre: "))
    apellido=str(input("ingrese tu apellido: "))
    genero=str(input("ingrese tu genero: "))
    edad=int(input("ingrese tu edad: "))
    peso=float(input("ingrese tu peso: "))
    estatura=float(input("ingrese tu estatura: "))
    inicio=inicio+1
    
    calculo(peso,estatura)







