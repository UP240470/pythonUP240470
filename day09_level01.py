#1
edad=int(input("Ingresa su edad:"))
if edad >= 18:
    print("Puedes conducir")
else:
    print("No tienes edad para conducir")

#2
mi_edad=19
tu_edad=int(input("Ingresa tu edad: "))

if tu_edad==mi_edad:
    print("Tenemos la misma edad")
if tu_edad>mi_edad:
    diferencia=tu_edad-mi_edad
    if diferencia==1:
            print("Eres mayor por un año")
    else:
            print("Eres mayor que yo por", diferencia,"años")

elif tu_edad<mi_edad:
        print("Eres menor que yo")

#3
A=float(input("Dame un numero"))
B=float(input("Dame un numero"))

if A>B:
      print("a es mayor que b")
if A<B:
      print("a es menor que b")    
else:
      print("a es igual a b")        










