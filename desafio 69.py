#desafio69
homens=0
mulher_20=0
pessoas_18=0
while True:
    idade=int(input("idade:"))
    sexo=input("sexo(M/F):").upper().strip()[0]
    while sexo not in 'MF':
        sexo=input("sexo(M/F)").upper().strip()[0]

    if sexo=='H':
        homens=homens+1
    elif sexo=='F' and idade<20:
        mulher_20=mulher_20+1
    elif idade>18:
        pessoas_18=pessoas_18+1
    pergunta_break=input("deseja continuar? [S/N]").upper().strip()[0]
    while pergunta_break not in 'SN':
         pergunta_break=input("deseja continuar? [S/N]").upper().strip()[0]
    if pergunta_break=='N':
        break
print(f"{homens} homens foram cadastrados")
print(f"{pessoas_18} pessoas possuem mais de 18 anos")
print(f"{mulher_20} mulher possuem menos de 20 anos ")

    
        
