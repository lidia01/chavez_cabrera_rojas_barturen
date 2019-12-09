#inpuesto mensual
#Declarar
trabajador=""
renumeracion_anual=0.0
tasa=0.0
trabajador=str(input("ingrese nombre del trabajador:"))
renumeracion_anual=float(input("ingrese renumeracion neta anual:"))
tasa=float(input("ingrese tasa "))

#PROCESSING
total=renumeracion_anual*tasa
if (total>400):
    print("inpuesto mensual")
#fin_if
