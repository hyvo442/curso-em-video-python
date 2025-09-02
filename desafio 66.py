n=int(input("digite um numero"))
contagem_n=1
soma_n=n
while True:
    n=int(input("digite outro numero"))
    contagem_n=contagem_n+1
    if n==999:
        break
    soma_n=soma_n+n
print(f"voce digitou {contagem_n} termos", end= ' ')
print(f"e a soma deles é {soma_n}")
