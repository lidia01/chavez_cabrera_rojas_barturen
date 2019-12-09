#descuento
#Declarar
precio=0.0
precio_final=0.0

#input
precio=float(input("ingrese precio:"))
precio_final=float(input("ingrese precion final:"))

#Procesing
descuento=(1-precio_final/precio)*100
if(descuento>30):
    print("descuento")
#fin_if

