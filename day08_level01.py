#1
dog={}

#2
dog['name']='Firulais'
dog['color']='marron'
dog['breed']='Labrador'
dog['legs']=4
dog['age']=5

#3
student = {
    'first_name': 'Mira',
    'last_name': 'Rumi',
    'gender': 'Non-binary',
    'age':18,
    'marital_status': 'single',
    'skills': ['Python', 'HTML'],
    'country': 'Canada',
    'city': 'Toroto',
    'address': 'Calle  123'
}

#4
print("Longitud del diccionario student:",len(student))

#5
skills=student['skills']
print("Habilidades:",skills)
print("Tipo de datos de 'skills':",type(skills))

#6
student['skills'].append('CSS')
student['skills'].append('JavaScript')

#7
keys=list(student.keys())
print("claves del diccionario:",keys)

#8
values=list(student.values())
print("Valores del diccionario:", values)

#9
items= list(student.items())
print("Diccionario como lista de tuplas:",items)

#10
student.pop('marital_status')

#11
del dog

print(" Diccionario student final:",student)





