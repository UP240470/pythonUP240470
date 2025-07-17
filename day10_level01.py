#1
for numero in range(11):
    print(numero)

#1.2
numero=0
while numero<=10:
    print(numero)
    numero += 1
#2
for numero in range(10,-1,-1):
    print(numero)

#2.1
numero=10
while numero>= 0:
    print(numero)
    numero-=1

#3
for i in range(1,8):
    print('#'*i)


#4
for fila in range(8):
    for columna in range(8):
        print('#',end=' ')
    print()    

#5
for numero in range(11):
    print(f"{numero}x{numero}={numero*numero}")

#6
tecnologias =['Python','Numpy','Pandas','Django','Flask']
for tecnologia in tecnologias:
    print(tecnologia)

#7
for numero in range (0,101):
    if numero % 2==0:
        print(numero)

#8
for numero in range(0,101):
    if numero %2!=0:
        print(numero)








