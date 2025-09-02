#Desafio 106
while True:
    duvida=input("qual comando voce possui duvida?")
    help(duvida)
    pergunta_break=input("deseja continar[s/n]")
    while pergunta_break not in 'sn':
        if pergunta_break=='n':
            break