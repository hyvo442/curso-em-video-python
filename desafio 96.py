#desafio 96
def area(largura,comprimento):
    c=largura*comprimento
    print(f"a area dos dados informados são {c}")
    return largura,comprimento
while True :
    p=int(input("largura:"))
    y=int(input("comprimento:"))
    print(f'{area(p,y)}')
    pergunta_Break=input("deseja continuar[s/n]")
    while pergunta_Break not in 'sn':
        pergunta_Break=input("deseja continuar[s/n]")
    if pergunta_Break=='n':
        break
