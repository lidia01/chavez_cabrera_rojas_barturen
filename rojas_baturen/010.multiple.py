#programa paga ganar descuento
import os
#declarar
nomnbre=""
monto=0

#Input via os
nombre=os.sys.argv[1]
monto=(int(os.sys.argv[2]))

#prosecing
#si el monto es mayor a 100
#mostrar "ganaste un descuento de 10%"
if(monto>100):
    print(nombre,"ganaste un descuento de 10%")
if(monto<=100):
    print(nombre,"rellenar sus datos para una rifa de fin de año")
