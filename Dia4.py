#1.
espacio=' '
thirty='thirty'
days='days'
of='of'
python='python'
texto=thirty+espacio+days+espacio+of+espacio+python
print(texto)
#2.
codigo='codigo'
For='for'
all='all'
text2=codigo+espacio+For+espacio+all
print(text2)

#3.
compañia='Codificacion para todos'
#4.
print(compañia)
#5.
print(len(compañia))
#6.
print(compañia.upper())
#7.
print(compañia.upper())
#8.
print(compañia.capitalize())
print(compañia.title())
print(compañia.swapcase())

#9.
cortado=compañia.find(' ')
resultado=compañia[cortado +1:]
print(resultado)
#10.
print(compañia.index('Codificacion'))
print(compañia.find('Codificacion'))
print('Codificacion' in compañia)
#11.
print(compañia.replace('Codificacion', 'Python'))

#12.
print('Python for Everyone'.replace('Everyone', 'All'))

#13.
print(compañia.split())

#14.
redes_sociales='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(redes_sociales.split())

#15.
print(compañia[0])

#16.
print(compañia[-1])

#17.
print(compañia[10])

#18.
frase='Python For Everyone'
acronimo=''.join([word[0] for word in frase.split()])
print(acronimo)

#19.
frase2='Coding For All'
acronimo2=''.join([word[0] for word in frase2.split()])
print(acronimo2)

#20.
posicion=frase2.index('C')
print(posicion)

#21.
posicion=frase2.index('F')
print(posicion)

#22.
print('Coding For All People'.rfind('l'))

#23.
palabra='You cannot end a sentence with because because because is a conjunction'
print(palabra.find('because'))

#24
print(palabra.rindex('because'))

#25.
start=palabra.find('because')
end=palabra.rindex('because') + len('because')
print(palabra[start:end])

#26.
print(frase2.startswith('Coding'))
print(frase2.endswith('coding'))

#27.
messy = '   Coding For All      '
print(messy.strip())

#28.
"Coding For All".startswith("Coding")  

#29.
print('no')

#30.
remover='   Coding For All      '
print(remover.strip())

#31.
print('30DaysOfPython'.isidentifier())        
print('thirty_days_of_python'.isidentifier()) 

#32.
bibliotecas=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(bibliotecas))

#33.
print("I am enjoying this challenge.\nI just wonder what is next.")

#34.
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35.
radio = 10
area = 3.14 * radio ** 2
print("El area de un circulo con radio {} es {} metros cuadrados".format(radio, int(area)))





