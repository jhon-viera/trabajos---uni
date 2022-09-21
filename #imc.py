#imc
peso=float(input("escrbir tu peso en kg: "))
talla=float(input("talla en mt: "))

imc=peso/(talla**2)
if imc < 18.5:
    print("bajo peso")
elif 18.5<= imc and  IMC < 25:
    print("normal")
elif 25 <= imc and imc <30:
    print("imc",imc)