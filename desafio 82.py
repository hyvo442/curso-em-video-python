#desafio 82 
lista_geral=[]
lista_par=[]
lista_impar=[]
while True:
    num=int(input("digite um numero"))
    lista_geral.append(num)
    if num %2==0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    pergunta_break=input("quer continuar?")
    while pergunta_break not in 'sn':
        pergunta_break=input("quer continuar?")
    if pergunta_break=='n':
        break
print(f'a lista geral de termos é {lista_geral}')
print(f'a lista de termos pares é {lista_par}')
print(f'a lista de termos impares é {lista_impar}')
    