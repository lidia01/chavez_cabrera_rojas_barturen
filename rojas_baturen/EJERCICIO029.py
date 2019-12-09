#pago de salario
#Declarar
cantidad_empleados=0
cantidad_horas=0

#input
cantidad_empleados=int(input("ingrese cantidad de empleados:"))
cantidad_horas=int(input("ingrese cantidad de horas:"))

#Procesing
salario=cantidad_horas*cantidad_empleados
if (salario<1000):
    print("bajo salario")
else:
    print("mayor salario")
#fin_if
