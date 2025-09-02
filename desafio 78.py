#desafio 78
p1=int(input('digite um numero'))
p2=int(input('digite outro numero'))
p3=int(input('digite outro numero'))
p4=int(input('digite outro numero'))
p5=int(input('digite outro numero'))
lista=[p1,p2,p3,p4,p5]
maior=0
menor=0
local_maior=0
local_menor=0
posição=0
for c in lista:
    if posição==0:
        maior=c
        menor=c
        local_maior=posição
        local_menor=posição
    if c>maior:
        maior=c
        local_maior=posição
    if c<menor:
        menor=c
        local_menor=posição
    posição+=1
print(f"o maior termo digitado foi {maior} e ele esta na posição {local_maior+1}")
print(F"o menor termo digitado foi {menor} e ele esta na posição {local_menor+1}")
        