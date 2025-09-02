#desafio 60
numero=int(input("digite um numero"))
numero1=numero
fatorial=1
while numero!=1:
    fatorial=fatorial*numero
    numero=numero-1
print(f" o fatorial de {numero1} é {fatorial}")