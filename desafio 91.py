#desafio 91
import random
list1={'nome1':'','numero':'',
       'nome2':'','numero2':'',
       'nome3':'','numero3':'',
       'nome4':'','numero4':''}
lista_k=[]
for c in range(1,5):
    while True:
        k=random.randint(1,4)
        if k in lista_k:
            ç=0
        else:
            lista_k.append(k)
            break
    pergunta=input("nome:")
    list1[f'nome{k}']=pergunta
n=0
lista=[]
while True:
    w=random.randint(1,6)
    lista.append(w)
    n=n+1
    if n==4:
        break
lista.sort()
lista.reverse()
list1['numero']=lista[0]
list1['numero2']=lista[1]
list1['numero3']=lista[2]
list1['numero4']=lista[3]
print(list1)
