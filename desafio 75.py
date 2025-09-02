#desafio 75
v1=int(input("digite um valor"))
v2=int(input("digite outro um valor"))
v3=int(input("digite outro um valor"))
v4=int(input("digite outro um valor"))
lista=(v1,v2,v3,v4)
lista2=[]
print(f"o numero 9 apareceu {lista.count(9)} vezes")
for c in lista:
    if c % 2==0:
        lista2.append(c)

print(f"os numeros pares digitados foram {lista2}")

print(f"os numero 3 apareceu na {lista.index(3)}º posição")



seila='meu pau'
y=len(seila)
print(f"{y}")