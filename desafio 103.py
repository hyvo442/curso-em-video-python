#desafio 103
def ficha(jogador,gols):
    if jogador=='':
        jogador='<desconhecido>'
    if gols=='':
        gols='0'
    print(f"o jogador {jogador} fez {gols} gol(s) no campeonato")
nome=input('jogador:')
gol=input('gols:')
ficha(nome,gol)