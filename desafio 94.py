#desafio 94
lista=[]
pessoas=0
media_idade=0
media_idade2=0
while True:
    pessoas=pessoas+1
    dicionario={'nome':'','sexo':'','idade':''}
    nome=input("nome")
    dicionario['nome']=nome
    sexo=input("sexo:[m/f]")
    while sexo not in 'mf':
        sexo=input("sexo:[m/f]")
    dicionario['sexo']=sexo
    idade=int(input('idade:'))
    dicionario['idade']=idade
    lista.append(dicionario)
    media_idade=media_idade+idade
    media_idade2=media_idade/pessoas
    pergunta_break=input('quer continuar [s/n]')
    while pergunta_break not in 'sn':
        pergunta_break=input('quer continuar [s/n]')
    if pergunta_break=='n':
        break
print(pessoas)
print(media_idade2)
for c in lista:
    if c['sexo']=='f':
        print(c)
for d in lista:
    if d['idade']>media_idade2:
        print(d)