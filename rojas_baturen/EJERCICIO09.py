#exceso de precio de arroz
#declaracion
cliente=""
producto=""
cantidad=0.0
precio=0.0
#Input
cliente=input("ingrese cliente:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad:"))
precio=int(input("ingrese precio:"))

#procesing
total=(cantidad*precio)
if(total>5):
    print("exceso_percio_arroz")
#fin_if
