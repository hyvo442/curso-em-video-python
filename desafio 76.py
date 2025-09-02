#desa=fio 76
lista=('pão','2','cafe','4','doce','10','refri','6')
print('-'*35)
print('         LISTAGEM DE PREÇOS')
print("-"*35)
palavras=len(lista)
numero=0
while True:
    print(f"{lista[numero]}",end='')
    y=len(lista[numero])
    numero+=1
    l=len(lista[numero])
    print('.'*(((35-3)-l)-y),end='')
    print(f"{lista[numero]} R$")
    numero+=1
    if numero==palavras:
        break
print('-'*35)