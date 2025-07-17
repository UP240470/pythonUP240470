person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# 2
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("¿Tiene habilidad con python?", has_python)

# 3. 
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print("Es un desarrollador de front end")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print("HEs un desarrollador de backend")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("Es un desarrollador de fullstack")
    else:
        print("Titulo desconocido")

# 4
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = person['first_name'] + " " + person['last_name']
    print(f"{full_name} lives in Finland. He is married.")