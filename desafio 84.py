#desafio 84
geral=list()
dados=list()
pessoas_cadastradas=0
for c in range(0,4):
    dados.append(int(input("peso:")))
    dados.append(input("nome:"))
    pergunta_Brak=input("quer continuar?").upper()
    pessoas_cadastradas+=1
    geral.append(dados[:])
    dados.clear()
    organizado=sorted(geral)
    reverso=reversed(organizado)
    while pergunta_Brak not in "SN":
        pergunta_Brak=input("quer continuar?").upper()
    if pergunta_Brak=='N':
        break
print(f"{organizado}")
print(F"{pessoas_cadastradas} pessoas foram cadastradas")
print(F"os nomes organizados dos mais leves pros mais pesados é:")
for p in organizado:
    print(f'{p[1]} possui um peso de {p[0]}')
print('os nomes organizados dos mais pesados pros mais leves é:')
for p in reverso:
    print(f'{p[1]} possui um peso de {p[0]}')




    
    