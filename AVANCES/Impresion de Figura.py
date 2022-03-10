print ("A dibujar un rectangul:")

try:
    length = int(input("Ingrese la medida de los lados del cuadrado "))
except ValueError:
    print ("\nParece ser que se ingreso un valor no valido, intenta nuevamente")


assert (length > 0), "\nLas medidas del cuadrado seran mostrados"

row = "x"*length
i = length

print ("\n")

while i > 0: 
    print (row)
    i = i-1

area = length*length

print ("\nEl area del cuadrado es: ", str(area))