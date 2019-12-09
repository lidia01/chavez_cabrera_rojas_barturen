#precioa altos
#Declarar
costo_gas=0.0
costo_cocina=0.0
costo_gas=float(input("ingrese costo de gas:"))
costo_cocina=float(input("ingrese costo de cocina:"))

#Procesing
total=costo_gas+costo_cocina
if(total<200):
    print(" barato")
else:
    print("caro")
#fin_if
