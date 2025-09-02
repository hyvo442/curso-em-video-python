#desafio 45
import random
lista = ['pedra', 'papel', 'tesoura']
elemento = random.choice(lista)
escolha=str(input("pedra,papel ou tesoura?"))
print(f'{elemento}')
if escolha=='pedra' and elemento=='tesoura':
  print("voce ganhou")
elif escolha=='pedra' and elemento=='papel':
  print('voce perdeu')
elif escolha=='papel' and elemento=='pedra':
  print("voce ganhou")
elif escolha=='papel' and elemento=='tesoura':
  print("você perdeu")
elif escolha=='tesoura' and elemento=='papel':
  print("voce ganhou")
elif escolha=='tesoura' and elemento=='pedra':
  print("voce perdeu")
elif escolha==elemento:
  print("empate")
