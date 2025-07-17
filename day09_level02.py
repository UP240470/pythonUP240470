puntaje=int(input("Dame tu calificacion"))

if puntaje>=80 and puntaje<=100:
    print("Tienes A")
if puntaje>=70 and puntaje <=89:
    print("Tienes B")
if puntaje>=60 and puntaje <=69:
    print("Tienes C")
if puntaje>=50 and puntaje <=59:
    print("Tienes D")    
if puntaje<50:
    print("Tienes F")

#2
mes=str(input("Dame el mes en minusculas"))

if mes in ['septiembre','octubre','noviembre']:
    print("La estacion es Otoño")

if mes in ['diciembre','enero','febrero']:
    print("La estacion es invierno")


if mes in ['marzo','abril','mayo']:
    print("La estacion es primavera")


if mes in ['junio','julio','agosto']:
    print("La estacion es verano")

#3
frutas=['platano','naranja','mango','limon']
fruta_nueva=input("Ingresa una fruta:").lower()

if fruta_nueva in frutas:
    print("La fruta ya existe en la lista")
else:
    frutas.append(fruta_nueva)    
    print("fruta agregada. Lista actualizada:",frutas)




