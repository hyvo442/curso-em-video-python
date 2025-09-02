#Desafio 101
def votar(idade):
    if idade<16:
        print('voce nao possui idade para votar')
    if 16<idade<18:
        print('voce pode votar de forma opcional')
    if idade>=18:
        print('voce possui a obrigação de votar')
n=int(input("qual a sua idade?"))
votar(n)
