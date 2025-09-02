#desafio 80
lista = []
while True:
    posição=0
    y = int(input("digite um numero"))
    for c in range(0,len(lista)):
        if c==0:
            posição=c
        if y>=lista[c]:
            posição=c+1
    lista.insert(posição,y)
    pergunta_break=input("quer parar")
    while pergunta_break not in 'sn':
        pergunta_break=input("quer parar")
    if pergunta_break=='s':
        break
print(f"{lista}")