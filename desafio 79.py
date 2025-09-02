# DESAFIO 79
lista = []
while True:
    y = int(input("digite um numero"))
    if y in lista == True:
        p = ''
    else:
        lista.append(y)
    pergunta_break = input("deseja continuar").lower()
    while pergunta_break not in 'sn':
        pergunta_break = input("deseja continuar").lower()
    if pergunta_break == 'n':
        break
ordenada = sorted(lista)
print(f"a lista de numeros digitados em ordem é:{ordenada}")
