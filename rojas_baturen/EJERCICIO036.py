#costo del cine
#Declarar
entradas=0.0
cancha=0.0

#input
entradas=float(input("ingrese pago de las entradas:"))
cancha=float(input(("ingrese pago de la cancha:")))

#Procesing
costo=entradas+cancha
if(costo<50):
    print("bueno")
else:
    print("malo")
#fin_if
