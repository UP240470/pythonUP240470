#1
def sumar_dos_numeros (a,b):
    return a+b
print(sumar_dos_numeros(1,2))

#2
def area_de_circulo(radio):
    pi=3.14
    return pi*radio*radio
print(area_de_circulo(5))
#3
def sumar_todos_numeros(*args):
    for valor in args:
        if not isinstance(valor,(int,float)):
            return "Error: todos los elementos deben ser numeros"
        return sum(args)
    
resultado = sumar_todos_numeros(5, 10, 15, 20)
print(f"Resultado de la suma total: {resultado}")

    
#4
def convertir_celcius_a_fahrenheit(celsius):
    return(celsius*9/5)+32
print(convertir_celcius_a_fahrenheit(1000))

#5
def verificar_estacion(mes):
    mes=mes.lower()
    if mes in ['diciembre','enero','febrero']:
        return 'invierno'
    elif mes in ['marzo','abril','mayo']:
        return 'primavera'
    elif mes in ['junio','julio','agosto']:
        return 'verano'
    elif mes in ['septiembre','octubre','noviembre']:
        return 'otoño'
    else:
        return 'mes invalido'
print(verificar_estacion('diciembre'))

#6
def calcular_pendientes(x1,y1,x2,y2):
    if x2-x1==0:
        return "Infinita (division por cero)"
    return(y2-y1)/(x2-x1)
print(calcular_pendientes(50,10,30,70))

#7
import cmath
def resolver_ecuacion(a,b,c):
    discriminante=cmath.sqrt(b**2-4*a*c)
    x1=(-b+discriminante)/(2*a)
    x2=(-b-discriminante)/(2*a)
    return x1,x2
print(resolver_ecuacion(20,60,80))

#8
def imprimir_lista(lista):
    for elemementos in lista:
           print(elemementos)
#9
def revertir_lista(lista):
    lista_invertida=[]
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida

#10
def capitalizar_lista(lista):
    return[elemento.capitalize()for elemento in lista]

#11
def agregar_elemento(lista,item):
    if item in lista:
        lista.remove(item)
    return lista

#13
def suma_de_numeros(n):
    return sum(range(n+1))

#14
def suma_de_impares(n):
    return sum(range(n+1))

#15
def suma_de_pares(n):
    return sum(i for i in range(n+1)if i%2==0)



















