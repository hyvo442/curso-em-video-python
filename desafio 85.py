#desafio 85
lista=[]
for c in range(0,7):
    n=int(input("digite um numero"))
    lista.append(n)
print("os valores pares são:",end=' ')
for d in lista:
    if d%2==0:
        print(f"{d}", end=' ')
print("")
print('os valores impares são:',end=' ')
for e in lista:
    if d%2==0:
        nada=''
    else:
        print(f"{e}",end=' ' )
