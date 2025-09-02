#desafio 81 
valores=0
lista=[]
p='nao esta'
while True:
    numero=int(input("digite um numero:"))
    lista.append(numero)
    if numero==5:
        p='esta' 
    valores+=1
    organizado=sorted(lista)
    pergunta_break=input("quer continuar")
    while pergunta_break not in 'sn':
        pergunta_break=input("quer continuar")
    if pergunta_break=='n':
        break
print(f'{valores} numeros foram digitados')
print(f"{organizado} esses sao os valores digitados em ordem decrescente")
print(F'o numero 5 {p} na lista')