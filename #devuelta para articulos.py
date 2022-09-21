#devuelta para articulos
precio=float(input("ingrese el precio del articulo: "))
pago=float(input("¡cuanto ha pagado el cliente? "))

cambio=pago-precio
falatante=precio-pago

if(cambio<0):
    print("falta dinero en el pago.el dinero faltante es ",falatante)

elif(cambio==0):
    print("se ha pagado exact. no es necesario dar vuelta ")

if(cambio>0):
    print(("el cambio a dara es ",cambio))