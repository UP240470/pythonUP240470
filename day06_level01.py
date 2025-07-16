#1
tupla_vacia= ()
print("Tupla vacia:", tupla_vacia)

#2
hermana=('Marisol')
hermano = ('Carlos Daniel')
print("Hermanas:", hermana)
print("Hermanos:", hermano)

#3
hermano_y_hermanas= hermana+hermano
print("Hermanos y hermanas:", hermano_y_hermanas)

#4
print("total de hermanos:",len(hermano_y_hermanas))

#5
miembros_familia= list (hermano_y_hermanas)
miembros_familia.append('Noe')
miembros_familia.append('Sandra Veronica')
miembros_familia=tuple(miembros_familia)
print("Miembros de la familia:", miembros_familia)












