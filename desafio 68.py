#desafio 68
import random
vitorias=0
nome=input("qual o seu nome?")
jogador=nome
maquina='computador'
par=''
impar=''
vencedor=''
vitorias=0
while True:
    computador=random.randint(1,2)
    n=input('impar ou par')
    print(f'{computador}')
    while n not in 'imparpar':
        n=input('impar ou par')
    if n == 'par':
        par=nome
        impar=maquina
    else:
        par=maquina
        inpar=nome
    s=int(input('qual o seu numero?'))
    if (s+computador) % 2==0:
        vencedor=par
    else:
        vencedor=impar
    if vencedor==maquina:
        print('voce perdeu')
        break
    else: 
        vitorias=vitorias+1 
        print(f'{vencedor} é o vencedor')
    pergunta_break=input("deseja continuar? [S/N]").upper()
    while pergunta_break not in 'SN':
         pergunta_break=input("resposta incorreta.Deseja continuar? [S/N]").upper()
    if pergunta_break=='N':
        break
print(f"voce conseguiu um total de {vitorias} vitorias")

    
