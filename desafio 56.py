#desafio 56
media_idade=0
mulheres_20=0
maioridade=0
nomevelho=''
for p in range(1,5):
    print(f"--------------{p}º pessoa----------------")
    sexo=input("qual o sexo da pessoa? [M/F]").upper()
    if sexo=='M':
        nome=input("nome:")
        idade=int(input('idade:'))
        media_idade=media_idade+idade
        
        if p==1 and sexo in 'mM':
            maioridade=idade
            nomevelho=nome
        if sexo in 'Mm' and idade>maioridade:
            maioridade=idade
            nomevelho=nome
        
    elif sexo=='F':
        nome=input("nome:")
        idade=int(input('idade:'))
        if idade<20:
            mulheres_20=mulheres_20+1
        media_idade=media_idade+idade

print(f"a media de idade do grupo é {media_idade/4}")
print(f" a quantidade de mulheres que possuem menos de 20 anos é: {mulheres_20}")
print(f'o homem mais velho possui {maioridade} anos e o nome dele é {nomevelho}')

