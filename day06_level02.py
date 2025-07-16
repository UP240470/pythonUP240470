#1
miembros_familia=('Carlos Daniel','Marisol','Sandra Veronica', 'Noe')
hermanos,hermanas, mama, papa = miembros_familia
print("hermano", hermanos)
print("Hermana.:", hermanas)
print("Mama:",mama)
print("papa:",papa)

#2
frutas=('platano','naranja','mango')
vegetales=('tomate','zanahoria','lechuga')
productos_animales=('leche','queso','yogurt')

food_stuff_tp= frutas+vegetales+productos_animales
print("food stuff (tupla):",food_stuff_tp)


#3
food_stuff_it=list(food_stuff_tp)
print("Food stuff (lista):",food_stuff_it)

#4
longitud=len(food_stuff_it)
if longitud % 2==0:
    items_medios=food_stuff_it[longitud //2-1: longitud // 2+1]
else:
    items_medios=[food_stuff_it[longitud //2]]
print("Elementos del medio:", items_medios)

#5
primeros_tres= food_stuff_it[:3]
ultimos_tres= food_stuff_it[-3:]
print("Primeros tres:", primeros_tres)
print("Ultimos tres:", ultimos_tres)

#6
del food_stuff_tp

#7
nordic_countries=('Denmark','Finland','Iceland','Norway','Sweden')

print("¿Estonia es un pais nordico?",'Estonia' in nordic_countries)
print("¿Iceland es un pais nordico?", 'Iceland' in nordic_countries)









