#programa 05
import os
#declara
nombre=""
edad=0

#Input via os
nombre=(os.sys.argv[1])
edad=int(os.sys.argv[2])

#processing
#si es mayor a 18 años
#mostrar "independencia economica"
if (edad > 18):
    print("independenca economica")
else:
    print("no puede independizarce economicamente")

