it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
union_AB=A.union(B)
print("Union de A y B:",union_AB)

#2
interseccion_AB=A.intersection(B)
print("Interseccion de A y B:",interseccion_AB)

#3
es_subconjunto=A.issubset(B)
print("¿A es subconjunto de B?", es_subconjunto)


#4
son_disjuntos= A.isdisjoint(B)
print("¿A y B son disjuntos?",son_disjuntos)

#5
A_union_B=A.union(B)
B_union_A=B.union(A)
print("A unido con B",A_union_B)
print("B unido con A", B_union_A)

#6
simetrica_AB=A.symmetric_difference(B)
print("Diferencia simetrica entre A y B", simetrica_AB)

#7
del A
del B













