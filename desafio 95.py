#Desafio 95
dicionario={}
lista_geral=[]
while True:
  lista=[]
  soma_gols=0
  nome=input('nome:')
  jogos=int(input("quantos jogos o jogador fez?"))
  for c in range(0,jogos):
    gols=int(input(f"quantos gols ele fez no {c+1} jogo?"))
    soma_gols+=gols
    lista.append(gols)
  lista_geral.append(lista)
  lista.clear
  dicionario[f'{nome}']=soma_gols
  pergunta=input("quer continuar")
  if pergunta=='n':
    break
variavel=0
for k,v in dicionario.items():
  print(f'{variavel+1}- o jogador {k} fez {v} gol(s)')
  variavel+=1

escolha=int(input('deseja ve os gols de algum jogador?'))
if 1>escolha or escolha>len(lista_geral):
  print('nao existe esse jogador')
else:
  posição=0
  while True:
    print(f'no {posição+1}º jogo ele fez {lista_geral[escolha-1][posição]} gol(s)')
    posição+=1
    if posição==len(lista_geral[escolha-1]):
      break
  