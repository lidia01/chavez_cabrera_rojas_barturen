#mayor de edad
#declaracion
nombre=""
dni=""
año_nacimiento=0
año_actual=0

#Input
nombre=input("ingrese nombre:")
dni=input("ingrese dni:")
año_nacimiento=int(input("año_nacimiento:"))
año_actual=int(input("año actual:"))

#procesing
edad=(año_actual - año_nacimiento)
if(edad>18):
    print("mayor_edad")
#fin_if

