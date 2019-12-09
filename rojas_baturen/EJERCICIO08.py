#exceso de compras
#declaracion
cliente=""
dni:""
producto=""
cantidad=0

#Input
cliente=input("ingrese cliente:")
dni=input("ingrese dni:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad:"))

#procesing
total=(cantidad)
if(total>800):
    print("exeso_compras")
#fin_if
