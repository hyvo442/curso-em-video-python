jogador_futebol={'nome':'','partidas jogadas':''}
while True:
  jogador_futebol['nome']=input("nome:")
  partidas=int(input("partidas jogadas:"))
  jogador_futebol['partidas jogadas']=partidas
  for c in range(0,partidas):
    jogador_futebol[f'partida {c+1}']=int(input(f"quantos gols fez no jogo {c+1}"))
  break
gols=0
print(f"{jogador_futebol['nome']} jogou {jogador_futebol['partidas jogadas']} partidas")
for p in range(0,partidas):
  print(f"    => na partida {p+1}, fez {jogador_futebol[f'partida {p+1}']} gol")
  gols=gols+jogador_futebol[f'partida {p+1}']

print(f"fez um total de {gols} gols")