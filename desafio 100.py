lista=[]
import random
while True:
  n=int(input("digite um numero:"))
  lista.append(n)
  pergunta_break=input("quer continuar?")
  while pergunta_break not in 'sn':
    pergunta_break=input("quer continuar?")
  if pergunta_break=='n':
    break
def sorteio(p):
  lista2=[]
  i=0
  while True:
    i=i+1
    lista2.append(random.choice(p))
    if i==5:
      break
  return lista2
def somaPar(p):
  soma=0
  for c in p:
    if c%2==0:
      soma=soma+c
  return soma
print(f'a soma de numeros pares de uma lista com 5 numeros digitados foi {somaPar(sorteio(lista))}')