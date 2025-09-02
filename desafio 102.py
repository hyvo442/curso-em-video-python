#Desafio 102
from random import choice

def fatorial(n,show):
    soma=1
    while True:
        soma=soma*n
        n=n-1
        if show=='sim':
            print(soma,end='')
            print('->',end='')
        if n==1:
            break
    print(soma)
numero=int(input('numero:'))
escolha=input('quer ver o processo de fatorial?')
fatorial(numero,escolha)