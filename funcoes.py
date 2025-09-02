def dobro(n):
    print(n*2)
def metade(n):
    print(n/2)
def moeda(n):
    print(f"{n}R$ multiplicado por 2 é {n*2}R$")
def moeda2(n):
    print('-'*30)
    print("       RESUMO DO VALOR")
    print('-'*30)
    print(f'Valor analisado: {n}')
    print(f'Dobro do preço: {n*2}')
    print(f'Metade do preco: {n/2}')
    print(F"80% de aumento: {(n)+((n*80)/100)}")
    print(F"35% de redução: {((n*65)/100)}")
    print('-'*30)
def moedaa3():
    while True:
        try:
            n=int(input("digite um numero"))
            print('-'*30)
            print("       RESUMO DO VALOR")
            print('-'*30)
            print(f'Valor analisado: {n}')
            print(f'Dobro do preço: {n*2}')
            print(f'Metade do preco: {n/2}')
            print(F"80% de aumento: {(n)+((n*80)/100)}")
            print(F"35% de redução: {((n*65)/100)}")
            print('-'*30)
            break
        except ValueError:
            print('numero nao digitado') 
