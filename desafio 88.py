#desafio 88
import random
numero=int(input("quantos jogos você quer que eu sorteie"))
lista=[]
c=0
for d in range(0,numero):
    print(f'{d+1}º jogo:',end=' ')
    while True:
        n=random.randint(0,60)
        if n in lista:
            k=0
        else:
            lista.append(n)
            c=c+1
        if c==6:
            break
    organizado=sorted(lista)
    print(f"{organizado}")
    list.clear(lista)
    c=0
