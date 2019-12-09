#pago con trajeta
#Declarar
producto=""
compra=0.0

#input
producto=input("ingrese producto:")
compra=float(input("ingrese cantidad de compra:"))

#processing
pago_tarjeta=(compra>50)
if (compra>50):
    print("pago con tarjeta")
#fin_if
