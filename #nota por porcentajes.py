#nota por porcentajes

def calcularnota(n1, n2, n3):
    return(n1*0.3)+(n2*0.3)+(n3*0.4)
n1=float(input("ingrese nota 1: "))
n2=float(input("ingrese nota 2: "))
n3=float(input("ingrese nota 3: "))

notafinal=calcularnota(n1, n2, n3)

print("la nota final es: ",notafinal)