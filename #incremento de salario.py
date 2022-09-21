#incremento de salario 
nombre=input("digite  el  nombre  y  apelldio  del  empleado:  ")
salario=float(input("salario  mensual  del  empleado:  "))
porcentajeincremento=int(input("porecentaje incremento:"))

incremento=salario*(porcentajeincremento/100)

print("nombre del trabajador:",nombre)
print("salario sin incremento: ",salario)
print("salario incrementado: ",incremento)