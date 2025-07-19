#1
import random
import string

def shuffle_list(lista):
    copia = lista.copy()
    random.shuffle(copia)
    return copia

print(shuffle_list([1, 2, 3, 4, 5, 6, 7]))

#2
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers()) 


