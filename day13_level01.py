#1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [n for n in numbers if n <= 0]
print(negativos_y_cero) 

#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanado = [num for sublista in list_of_lists for fila in sublista for num in fila]
print(aplanado)  

#3
tabla = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
for fila in tabla:
    print(fila)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

resultado = [[pais.upper(), pais[:3].upper(), capital.upper()] 
             for fila in countries for (pais, capital) in fila]

print(resultado)

#5
dict_paises = [{'country': pais.upper(), 'city': capital.upper()} 
               for fila in countries for (pais, capital) in fila]

print(dict_paises)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

nombres_concatenados = [f"{nombre} {apellido}" 
                        for fila in names for (nombre, apellido) in fila]

print(nombres_concatenados)

#7

pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
interseccion = lambda x1, y1, m: y1 - m * x1


x1, y1 = 2, 4
x2, y2 = 4, 8

m = pendiente(x1, y1, x2, y2)
b = interseccion(x1, y1, m)

print(f"Pendiente: {m}")      
print(f"Intersección: {b}")   




