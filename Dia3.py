#1.
edad=19
#2.
Altura=1.80
#3.
num_complejo=1j
#4.
base=float(input ("Dame la base"))
altura=float(input("Dame la altura"))
area=0.5*base*altura
print("El area del triangulo es:",area)
#5.
lA=float(input("Dame el lado A del triangulo"))
LB=float(input("Dame el lado B"))
LC=float(input("Dame el lado C"))
perimetro=lA+LB+LC
print("El perimetro del triangulo es:",perimetro)
#6.
largo=float(input("Dame el  largo del rectangulo"))
ancho=float(input("Dame su ancho del rectangulo"))
area=largo*ancho
perimetro6=2*(largo+ancho)
print("el area del rectangulo es: ",area,"el perimetro es de: ",perimetro)
#7.
radio=float(input("Dame el radio del circulo"))
area=3.14*radio*radio
circuferencia=2*3.14*radio
print("El area del circulo es: ",area,"La circuferencia es de: ",circuferencia)
#8
pendiente1=2
interseccion_x=1
interseccion_y =-2
print("la pendiente es :", pendiente1)
print("la Intersección en x es de :", interseccion_x)
print("la Intersección en y es de: ", interseccion_y)
#9.
x1,y1=2,2
x2,y2=6,10
pendiente2= (y2 - y1) / (x2 - x1)
print("La pendiente entre los puntos (2, 2) y (6, 10) es:", pendiente2)
#10.
iguales = pendiente1 == pendiente2
print("¿Las pendientes son iguales?", iguales)
#11.
valor=float(input("Dame un numero, nota si quieres que de 0 escoge -3"))
res=(valor*valor)+(valor*6)+9
print("el resultado es de:",res)
#12.
phyton='phyton'
dragon='dragon'
print("La longitud de python es de ",len(phyton),"y de dragon es de ",len(dragon))
print("estas palabras son: ",len(phyton)!=len(dragon))
#13.
print('on' in 'python' and 'on' in 'dragon')
#14.
frase = "Espero que este curso no esté lleno de jargon."
print("la frase Espero que este curso no esté lleno de jargon tiene jargon ","jargon" in frase)
#15.
print('on' not in 'dragon' and 'on' not in 'python')
#16.
phyton= len("python")
longitud_flotante = float(phyton)
longitud_cadena = str(phyton)
print(phyton, longitud_flotante, longitud_cadena)
#17.
numero = int(input("Ingresa un número: "))
if numero%2==0:
    print("Es par.")
else:
    print("Es impar.")
#18.
print(7 // 3 == int(2.7))
#19.
print(type('10') == type(10))
#20.
try:
    print(int('9.8') == 10)
except ValueError:
    print("No se puede convertir '9.8' a entero.")
#21.
horas=int(input("Dame las horas"))
tarifa=int(input("Dame la tarifa"))
pago_total=horas*tarifa
print("Tus ganancias semanales son: ",pago_total)

#22.
num_años=int(input("Dame tu edad: "))
edad_segundos=num_años*31536000
print(("Tu edad en segundos son: "),edad_segundos)

#23.


#prueba



