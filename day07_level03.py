#1
age=[22,19,24,25,26,24,25,24]
age_set=set(age)

print("Lista original:",age)
print("Conjunto sin duplicados",age_set)

print("Longitud de la lista:", len(age))
print("Longitud del set:", len(age_set))

if len(age)>len(age_set):
    print("La lista es mas grande porque contiene elementos duplicados")
elif len(age)<len(age_set):
    print("El set es mas grande, pero esto no debe pasar en este caso")
else:
    print("Ambos tienen la misma longitud")


#2
"""La cadena representa texto y no puede modificarse una vez creado
ademas te permite acceder a cada letra mediante indice. Una lista es una 
coleccion ordenada y modificable que puede contener elemntos repetidos
y se accede a ellos por posicion. Una tupla es una coleccion ordenada,
pero no se puede cambiar despues de su creacion. Un conjunto(set) es una 
coleccion no ordenada y sin duplicaciones aqui se pueden hacer uniones y intersecciones. """

#3
frase="I am a teacher and I love to inspire and teach people"

palabras=frase.split()
palabras_unicas=set(palabras)

print("palabra unica",palabras_unicas)
print("Numero de palabras Unicas",len(palabras_unicas))



