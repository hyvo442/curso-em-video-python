#Desafio 87
soma=0
lista=[]
valores=0
for c in range(1,10):
    n=int(input("digite um numero"))
    lista.append(n)
    if n %2==0:
        soma+=n
print(f'''[{lista[0]}] [{lista[1]}] [{lista[2]}]
[{lista[3]}] [{lista[4]}] [{lista[5]}]    
[{lista[6]}] [{lista[7]}] [{lista[8]}]''')
print(f'{soma} é a soma dos valores pares')
valor=lista[2]+lista[5]+lista[8]
print(f"{valor} é a soma dos valores da terceira coluna")
maior=0
lista_maior=[lista[3],lista[4],lista[5]]
print(F'{max(lista_maior)} é o maior valor da segunda linha')

