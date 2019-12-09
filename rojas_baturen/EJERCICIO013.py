#comprador compulsivo
#declarar
cliente=""
producto=""
cantidad=0
costo_de_unidad=0.0
cliente=str(input("ingrese nombre del cliente:"))
producto=str(input(input("ingrese nomnre del  producto: ")))
cantidad=int(input("ingrese cantidad: "))
costo_de_unidad=float(input("ingrese el costo de unidad:"))
#PROCESING
total=cantidad*costo_de_unidad
if (total>25000):
    print("comprador compulsivo")
else:
    print("no es comprador compulsivo")
#fin_if
