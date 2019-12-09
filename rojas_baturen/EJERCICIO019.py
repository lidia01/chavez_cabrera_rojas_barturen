#curso reprobado
#declarar
alumno=""
nota1=0
nota2=0
nota3=0

#input
alumno=input("ingrese nombre del alumno:")
nota1=int(input("ingrese la nota1:"))
nota2=int(input("ingrese la nota2:"))
nota3=int(input("ingrese la nota3:"))

#Procesing
promedio=(nota1+ nota2 + nota3) /3
if (promedio<10.5):
    print("reprobo el curso")
#fin_if
