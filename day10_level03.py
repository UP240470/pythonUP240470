from data.countries import countries

print("Paises que contiene 'land':")
paisess_con_lan=[pais for pais in countries if 'land' in pais.lower()]
for pais in paisess_con_lan:
    print(f"- {pais}")

#2
frutas=['banana','naranja','mango','limon']
frutas_invertidas=[]

for i in range (len(frutas)-1,-1,-1):
    frutas_invertidas.append(frutas[i])

print("Lista de frutas invertidas")
print(frutas_invertidas)

#3
from data.countries_data import countries_data

#3.1
lenguajes=set( )
for pais in countries_data:
    for lenguaje in pais['languages']:
        lenguajes.add(lenguaje)
print(".1 Total de lenguajes unicos:{len(lenguajes)}")

#3.2
conteo_lenguajes={}
for pais in countries_data:
    for lenguaje in pais['languages']:
        conteo_lenguajes[lenguaje]=conteo_lenguajes.get(lenguaje, 0)+1

top_lenguajes=sorted(conteo_lenguajes.items(),key=lambda x: x[1], reverse=True)[:10]

print("Top 10 lenguajes mas hablados ")
for idx,(lenguaje,conteo) in enumerate(top_lenguajes,1):
    print(f"{idx}.{lenguaje}:{conteo}paises")

#3.3
paises_poblados=sorted(countries_data,
                       key=lambda x: x['population'],
                       reverse=True)[:10]  
print("Top 10 paises mas poblados:")
for idx,pais in enumerate(paises_poblados,1):
    nombre=pais['name']
    poblacion=f"{pais['population']:,}".replace(",",".")
    print(f"{idx}.{nombre}:{poblacion}habitantes")





