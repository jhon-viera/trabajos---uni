#aprobacion de estudiantes

nombre=input("digite  el  nombre  y  apelldio  del  estudiante:  ")
grado=int(input("digite  el  grado del estudiante :  "))

nota1=float(input("nota numero 1:"))
nota2=float(input("nota numero 2: "))
nota3=float(input("nota numero 3: "))
nota4=float(input("nota numero 4: "))

promedio=nota1+nota2+nota3+nota4/4

if promedio >=12:
    print("el estudiante aprobo ")

else:
    print("el estudiante reprobo")

notafinal=promedio/4
print("nombre del etudiante: ",nombre)
print("grado del etudiante: ",grado)
print("nota final: ",notafinal)