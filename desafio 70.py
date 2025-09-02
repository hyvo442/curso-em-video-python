#desafio 70
total_gasto=0
produtos_1000=0
mais_barato=''
preco_barato=0
preco_1000=0
total_gasto=0
while True:
    nome=input("qual o nome do produto?")
    preco=int(input("qual o preco do produto?"))
    if total_gasto==0:
        mais_barato=nome
        preco_barato=preco
    if preco<preco_barato:
        mais_barato=nome
        preco_barato=preco
    if preco>=1000:
        preco_barato=preco_1000+1
    total_gasto=preco+total_gasto
    perguta_break=perguta_break=input("deseja continuar? [S/N]").upper().strip()[0]
    while perguta_break not in 'SN':
        perguta_break=input("deseja continuar? [S/N]").upper().strip()[0]
    if perguta_break=='N':
        break

print(f"o total da compra é {total_gasto} R$")
print(f"{preco_1000} produtos custam mais de 1000 reais")
print(f"{nome} é o produto mais barato custando {preco_barato}")