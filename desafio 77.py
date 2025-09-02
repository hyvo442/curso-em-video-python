# desafio 77
lista = ('aprender', 'comer', 'dormir', 'beber', 'reproduzir', 'morrer')
for p in lista:
    print(f"\nna palavra {p} temos", end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
       