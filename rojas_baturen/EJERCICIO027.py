#calidad de velocidad
#Declarar
velocidad=0.0
tiempo=0.0
velocidad=float(input("ingrese velocidad:"))
tiempo=float(input("ingrese tiempo:"))

#Procesing
distancia=velocidad*tiempo
if(distancia>400):
    print("buena")
else:
    print("mala")
#fin_si
