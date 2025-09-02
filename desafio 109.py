import funcoes
num=int(input("digite um numero:"))
escolha=input("voce vai querer que seja formato ou não o print? [s/n]")
while escolha not in 'sn':
    escolha=input("voce vai querer que seja formato ou não o print? [s/n]")
if escolha=='s':
    funcoes.moeda(num)
else:
    funcoes.dobro(num)