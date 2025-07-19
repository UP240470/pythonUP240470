#1
import random
import string

def random_user_id():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=6))
print(random_user_id()) 

#2
def user_id_gen_by_user():
    num_caracteres = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Cantidad de IDs a generar: "))
    caracteres = string.ascii_letters + string.digits
    for _ in range(num_ids):
        print(''.join(random.choices(caracteres, k=num_caracteres)))

#3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())  




